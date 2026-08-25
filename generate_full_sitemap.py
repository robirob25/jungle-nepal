import os, datetime

dist_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'
domain = 'https://junglenepal.com'
today = datetime.datetime.now().strftime('%Y-%m-%d')

urls = [
    (f"{domain}/", "1.0", "daily"),
    (f"{domain}/a-propos", "0.9", "monthly"),
    (f"{domain}/destinations", "0.9", "weekly"),
    (f"{domain}/contact", "0.8", "monthly"),
    (f"{domain}/destinations/bardia", "0.9", "weekly"),
    (f"{domain}/destinations/chitwan", "0.9", "weekly"),
    (f"{domain}/destinations/suklaphanta", "0.8", "weekly"),
    (f"{domain}/destinations/annapurna", "0.8", "weekly"),
    (f"{domain}/destinations/katmandou", "0.8", "weekly"),
    (f"{domain}/tours/jungle-extreme", "0.9", "weekly"),
    (f"{domain}/tours/nepal-sauvage", "0.9", "weekly"),
    (f"{domain}/tours/chitwan-bardia-complete", "0.9", "weekly"),
    (f"{domain}/tours/bardia-explorateur", "0.9", "weekly"),
    (f"{domain}/tours/bardia-nuit-sauvage", "0.8", "weekly"),
    (f"{domain}/tours/babai-special", "0.8", "weekly"),
    (f"{domain}/tours/bardia-babai-camping", "0.8", "weekly"),
    (f"{domain}/tours/rafting-safari", "0.8", "weekly"),
    (f"{domain}/tours/chitwan-culture", "0.8", "weekly"),
    (f"{domain}/tours/panthere-des-neiges", "0.9", "weekly"),
    (f"{domain}/tours/tiji-mustang", "0.8", "weekly"),
    (f"{domain}/tours/rara-lake-bardia", "0.8", "weekly"),
    (f"{domain}/tours/immersion-spirituelle", "0.8", "weekly"),
    (f"{domain}/tours/carnet-de-voyage", "0.8", "weekly"),
    (f"{domain}/tours/nepal-immersion-totale", "0.8", "weekly")
]

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for loc, priority, changefreq in urls:
    sitemap_xml += f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""

sitemap_xml += "</urlset>\n"

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print("✓ Generated perfect static sitemap.xml for https://junglenepal.com!")
