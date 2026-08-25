import json, re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_code = f.read()

# Update each tour card image on index.astro
for t in tours:
    slug = t['slug']
    new_img = t.get('image')
    if not new_img:
        continue

    # Regex find card for this slug
    pattern = rf'(<!-- TRIP CARD:.*?/tours/{slug}\.html.*?<img\s+src=[\'"])[^\'"]+([\'"])'
    idx_code = re.sub(pattern, rf'\g<1>{new_img}\g<2>', idx_code, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_code)

print("Updated homepage tour cards with authentic Google Drive photos!")
