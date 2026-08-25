import json, os, shutil
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

uploaded = [
    # 1. Tiger marking tree in forest
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500663623.jpg",
        "fname": "tiger_territory_marking.webp",
        "title": "Tigre du Bengale en territoire",
        "desc": "Marquage olfactif d'un arbre en forêt primaire",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    # 2. Two deer in plain
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500663840.jpg",
        "fname": "deer_pair_savanna.webp",
        "title": "Cerfs des marais (Barasingha)",
        "desc": "Duo aux aguets dans les prairies dorées du Terai",
        "location": "Parc National de Suklaphanta",
        "category": "mammiferes"
    },
    # 3. Two Nilgai antelopes
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500664133.jpg",
        "fname": "nilgai_mother_calf.webp",
        "title": "Antilopes Nilgaut (Taureau bleu)",
        "desc": "Mère et jeune en lisière forestière de Bardia",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    # 4. Tiger at water pond
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500664380.jpg",
        "fname": "tiger_water_pond.webp",
        "title": "Tigre du Bengale au point d'eau",
        "desc": "Mâle dominant sur les berges d'un point d'eau",
        "location": "Parc National de Bardia",
        "category": "felins"
    }
]

curated_items = []

for item in uploaded:
    src = item['src']
    target_path = os.path.join(dest_dir, item['fname'])
    rel_path = f"/assets/curated_gallery/{item['fname']}"
    
    img = Image.open(src).convert('RGB')
    max_w = 2048
    if img.size[0] > max_w:
        ratio = max_w / float(img.size[0])
        new_h = int(float(img.size[1]) * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    img.save(target_path, 'WEBP', quality=90, method=6)
    print(f"✓ Processed {item['fname']} ({img.size})")
    
    curated_items.append({
        "file": rel_path,
        "title": item['title'],
        "desc": item['desc'],
        "location": item['location'],
        "category": item['category']
    })

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(curated_items, f, indent=2, ensure_ascii=False)

print(f"Saved {len(curated_items)} selected photos to wildlife_gallery.json!")
