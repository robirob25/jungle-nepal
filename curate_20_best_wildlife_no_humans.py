import json, os

# Master 20-22 curated elite wildlife photographs (100% Animals, 0% Humans)
curated_masterpieces = [
    # ==================== 🐅 FÉLINS (6 clichés d'exception) ====================
    {
        "file": "/assets/wildlife_gallery/wildlife_tiger_water.webp",
        "title": "Tigre du Bengale au crépuscule",
        "desc": "Mâle dominant venant s'abreuver sur les berges fluviales de Bardia",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_tiger_stalk.webp",
        "title": "Tigresse en approche silencieuse",
        "desc": "Avancée furtive dans la canopée et les herbes de sous-bois",
        "location": "Vallée sauvage de Babai",
        "category": "felins"
    },
    {
        "file": "/assets/wildlife_gallery/julien_tigre_bengale2.webp",
        "title": "Tigre royal en lisière",
        "desc": "Traversée majestueuse d'une clairière au pas ralenti",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_tiger_jungle.webp",
        "title": "Tigre du Bengale en territoire",
        "desc": "Marquage et surveillance d'un sentier de chasse ancestral",
        "location": "Bardia National Park",
        "category": "felins"
    },
    {
        "file": "/assets/wildlife_gallery/julien_leopard_indien.webp",
        "title": "Léopard indien en affût",
        "desc": "Le grand félin camouflé sur sa branche maîtresse",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "file": "/assets/wildlife_gallery/snow_leopard_portrait.webp",
        "title": "Panthère des neiges",
        "desc": "Le fantôme des falaises himalayennes à plus de 4 000 m",
        "location": "Haut Mustang & Annapurna",
        "category": "felins"
    },

    # ==================== 🐘 GRANDS MAMMIFÈRES (6 clichés d'exception) ====================
    {
        "file": "/assets/wildlife_gallery/wildlife_elephant_jungle.webp",
        "title": "Éléphant d'Asie sauvage",
        "desc": "Grand mâle solitaire émergeant des forêts denses de Sal",
        "location": "Forêt primaire de Bardia",
        "category": "mammiferes"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_rhino_mist.webp",
        "title": "Grand Rhinocéros unicorne",
        "desc": "Silhouette préhistorique dans les brumes matinales du fleuve",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    {
        "file": "/assets/wildlife_gallery/julien_elephant_mere_petit.webp",
        "title": "Éléphante d'Asie et son éléphanteau",
        "desc": "Moment d'intimité et de protection maternelle au cœur de la jungle",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "file": "/assets/wildlife_gallery/chitwan_rhino.webp",
        "title": "Rhinocéros unicorne au pâturage",
        "desc": "Colosse cuirassé broutant paisiblement dans la savane",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_deer_plain.webp",
        "title": "Cerfs des marais (Barasingha)",
        "desc": "Duo de grands cerfs aux aguets dans les prairies dorées",
        "location": "Parc National de Suklaphanta",
        "category": "mammiferes"
    },
    {
        "file": "/assets/drive_wildlife/Semnopith_que_ardois__1.webp",
        "file_alt": "/assets/wildlife_gallery/julien_cerf_axis.webp",
        "title": "Cerf Axis tacheté (Chital)",
        "desc": "Hardes vigilantes en sous-bois attentives aux appels d'alarme",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },

    # ==================== 🦚 OISEAUX (6 clichés d'exception) ====================
    {
        "file": "/assets/wildlife_gallery/wildlife_calao_hornbill.webp",
        "title": "Grand Calao bicorne",
        "desc": "Sentinelle spectaculaire perchée au sommet de la canopée",
        "location": "Parc National de Chitwan",
        "category": "oiseaux"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_peacock_wheel.webp",
        "title": "Paon bleu en parade nuptiale",
        "desc": "Déploiement féerique de la roue au soleil levant",
        "location": "Lisières sauvages de Bardia",
        "category": "oiseaux"
    },
    {
        "file": "/assets/drive_wildlife/Martin_chasseur_de_Smyrne_1.webp",
        "title": "Martin-chasseur de Smyrne",
        "desc": "Plumage bleu électrique éclatant en affût sur une branche",
        "location": "Zones humides de Bardia",
        "category": "oiseaux"
    },
    {
        "file": "/assets/drive_wildlife/Gu_pier_d_orient_11.webp",
        "title": "Guêpier d'Orient",
        "desc": "Oiseau acrobatique aux reflets émeraude et dorés",
        "location": "Plaines du Terai",
        "category": "oiseaux"
    },
    {
        "file": "/assets/wildlife_gallery/julien_rollier_oiseau.webp",
        "title": "Rollier indien (Indian Roller)",
        "desc": "Oiseau sacré aux ailes bleu turquoise éclatantes",
        "location": "Savanes de Suklaphanta",
        "category": "oiseaux"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_marabout_flight.webp",
        "title": "Marabout chevelu en vol",
        "desc": "Envol majestueux au-dessus des prairies inondables",
        "location": "Zones humides du Terai",
        "category": "oiseaux"
    },

    # ==================== 🐊 REPTILES & RIVIÈRES (3 clichés d'exception) ====================
    {
        "file": "/assets/wildlife_gallery/wildlife_croco_water.webp",
        "title": "Crocodile des marais (Mugger)",
        "desc": "Prédateur à fleur d'eau avec reflet miroir parfait",
        "location": "Rivière Rapti • Chitwan",
        "category": "reptiles"
    },
    {
        "file": "/assets/wildlife_gallery/julien_gangetic_dolphin.webp",
        "title": "Dauphin d'eau douce du Gange",
        "desc": "Émersion furtive d'un dauphin sauvage dans les rapides",
        "location": "Fleuve Karnali • Bardia",
        "category": "reptiles"
    },
    {
        "file": "/assets/wildlife_gallery/wildlife_nilgai_forest.webp",
        "title": "Antilopes Nilgaut (Taureau bleu)",
        "desc": "La plus grande antilope d'Asie en lisière forestière",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    }
]

# Verify all file paths exist
validated_photos = []
for p in curated_masterpieces:
    fpath = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public" + p['file']
    if os.path.exists(fpath):
        validated_photos.append(p)
    elif "file_alt" in p and os.path.exists("/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public" + p['file_alt']):
        p['file'] = p['file_alt']
        validated_photos.append(p)
    else:
        print(f"Warning missing: {p['file']}")

print(f"Total curated masterpieces (0% humans, 100% wild animals): {len(validated_photos)}")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(validated_photos, f, indent=2, ensure_ascii=False)

