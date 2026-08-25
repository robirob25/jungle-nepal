import urllib.request, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife'
os.makedirs(dest_dir, exist_ok=True)

specific_files = [
    # Owls / Chouettes
    ("Petit_duc_indien_1.webp", "1WmaR8DcABmYk0_Km-WmX78ssIZFn7xoH"),
    ("Petit_duc_indien_2.webp", "1xrmZ4M03c6hCT0RXJ1JR-zebIwqsvAhi"),
    ("Chevechette_de_jungle_1.webp", "1QbOOEa5ywm3w8htCk7FqivzN8O6yY9vH"),
    ("Chevechette_de_jungle_2.webp", "1dVXIkoGkpjNyTmeNmo5P_v3U9VkxeY27"),
    # Lizards & Reptiles
    ("Varan_du_Bengale_2.webp", "1S3Qqh7XJKeKYPoxE6_LSSg9RaTQzj4Mb"), # or additional reptile
]

for fname, fid in specific_files:
    target_webp = os.path.join(dest_dir, fname)
    if os.path.exists(target_webp) and os.path.getsize(target_webp) > 5000:
        print(f"Already exists: {fname}")
        continue
    
    url = f"https://lh3.googleusercontent.com/d/{fid}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 5000:
                tmp_jpg = target_webp.replace('.webp', '.jpg')
                with open(tmp_jpg, 'wb') as f:
                    f.write(data)
                
                img = Image.open(tmp_jpg).convert('RGB')
                max_w = 2048
                if img.size[0] > max_w:
                    ratio = max_w / float(img.size[0])
                    new_h = int(float(img.size[1]) * ratio)
                    img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
                img.save(target_webp, 'WEBP', quality=88, method=6)
                if os.path.exists(tmp_jpg):
                    os.remove(tmp_jpg)
                print(f"✓ Downloaded & Saved: {fname} ({img.size})")
    except Exception as e:
        print(f"✗ Failed {fname}: {e}")

