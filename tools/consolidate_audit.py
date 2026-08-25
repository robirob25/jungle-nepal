import os, re, glob
from html.parser import HTMLParser

dist_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

html_files = glob.glob(os.path.join(dist_dir, '**/*.html'), recursive=True)
print(f"Auditing {len(html_files)} compiled HTML pages...")

class LinkImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == 'img' and 'src' in attr_dict:
            self.images.append(attr_dict['src'])
        if tag == 'a' and 'href' in attr_dict:
            self.links.append(attr_dict['href'])

broken_images = []
broken_links = []
total_images_checked = 0
total_links_checked = 0

for hf in html_files:
    rel_page = os.path.relpath(hf, dist_dir)
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = LinkImageParser()
    try:
        parser.feed(content)
    except Exception as e:
        print(f"Parse error on {rel_page}: {e}")
        continue
    
    for src in parser.images:
        total_images_checked += 1
        if src.startswith('http') or src.startswith('data:'):
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if clean_src.startswith('/'):
            target_path = os.path.join(dist_dir, clean_src.lstrip('/'))
        else:
            target_path = os.path.join(os.path.dirname(hf), clean_src)
        
        if not os.path.exists(target_path):
            broken_images.append((rel_page, src, target_path))

    for href in parser.links:
        total_links_checked += 1
        if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('#') or href.startswith('javascript:'):
            continue
        clean_href = href.split('?')[0].split('#')[0]
        if not clean_href:
            continue
        if clean_href.startswith('/'):
            target_path = os.path.join(dist_dir, clean_href.lstrip('/'))
        else:
            target_path = os.path.join(os.path.dirname(hf), clean_href)
        
        exists = (
            os.path.exists(target_path) or
            os.path.exists(target_path + '.html') or
            os.path.exists(os.path.join(target_path, 'index.html'))
        )
        if not exists:
            broken_links.append((rel_page, href, target_path))

print(f"\n================ AUDIT SUMMARY ================")
print(f"✓ Total compiled HTML pages: {len(html_files)}")
print(f"✓ Total Image references verified: {total_images_checked}")
print(f"❌ Broken images count: {len(broken_images)}")
if broken_images:
    for page, src, p in broken_images[:10]:
        print(f"   Broken image in {page}: {src}")

print(f"✓ Total Links verified: {total_links_checked}")
print(f"❌ Broken links count: {len(broken_links)}")
if broken_links:
    for page, href, p in broken_links[:10]:
        print(f"   Broken link in {page}: {href}")

