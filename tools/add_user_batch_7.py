import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 24. Roussette géante en vol
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501131708.jpg",
        "fname": "roussette_chauve_souris_vol.webp",
        "title": "Roussette géante d'Inde en vol",
        "desc": "Grand mammifère ailé fendant la canopée au crépuscule",
        "location": "Canopée de Bardia & Katmandou",
        "category": "mammiferes"
    },
    # 25. Tigre dans les herbes
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501131748.jpg",
        "fname": "tigre_bengale_hautes_herbes.webp",
        "title": "Tigre du Bengale dans la savane",
        "desc": "Fauve en déplacement au milieu des herbes à éléphant",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    # 26. Pic à dos d'or
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501131873.jpg",
        "fname": "pic_flamboyant_ailes_or.webp",
        "title": "Pic à dos d'or (Flameback)",
        "desc": "Oiseau spectaculaire déployant ses ailes dorées sur une branche morte",
        "location": "Forêts de Bardia",
        "category": "oiseaux"
    },
    # 27. Serpent sur tronc fleuri
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501131895.jpg",
        "fname": "serpent_jungle_tronc_fleuri.webp",
        "title": "Serpent de la jungle en affût",
        "desc": "Reptile grimpant enroulé autour d'un vieux tronc fleuri",
        "location": "Zones humides de Bardia",
        "category": "reptiles"
    }
]

for item in new_batch:
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
    
    if not any(i['file'] == rel_path for i in items):
        items.append({
            "file": rel_path,
            "title": item['title'],
            "desc": item['desc'],
            "location": item['location'],
            "category": item['category']
        })

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"Total curated photos now: {len(items)}")
