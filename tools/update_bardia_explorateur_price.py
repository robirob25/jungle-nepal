import json, re, glob

# 1. Update tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    if t['slug'] == 'bardia-explorateur':
        t['price'] = '490€'

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

# 2. Update Layout.astro priceRange
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('"priceRange": "450€ - 3890€"', '"priceRange": "490€ - 3890€"')
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

# 3. Update all .astro pages where bardia-explorateur card appears or inside bardia-explorateur.astro
astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    is_detail = 'bardia-explorateur.astro' in fpath

    if is_detail:
        content = content.replace('"price": "450"', '"price": "490"')
        content = content.replace('>450€<', '>490€<')
        content = content.replace('450€ <span', '490€ <span')

    # If it's a card linking to /tours/bardia-explorateur.html
    if '/tours/bardia-explorateur.html' in content:
        content = re.sub(
            r'(href=[\'"]/tours/bardia-explorateur\.html[\'"].*?text-jungle-950[^>]*>)450€(<)',
            r'\g<1>490€\g<2>',
            content,
            flags=re.DOTALL
        )
        content = re.sub(
            r'(Bardia explorateur.*?text-jungle-950[^>]*>)450€(<)',
            r'\g<1>490€\g<2>',
            content,
            flags=re.DOTALL
        )

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated price in: {fpath}")

print("Price for Bardia Explorateur successfully updated to 490€!")
