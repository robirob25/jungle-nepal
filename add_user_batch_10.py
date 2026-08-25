import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 37. Rollier indien sur bois mort
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501514945.jpg",
        "fname": "rollier_indien_branche_morte.webp",
        "title": "Rollier indien sur branche haute",
        "desc": "Oiseau aux teintes saphir et améthyste sur fond épuré",
        "location": "Plaines de Suklaphanta",
        "category": "oiseaux"
    },
    # 38. Aigle serpentaire & Drongo
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501514970.jpg",
        "fname": "aigle_serpentaire_drongo_ciel.webp",
        "title": "Aigle serpentaire et Drongo",
        "desc": "Combat aérien spectaculaire au-dessus de la canopée",
        "location": "Ciel de Bardia",
        "category": "oiseaux"
    },
    # 39. Tigre en embuscade verticale
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501514974.jpg",
        "fname": "tigre_bengale_embuscade_vertical.webp",
        "title": "Regard perçant du Tigre",
        "desc": "Portrait vertical captivant du grand félin en affût derrière un tronc",
        "location": "Forêt dense de Bardia",
        "category": "felins"
    },
    # 40. Tigre avançant de face
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501515071.jpg",
        "fname": "tigre_bengale_face_arbre_foret.webp",
        "title": "Tigre du Bengale en approche",
        "desc": "Le roi de la jungle marchant droit vers l'objectif",
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
