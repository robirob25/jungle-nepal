import json, re, os

# ==================== 1. FÉLINS (20 photos) ====================
felins = [
    {"file": "/assets/wildlife_gallery/wildlife_tiger_water.webp", "title": "Tigre du Bengale au point d'eau", "desc": "Mâle dominant venant s'abreuver sur les berges au crépuscule", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/wildlife_gallery/wildlife_tiger_stalk.webp", "title": "Tigresse en approche silencieuse", "desc": "Avancée furtive dans la canopée et les herbes de sous-bois", "location": "Vallée sauvage de Babai", "category": "felins"},
    {"file": "/assets/wildlife_gallery/julien_tigre_bengale2.webp", "title": "Tigre royal en lisière", "desc": "Traversée majestueuse d'une clairière au pas ralenti", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/wildlife_gallery/wildlife_tiger_jungle.webp", "title": "Tigre du Bengale en territoire", "desc": "Marquage et surveillance d'un sentier de chasse ancestral", "location": "Bardia National Park", "category": "felins"},
    {"file": "/assets/wildlife_gallery/julien_leopard_indien.webp", "title": "Léopard indien en affût", "desc": "Le grand félin camouflé sur sa branche maîtresse", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/snow-leopard/snow_leopard_portrait.webp", "title": "Panthère des neiges", "desc": "Le fantôme des falaises himalayennes à plus de 4 000 m", "location": "Haut Mustang & Annapurna", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_2.webp", "title": "Tigre du Bengale royal", "desc": "Pistage pédestre silencieux en sous-bois dense", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_3.webp", "title": "Tigre dans les hautes herbes", "desc": "Regard perçant d'un prédateur dans la savane", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_4.webp", "title": "Fauve en observation", "desc": "Affût discret le long d'un bras de rivière", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_5.webp", "title": "Tigre mâle en marche", "desc": "Progression féline au cœur de la jungle préservée", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_6.webp", "title": "Tigre royal à l'ombre des banians", "desc": "Repos salvateur aux heures chaudes de midi", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_7.webp", "title": "Tigre en lisière de savane", "desc": "Surveillance des hardes de cerfs en plaine", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_8.webp", "title": "Tigre au regard perçant", "desc": "Moment d'intensité pure lors d'un safari à pied", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_9.webp", "title": "Seigneur de Bardia", "desc": "Silhouette musculeuse traversant un chemin de terre", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_10.webp", "title": "Tigre sur la piste", "desc": "Reconnaissance d'empreintes fraîches sur le sentier", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/Tigre_du_bengale_11.webp", "title": "Tigresse dans la clairière", "desc": "Élégance naturelle d'une femelle en chasse", "location": "Vallée de Babai", "category": "felins"},
    {"file": "/assets/drive_wildlife/Leopard_3.webp", "title": "Léopard indien dans l'arbre", "desc": "Le prince discret des arbres de la jungle népalaise", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/leopard_1.webp", "title": "Léopard en sous-bois", "desc": "Camouflage parfait au milieu de la végétation", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/leopard_2.webp", "title": "Léopard indien aux aguets", "desc": "Observation fascinante à hauteur d'homme", "location": "Parc National de Bardia", "category": "felins"},
    {"file": "/assets/drive_wildlife/tigre1.webp", "title": "Tigre du Bengale de face", "desc": "Rencontre inoubliable avec le roi de la jungle", "location": "Secteur Baghaura • Bardia", "category": "felins"}
]

# ==================== 2. GRANDS MAMMIFÈRES (20 photos) ====================
mammiferes = [
    {"file": "/assets/wildlife_gallery/wildlife_elephant_jungle.webp", "title": "Éléphant sauvage d'Asie", "desc": "Grand mâle solitaire émergeant des forêts denses de Sal", "location": "Forêt primaire de Bardia", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/wildlife_rhino_mist.webp", "title": "Grand Rhinocéros unicorne", "desc": "Silhouette préhistorique dans les brumes matinales du fleuve", "location": "Parc National de Chitwan", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/julien_elephant_mere_petit.webp", "title": "Éléphante d'Asie et son éléphanteau", "desc": "Moment d'intimité et de protection maternelle", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/chitwan_rhino.webp", "title": "Rhinocéros unicorne au pâturage", "desc": "Colosse cuirassé broutant paisiblement dans la savane", "location": "Parc National de Chitwan", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/wildlife_deer_plain.webp", "title": "Cerfs des marais (Barasingha)", "desc": "Duo de grands cerfs aux aguets dans les prairies dorées", "location": "Parc National de Suklaphanta", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/wildlife_nilgai_forest.webp", "title": "Antilopes Nilgaut (Taureau bleu)", "desc": "La plus grande antilope d'Asie en lisière forestière", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Elephant_d_Asie_2.webp", "title": "Éléphant d'Asie en déplacement", "desc": "Progression silencieuse d'un colosse en sous-bois", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Elephant_d_Asie_3.webp", "title": "Éléphant sauvage en forêt de Sal", "desc": "Grand solitaire avançant sur une piste ancestrale", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Elephant_d_Asie_4.webp", "title": "Éléphant d'Asie près du cours d'eau", "desc": "Halte rafraîchissante sur les berges fluviales", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Rhinoc_ros_indien_1.webp", "title": "Rhinocéros indien dans les hautes herbes", "desc": "Le colosse cuirassé dans son biotope naturel", "location": "Parc National de Chitwan", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Rhinoc_ros_indien_2.webp", "title": "Grand Rhinocéros en clairière", "desc": "Observation privilégiée lors d'un safari à pied", "location": "Parc National de Chitwan", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Rhinoc_ros_indien_3.webp", "title": "Rhinocéros unicorne au bord de l'eau", "desc": "Pause hydratation sous le soleil du Terai", "location": "Parc National de Chitwan", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Chital_1.webp", "title": "Cerf Axis tacheté (Chital)", "desc": "Hardes vigilantes attentives aux moindres bruits de la jungle", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Chital_2.webp", "title": "Cerf Axis mâle aux grands bois", "desc": "Élégance d'un mâle adulte en sous-bois lumineux", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Chital_3.webp", "title": "Hardes de Chitals en savane", "desc": "Groupe familial broutant en bordure de forêt", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Cerf_sambar_1.webp", "title": "Cerf Sambar majestueux", "desc": "Le plus grand cervidé du Népal dans l'ombre végétale", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Semnopith_que_ardois__1.webp", "title": "Semnopithèque ardoisé (Langur gris)", "desc": "Sentinelle arboricole prévenant l'approche du tigre", "location": "Canopée de Bardia", "category": "mammiferes"},
    {"file": "/assets/drive_wildlife/Muntjac_indien_1.webp", "title": "Muntjac indien (Cerf aboyeur)", "desc": "Petit cervidé discret au cri d'alerte caractéristique", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/julien_cerf_axis.webp", "title": "Cerfs Axis en harde", "desc": "Compagnons d'alerte des singes dans les clairières", "location": "Parc National de Bardia", "category": "mammiferes"},
    {"file": "/assets/wildlife_gallery/julien_cerf_cochon.webp", "title": "Cerf-cochon du Terai", "desc": "Petit cervidé agile évoluant dans les herbes inondables", "location": "Chitwan National Park", "category": "mammiferes"}
]

# ==================== 3. OISEAUX (20 photos incluant calaos, paons, 2 rapaces, chouettes & hiboux) ====================
oiseaux = [
    {"file": "/assets/wildlife_gallery/wildlife_calao_hornbill.webp", "title": "Grand Calao bicorne", "desc": "Sentinelle spectaculaire au sommet de la canopée", "location": "Parc National de Chitwan", "category": "oiseaux"},
    {"file": "/assets/wildlife_gallery/wildlife_peacock_wheel.webp", "title": "Paon bleu en parade nuptiale", "desc": "Déploiement féerique de la roue au soleil levant", "location": "Lisières sauvages de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Petit_duc_indien_1.webp", "title": "Petit-duc indien (Hibou)", "desc": "Rapace nocturne fascinant camouflé dans le creux d'un tronc", "location": "Forêts de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Chevechette_de_jungle_1.webp", "title": "Chevêchette de jungle (Chouette)", "desc": "Petite chouette forestière diurne aux yeux d'or perçants", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Elanion_blanc_1.webp", "title": "Élanion blanc (Rapace 1/2)", "desc": "Rapace gracieux en vol stationnaire au-dessus de la plaine", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Pygargue___t_te_grise_1.webp", "title": "Pygargue à tête grise (Rapace 2/2)", "desc": "Grand aigle pêcheur perché au-dessus des eaux calmes", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Martin-chasseur_gurial_1.webp", "title": "Martin-chasseur gurial", "desc": "Oiseau pêcheur au plumage bleu et chocolat éclatant", "location": "Zones humides de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Martin-chasseur_violet_1.webp", "title": "Martin-chasseur violet", "desc": "Plumage étincelant en affût sur une branche basse", "location": "Parc National de Chitwan", "category": "oiseaux"},
    {"file": "/assets/wildlife_gallery/julien_rollier_oiseau.webp", "title": "Rollier indien (Indian Roller)", "desc": "Oiseau sacré aux ailes turquoise étincelantes en vol", "location": "Plaines de Suklaphanta", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Rollier_indien_1.webp", "title": "Rollier indien en affût", "desc": "Couleurs féeriques perchées sur une branche sèche", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Grue_antigone_1.webp", "title": "Grue antigone (Sarus Crane)", "desc": "Le plus grand oiseau volant du monde en couple", "location": "Marais du Terai", "category": "oiseaux"},
    {"file": "/assets/wildlife_gallery/wildlife_marabout_flight.webp", "title": "Marabout chevelu en vol", "desc": "Envol majestueux au-dessus des prairies inondables", "location": "Zones humides du Terai", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Calao_bicorne_1.webp", "title": "Grand Calao bicorne en volée", "desc": "Le géant frugivore fendant l'air entre les cimes", "location": "Parc National de Chitwan", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Calao_de_Gingi_1.webp", "title": "Calao de Gingi (Indian Grey)", "desc": "Espèce arboricole agile nichant dans les vieux troncs", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Calao_Pie_1.webp", "title": "Calao pie d'Orient", "desc": "Oiseau au casque noir et blanc contrasté", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Perruche_Alexandre_1.webp", "title": "Perruche d'Alexandre", "desc": "Grande perruche colorée aux épaules pourpres", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Perruche___t_te_prune_1.webp", "title": "Perruche à tête prune", "desc": "Petit perroquet sauvage aux teintes violettes et vertes", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Perruche___collier_1.webp", "title": "Perruche à collier", "desc": "Volée bruyante et vive dans la végétation luxuriante", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Loriot___capuchon_noir_1.webp", "title": "Loriot à capuchon noir", "desc": "Passereau d'un jaune d'or éclatant au cœur des feuillages", "location": "Parc National de Bardia", "category": "oiseaux"},
    {"file": "/assets/drive_wildlife/Tourterelle_tigrine_1.webp", "title": "Tourterelle tigrine", "desc": "Colombe sauvage aux motifs perlés sur le cou", "location": "Plaines du Terai", "category": "oiseaux"}
]

# ==================== 4. REPTILES & RIVIÈRES (Crocodiles, Lézards / Varans, Dauphins du Gange, Serpents) ====================
reptiles = [
    {"file": "/assets/wildlife_gallery/wildlife_croco_water.webp", "title": "Crocodile des marais (Mugger)", "desc": "Prédateur à fleur d'eau avec reflet miroir limpide", "location": "Rivière Rapti • Chitwan", "category": "reptiles"},
    {"file": "/assets/drive_wildlife/Varan_du_Bengale_1.webp", "title": "Varan du Bengale (Lézard géant)", "desc": "Grand lézard préhistorique se réchauffant sur une souche", "location": "Parc National de Bardia", "category": "reptiles"},
    {"file": "/assets/drive_wildlife/Varan_du_Bengale_2.webp", "title": "Lézard Varan en déplacement", "desc": "Progression puissante au sol parmi les racines", "location": "Parc National de Bardia", "category": "reptiles"},
    {"file": "/assets/wildlife_gallery/julien_gangetic_dolphin.webp", "title": "Dauphin d'eau douce du Gange", "desc": "Émersion furtive d'un dauphin sauvage dans les rapides", "location": "Fleuve Karnali • Bardia", "category": "reptiles"},
    {"file": "/assets/drive_wildlife/Serpent_1.webp", "title": "Serpent de la jungle", "desc": "Reptile discret ondulant dans la végétation des rives", "location": "Zones humides de Bardia", "category": "reptiles"},
    {"file": "/assets/drive_wildlife/Serpent_2.webp", "title": "Reptile aquatique du Terai", "desc": "Espèce fluviale nageant avec grâce en bordure de banc de sable", "location": "Rivière Rapti • Chitwan", "category": "reptiles"}
]

# Balance all items
all_curated = []
max_len = max(len(felins), len(mammiferes), len(oiseaux), len(reptiles))
for i in range(max_len):
    if i < len(felins): all_curated.append(felins[i])
    if i < len(mammiferes): all_curated.append(mammiferes[i])
    if i < len(oiseaux): all_curated.append(oiseaux[i])
    if i < len(reptiles): all_curated.append(reptiles[i])

print(f"Total curated: {len(all_curated)}")
print(f" - Félins: {len(felins)}")
print(f" - Mammifères: {len(mammiferes)}")
print(f" - Oiseaux: {len(oiseaux)} (avec 2 rapaces, chouettes & hiboux)")
print(f" - Reptiles: {len(reptiles)} (crocodiles, lézards/varans, dauphins)")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(all_curated, f, indent=2, ensure_ascii=False)

