import urllib.request, xml.etree.ElementTree as ET, json

sitemap_urls = [
    'https://junglenepal.com/wp-sitemap.xml',
    'https://junglenepal.com/sitemap_index.xml',
    'https://junglenepal.com/sitemap.xml',
    'https://junglenepal.com/wp-sitemap-posts-page-1.xml',
    'https://junglenepal.com/wp-sitemap-posts-post-1.xml'
]

headers = {'User-Agent': 'Mozilla/5.0'}

found_urls = []

for sm_url in sitemap_urls:
    try:
        req = urllib.request.Request(sm_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            root = ET.fromstring(content)
            for elem in root.iter():
                if elem.tag.endswith('loc') and elem.text:
                    found_urls.append(elem.text.strip())
            print(f"Fetched {sm_url} -> {len(found_urls)} URLs so far")
    except Exception as e:
        print(f"Could not fetch {sm_url}: {e}")

print(f"Total unique URLs found: {len(set(found_urls))}")
for u in sorted(list(set(found_urls))):
    print(" - ", u)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/old_site_urls.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(set(found_urls))), f, indent=2)

