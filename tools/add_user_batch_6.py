import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 20. Duo de Martins-chasseurs
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501120404.jpg",
        "fname": "duo_martins_chasseurs.webp",
        "title": "Duo de Martins-chasseurs",
        "desc": "Couple d'oiseaux pêcheurs au plumage bleu turquoise éclatant",
        "location": "Zones humides de Bardia",
        "category": "oiseaux"
    },
    # 21. Cerf Sambar dans l'eau
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501120412.jpg",
        "fname": "cerf_sambar_dans_eau.webp",
        "title": "Cerf Sambar à la baignade",
        "desc": "Grand cervidé traversant un bras de rivière aux reflets dorés",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    # 22. Portrait d'éléphant d'Asie
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501120638.jpg",
        "fname": "portrait_elephant_asie.webp",
        "title": "Portrait d'Éléphant d'Asie",
        "desc": "Gros plan saisissant sur le regard et les défenses d'un vieux mâle",
        "location": "Forêt primaire de Bardia",
        "category": "mammiferes"
    },
    # 23. Varan du Bengale sur tronc
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501120864.jpg",
        "fname": "varan_bengale_arbre.webp",
        "title": "Varan du Bengale (Lézard géant)",
        "desc": "Grand reptile préhistorique escaladant le tronc d'un banian",
        "location": "Parc National de Bardia",
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
