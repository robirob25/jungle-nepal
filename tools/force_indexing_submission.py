import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import os

# IndexNow API Key
INDEXNOW_KEY = "679a8bc43d8e4526b3490fd38e079c65"

# Create IndexNow verification files
with open(f"public/{INDEXNOW_KEY}.txt", "w", encoding="utf-8") as f:
    f.write(INDEXNOW_KEY)

# Parse all URLs from sitemap.xml
tree = ET.parse('public/sitemap.xml')
root = tree.getroot()
urls = [elem.text for elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

print(f"Extracted {len(urls)} URLs from sitemap.xml for indexing submission.")

# 1. Submit to IndexNow (Bing, Yandex, Seznam, Naver, etc.)
indexnow_payload = {
    "host": "junglenepal.com",
    "key": INDEXNOW_KEY,
    "keyLocation": f"https://junglenepal.com/{INDEXNOW_KEY}.txt",
    "urlList": urls
}

headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'JungleNepalBot/1.0'
}

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(indexnow_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=15) as response:
        print(f"✓ IndexNow Submission: HTTP {response.status} (Successfully submitted {len(urls)} URLs)")
except Exception as e:
    print(f"IndexNow Submission note: {e}")

# 2. Ping Google & Bing Sitemaps
sitemap_url = "https://junglenepal.com/sitemap.xml"
pings = [
    ("Google", f"https://www.google.com/ping?sitemap={urllib.parse.quote(sitemap_url)}"),
    ("Bing", f"https://www.bing.com/ping?sitemap={urllib.parse.quote(sitemap_url)}")
]

for engine, ping_url in pings:
    try:
        req = urllib.request.Request(ping_url, headers={'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"✓ {engine} Ping: HTTP {resp.status}")
    except Exception as e:
        print(f"{engine} Ping note: {e}")

