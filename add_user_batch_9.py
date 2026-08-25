import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

new_batch = [
    # 33. Ibis noir à cou rouge
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501503231.jpg",
        "fname": "ibis_noir_cou_rouge.webp",
        "title": "Ibis noir à cou rouge (Red-naped Ibis)",
        "desc": "Grand échassier au long bec incurvé sondant les zones humides",
        "location": "Plaines du Terai",
        "category": "oiseaux"
    },
    # 34. Marabout chevelu posé
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501503268.jpg",
        "fname": "marabout_chevelu_pose_marais.webp",
        "title": "Marabout chevelu en affût",
        "desc": "Silhouette austère et fascinante dominant les herbes inondées",
        "location": "Zones humides de Bardia",
        "category": "oiseaux"
    },
    # 35. Perruche à tête prune
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501503318.jpg",
        "fname": "perruche_tete_prune_fleur.webp",
        "title": "Perruche à tête prune",
        "desc": "Plumage multicolore éclatant se nourrissant du nectar d'une fleur",
        "location": "Canopée de Bardia",
        "category": "oiseaux"
    },
    # 36. Rhinocéros et oiseaux pique-bœufs
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501503377.jpg",
        "fname": "rhino_unicorne_oiseaux_pique_boeuf.webp",
        "title": "Rhinocéros unicorne et martins",
        "desc": "Symbiose naturelle dans les herbes à éléphant de Chitwan",
        "location": "Parc National de Chitwan",
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
