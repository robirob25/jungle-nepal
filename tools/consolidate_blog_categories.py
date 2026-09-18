import json
from collections import Counter

CATEGORY_MAPPING_FR = {
    # 1. Faune sauvage & pistage (16 posts)
    "voir-des-tigres-au-nepal": "Faune sauvage & pistage",
    "art-du-pistage-jungle-nepal-traces-cris-alarme": "Faune sauvage & pistage",
    "pister-le-tigre-du-bengale-a-bardia": "Faune sauvage & pistage",
    "leopard-indien-panthere-nepal-guide-safari": "Faune sauvage & pistage",
    "oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis": "Faune sauvage & pistage",
    "quels-animaux-voir-lors-dun-safari-au-nepal": "Faune sauvage & pistage",
    "comportement-du-tigre-du-bengale": "Faune sauvage & pistage",
    "comportement-du-rhinoceros-unicornis": "Faune sauvage & pistage",
    "elephant-sauvage-nepal-guide-safari": "Faune sauvage & pistage",
    "gavial-du-gange-crocodiles-nepal-guide": "Faune sauvage & pistage",
    "observer-les-oiseaux-au-nepal-guide-birdwatching": "Faune sauvage & pistage",
    "rapaces-chouettes-oiseaux-proie-nepal-guide": "Faune sauvage & pistage",
    "animaux-rares-safari-nepal-guide": "Faune sauvage & pistage",
    "singes-nepal-langurs-macaques-guide": "Faune sauvage & pistage",
    "nilgaut-cerfs-ongules-sauvages-nepal-guide": "Faune sauvage & pistage",
    "reptiles-varans-agames-serpents-nepal-guide": "Faune sauvage & pistage",

    # 2. Guides des parcs & comparatifs (6 posts)
    "guide-complet-parc-national-de-bardia-nepal": "Guides des parcs & comparatifs",
    "bardia-ou-chitwan-quel-parc-choisir": "Guides des parcs & comparatifs",
    "safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia": "Guides des parcs & comparatifs",
    "guide-parc-national-de-chitwan-nepal": "Guides des parcs & comparatifs",
    "guide-complet-parc-national-de-suklaphanta": "Guides des parcs & comparatifs",
    "safari-nepal-ou-afrique-que-choisir": "Guides des parcs & comparatifs",

    # 3. Safaris à pied & expéditions (7 posts)
    "safari-a-pied-au-nepal-guide-complet": "Safaris à pied & expéditions",
    "combiner-trek-et-safari-au-nepal-guide-complet": "Safaris à pied & expéditions",
    "camping-safari-a-bardia-nuits-en-jungle-au-nepal": "Safaris à pied & expéditions",
    "safari-photo-au-nepal-spots-materiel-conseils": "Safaris à pied & expéditions",
    "safari-pirogue-rafting-nepal-guide": "Safaris à pied & expéditions",
    "panthere-des-neiges-au-nepal": "Safaris à pied & expéditions",
    "trek-jungle-nepal-safari-pied": "Safaris à pied & expéditions",

    # 4. Conseils pratiques & préparation (10 posts)
    "prix-dun-safari-au-nepal": "Conseils pratiques & préparation",
    "comment-organiser-un-safari-au-nepal": "Conseils pratiques & préparation",
    "quand-partir-au-nepal-pour-un-safari-guide": "Conseils pratiques & préparation",
    "sante-paludisme-vaccins-safari-nepal-conseils-medicaux": "Conseils pratiques & préparation",
    "safari-bardia-prix-forfaits-et-ce-que-ca-inclut": "Conseils pratiques & préparation",
    "combien-de-jours-pour-un-safari-au-nepal": "Conseils pratiques & préparation",
    "agence-safari-nepal-francophone": "Conseils pratiques & préparation",
    "sac-safari-nepal": "Conseils pratiques & préparation",
    "safari-nepal-en-famille-guide-securite": "Conseils pratiques & préparation",
    "condition-physique-safari-a-pied-nepal": "Conseils pratiques & préparation",

    # 5. Culture locale & écotourisme (2 posts)
    "le-safari-ethique-au-nepal-privilegier-la-marche": "Culture locale & écotourisme",
    "culture-tharu-nepal-immersion-jungle": "Culture locale & écotourisme"
}

CATEGORY_MAPPING_EN = {
    "Faune sauvage & pistage": "Wildlife & tracking",
    "Guides des parcs & comparatifs": "Park guides & comparisons",
    "Safaris à pied & expéditions": "Walking safaris & expeditions",
    "Conseils pratiques & préparation": "Practical advice & planning",
    "Culture locale & écotourisme": "Local culture & ecotourism"
}

# Process FR
with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

for p in posts_fr:
    slug = p['slug']
    if slug in CATEGORY_MAPPING_FR:
        p['category'] = CATEGORY_MAPPING_FR[slug]
    else:
        print(f"Warning: slug {slug} not found in FR mapping!")

with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

# Process EN
with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

for p in posts_en:
    slug = p['slug']
    if slug in CATEGORY_MAPPING_FR:
        cat_fr = CATEGORY_MAPPING_FR[slug]
        p['category'] = CATEGORY_MAPPING_EN[cat_fr]
    else:
        print(f"Warning: slug {slug} not found in EN mapping!")

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("=== FR Category Breakdown ===")
counts_fr = Counter([p['category'] for p in posts_fr])
for c, cnt in counts_fr.items():
    print(f"  {c}: {cnt} posts")

print("=== EN Category Breakdown ===")
counts_en = Counter([p['category'] for p in posts_en])
for c, cnt in counts_en.items():
    print(f"  {c}: {cnt} posts")
