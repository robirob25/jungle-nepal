import json
import os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/all_tours_raw.json', 'r', encoding='utf-8') as f:
    raw_tours = json.load(f)

hero_images_curated = {
    "nepal-sauvage": [
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-27-at-13.17.14.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
    ],
    "nepal-immersion-totale": [
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "babai-special": [
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg"
    ],
    "bardia-babai-camping": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg"
    ],
    "bardia-explorateur": [
        "https://junglenepal.com/wp-content/uploads/2025/12/P1133754-scaled.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ],
    "rafting-safari": [
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ],
    "bardia-nuit-sauvage": [
        "https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-8.webp",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "tiji-mustang": [
        "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
    ],
    "chitwan-culture": [
        "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ],
    "rara-lake-bardia": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-2.webp",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ],
    "chitwan-bardia-complete": [
        "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "carnet-de-voyage": [
        "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "jungle-extreme": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3.webp",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png"
    ],
    "immersion-spirituelle": [
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0177-1-scaled.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg"
    ]
}

meta_map = {
    "bardia-explorateur-5-jours-dans-la-jungle": {"short_id": "bardia-explorateur", "category": "safari", "badge": "⭐ Best-Seller", "rating": 4.8, "reviews": 56, "difficulty": "Accessible à tous", "style": "Safari & Lodge Confort", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}},
    "chitwan-culture-et-jungle-sauvage": {"short_id": "chitwan-culture", "category": "chitwan", "badge": "🦏 Rhinos & Tharu", "rating": 4.9, "reviews": 28, "difficulty": "Facile", "style": "Safari & Culture Locale", "radar": {"wildlife": 4, "nature": 4, "culture": 5, "relax": 3, "nightlife": 1}},
    "rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting": {"short_id": "rafting-safari", "category": "rafting", "badge": "🚣 Rafting & Safari", "rating": 5.0, "reviews": 15, "difficulty": "Sportif", "style": "Aventure & Eaux Vives", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}},
    "bardia-aventure-immersive-en-jungle-et-camping-sauvage": {"short_id": "bardia-nuit-sauvage", "category": "bivouac", "badge": "🌙 Micro-Aventure", "rating": 4.9, "reviews": 31, "difficulty": "Accessible", "style": "Bivouac Express", "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 2, "nightlife": 0}},
    "rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus": {"short_id": "rara-lake-bardia", "category": "trek", "badge": "🏔️ Expédition 4x4 & Lac Sacré", "rating": 5.0, "reviews": 18, "difficulty": "Aventurier", "style": "Grand Trek & 4x4", "radar": {"wildlife": 4, "nature": 5, "culture": 4, "relax": 2, "nightlife": 0}},
    "bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee": {"short_id": "bardia-babai-camping", "category": "bivouac", "badge": "⛺ Bivouac Sauvage", "rating": 4.9, "reviews": 24, "difficulty": "Aventure", "style": "Expédition Bivouac", "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 2, "nightlife": 0}},
    "nepal-immersion-totale-culture-vie-sauvage-et-aventure": {"short_id": "nepal-immersion-totale", "category": "safari", "badge": "🔥 Promo -300€", "rating": 4.9, "reviews": 42, "difficulty": "Dynamique", "style": "Immersion 360°", "radar": {"wildlife": 5, "nature": 5, "culture": 5, "relax": 2, "nightlife": 1}},
    "deep-into-the-wild-babai-special-experience-5-jours": {"short_id": "babai-special", "category": "safari", "badge": "⚡ Aventure ++", "rating": 5.0, "reviews": 19, "difficulty": "Aventurier", "style": "Tracking Tigre & Bivouac", "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 1, "nightlife": 0}},
    "chitwan-bardia-laventure-jungle-complete": {"short_id": "chitwan-bardia-complete", "category": "chitwan", "badge": "🌿 Double Safari Parcs", "rating": 4.9, "reviews": 33, "difficulty": "Modéré", "style": "Le Grand Safari Népalais", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}},
    "tiji-festival-tour-upper-mustang": {"short_id": "tiji-mustang", "category": "culture", "badge": "🕉️ Spécial Culture", "rating": 5.0, "reviews": 12, "difficulty": "Modéré", "style": "Himalaya & Culture Sacrée", "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 2, "nightlife": 0}},
    "nepal-special-carnet-de-voyage": {"short_id": "carnet-de-voyage", "category": "culture", "badge": "🎨 Spécial Dessin & Carnet", "rating": 5.0, "reviews": 16, "difficulty": "Accessible", "style": "Art, Nature & Croquis", "radar": {"wildlife": 4, "nature": 5, "culture": 5, "relax": 4, "nightlife": 1}},
    "jungle-extreme-special-faune-sauvage": {"short_id": "jungle-extreme", "category": "safari", "badge": "🐅 Passion Faune Pro", "rating": 5.0, "reviews": 21, "difficulty": "Intense", "style": "Immersion & Photographie", "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 1, "nightlife": 0}},
    "nepal-sauvage-de-la-jungle-aux-montagnes-sacrees": {"short_id": "nepal-sauvage", "category": "safari", "badge": "❤️ Coup de cœur", "rating": 4.9, "reviews": 38, "difficulty": "Modéré", "style": "Safari 360° & Culture", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}},
    "immersion-spirituelle-en-himalaya": {"short_id": "immersion-spirituelle", "category": "culture", "badge": "🧘 Retraite & Méditation", "rating": 4.9, "reviews": 17, "difficulty": "Doux", "style": "Retraite Spirituelle & Yoga", "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 5, "nightlife": 0}}
}

structured_tours = []
for t in raw_tours:
    slug = t.get('slug')
    meta = meta_map.get(slug)
    if not meta:
        continue
    
    short_id = meta['short_id']
    curated = hero_images_curated.get(short_id, [])

    p_disc = t.get('price_discount')
    p_orig = t.get('price_original')
    price = p_disc or p_orig or 'Sur devis'
    orig_price = p_orig if (p_disc and p_orig and p_disc != p_orig) else None

    # Clean days
    days = []
    for idx, d in enumerate(t.get('days', [])):
        d_num = idx + 1
        d_title = d.get('title', f'Jour {d_num}')
        d_desc = d.get('desc', '').replace('&#215;', '×').replace('&amp;', '&').strip()
        days.append({
            "day": d_num,
            "title": d_title,
            "desc": d_desc
        })

    structured_tours.append({
        "slug": short_id,
        "rawSlug": slug,
        "title": t.get('title', '').strip(),
        "duration": t.get('duration', '5 jours'),
        "daysCount": len(days) or t.get('days_count', 5),
        "price": price,
        "originalPrice": orig_price,
        "category": meta["category"],
        "badge": meta["badge"],
        "rating": meta["rating"],
        "reviews": meta["reviews"],
        "difficulty": meta["difficulty"],
        "style": meta["style"],
        "radar": meta["radar"],
        "overview": t.get('overview', '').strip(),
        "highlights": t.get('highlights', []),
        "images": curated,
        "days": days
    })

os.makedirs('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data', exist_ok=True)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(structured_tours, f, ensure_ascii=False, indent=2)

print(f"Exported {len(structured_tours)} tours to src/data/tours.json successfully!")
