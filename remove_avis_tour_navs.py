import os
import re

for base_dir in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours', '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours']:
    for f in os.listdir(base_dir):
        if not f.endswith('.html'):
            continue
        fpath = os.path.join(base_dir, f)
        with open(fpath, 'r', encoding='utf-8') as file:
            c = file.read()

        # Remove the exact Google reviews link in nav
        pattern = r'<a\s+href=[\"\'][^\"\']*LocalPoiReviews[\"\'][^>]*>.*?</a>\s*'
        c = re.sub(pattern, '', c, flags=re.DOTALL)
        
        # Also remove <a href="#avis-voyageurs"...> or <a href="#avis"...> inside header
        def clean_header(m):
            h = m.group(0)
            h = re.sub(r'<a\s+href=[\"\']#(?:avis|avis-voyageurs)[\"\'][^>]*>.*?</a>\s*', '', h, flags=re.DOTALL)
            return h
        
        c = re.sub(r'<header[^>]*>.*?</header>', clean_header, c, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as file:
            file.write(c)

print("Removed Avis link from all tour navigation headers!")
