import urllib.request, xml.etree.ElementTree as ET, json

sitemaps = [
    'https://junglenepal.com/wp-sitemap-posts-page-1.xml',
    'https://junglenepal.com/wp-sitemap-posts-post-1.xml',
    'https://junglenepal.com/wp-sitemap-taxonomies-category-1.xml',
    'https://junglenepal.com/post-sitemap.xml',
    'https://junglenepal.com/page-sitemap.xml',
    'https://junglenepal.com/tour-sitemap.xml'
]

headers = {'User-Agent': 'Mozilla/5.0'}
all_urls = []

for sm in sitemaps:
    try:
        req = urllib.request.Request(sm, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            root = ET.fromstring(content)
            for elem in root.iter():
                if elem.tag.endswith('loc') and elem.text:
                    u = elem.text.strip()
                    if not u.endswith('.xml'):
                        all_urls.append(u)
            print(f"Parsed {sm} -> {len(all_urls)} URLs total")
    except Exception as e:
        print(f"Error {sm}: {e}")

unique_urls = sorted(list(set(all_urls)))
print(f"\nTOTAL CANONICAL URLS ON JUNGLENEPAL.COM: {len(unique_urls)}")
for u in unique_urls:
    print(" - ", u)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/old_site_canonical_urls.json', 'w', encoding='utf-8') as f:
    json.dump(unique_urls, f, indent=2)

