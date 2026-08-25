import os
import re
import urllib.parse
from html.parser import HTMLParser

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

all_html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            all_html_files.append(os.path.join(root, f))

print(f"Total HTML pages to audit: {len(all_html_files)}")

# Parser to extract links, images, forms, ids, metadata
class AuditParser(HTMLParser):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.title = None
        self.meta_desc = None
        self.og_title = None
        self.og_image = None
        self.links = []
        self.images = []
        self.ids = []
        self.has_viewport = False
        self.in_title = False
        self.title_buffer = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'title':
            self.in_title = True
            self.title_buffer = []
        
        if tag == 'meta':
            name = attrs_dict.get('name', '').lower()
            prop = attrs_dict.get('property', '').lower()
            content = attrs_dict.get('content', '')
            if name == 'description':
                self.meta_desc = content
            elif name == 'viewport':
                self.has_viewport = True
            elif prop == 'og:title':
                self.og_title = content
            elif prop == 'og:image':
                self.og_image = content
                
        if 'id' in attrs_dict:
            self.ids.append(attrs_dict['id'])
            
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(attrs_dict['href'])
            
        if tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', None)
            self.images.append((src, alt))

    def handle_data(self, data):
        if self.in_title:
            self.title_buffer.append(data)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
            self.title = ''.join(self.title_buffer).strip()

results = {}
broken_internal_links = []
missing_alts = []
duplicate_ids_total = []
missing_metadata = []

# Known routes in dist
known_files = set()
for root, dirs, files in os.walk(base_dir):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), base_dir)
        known_files.add('/' + rel.replace('\\', '/'))
        if f == 'index.html':
            dir_route = '/' + os.path.relpath(root, base_dir).replace('\\', '/')
            if dir_route == '/.':
                dir_route = '/'
            else:
                dir_route = dir_route + '/'
            known_files.add(dir_route)

for fpath in all_html_files:
    rel_path = os.path.relpath(fpath, base_dir)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    parser = AuditParser(fpath)
    try:
        parser.feed(content)
    except Exception as e:
        print(f"HTML Parse error in {rel_path}: {e}")

    # Check Title & Meta Description
    if not parser.title or len(parser.title) < 5:
        missing_metadata.append((rel_path, "Missing or very short <title>"))
    if not parser.meta_desc or len(parser.meta_desc) < 10:
        missing_metadata.append((rel_path, "Missing or very short <meta name='description'>"))

    # Check Duplicate IDs in page
    seen_ids = set()
    dup_ids = []
    for elem_id in parser.ids:
        if elem_id in seen_ids:
            dup_ids.append(elem_id)
        seen_ids.add(elem_id)
    if dup_ids:
        duplicate_ids_total.append((rel_path, list(set(dup_ids))))

    # Check Missing Alt attributes on Images
    for src, alt in parser.images:
        if alt is None or alt.strip() == '':
            missing_alts.append((rel_path, src))

    # Check Internal Links
    for href in parser.links:
        if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('javascript:') or href.startswith('#'):
            continue
        
        # Remove query & hash
        parsed_href = urllib.parse.urlparse(href).path
        if not parsed_href:
            continue
            
        # Resolve target
        if parsed_href.startswith('/'):
            target_path = parsed_href
        else:
            # relative to current file's dir
            current_dir = '/' + os.path.dirname(rel_path).replace('\\', '/')
            if current_dir == '/.':
                current_dir = '/'
            target_path = urllib.parse.urljoin(current_dir, parsed_href)

        # Check if target exists
        exists = False
        possible_checks = [
            target_path,
            target_path + '.html' if not target_path.endswith('.html') and not target_path.endswith('/') else target_path,
            target_path + '/index.html' if target_path.endswith('/') else target_path + '/index.html',
            target_path.rstrip('/') + '.html',
            target_path.rstrip('/') + '/index.html'
        ]
        for pc in possible_checks:
            if pc in known_files:
                exists = True
                break
        
        if not exists:
            broken_internal_links.append((rel_path, href, target_path))

print("\n================== AUDIT RESULTS ==================")
print(f"1. Total HTML Pages: {len(all_html_files)}")
print(f"2. Broken Internal Links: {len(broken_internal_links)}")
for source, href, target in broken_internal_links[:10]:
    print(f"   - In [{source}] -> broken link href='{href}' (resolved: {target})")

print(f"\n3. Missing Alt on Images: {len(missing_alts)}")
for source, src in missing_alts[:5]:
    print(f"   - In [{source}] -> img without alt: {src[:60]}")

print(f"\n4. Duplicate HTML IDs: {len(duplicate_ids_total)}")
for source, dups in duplicate_ids_total[:5]:
    print(f"   - In [{source}] -> duplicate IDs: {dups}")

print(f"\n5. SEO / Metadata Issues: {len(missing_metadata)}")
for source, issue in missing_metadata[:5]:
    print(f"   - In [{source}] -> {issue}")

