import glob, re, os
from upgrade_all_image_alts import generate_seo_alt

astro_files = glob.glob('src/pages/**/*.astro', recursive=True)

total_upgrades = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lang = 'en' if '/en/' in fpath else 'fr'
    
    file_upgrades = 0
    def repl_img(match):
        global total_upgrades
        tag = match.group(0)
        if re.search(r'alt=\{[^}]+\}', tag):
            return tag
        src_m = re.search(r'src=[\"\']([^\"\']+)[\"\']', tag)
        if not src_m:
            return tag
        src = src_m.group(1)
        if not any(src.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.webp', '.png']):
            return tag
            
        alt_m = re.search(r'alt=[\"\']([^\"\']*)[\"\']', tag)
        old_alt = alt_m.group(1) if alt_m else ""
        
        if not old_alt or len(old_alt) < 15 or old_alt.lower() in ['image', 'photo', 'jungle', 'nepal', 'banner']:
            if 'logo' in src.lower():
                new_alt = "Jungle Nepal Adventure — Agence de safari éthique au Népal" if lang == 'fr' else "Jungle Nepal Adventure — Ethical wildlife safari agency in Nepal"
            else:
                new_alt = generate_seo_alt(src, old_alt, os.path.basename(fpath), lang=lang)
            
            clean_tag = re.sub(r'\s+alt=[\"\'][^\"\']*[\"\']', '', tag)
            res = clean_tag.replace('<img', f'<img alt="{new_alt}"', 1)
            total_upgrades += 1
            return res
        return tag

    new_content = re.sub(r'<img[^>]+>', repl_img, content)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Upgraded {total_upgrades} static image alt tags across Astro files!")
