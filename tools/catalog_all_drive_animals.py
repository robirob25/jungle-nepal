import os, json
from PIL import Image

# Exhaustive list of all animal photos from Drive and authentic shoots
catalog = [
    # --- FÉLINS ---
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_tiger_water.webp",
        "file": "/assets/wildlife_gallery/wildlife_tiger_water.webp",
        "title": "Tigre du Bengale au point d'eau",
        "desc": "Observation d'un mâle dominant sur les berges au crépuscule",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_tiger_stalk.webp",
        "file": "/assets/wildlife_gallery/wildlife_tiger_stalk.webp",
        "title": "Tigresse en approche silencieuse",
        "desc": "Pistage pédestre en sous-bois dense à 50 mètres",
        "location": "Vallée de Babai",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_tigre_bengale2.webp",
        "file": "/assets/wildlife_gallery/julien_tigre_bengale2.webp",
        "title": "Tigre royal en marche",
        "desc": "Traversée d'une clairière au pas lent et majestueux",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_tiger_jungle.webp",
        "file": "/assets/wildlife_gallery/wildlife_tiger_jungle.webp",
        "title": "Tigre royal en pistage",
        "desc": "Marquage de territoire le long des sentiers ancestraux",
        "location": "Bardia National Park",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_leopard_indien.webp",
        "file": "/assets/wildlife_gallery/julien_leopard_indien.webp",
        "title": "Léopard indien en affût",
        "desc": "Le fantôme discret de la canopée perché sur un grand arbre",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/adrien_tigre1.webp",
        "file": "/assets/wildlife_gallery/adrien_tigre1.webp",
        "title": "Tigre du Bengale face à face",
        "desc": "Moment d'intensité absolue lors d'un safari à pied",
        "location": "Secteur Baghaura • Bardia",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/snow-leopard/snow_leopard_portrait.webp",
        "file": "/assets/wildlife_gallery/snow_leopard_portrait.webp",
        "title": "Panthère des neiges",
        "desc": "Le seigneur insaisissable des falaises himalayennes",
        "location": "Haut Mustang & Annapurna",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_tigre_bengale3.webp",
        "file": "/assets/wildlife_gallery/julien_tigre_bengale3.webp",
        "title": "Tigre au repos sous les banians",
        "desc": "Sieste ombragée aux heures chaudes de l'après-midi",
        "location": "Parc National de Bardia",
        "category": "felins"
    },

    # --- OISEAUX ---
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_calao_hornbill.webp",
        "file": "/assets/wildlife_gallery/wildlife_calao_hornbill.webp",
        "title": "Grand Calao bicorne",
        "desc": "L'oiseau géant sentinelle de la canopée subtropicale",
        "location": "Parc National de Chitwan",
        "category": "oiseaux"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_peacock_wheel.webp",
        "file": "/assets/wildlife_gallery/wildlife_peacock_wheel.webp",
        "title": "Paon bleu en parade nuptiale",
        "desc": "Déploiement spectaculaire de la roue dans les herbes hautes",
        "location": "Lisières sauvages de Bardia",
        "category": "oiseaux"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_marabout_flight.webp",
        "file": "/assets/wildlife_gallery/wildlife_marabout_flight.webp",
        "title": "Marabout chevelu en vol",
        "desc": "Envol majestueux au-dessus des plaines dorées à l'aube",
        "location": "Zones humides du Terai",
        "category": "oiseaux"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_rollier_oiseau.webp",
        "file": "/assets/wildlife_gallery/julien_rollier_oiseau.webp",
        "title": "Rollier indien (Indian Roller)",
        "desc": "Oiseau sacré aux ailes turquoise étincelantes en vol",
        "location": "Plaines de Suklaphanta & Bardia",
        "category": "oiseaux"
    },

    # --- GRANDS MAMMIFÈRES ---
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_elephant_jungle.webp",
        "file": "/assets/wildlife_gallery/wildlife_elephant_jungle.webp",
        "title": "Éléphant sauvage d'Asie",
        "desc": "Mâle solitaire imposant progressant sur une sente forestière",
        "location": "Forêt primaire de Bardia",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_rhino_mist.webp",
        "file": "/assets/wildlife_gallery/wildlife_rhino_mist.webp",
        "title": "Grand Rhinocéros unicorne",
        "desc": "Silhouette préhistorique émergeant des brumes matinales",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_elephant_mere_petit.webp",
        "file": "/assets/wildlife_gallery/julien_elephant_mere_petit.webp",
        "title": "Éléphante d'Asie et son éléphanteau",
        "desc": "Scène émouvante d'apprentissage et de protection maternelle",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/original_site/chitwan_rhino.webp",
        "file": "/assets/wildlife_gallery/chitwan_rhino.webp",
        "title": "Rhinocéros unicorne au pâturage",
        "desc": "Le géant cuirassé broutant paisiblement dans la savane",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_deer_plain.webp",
        "file": "/assets/wildlife_gallery/wildlife_deer_plain.webp",
        "title": "Cerfs des marais (Barasingha)",
        "desc": "Duo vigilant aux aguets au cœur des vastes prairies",
        "location": "Parc National de Suklaphanta",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_cerf_axis.webp",
        "file": "/assets/wildlife_gallery/julien_cerf_axis.webp",
        "title": "Cerf Axis tacheté (Chital)",
        "desc": "Le cerf emblématique compagne d'alerte des singes langurs",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_nilgai_forest.webp",
        "file": "/assets/wildlife_gallery/wildlife_nilgai_forest.webp",
        "title": "Antilopes Nilgaut (Taureau bleu)",
        "desc": "La plus grande antilope d'Asie en lisière de forêt",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_cerf_cochon.webp",
        "file": "/assets/wildlife_gallery/julien_cerf_cochon.webp",
        "title": "Cerf-cochon (Hog Deer)",
        "desc": "Petit cervidé discret évoluant dans les herbes éléphant",
        "location": "Prairies inondables de Chitwan",
        "category": "mammiferes"
    },

    # --- REPTILES & RIVIÈRES ---
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/wildlife_croco_water.webp",
        "file": "/assets/wildlife_gallery/wildlife_croco_water.webp",
        "title": "Crocodile des marais (Mugger)",
        "desc": "Prédateur à l'affût avec reflet spectaculaire sur l'eau",
        "location": "Rivière Rapti • Chitwan",
        "category": "reptiles"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/original_site/elephants_river.webp",
        "file": "/assets/wildlife_gallery/elephants_river.webp",
        "title": "Troupeau d'éléphants à la baignade",
        "desc": "Rafraîchissement collectif dans les eaux limpides de la rivière",
        "location": "Rivière Karnali • Bardia",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_gangetic_dolphin.webp",
        "file": "/assets/wildlife_gallery/julien_gangetic_dolphin.webp",
        "title": "Dauphin d'eau douce du Gange",
        "desc": "Espèce rarissime en voie d'extinction nageant dans les rapides",
        "location": "Fleuve Karnali • Bardia",
        "category": "reptiles"
    },
]

out_dir = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery"
os.makedirs(out_dir, exist_ok=True)

processed_items = []

for item in catalog:
    src = item['src']
    target = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public" + item['file']
    
    # If source exists and target does not or needs webp
    if os.path.exists(src):
        img = Image.open(src).convert('RGB')
        max_w = 2048
        if img.size[0] > max_w:
            ratio = max_w / float(img.size[0])
            new_h = int(float(img.size[1]) * ratio)
            img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
        img.save(target, 'WEBP', quality=88, method=6)
        print(f"Verified & saved {item['file']} ({img.size})")
        processed_items.append(item)
    else:
        print(f"Warning: source missing {src}")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(processed_items, f, indent=2, ensure_ascii=False)

print(f"\nTotal verified animal photos in gallery: {len(processed_items)}")
