import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 16. Langur gris cri d'alarme
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500938343.jpg",
        "fname": "langur_gris_cri_alarme.webp",
        "title": "Semnopithèque ardoisé (Cri d'alarme)",
        "desc": "Cri d'alerte puissant signalant la présence d'un tigre à proximité",
        "location": "Canopée de Bardia",
        "category": "mammiferes"
    },
    # 17. Aigle serpentaire en vol
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500938483.jpg",
        "fname": "aigle_serpentaire_vol.webp",
        "title": "Aigle serpentaire en plein vol",
        "desc": "Rapace majestueux aux ailes rayées fendant la forêt",
        "location": "Parc National de Bardia",
        "category": "oiseaux"
    },
    # 18. Éléphant de face dans la jungle
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500939431.jpg",
        "fname": "elephant_asie_face_jungle.webp",
        "title": "Éléphant d'Asie de face",
        "desc": "Rencontre puissante et frontale au cœur de la jungle primaire",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    # 19. Langur sentinelle sur termitière
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500939458.jpg",
        "fname": "langur_sentinelle_termitiere.webp",
        "title": "Langur gris sentinelle",
        "desc": "Observation attentive de la plaine depuis une racine haute",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
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
