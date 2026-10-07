import os
import json
import re
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
public_dir = os.path.join(base_dir, "public")
fr_posts_path = os.path.join(base_dir, "src", "data", "blog_posts.json")
en_posts_path = os.path.join(base_dir, "src", "data", "blog_posts.en.json")

with open(fr_posts_path, "r", encoding="utf-8") as f:
    posts_fr = json.load(f)

with open(en_posts_path, "r", encoding="utf-8") as f:
    posts_en = json.load(f)

en_slugs = {p["slug"] for p in posts_en}

# Static and Core Routes
STATIC_ROUTES = [
    ("", "1.0", "daily"),
    ("destinations", "0.9", "weekly"),
    ("destinations/bardia", "0.9", "weekly"),
    ("destinations/chitwan", "0.9", "weekly"),
    ("destinations/suklaphanta", "0.9", "weekly"),
    ("destinations/annapurna", "0.8", "weekly"),
    ("destinations/katmandou", "0.8", "weekly"),
    ("blog", "0.9", "daily"),
    ("a-propos", "0.7", "monthly"),
    ("contact", "0.8", "monthly"),
]

# Tours and Activities Routes
TOURS = [
    "bardia-explorateur",
    "chitwan-culture",
    "nepal-sauvage",
    "babai-special",
    "bardia-nuit-sauvage",
    "bardia-babai-camping",
    "chitwan-bardia-complete",
    "rafting-safari",
    "rafting-safari-bardia",
    "rara-lake-bardia",
    "safari-jeep-bardia",
    "safari-jeep-chitwan",
    "safari-pied-bardia",
    "safari-pied-chitwan",
    "jungle-extreme",
    "tiji-mustang",
    "panthere-des-neiges",
    "dashain-immersion-culturelle",
    "nepal-immersion-totale",
    "carnet-de-voyage",
    "immersion-spirituelle",
]

today = datetime.now().strftime("%Y-%m-%d")

xml_entries = []

# 1. Static Routes (FR & EN with exact hreflang alternates)
for route, priority, changefreq in STATIC_ROUTES:
    fr_path = f"/{route}/" if route else "/"
    en_path = f"/en/{route}/" if route else "/en/"
    
    fr_url = f"https://junglenepal.com{fr_path}"
    en_url = f"https://junglenepal.com{en_path}"
    
    # FR URL entry
    xml_entries.append(f"""  <url>
    <loc>{fr_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}"/>
  </url>""")
    
    # EN URL entry
    xml_entries.append(f"""  <url>
    <loc>{en_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}"/>
  </url>""")

# 2. Tours and Activities Routes (FR & EN)
for tour in TOURS:
    fr_url = f"https://junglenepal.com/tours/{tour}/"
    en_url = f"https://junglenepal.com/en/tours/{tour}/"
    
    # Higher priority for 1-day activities and key flagship tours
    priority = "0.9" if tour in ["safari-pied-bardia", "safari-jeep-bardia", "safari-pied-chitwan", "bardia-explorateur", "chitwan-culture"] else "0.85"
    
    xml_entries.append(f"""  <url>
    <loc>{fr_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}"/>
  </url>""")
    
    xml_entries.append(f"""  <url>
    <loc>{en_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}"/>
  </url>""")

# 3. Blog Articles (All 58 FR and All 58 EN with bidirectional hreflang)
for p in posts_fr:
    slug = p["slug"]
    date = p.get("date", today)
    fr_url = f"https://junglenepal.com/blog/{slug}/"
    en_url = f"https://junglenepal.com/en/blog/{slug}/"
    
    xml_entries.append(f"""  <url>
    <loc>{fr_url}</loc>
    <lastmod>{date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}"/>
  </url>""")
    
    xml_entries.append(f"""  <url>
    <loc>{en_url}</loc>
    <lastmod>{date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_url}"/>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{"\n".join(xml_entries)}
</urlset>
"""

sitemap_path = os.path.join(public_dir, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print(f"Generated complete sitemap.xml with {len(xml_entries)} URLs across FR & EN!")

# Also generate sitemap_index.xml pointing to sitemap.xml
sitemap_index = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://junglenepal.com/sitemap.xml</loc>
    <lastmod>{today}</lastmod>
  </sitemap>
</sitemapindex>
"""
with open(os.path.join(public_dir, "sitemap_index.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_index)

print("Generated sitemap_index.xml!")
