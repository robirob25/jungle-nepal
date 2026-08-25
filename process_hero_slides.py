import os
from PIL import Image

src_imgs = [
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484468073.jpg", "hero_1_tiger_water.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484467595.jpg", "hero_2_rhino_mist.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484466398.jpg", "hero_3_tiger_jungle.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484466751.jpg", "hero_4_deer_plain.webp"),
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484467587.jpg", "hero_5_nilgai_forest.webp"),
]

out_dir = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/hero"
os.makedirs(out_dir, exist_ok=True)

for src, out_name in src_imgs:
    img = Image.open(src).convert('RGB')
    
    # Resize keeping aspect ratio, max width 2048px
    max_w = 2048
    if img.size[0] > max_w:
        ratio = max_w / float(img.size[0])
        new_h = int(float(img.size[1]) * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    
    out_path = os.path.join(out_dir, out_name)
    img.save(out_path, 'WEBP', quality=88, method=6)
    size_kb = os.path.getsize(out_path) / 1024.0
    print(f"Processed {out_name}: {img.size} ({size_kb:.1f} KB)")

print("All 5 hero background photos successfully converted to WebP!")
