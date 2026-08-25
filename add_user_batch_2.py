import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 5. Grand Calao bicorne
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500680327.jpg",
        "fname": "calao_bicorne_canopee.webp",
        "title": "Grand Calao bicorne",
        "desc": "Sentinelle spectaculaire au sommet de la canopée",
        "location": "Parc National de Chitwan",
        "category": "oiseaux"
    },
    # 6. Crocodile des marais
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500680387.jpg",
        "fname": "crocodile_marais_rapti.webp",
        "title": "Crocodile des marais (Mugger)",
        "desc": "Prédateur à fleur d'eau avec reflet miroir limpide",
        "location": "Rivière Rapti • Chitwan",
        "category": "reptiles"
    },
    # 7. Grand Rhinocéros unicorne
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500680481.jpg",
        "fname": "rhino_unicorne_brume.webp",
        "title": "Grand Rhinocéros unicorne",
        "desc": "Silhouette préhistorique dans les brumes matinales",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    # 8. Tigre en marche
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500680490.jpg",
        "fname": "tigre_bengale_pistage.webp",
        "title": "Tigre du Bengale royal",
        "desc": "Progression puissante à travers la végétation dense",
        "location": "Parc National de Bardia",
        "category": "felins"
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
    
    # Avoid duplicates if already added
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
