import os, glob

base_url = "https://junglenepal.com"

# List all pages
pages = [
    "/index.html",
    "/a-propos.html",
    "/contact.html",
    "/destinations/index.html",
    "/destinations/bardia.html",
    "/destinations/chitwan.html",
    "/destinations/suklaphanta.html",
    "/destinations/annapurna.html",
    "/destinations/katmandou.html",
    "/tours/bardia-explorateur.html",
    "/tours/chitwan-culture.html",
    "/tours/rafting-safari.html",
    "/tours/bardia-nuit-sauvage.html",
    "/tours/rara-lake-bardia.html",
    "/tours/bardia-babai-camping.html",
    "/tours/nepal-immersion-totale.html",
    "/tours/babai-special.html",
    "/tours/chitwan-bardia-complete.html",
    "/tours/tiji-mustang.html",
    "/tours/carnet-de-voyage.html",
    "/tours/jungle-extreme.html",
    "/tours/nepal-sauvage.html",
    "/tours/immersion-spirituelle.html",
    "/tours/panthere-des-neiges.html"
]

sitemap_entries = []
for p in pages:
    priority = "1.0" if p == "/index.html" else ("0.9" if "/tours/" in p else "0.8")
    changefreq = "weekly" if "/tours/" in p or p == "/index.html" else "monthly"
    sitemap_entries.append(f"""  <url>
    <loc>{base_url}{p}</loc>
    <lastmod>2026-08-23</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_txt)

print("Generated public/sitemap.xml (24 URLs) and public/robots.txt!")
