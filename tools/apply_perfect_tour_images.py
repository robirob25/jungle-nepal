import json
import os
import re

tour_images = {
    'nepal-sauvage': 'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png',
    'babai-special': 'https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg',
    'bardia-explorateur': 'https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png',
    'bardia-babai-camping': 'https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg',
    'bardia-nuit-sauvage': 'https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png',
    'chitwan-culture': 'https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png',
    'chitwan-bardia-complete': 'https://junglenepal.com/wp-content/uploads/2025/03/68.png',
    'nepal-immersion-totale': 'https://junglenepal.com/wp-content/uploads/2025/12/Elephant-sauvage-Bardia.png',
    'rafting-safari': 'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png',
    'rara-lake-bardia': 'https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg',
    'jungle-extreme': 'https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png',
    'tiji-mustang': 'https://junglenepal.com/wp-content/uploads/2017/01/himalayas-5817277_1920.jpg',
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

print("Updated processed_tours.json with high-res cover photos!")

# 2. Update update_tailored_destinations.py and re-run it
import update_tailored_destinations

# 3. Update all tour cards in index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for short_id, img_url in tour_images.items():
    # Replace any blurry image in card for this tour
    # Matches href="tours/{short_id}.html" block
    pattern = rf'(<a href="tours/{short_id}\.html"[^>]*>\s*<img src=")[^"]+(")'
    html = re.sub(pattern, rf'\g<1>{img_url}\g<2>', html)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html and all destination pages with perfect tour cover photos!")
