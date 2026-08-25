import os, re, glob, json
from html.parser import HTMLParser

dist_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

html_files = glob.glob(os.path.join(dist_dir, '**/*.html'), recursive=True)
unique_pages = {}
for h in html_files:
    rel = os.path.relpath(h, dist_dir)
    route = '/' + rel.replace('index.html', '').replace('.html', '')
    if route not in unique_pages:
        unique_pages[route] = h

print(f"Auditing {len(unique_pages)} unique public endpoints...")

results = {
    'total_pages': len(unique_pages),
    'seo': {
        'missing_title': [],
        'missing_description': [],
        'missing_h1': [],
        'multiple_h1': [],
        'missing_canonical': [],
        'missing_og': [],
        'missing_schema_json_ld': [],
        'broken_images': [],
        'images_without_alt': [],
        'total_images_checked': 0
    },
    'performance': {
        'page_weights_kb': {},
        'avg_weight_kb': 0
    },
    'links': {
        'broken_internal_links': [],
        'total_links_checked': 0
    }
}

for route, fpath in unique_pages.items():
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title check
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if not title_match or not title_match.group(1).strip():
        results['seo']['missing_title'].append(route)

    # Meta description
    meta_desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not meta_desc_match or not meta_desc_match.group(1).strip():
        results['seo']['missing_description'].append(route)

    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if len(h1s) == 0:
        results['seo']['missing_h1'].append(route)
    elif len(h1s) > 1:
        results['seo']['multiple_h1'].append((route, len(h1s)))

    # Canonical
    canonical_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not canonical_match or not canonical_match.group(1).strip():
        results['seo']['missing_canonical'].append(route)

    # OpenGraph
    og_match = re.search(r'<meta[^>]*property=["\']og:title["\']', content, re.IGNORECASE)
    if not og_match:
        results['seo']['missing_og'].append(route)

    # JSON-LD Schema
    schema_match = re.search(r'<script[^>]*type=["\']application/ld\+json["\']>(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
    if not schema_match:
        results['seo']['missing_schema_json_ld'].append(route)

    # Images
    img_matches = re.findall(r'<img\s+([^>]*?)>', content, re.IGNORECASE)
    for img_tag in img_matches:
        results['seo']['total_images_checked'] += 1
        src_m = re.search(r'src=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        
        if not alt_m or not alt_m.group(1).strip():
            src_val = src_m.group(1) if src_m else 'unknown'
            results['seo']['images_without_alt'].append((route, src_val))

        if src_m:
            src = src_m.group(1)
            if src.startswith('/'):
                disk_p = os.path.join(dist_dir, src.lstrip('/'))
                if not os.path.exists(disk_p):
                    results['seo']['broken_images'].append((route, src))

    # Links
    a_matches = re.findall(r'<a\s+([^>]*?)>', content, re.IGNORECASE)
    for a_tag in a_matches:
        results['links']['total_links_checked'] += 1
        href_m = re.search(r'href=["\']([^"\']*)["\']', a_tag, re.IGNORECASE)
        if href_m:
            href = href_m.group(1)
            if href.startswith('/') and not href.startswith('//'):
                clean_href = href.split('#')[0].split('?')[0]
                if clean_href:
                    target_disk = os.path.join(dist_dir, clean_href.lstrip('/'))
                    if not os.path.exists(target_disk) and not os.path.exists(target_disk + '.html') and not os.path.exists(os.path.join(target_disk, 'index.html')):
                        results['links']['broken_internal_links'].append((route, href))

    results['performance']['page_weights_kb'][route] = round(len(content.encode('utf-8')) / 1024, 2)

total_kb = sum(results['performance']['page_weights_kb'].values())
results['performance']['avg_weight_kb'] = round(total_kb / len(unique_pages), 2)

print("\n=== AUDIT RESULTS SUMMARY ===")
print(f"Total HTML Pages Checked: {results['total_pages']}")
print(f"Missing Titles: {len(results['seo']['missing_title'])}")
print(f"Missing Descriptions: {len(results['seo']['missing_description'])}")
print(f"Missing H1s: {len(results['seo']['missing_h1'])}")
print(f"Missing Canonical: {len(results['seo']['missing_canonical'])}")
print(f"Missing JSON-LD Schemas: {len(results['seo']['missing_schema_json_ld'])}")
print(f"Total Images Scanned: {results['seo']['total_images_checked']}")
print(f"Broken Images: {len(results['seo']['broken_images'])}")
print(f"Images Missing Alt Tags: {len(results['seo']['images_without_alt'])}")
print(f"Total Internal Links Scanned: {results['links']['total_links_checked']}")
print(f"Broken Internal Links: {len(results['links']['broken_internal_links'])}")
print(f"Average HTML Page Weight: {results['performance']['avg_weight_kb']} KB")
