import json
import os
import re

tour_images = {
    'nepal-sauvage': 'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png',
    'babai-special': 'https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg',
    'bardia-explorateur': 'https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png',
    'bardia-babai-camping': 'https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg',
    'bardia-nuit-sauvage': 'https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png',
    'jungle-extreme': 'https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png',
    'chitwan-culture': 'https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png',
    'chitwan-bardia-complete': 'https://junglenepal.com/wp-content/uploads/2025/03/68.png',
    'nepal-immersion-totale': 'https://junglenepal.com/wp-content/uploads/2025/12/Elephant-sauvage-Bardia.png',
    'rafting-safari': 'https://junglenepal.com/wp-content/uploads/2017/01/IMG_0140-scaled.jpg',
    'rara-lake-bardia': 'https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg',
    'tiji-mustang': 'https://junglenepal.com/wp-content/uploads/2026/01/Machapuchare-himalaya-montagne.png',
    'carnet-de-voyage': 'https://junglenepal.com/wp-content/uploads/2025/03/79.png',
    'immersion-spirituelle': 'https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg'
}

# 1. Update processed_tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    short_id = t['short_id']
    if short_id in tour_images:
        t['hero_img'] = tour_images[short_id]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

print("1. Updated processed_tours.json with 14 unique images")

# 2. Update index.html tour cards
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for short_id, img_url in tour_images.items():
    # Replace img src in card for this tour
    pattern = rf'(<a href="tours/{short_id}\.html"[^>]*>\s*<img src=")[^"]+(")'
    html = re.sub(pattern, rf'\g<1>{img_url}\g<2>', html)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("2. Updated index.html with 14 unique images")

# 3. Update all destination pages (bardia.html, chitwan.html, suklaphanta.html, annapurna.html, katmandou.html)
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
for fname in os.listdir(dest_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(dest_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    
    for short_id, img_url in tour_images.items():
        pattern = rf'(<a href="\.\./tours/{short_id}\.html"[^>]*>\s*<img src=")[^"]+(")'
        dhtml = re.sub(pattern, rf'\g<1>{img_url}\g<2>', dhtml)
        pattern2 = rf'(<a href="{short_id}\.html"[^>]*>\s*<img src=")[^"]+(")'
        dhtml = re.sub(pattern2, rf'\g<1>{img_url}\g<2>', dhtml)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(dhtml)

print("3. Updated all destination pages with 14 unique images")

# 4. Verification of zero duplicates in any page
for page_path in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html',
                  '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/bardia.html',
                  '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/chitwan.html']:
    with open(page_path, 'r', encoding='utf-8') as f:
        c = f.read()
    page_cards = re.findall(r'<a href=[\"\'](?:\.\./)?tours/([^\"]+)\.html[\"\'][^>]*>\s*<img src=[\"\']([^\"\']+)[\"\']', c)
    seen = {}
    print(f"\n--- Checking {os.path.basename(page_path)} ({len(page_cards)} cards) ---")
    for t_slug, img in page_cards:
        if img in seen:
            print(f"❌ DUPLICATE DETECTED: {t_slug} shares image with {seen[img]} ({img})")
        else:
            seen[img] = t_slug
            print(f"✅ {t_slug} -> {os.path.basename(img)}")

