import os
from PIL import Image

new_imgs = [
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484543073.jpg", "hero_6_elephant_jungle.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484542419.jpg", "hero_7_tiger_stalk.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484541982.jpg", "hero_8_croco_water.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484540865.jpg", "hero_9_calao_hornbill.webp"),
]

out_dir = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/hero"
os.makedirs(out_dir, exist_ok=True)

for src, out_name in new_imgs:
    img = Image.open(src).convert('RGB')
    max_w = 2048
    if img.size[0] > max_w:
        ratio = max_w / float(img.size[0])
        new_h = int(float(img.size[1]) * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    
    out_path = os.path.join(out_dir, out_name)
    img.save(out_path, 'WEBP', quality=88, method=6)
    size_kb = os.path.getsize(out_path) / 1024.0
    print(f"Processed {out_name}: {img.size} ({size_kb:.1f} KB)")

print("Processed all 4 new hero background photos!")
