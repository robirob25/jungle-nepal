import os
from PIL import Image

all_photos = [
    # 1. Tiger water
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484468073.jpg", 
     "wildlife_tiger_water.webp", "Tigre du Bengale", "Regard au point d'eau", "Parc National de Bardia", "felins"),
    
    # 2. Rhino mist
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484467595.jpg", 
     "wildlife_rhino_mist.webp", "Grand Rhinocéros unicorne", "Brume matinale dans les hautes herbes", "Parc National de Chitwan", "geants"),
    
    # 3. Tiger jungle walking
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484466398.jpg", 
     "wildlife_tiger_jungle.webp", "Tigre royal en pistage", "Marquage de territoire en forêt de Sal", "Vallée secrète de Babai", "felins"),
    
    # 4. Deer plain
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484466751.jpg", 
     "wildlife_deer_plain.webp", "Cerfs des marais (Barasingha)", "Duo au cœur de la savane", "Parc National de Suklaphanta", "herbivores"),
    
    # 5. Nilgai forest
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484467587.jpg", 
     "wildlife_nilgai_forest.webp", "Antilopes Nilgaut", "Mère et jeune en lisière", "Parc National de Bardia", "herbivores"),
    
    # 6. Elephant jungle
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484543073.jpg", 
     "wildlife_elephant_jungle.webp", "Éléphant sauvage d'Asie", "Mâle solitaire sur le sentier de jungle", "Forêt primaire de Bardia", "geants"),
    
    # 7. Tiger stalk
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484542419.jpg", 
     "wildlife_tiger_stalk.webp", "Tigresse en approche silencieuse", "Traque pédestre à 50 mètres", "Parc National de Bardia", "felins"),
    
    # 8. Croco water
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484541982.jpg", 
     "wildlife_croco_water.webp", "Crocodile des marais (Mugger)", "Affût et reflet parfait dans les eaux calmes", "Rivière Rapti & Karnali", "reptiles"),
    
    # 9. Hornbill Calao
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484540865.jpg", 
     "wildlife_calao_hornbill.webp", "Grand Calao bicorne", "Sentinelle de la canopée", "Forêts de Chitwan & Bardia", "oiseaux"),
    
    # 10. Marabout flight
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484606664.jpg", 
     "wildlife_marabout_flight.webp", "Marabout chevelu en vol", "Envol au-dessus des plaines dorées à l'aube", "Zones humides du Terai", "oiseaux"),
    
    # 11. Peacock wheel
    ("/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787484607170.jpg", 
     "wildlife_peacock_wheel.webp", "Paon bleu en parade", "Déploiement majestueux de la roue", "Lisières sauvages de Bardia", "oiseaux"),
]

out_dir = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery"
os.makedirs(out_dir, exist_ok=True)

processed_metadata = []

for src, fname, title, desc, loc, cat in all_photos:
    img = Image.open(src).convert('RGB')
    max_w = 2048
    if img.size[0] > max_w:
        ratio = max_w / float(img.size[0])
        new_h = int(float(img.size[1]) * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    
    out_path = os.path.join(out_dir, fname)
    img.save(out_path, 'WEBP', quality=88, method=6)
    
    # Also save as hero slide in /assets/hero/
    hero_path = os.path.join("/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/hero", fname)
    img.save(hero_path, 'WEBP', quality=88, method=6)

    size_kb = os.path.getsize(out_path) / 1024.0
    print(f"Processed {fname}: {img.size} ({size_kb:.1f} KB)")
    
    processed_metadata.append({
        "file": f"/assets/wildlife_gallery/{fname}",
        "title": title,
        "desc": desc,
        "location": loc,
        "category": cat
    })

import json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(processed_metadata, f, indent=2, ensure_ascii=False)

print("\nSaved 11 wildlife photos with full metadata in src/data/wildlife_gallery.json!")
