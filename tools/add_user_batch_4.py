import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 12. Duo de jeunes rapaces au nid
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500877061.jpg",
        "fname": "duo_rapaces_au_nid.webp",
        "title": "Duo de rapaces au nid",
        "desc": "Deux jeunes aigles observant la canopée depuis leur aire",
        "location": "Parc National de Bardia",
        "category": "oiseaux"
    },
    # 13. Rollier indien perché
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500877910.jpg",
        "fname": "rollier_indien_perche.webp",
        "title": "Rollier indien (Indian Roller)",
        "desc": "Oiseau sacré aux teintes pastel et bleu ciel en affût",
        "location": "Plaines de Suklaphanta",
        "category": "oiseaux"
    },
    # 14. Rollier indien à l'envol
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500878486.jpg",
        "fname": "rollier_indien_envol_turquoise.webp",
        "title": "Rollier indien à l'envol",
        "desc": "Déploiement étincelant des ailes bleu turquoise en plein vol",
        "location": "Parc National de Bardia",
        "category": "oiseaux"
    },
    # 15. Bébé macaque et sa mère
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787500878488.jpg",
        "fname": "bebe_macaque_mere.webp",
        "title": "Bébé singe et sa mère",
        "desc": "Regard innocent et tendresse maternelle au sein de la troupe",
        "location": "Secteur de Bardia & Katmandou",
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
