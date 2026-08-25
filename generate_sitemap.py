import os, glob
from datetime import datetime

dist_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'
public_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public'
base_url = 'https://junglenepaladventure.com'

# List of unique canonical pages
pages = [
    '/',
    '/a-propos',
    '/contact',
    '/destinations',
    '/destinations/bardia',
    '/destinations/chitwan',
    '/destinations/suklaphanta',
    '/destinations/katmandou',
    '/destinations/annapurna',
    '/tours/nepal-sauvage',
    '/tours/bardia-explorateur',
    '/tours/jungle-extreme',
    '/tours/bardia-nuit-sauvage',
    '/tours/bardia-babai-camping',
    '/tours/chitwan-bardia-complete',
    '/tours/nepal-immersion-totale',
    '/tours/panthere-des-neiges',
    '/tours/babai-special',
    '/tours/chitwan-culture',
    '/tours/immersion-spirituelle',
    '/tours/rafting-safari',
    '/tours/rara-lake-bardia',
    '/tours/tiji-mustang',
    '/tours/carnet-de-voyage'
]

today = datetime.now().strftime('%Y-%m-%d')

xml_entries = []
for p in pages:
    priority = '1.0' if p == '/' else ('0.9' if p.startswith('/tours/') else '0.8')
    changefreq = 'daily' if p == '/' else 'weekly'
    url = base_url + ('' if p == '/' else p)
    xml_entries.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(xml_entries)}
</urlset>
"""

with open(os.path.join(public_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print("Generated public/sitemap.xml and public/robots.txt successfully!")
