import urllib.parse
from run_technical_audit import AuditParser, all_html_files, known_files, base_dir
import os

broken_by_href = {}

for fpath in all_html_files:
    rel_path = os.path.relpath(fpath, base_dir)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    parser = AuditParser(fpath)
    parser.feed(content)
    
    for href in parser.links:
        if href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'wa.me')):
            continue
        parsed_href = urllib.parse.urlparse(href).path
        if not parsed_href:
            continue
        if parsed_href.startswith('/'):
            target_path = parsed_href
        else:
            current_dir = '/' + os.path.dirname(rel_path).replace('\\', '/')
            if current_dir == '/.':
                current_dir = '/'
            target_path = urllib.parse.urljoin(current_dir, parsed_href)

        possible_checks = [
            target_path,
            target_path + '.html' if not target_path.endswith('.html') and not target_path.endswith('/') else target_path,
            target_path + '/index.html' if target_path.endswith('/') else target_path + '/index.html',
            target_path.rstrip('/') + '.html',
            target_path.rstrip('/') + '/index.html'
        ]
        if not any(pc in known_files for pc in possible_checks):
            broken_by_href[href] = broken_by_href.get(href, 0) + 1

print("Top broken hrefs across the site:")
for href, count in sorted(broken_by_href.items(), key=lambda x: -x[1])[:30]:
    print(f"[{count} times] '{href}'")
