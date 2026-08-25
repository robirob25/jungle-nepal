import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 28. Mangouste indienne
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501147814.jpg",
        "fname": "mangouste_grise_jungle.webp",
        "title": "Mangouste grise d'Inde",
        "desc": "Petit carnivore vif et intrépide en exploration au sol",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    # 29. Chevêchette de jungle (Chouette)
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501491416.jpg",
        "fname": "chevechette_jungle_chouette.webp",
        "title": "Chevêchette de jungle (Chouette)",
        "desc": "Rapace nocturne fascinant aux grands yeux dorés perçants",
        "location": "Forêts de Bardia",
        "category": "oiseaux"
    },
    # 30. Grue antigone
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501491449.jpg",
        "fname": "grue_antigone_savane.webp",
        "title": "Grue antigone (Sarus Crane)",
        "desc": "Le plus grand oiseau volant au monde arpentant les plaines dorées",
        "location": "Marais et savanes du Terai",
        "category": "oiseaux"
    },
    # 31. Chacal doré
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501491801.jpg",
        "fname": "chacal_dore_herbes.webp",
        "title": "Chacal doré (Golden Jackal)",
        "desc": "Canidé sauvage aux yeux d'ambre en déplacement silencieux",
        "location": "Lisières de Bardia",
        "category": "mammiferes"
    },
    # 32. Grand mâle Nilgaut
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501491857.jpg",
        "fname": "nilgaut_male_taureau_bleu.webp",
        "title": "Taureau bleu (Mâle Nilgaut adulte)",
        "desc": "Impressionnant mâle adulte à la robe bleutée et barbiche noire",
        "location": "Parc National de Suklaphanta",
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
