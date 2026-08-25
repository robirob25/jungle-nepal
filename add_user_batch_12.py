import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 42. Tigre baignade
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501736938.jpg",
        "fname": "tigre_bengale_baignade_eau.webp",
        "title": "Tigre du Bengale à la baignade",
        "desc": "Moment intime de fraîcheur dans un point d'eau sauvage",
        "location": "Plaines inondables de Bardia",
        "category": "felins"
    },
    # 43. Lézard agame
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501745361.jpg",
        "fname": "lezard_agame_jardin_camouflage.webp",
        "title": "Agame des jardins (Lézard arboricole)",
        "desc": "Camouflage subtil parmi les branchages et feuillages",
        "location": "Bordures forestières de Bardia",
        "category": "reptiles"
    },
    # 44. Rapace au nid
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501747490.jpg",
        "fname": "aigle_au_nid_observation.webp",
        "title": "Aigle dans son aire séculaire",
        "desc": "Regard perçant et plumage doré dominant la vallée",
        "location": "Canopée de Bardia",
        "category": "oiseaux"
    },
    # 45. Élanion blanc en vol piqué
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501760396.jpg",
        "fname": "elanion_blanc_vol_pique.webp",
        "title": "Élanion blanc en piqué",
        "desc": "Plumage blanc immaculé et serres déployées dans le ciel d'azur",
        "location": "Plaines ouvertes de Suklaphanta",
        "category": "oiseaux"
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
