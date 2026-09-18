import json, glob, os, datetime
from upgrade_all_image_alts import generate_seo_alt

today = datetime.datetime.now().strftime("%Y-%m-%d")

with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

with open('src/data/tours.json', 'r', encoding='utf-8') as f:
    tours_fr = json.load(f)

with open('src/data/tours.en.json', 'r', encoding='utf-8') as f:
    tours_en = json.load(f)

with open('src/data/destinations.json', 'r', encoding='utf-8') as f:
    destinations = json.load(f)

entries = []

def add_url(loc_fr, loc_en=None, priority=0.8, changefreq="weekly", lastmod=today, image=None, title_fr="", title_en=""):
    img_obj_fr = None
    img_obj_en = None
    if image:
        img_url = image if image.startswith('http') else f"https://junglenepal.com{image}"
        img_obj_fr = {
            "loc": img_url,
            "title": title_fr or "Jungle Nepal Adventure Safari",
            "caption": generate_seo_alt(image, lang="fr")
        }
        img_obj_en = {
            "loc": img_url,
            "title": title_en or title_fr or "Jungle Nepal Adventure Safari",
            "caption": generate_seo_alt(image, lang="en")
        }
        
    entries.append({
        "loc": loc_fr,
        "lastmod": lastmod,
        "changefreq": changefreq,
        "priority": priority,
        "alt_fr": loc_fr,
        "alt_en": loc_en or loc_fr.replace("junglenepal.com/", "junglenepal.com/en/"),
        "image": img_obj_fr
    })
    if loc_en:
        entries.append({
            "loc": loc_en,
            "lastmod": lastmod,
            "changefreq": changefreq,
            "priority": priority,
            "alt_fr": loc_fr,
            "alt_en": loc_en,
            "image": img_obj_en
        })

# Home
add_url("https://junglenepal.com/", "https://junglenepal.com/en/", priority=1.0, changefreq="daily", image="/assets/original_site/tigre_bardia.webp", title_fr="Safari et tracking du tigre au Népal", title_en="Nepal wildlife and tiger safari")

# Blog Index
add_url("https://junglenepal.com/blog/", "https://junglenepal.com/en/blog/", priority=0.9, changefreq="daily", image="/assets/curated_gallery/tigre_bengale_traversee_riviere.webp", title_fr="Blog et guides safari au Népal", title_en="Nepal safari blog and field guides")

# Contact & About
add_url("https://junglenepal.com/contact/", "https://junglenepal.com/en/contact/", priority=0.8, changefreq="monthly")
add_url("https://junglenepal.com/a-propos/", "https://junglenepal.com/en/a-propos/", priority=0.8, changefreq="monthly", image="/assets/img_3.webp", title_fr="Équipe Jungle Nepal Adventure", title_en="Jungle Nepal Adventure Team")
add_url("https://junglenepal.com/mentions-legales/", "https://junglenepal.com/en/legal-mentions/", priority=0.3, changefreq="yearly")

# Destinations Index
add_url("https://junglenepal.com/destinations/", "https://junglenepal.com/en/destinations/", priority=0.9, changefreq="weekly", image="/assets/curated_gallery/rhino_unicorne_brume.webp", title_fr="Destinations safaris au Népal", title_en="Nepal safari destinations")

# Individual Destinations
for d in destinations:
    slug = d.get('slug', '')
    img = d.get('image', '')
    title_d = d.get('name', slug)
    if slug:
        add_url(f"https://junglenepal.com/destinations/{slug}/", f"https://junglenepal.com/en/destinations/{slug}/", priority=0.85, image=img, title_fr=f"Guide destination {title_d}", title_en=f"{title_d} destination guide")

# Individual Tours
for t in tours_fr:
    slug = t.get('slug', '')
    img = t.get('image', '')
    title_t = t.get('title', slug)
    if slug:
        add_url(f"https://junglenepal.com/tours/{slug}/", f"https://junglenepal.com/en/tours/{slug}/", priority=0.9, image=img, title_fr=title_t, title_en=title_t)

# All 41 Blog Posts
for p_fr, p_en in zip(posts_fr, posts_en):
    slug = p_fr.get('slug', '')
    if slug:
        is_top = slug in [
            'voir-des-tigres-au-nepal',
            'guide-parc-national-de-bardia-safari-conseils',
            'bardia-ou-chitwan-quel-parc-choisir',
            'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia',
            'sante-paludisme-vaccins-safari-nepal-conseils-medicaux',
            'oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis',
            'safari-a-pied-au-nepal-guide-complet',
            'art-du-pistage-jungle-nepal-traces-cris-alarme'
        ]
        prio = 0.9 if is_top else 0.8
        date = p_fr.get('date', today)
        img = p_fr.get('featuredImage', '')
        add_url(
            f"https://junglenepal.com/blog/{slug}/", 
            f"https://junglenepal.com/en/blog/{slug}/", 
            priority=prio, 
            changefreq="weekly", 
            lastmod=date,
            image=img,
            title_fr=p_fr.get('title', ''),
            title_en=p_en.get('title', '')
        )

# Build XML
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
    '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
]

for e in entries:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{e["loc"]}</loc>')
    xml_lines.append(f'    <lastmod>{e["lastmod"]}</lastmod>')
    xml_lines.append(f'    <changefreq>{e["changefreq"]}</changefreq>')
    xml_lines.append(f'    <priority>{e["priority"]:.2f}</priority>')
    if e.get("alt_fr"):
        xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="fr" href="{e["alt_fr"]}"/>')
    if e.get("alt_en"):
        xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{e["alt_en"]}"/>')
        xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{e["alt_fr"]}"/>')
    if e.get("image"):
        img = e["image"]
        xml_lines.append('    <image:image>')
        xml_lines.append(f'      <image:loc>{img["loc"]}</image:loc>')
        xml_lines.append(f'      <image:title>{img["title"]}</image:title>')
        xml_lines.append(f'      <image:caption>{img["caption"]}</image:caption>')
        xml_lines.append('    </image:image>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

sitemap_content = '\n'.join(xml_lines)

with open('public/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Generated comprehensive sitemap with {len(entries)} URLs, xhtml:link hreflangs, and image:image tags!")
