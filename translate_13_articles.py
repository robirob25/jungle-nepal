import json, re

# Load JSON
with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

fr_by_slug = {p['slug']: p for p in posts_fr}
en_by_slug = {p['slug']: p for p in posts_en}

short_slugs = [
    'cerf-des-marais-suklaphanta-savanes-sauvages-ouest-nepalais',
    'safari-nepal-en-famille-securite-lodges-enfants',
    'culture-tharu-traditions-cuisine-festival-dashain-bardia',
    'safari-combine-inde-nepal-corbett-dudhwa-suklaphanta-bardia',
    'pistage-a-pied-nepal-journee-type-pisteurs-tharu',
    'guide-ornithologique-nepal-oiseaux-bardia-suklaphanta',
    'safari-dos-elephant-nepal-pourquoi-refuser-cette-pratique',
    'comment-aller-a-bardia-transport-avion-bus-guide',
    'comment-aller-a-chitwan-katmandou-pokhara-bus-avion',
    'safari-a-pied-nepal-danger-regles-securite-guide',
    'animaux-bardia-faune-parc-national',
    'animaux-chitwan-faune-parc-national',
    'tigre-bardia-observation-chances-spots'
]

print(f"Targeting {len(short_slugs)} posts for rich translation and expansion.")
