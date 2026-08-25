import glob, os, re, json

files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/*.webp')
print(f"Total downloaded wildlife files: {len(files)}")

def categorize_and_title(filename):
    name = os.path.splitext(os.path.basename(filename))[0].replace('_', ' ')
    name_clean = re.sub(r'\s+\d+(?:-\d+)?$', '', name).strip()
    name_lower = name.lower()
    
    # 1. Félins
    if any(k in name_lower for k in ['tigre', 'tiger', 'leopard', 'léopard', 'panthere', 'panthère', 'chat']):
        cat = "felins"
        loc = "Parc National de Bardia"
        if "leopard" in name_lower or "léopard" in name_lower:
            title = f"Léopard indien ({name_clean})" if "leopard" not in name_clean.lower() else name_clean.title()
            desc = "Prédateur furtif observé en lisière et dans la canopée"
        elif "panthere" in name_lower or "panthère" in name_lower:
            title = "Panthère des neiges"
            loc = "Himalaya & Haut Mustang"
            desc = "Observation rare sur les crêtes rocheuses de haute altitude"
        else:
            title = "Tigre du Bengale royal" if name_clean.lower() in ['tigre', 'tiger', 'adrien tigre', 'julien tigre bengale'] else name_clean.title()
            desc = "Pistage pédestre silencieux au cœur du territoire des tigres"
        return cat, title, desc, loc

    # 2. Oiseaux
    bird_keywords = [
        'oiseau', 'rollier', 'calao', 'peacock', 'paon', 'marabout', 'martin-chasseur', 'martin chasseur',
        'guepier', 'guêpier', 'petit-duc', 'petit duc', 'chouette', 'chevechette', 'chevêchette',
        'elanion', 'élanion', 'grue', 'loriot', 'perruche', 'shama', 'sittelle', 'tarier', 'tourterelle',
        'prinia', 'moupinie', 'colombine', 'barbu', 'gravelot'
    ]
    if any(k in name_lower for k in bird_keywords):
        cat = "oiseaux"
        loc = "Parcs de Bardia & Chitwan"
        if "calao" in name_lower:
            title = "Grand Calao bicorne"
            desc = "Le plus grand oiseau frugivore de la canopée"
        elif "paon" in name_lower or "peacock" in name_lower:
            title = "Paon bleu en parade"
            desc = "Déploiement majestueux de la roue au lever du soleil"
        elif "marabout" in name_lower:
            title = "Marabout chevelu"
            desc = "Grand échassier planant au-dessus des plaines inondables"
        elif "rollier" in name_lower:
            title = "Rollier indien (Indian Roller)"
            desc = "Oiseau sacré aux éclats bleus turquoise en vol"
        elif "martin" in name_lower:
            title = "Martin-chasseur de Smyrne"
            desc = "Chasseur aquatique au plumage bleu et chocolat éclatant"
        elif "guepier" in name_lower or "guêpier" in name_lower:
            title = "Guêpier d'Orient"
            desc = "Voltigeur acrobatique aux couleurs émeraude et dorées"
        elif "duc" in name_lower or "chouette" in name_lower or "chevechette" in name_lower:
            title = name_clean.title()
            desc = "Rapace nocturne camouflé dans les cavités d'arbres"
        elif "elanion" in name_lower or "élanion" in name_lower:
            title = "Élanion blanc"
            desc = "Petit rapace gracieux en vol stationnaire au-dessus de la savane"
        elif "grue" in name_lower:
            title = "Grue antigone"
            desc = "Le plus grand oiseau volant du monde en couple"
        elif "perruche" in name_lower:
            title = name_clean.title()
            desc = "Volée bruyante et colorée dans les arbres fruitiers"
        else:
            title = name_clean.title()
            desc = "Avifaune sauvage exceptionnelle répertoriée au Népal"
        return cat, title, desc, loc

    # 3. Reptiles & Rivières
    if any(k in name_lower for k in ['croco', 'crocodile', 'gharial', 'gavial', 'serpent', 'python', 'dolphin', 'dauphin']):
        cat = "reptiles"
        loc = "Rivières Rapti & Karnali"
        if "gharial" in name_lower or "gavial" in name_lower:
            title = "Gavial du Gange"
            desc = "Reptile préhistorique piscivore au museau effilé"
        elif "dolphin" in name_lower or "dauphin" in name_lower:
            title = "Dauphin d'eau douce du Gange"
            desc = "Espèce fluviale rare et protégée des grands fleuves népalais"
        elif "serpent" in name_lower or "python" in name_lower:
            title = "Serpent de la jungle"
            desc = "Reptile discret des sous-bois et zones humides"
        else:
            title = "Crocodile des marais (Mugger)"
            desc = "Baignade de soleil sur les bancs de sable au bord de l'eau"
        return cat, title, desc, loc

    # 4. Grands Mammifères (Default for elephants, rhinos, deers, monkeys, etc.)
    cat = "mammiferes"
    loc = "Plaines & forêts du Terai"
    if any(k in name_lower for k in ['elephant', 'éléphant']):
        title = "Éléphant d'Asie sauvage"
        loc = "Parc National de Bardia"
        desc = "Troupeau en déplacement à travers les forêts de Sal"
    elif any(k in name_lower for k in ['rhino', 'rhinocéros', 'rhinoceros']):
        title = "Grand Rhinocéros unicorne"
        loc = "Parc National de Chitwan"
        desc = "Colosse cuirassé évoluant dans les herbes à éléphant"
    elif any(k in name_lower for k in ['chital', 'axis', 'cerf']):
        title = name_clean.title() if "cerf" in name_clean.lower() or "chital" in name_clean.lower() else f"Cerf Axis ({name_clean})"
        loc = "Parc National de Bardia"
        desc = "Herbivore agile vivant en hardes attentives aux prédateurs"
    elif any(k in name_lower for k in ['muntjac', 'aboyeur']):
        title = "Muntjac indien (Cerf aboyeur)"
        loc = "Forêts de Bardia"
        desc = "Petit cervidé dont le cri d'alerte signale la présence du tigre"
    elif any(k in name_lower for k in ['nilgai', 'nilgaut']):
        title = "Antilope Nilgaut"
        loc = "Parc National de Suklaphanta"
        desc = "Grande antilope robuste paissant en lisière de plaine"
    elif any(k in name_lower for k in ['singe', 'semnopitheque', 'langur']):
        title = "Semnopithèque ardoisé (Langur gris)"
        loc = "Canopée de Bardia"
        desc = "Sentinelle arboricole prévenant la jungle de l'approche des fauves"
    else:
        title = name_clean.title()
        desc = "Faune emblématique des écosystèmes préservés du Népal"

    return cat, title, desc, loc

all_items = []
for fpath in sorted(files):
    fname = os.path.basename(fpath)
    rel_path = f"/assets/drive_wildlife/{fname}"
    cat, title, desc, loc = categorize_and_title(fname)
    
    all_items.append({
        "file": rel_path,
        "title": title,
        "desc": desc,
        "location": loc,
        "category": cat
    })

# Also include the original curated set from /assets/wildlife_gallery/
existing_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/wildlife_gallery/*.webp')
for fpath in existing_files:
    fname = os.path.basename(fpath)
    rel_path = f"/assets/wildlife_gallery/{fname}"
    if not any(item['file'] == rel_path for item in all_items):
        cat, title, desc, loc = categorize_and_title(fname)
        all_items.append({
            "file": rel_path,
            "title": title,
            "desc": desc,
            "location": loc,
            "category": cat
        })

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(all_items, f, indent=2, ensure_ascii=False)

cat_stats = {}
for i in all_items:
    c = i['category']
    cat_stats[c] = cat_stats.get(c, 0) + 1

print(f"\n==========================================")
print(f"Total wildlife photos indexed: {len(all_items)}")
for c, count in sorted(cat_stats.items()):
    print(f" - {c.upper()}: {count} photos")
print(f"==========================================")
