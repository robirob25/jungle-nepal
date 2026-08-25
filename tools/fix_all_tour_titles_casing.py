import json, re, glob, os

# Canonical French sentence-case title mapping
title_clean_map = {
    # 1. népal immersion totale
    "Népal – Immersion Totale : Culture, Vie Sauvage et Aventure": "Népal – immersion totale : culture, vie sauvage et aventure",
    "Népal – Immersion Totale : Culture, vie sauvage et aventure": "Népal – immersion totale : culture, vie sauvage et aventure",
    "Népal – Immersion totale : Culture, Vie Sauvage et Aventure": "Népal – immersion totale : culture, vie sauvage et aventure",
    "Népal – Immersion totale : culture, vie sauvage et aventure": "Népal – immersion totale : culture, vie sauvage et aventure",

    # 2. chitwan culture
    "Chitwan – Culture et Jungle Sauvage": "Chitwan – culture et jungle sauvage",
    "Chitwan – Culture et jungle sauvage": "Chitwan – culture et jungle sauvage",

    # 3. bardia explorateur
    "Bardia Explorateur – 5 jours dans la jungle": "Bardia explorateur – 5 jours dans la jungle",
    "Bardia Explorateur – 5 Jours dans la jungle": "Bardia explorateur – 5 jours dans la jungle",

    # 4. rara lake
    "Rara Lake & Bardia Expedition – L’ultime aventure hors sentiers battus": "Rara Lake & Bardia expedition – l’ultime aventure hors sentiers battus",
    "Rara Lake & Bardia Expedition – L'ultime aventure hors sentiers battus": "Rara Lake & Bardia expedition – l'ultime aventure hors sentiers battus",

    # 5. bardia babai camping
    "Bardia Babai vallée  – Camping sauvage au cœur d’une nature vierge et isolée": "Bardia Babai vallée – camping sauvage au cœur d’une nature vierge et isolée",
    "Bardia Babai vallée – Camping sauvage au cœur d’une nature vierge et isolée": "Bardia Babai vallée – camping sauvage au cœur d’une nature vierge et isolée",
    "Bardia Babai vallée – Camping sauvage au cœur d'une nature vierge et isolée": "Bardia Babai vallée – camping sauvage au cœur d'une nature vierge et isolée",

    # 6. babai special
    "Deep Into the Wild: Babai Spécial Experience – 5 jours": "Deep into the wild : Babai spécial experience – 5 jours",
    "Deep into the Wild: Babai Spécial Experience – 5 jours": "Deep into the wild : Babai spécial experience – 5 jours",

    # 7. chitwan bardia complete
    "Chitwan + Bardia – L’aventure jungle complète": "Chitwan + Bardia – l’aventure jungle complète",
    "Chitwan + Bardia – L'aventure jungle complète": "Chitwan + Bardia – l'aventure jungle complète",

    # 8. rafting safari
    "Rivières sauvages et patrimoines cachés – Expédition et rafting": "Rivières sauvages et patrimoines cachés – expédition et rafting",

    # 9. panthere des neiges
    "Expédition : Panthère des Neiges Exclusive (17 jours)": "Expédition : panthère des neiges exclusive (17 jours)",
    "Expédition : Panthère des neiges exclusive (17 jours)": "Expédition : panthère des neiges exclusive (17 jours)",
    "Expédition : panthère des neiges exclusive": "Expédition : panthère des neiges exclusive",

    # 10. tiji mustang
    "Tiji Festival – Upper Mustang": "Tiji Festival – Upper Mustang",

    # 11. carnet de voyage
    "Népal – Carnet de dessin et de voyage  – 15 jours": "Népal – carnet de dessin et de voyage – 15 jours",
    "Népal – Carnet de dessin et de voyage – 15 jours": "Népal – carnet de dessin et de voyage – 15 jours",

    # 12. bardia nuit sauvage
    "Bardia – Aventure immersive en jungle et camping sauvage": "Bardia – aventure immersive en jungle et camping sauvage",

    # 13. jungle extreme
    "Jungle extrême – Spécial faune sauvage": "Jungle extrême – spécial faune sauvage",

    # 14. nepal sauvage
    "Népal sauvage – de la jungle aux montagnes sacrées": "Népal sauvage – de la jungle aux montagnes sacrées",

    # 15. immersion spirituelle
    "Immersion spirituelle en Himalaya": "Immersion spirituelle en Himalaya",
}

# 1. Update tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for tour in tours:
    t = tour.get('title', '')
    if t in title_clean_map:
        tour['title'] = title_clean_map[t]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, ensure_ascii=False, indent=2)

print("✓ Updated tours.json")

# 2. Update all .astro files in src/pages/tours, index.astro, etc.
all_astro = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in all_astro:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    for old_t, new_t in title_clean_map.items():
        content = content.replace(old_t, new_t)
    
    # Specific regex replacements for H1 and breadcrumbs
    content = re.sub(
        r'<h1([^>]*)>Népal – Immersion Totale : Culture, Vie Sauvage et Aventure</h1>',
        r'<h1\1>Népal – immersion totale : culture, vie sauvage et aventure</h1>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<h1([^>]*)>Chitwan – Culture et Jungle Sauvage</h1>',
        r'<h1\1>Chitwan – culture et jungle sauvage</h1>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<h1([^>]*)>Bardia Explorateur – 5 jours dans la jungle</h1>',
        r'<h1\1>Bardia explorateur – 5 jours dans la jungle</h1>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<h1([^>]*)>Bardia – Aventure immersive en jungle et camping sauvage</h1>',
        r'<h1\1>Bardia – aventure immersive en jungle et camping sauvage</h1>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<h1([^>]*)>Rivières sauvages et patrimoines cachés – Expédition et rafting</h1>',
        r'<h1\1>Rivières sauvages et patrimoines cachés – expédition et rafting</h1>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<h1([^>]*)>Jungle extrême – Spécial faune sauvage</h1>',
        r'<h1\1>Jungle extrême – spécial faune sauvage</h1>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<h1([^>]*)>Népal – Carnet de dessin et de voyage  – 15 jours</h1>',
        r'<h1\1>Népal – carnet de dessin et de voyage – 15 jours</h1>',
        content,
        flags=re.IGNORECASE
    )

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated titles in {os.path.basename(fpath)}")

print("All tour titles converted to clean sentence case!")
