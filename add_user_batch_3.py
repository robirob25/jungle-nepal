import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 9. Marabout chevelu en vol
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500735927.jpg",
        "fname": "marabout_chevelu_envol.webp",
        "title": "Marabout chevelu en vol",
        "desc": "Envol majestueux au-dessus des prairies inondables à l'aube",
        "location": "Zones humides du Terai",
        "category": "oiseaux"
    },
    # 10. Paon bleu en parade
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500680490.jpg",
        "src_actual": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500736756.jpg",
        "fname": "paon_bleu_parade_roue.webp",
        "title": "Paon bleu en parade nuptiale",
        "desc": "Déploiement féerique de la roue au soleil levant",
        "location": "Lisières sauvages de Bardia",
        "category": "oiseaux"
    },
    # 11. Grand Éléphant d'Asie
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500737156.jpg",
        "fname": "elephant_asie_male_jungle.webp",
        "title": "Éléphant sauvage d'Asie",
        "desc": "Grand mâle solitaire émergeant des forêts denses de Sal",
        "location": "Forêt primaire de Bardia",
        "category": "mammiferes"
    }
]

for item in new_batch:
    src = item.get('src_actual', item['src'])
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
