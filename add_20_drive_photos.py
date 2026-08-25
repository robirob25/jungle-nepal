import json, os, shutil
from PIL import Image

src_wildlife = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife'
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Existing thumbnails
existing_thumbs = []
for i in items:
    p = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public', i['file'].lstrip('/'))
    if os.path.exists(p):
        t = Image.open(p).convert('RGB').resize((32, 32))
        existing_thumbs.append((i['title'], t))

new_photos = [
    # 1. FELINS (5 photos with 3 leopards)
    {
        "src_name": "leopard_1.webp",
        "fname": "leopard_asie_affut_lisiere.webp",
        "title": "Léopard d'Asie en affût",
        "desc": "Fauve tacheté observant silencieusement depuis la lisière de jungle",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "src_name": "leopard_2.webp",
        "fname": "leopard_indien_camouflage.webp",
        "title": "Léopard indien dans les branchages",
        "desc": "Prédateur solitaire parfaitement dissimulé dans la canopée",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "src_name": "Leopard_3.webp",
        "fname": "leopard_sur_branche_maitresse.webp",
        "title": "Léopard sur branche maîtresse",
        "desc": "Observation haute et sereine au-dessus des pistes sauvages",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    {
        "src_name": "Tigre_du_bengale_2.webp",
        "fname": "tigre_bengale_traversee_riviere.webp",
        "title": "Tigre du Bengale traversant la rivière",
        "desc": "Félin puissant fendant le cours d'eau sous le soleil couchant",
        "location": "Rivière Babai • Bardia",
        "category": "felins"
    },
    {
        "src_name": "Tigre_du_bengale_6.webp",
        "fname": "tigre_bengale_penombre_sal.webp",
        "title": "Tigre du Bengale dans la pénombre",
        "desc": "Pistage intense au cœur des futaies denses d'arbres de Sal",
        "location": "Parc National de Bardia",
        "category": "felins"
    },

    # 2. GRANDS MAMMIFERES (5 photos)
    {
        "src_name": "Ours_lippu_1.webp",
        "fname": "ours_lippu_sloth_bear.webp",
        "title": "Ours lippu (Sloth Bear)",
        "desc": "Mammifère fascinant aux longues griffes en quête de termitières",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "src_name": "Muntjac_indien_1.webp",
        "fname": "cerf_aboyeur_muntjac.webp",
        "title": "Cerf aboyeur (Muntjac indien)",
        "desc": "Petit cervidé timide et vif dissimulé dans la strate basse",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    {
        "src_name": "Chital_1.webp",
        "fname": "cerf_axis_chital_tachete.webp",
        "title": "Cerf Axis (Chital tacheté)",
        "desc": "Cervidé gracieux à la robe tachetée de blanc en sous-bois",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "src_name": "Chital_2.webp",
        "fname": "troupe_chitals_clairiere.webp",
        "title": "Harde de Cerfs Axis en clairière",
        "desc": "Groupe familial broutant paisiblement dans la lumière dorée",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    {
        "src_name": "Elephant_d_Asie_2.webp",
        "fname": "troupeau_elephants_asie_lisiere.webp",
        "title": "Troupeau d'éléphants d'Asie",
        "desc": "Matriarche et éléphanteau se déplaçant en lisière de forêt",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },

    # 3. OISEAUX (5 photos)
    {
        "src_name": "Chev_che_brame_3.webp",
        "fname": "cheveche_brame_chouette_tachetee.webp",
        "title": "Chevêche brame (Chouette tachetée)",
        "desc": "Petite chouette aux grands yeux d'or scrutant son perchoir",
        "location": "Parc National de Chitwan",
        "category": "oiseaux"
    },
    {
        "src_name": "Martin-p_cheur_pie_1.webp",
        "fname": "martin_pecheur_pie_rapide.webp",
        "title": "Martin-pêcheur pie (Pied Kingfisher)",
        "desc": "Maître de la pêche en vol stationnaire au-dessus de la rivière",
        "location": "Rivière Rapti • Chitwan",
        "category": "oiseaux"
    },
    {
        "src_name": "Loriot___capuchon_noir_1.webp",
        "fname": "loriot_capuchon_noir_or.webp",
        "title": "Loriot à capuchon noir",
        "desc": "Plumage éclatant jaune or contrastant avec sa tête d'ébène",
        "location": "Canopée de Bardia",
        "category": "oiseaux"
    },
    {
        "src_name": "Jacana_bronz__1.webp",
        "fname": "jacana_bronze_nenuphars.webp",
        "title": "Jacana bronzé",
        "desc": "Échassier aux doigts démesurés marchant sur les feuilles de nénuphar",
        "location": "Marais de Chitwan",
        "category": "oiseaux"
    },
    {
        "src_name": "Barbu___plastron_rouge_1.webp",
        "fname": "barbu_plastron_rouge_rubis.webp",
        "title": "Barbu à plastron rouge",
        "desc": "Oiseau frugivore multicolore nichant dans les troncs creux",
        "location": "Forêts de Bardia",
        "category": "oiseaux"
    },

    # 4. REPTILES & RIVIERES (5 photos)
    {
        "src_name": "Agame_arlequin_1.webp",
        "fname": "agame_arlequin_male_rocher.webp",
        "title": "Agame arlequin mâle",
        "desc": "Lézard paré de reflets vifs dominant son territoire rocheux",
        "location": "Zones rocheuses de Bardia",
        "category": "reptiles"
    },
    {
        "src_name": "Agame_arlequin_4.webp",
        "fname": "agame_des_rochers_soleil.webp",
        "title": "Agame des rochers au soleil",
        "desc": "Reptile thermorégulateur se chauffant sur les blocs de galets",
        "location": "Berges de la Karnali • Bardia",
        "category": "reptiles"
    },
    {
        "src_name": "Varan_du_Bengale_1.webp",
        "fname": "varan_bengale_berges_sable.webp",
        "title": "Varan du Bengale sur berge",
        "desc": "Grand reptile fouillant les bancs de graviers et racines",
        "location": "Parc National de Bardia",
        "category": "reptiles"
    },
    {
        "src_name": "Serpent_1.webp",
        "fname": "serpent_eau_terai_courant.webp",
        "title": "Serpent d'eau du Terai",
        "desc": "Reptile semi-aquatique ondulant entre les racines des berges",
        "location": "Rivière Rapti • Chitwan",
        "category": "reptiles"
    },
    {
        "src_name": "Agame_arlequin_7.webp",
        "fname": "agame_arboricole_multicolore.webp",
        "title": "Agame arboricole multicolore",
        "desc": "Agilité remarquable sur les troncs centenaires de Sal",
        "location": "Forêt de Bardia",
        "category": "reptiles"
    }
]

added_count = 0
for p in new_photos:
    src_file = os.path.join(src_wildlife, p['src_name'])
    if not os.path.exists(src_file):
        print(f"Error: {src_file} does not exist!")
        continue
    
    img = Image.open(src_file).convert('RGB')
    t = img.resize((32, 32))
    
    # Check duplicate against existing
    is_dup = False
    for title, ex_t in existing_thumbs:
        diff = sum(abs(p1 - p2) for p1, p2 in zip(t.tobytes(), ex_t.tobytes())) / (32 * 32 * 3)
        if diff < 15:
            print(f"Duplicate detected: {p['src_name']} matches {title}")
            is_dup = True
            break
    
    if is_dup:
        continue
    
    # Save target WebP
    target_path = os.path.join(dest_dir, p['fname'])
    rel_path = f"/assets/curated_gallery/{p['fname']}"
    
    max_w = 2048
    if img.size[0] > max_w:
        ratio = max_w / float(img.size[0])
        new_h = int(float(img.size[1]) * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    img.save(target_path, 'WEBP', quality=90, method=6)
    
    existing_thumbs.append((p['title'], t))
    items.append({
        "file": rel_path,
        "title": p['title'],
        "desc": p['desc'],
        "location": p['location'],
        "category": p['category']
    })
    added_count += 1
    print(f"✓ Successfully added [{p['category'].upper()}]: {p['fname']} -> {p['title']}")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully added {added_count}/20 new photos. Total curated gallery count: {len(items)}")
