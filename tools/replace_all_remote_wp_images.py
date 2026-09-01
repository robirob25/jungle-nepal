import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# Map old remote WordPress URLs to modern local WebP assets
url_map = {
    'https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg': '/assets/original_site/tigre_bardia.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png': '/assets/original_site/tigre_bardia.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png': '/assets/original_site/chitwan_rhino.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg': '/assets/original_site/suklaphanta.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/himalayas-5817277_1920.jpg': '/assets/original_site/machapuchare.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg': '/assets/original_site/temple_sacred.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg': '/assets/original_site/nepal_landscape.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/1.png': '/assets/original_site/fishtail_sacred_himalaya.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg': '/assets/original_site/himalayas_sunrise_peaks.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg': '/assets/original_site/suklaphanta.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg': '/assets/original_site/bivouac_camp.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg': '/assets/original_site/temple_sacred.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg': '/assets/original_site/temple_sacred.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png': '/assets/original_site/safari_pied.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png': '/assets/original_site/safari_pied.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png': '/assets/original_site/tigre_route.webp',
    'https://junglenepal.com/wp-content/uploads/2025/12/Tharu-danse.png': '/assets/original_site/babai_walk.webp',
    'https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg': '/assets/original_site/elephants_river.webp',
}

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    for old_url, new_url in url_map.items():
        c = c.replace(old_url, new_url)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Replaced remote WP image URLs in {fpath.split('/')[-1]}")

print("Done converting all remote image URLs to reliable local assets!")
