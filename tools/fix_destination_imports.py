import os
import re

for dest_dir, prefix in [
    ('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations', '../../'),
    ('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/destinations', '../../../')
]:
    for f in os.listdir(dest_dir):
        if f.endswith('.astro'):
            fpath = os.path.join(dest_dir, f)
            with open(fpath, 'r', encoding='utf-8') as file:
                c = file.read()
            
            c = re.sub(r'from\s+[\'\"].*?/layouts/Layout\.astro[\'\"]', f"from '{prefix}layouts/Layout.astro'", c)
            c = re.sub(r'from\s+[\'\"].*?/components/Header\.astro[\'\"]', f"from '{prefix}components/Header.astro'", c)
            c = re.sub(r'from\s+[\'\"].*?/components/Footer\.astro[\'\"]', f"from '{prefix}components/Footer.astro'", c)
            c = re.sub(r'from\s+[\'\"].*?/data/tours\.json[\'\"]', f"from '{prefix}data/tours.json'", c)

            with open(fpath, 'w', encoding='utf-8') as file:
                file.write(c)

print("Fixed import prefixes for all destination pages!")
