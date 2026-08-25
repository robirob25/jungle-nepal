import re
import os

tour_images = {
    'bardia-explorateur': 'https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png',
    'jungle-extreme': 'https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png',
    'babai-special': 'https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg',
    'nepal-sauvage': 'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png',
    'bardia-babai-camping': 'https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg',
    'bardia-nuit-sauvage': 'https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png',
    'chitwan-culture': 'https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png',
    'chitwan-bardia-complete': 'https://junglenepal.com/wp-content/uploads/2025/03/68.png',
    'nepal-immersion-totale': 'https://junglenepal.com/wp-content/uploads/2025/12/Elephant-sauvage-Bardia.png',
    'rafting-safari': 'https://junglenepal.com/wp-content/uploads/2017/01/IMG_0140-scaled.jpg',
    'rara-lake-bardia': 'https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg',
    'tiji-mustang': 'https://junglenepal.com/wp-content/uploads/2026/01/Machapuchare-himalaya-montagne.png',
    'carnet-de-voyage': 'https://junglenepal.com/wp-content/uploads/2025/03/79.png',
    'immersion-spirituelle': 'https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg'
}

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for short_id, img_url in tour_images.items():
    # Matches href="tours/{short_id}.html" ... <img src="..."
    pattern = rf'(<a\s+href="tours/{short_id}\.html"[^>]*>\s*<img\s+src=")[^"]+(")'
    html = re.sub(pattern, rf'\g<1>{img_url}\g<2>', html)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html trip cards with distinct HD photos!")

# 2. Update destinations/*.html
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
for fname in os.listdir(dest_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(dest_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        dhtml = f.read()
    
    for short_id, img_url in tour_images.items():
        pattern = rf'(<a\s+href="(?:\.\./)?tours/{short_id}\.html"[^>]*>\s*<img\s+src=")[^"]+(")'
        dhtml = re.sub(pattern, rf'\g<1>{img_url}\g<2>', dhtml)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(dhtml)

print("Updated all destination pages with distinct HD photos!")

# 3. Final Verification
for page in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html',
             '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/bardia.html',
             '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/chitwan.html',
             '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/suklaphanta.html',
             '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/annapurna.html',
             '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/katmandou.html']:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'<a\s+href=[\"\'](?:\.\./)?tours/([^\"]+)\.html[\"\'][^>]*>\s*<img\s+src=[\"\']([^\"\']+)[\"\']', content)
    seen = {}
    print(f"\nAudit {os.path.basename(page)}: {len(matches)} cards")
    for t_slug, img in matches:
        if img in seen:
            print(f"❌ ERROR: Duplicate {t_slug} with {seen[img]}")
        else:
            seen[img] = t_slug
            print(f"  ✅ {t_slug:25} -> {os.path.basename(img)}")
