import os, glob
from PIL import Image

asset_dirs = [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/original_site',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/snow-leopard'
]

converted = 0
total_saved_bytes = 0

for d in asset_dirs:
    for f in os.listdir(d):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.startswith('.'):
            p = os.path.join(d, f)
            if not os.path.isfile(p):
                continue
            base, _ = os.path.splitext(p)
            webp_path = base + '.webp'
            
            try:
                im = Image.open(p)
                orig_size = os.path.getsize(p)
                
                # Convert RGBA or RGB
                if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
                    im.save(webp_path, 'WEBP', quality=88, method=6)
                else:
                    rgb_im = im.convert('RGB')
                    rgb_im.save(webp_path, 'WEBP', quality=84, method=6)
                
                webp_size = os.path.getsize(webp_path)
                saved = orig_size - webp_size
                total_saved_bytes += max(0, saved)
                converted += 1
                print(f"✓ Converted {f} -> {os.path.basename(webp_path)} ({orig_size//1024}KB -> {webp_size//1024}KB)")
            except Exception as e:
                print(f"✗ Failed {f}: {e}")

print(f"\nSuccessfully converted {converted} images to WebP! Total bandwidth saved: {total_saved_bytes//1024} KB")
