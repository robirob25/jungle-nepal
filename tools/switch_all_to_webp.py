import os, glob, re, json

# 1. Update tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    if t.get('image'):
        base, _ = os.path.splitext(t['image'])
        webp_disk = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public' + base + '.webp'
        if os.path.exists(webp_disk):
            t['image'] = base + '.webp'
    if t.get('gallery'):
        new_gal = []
        for g in t['gallery']:
            base, _ = os.path.splitext(g)
            webp_disk = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public' + base + '.webp'
            if os.path.exists(webp_disk):
                new_gal.append(base + '.webp')
            else:
                new_gal.append(g)
        t['gallery'] = new_gal

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

# 2. Update all .astro source files
astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)
updated_count = 0

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    orig = c
    # Replace .jpg, .jpeg, .png with .webp if the .webp file exists in public/
    def replace_webp(match):
        full_path = match.group(0)
        img_url = match.group(1)
        base, ext = os.path.splitext(img_url)
        if ext.lower() in ('.jpg', '.jpeg', '.png') and 'favicon' not in img_url and 'logo' not in img_url:
            webp_disk = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public' + base + '.webp'
            if os.path.exists(webp_disk):
                return full_path.replace(img_url, base + '.webp')
        return full_path

    c = re.sub(r'[\'"](/assets/[^\'"]+\.(?:jpg|jpeg|png))[\'"]', replace_webp, c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_count += 1

print(f"Switched to WebP format across {updated_count} astro files and tours.json!")
