import os
import re

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours'
en_tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours'

# In FR tour pages:
for f in os.listdir(tours_dir):
    if f.endswith('.astro'):
        slug = f[:-6]
        fpath = os.path.join(tours_dir, f)
        with open(fpath, 'r', encoding='utf-8') as file:
            c = file.read()
        
        # replace href="slug.html" with href="/tours/slug.html"
        c = re.sub(rf'href=[\'\"]{slug}\.html[\'\"]', f'href="/tours/{slug}.html"', c)
        c = re.sub(rf'href=[\'\"]\./{slug}\.html[\'\"]', f'href="/tours/{slug}.html"', c)
        
        with open(fpath, 'w', encoding='utf-8') as file:
            file.write(c)

# In EN tour pages:
for f in os.listdir(en_tours_dir):
    if f.endswith('.astro'):
        slug = f[:-6]
        fpath = os.path.join(en_tours_dir, f)
        with open(fpath, 'r', encoding='utf-8') as file:
            c = file.read()
        
        # replace href="slug.html" with href="/en/tours/slug.html"
        c = re.sub(rf'href=[\'\"]{slug}\.html[\'\"]', f'href="/en/tours/{slug}.html"', c)
        c = re.sub(rf'href=[\'\"]\./{slug}\.html[\'\"]', f'href="/en/tours/{slug}.html"', c)
        
        with open(fpath, 'w', encoding='utf-8') as file:
            file.write(c)

print("Fixed all tour language switcher links!")
