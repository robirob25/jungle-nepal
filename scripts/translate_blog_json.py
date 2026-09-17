#!/usr/bin/env python3
import json
import os
import re

DATA_DIR = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data"
FR_JSON = os.path.join(DATA_DIR, "blog_posts.json")
EN_JSON = os.path.join(DATA_DIR, "blog_posts.en.json")

with open(FR_JSON, 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Dictionary for blog titles and descriptions translation
TITLE_DESC_MAP = {
    "Observer les oiseaux au Népal : guide complet du birdwatching à Bardia et Chitwan": 
        ("Birdwatching in Nepal: Complete Guide to Birding in Bardia & Chitwan", 
         "Expert guide to birdwatching in Nepal. Over 500 species in Bardia and Chitwan: Great Hornbills, Kingfishers, and secret spots."),
    
    "Safari à Pied au Népal : Guide complet du Walking Safari à Bardia (2026)":
        ("Walking Safari in Nepal: Complete Guide to Bardia Walking Safaris (2026)",
         "Experience the unique thrill of walking safaris in Nepal's Bardia National Park. Tracker tips, safety rules, gear & pure wilderness."),

    "Safari Photo au Népal : Conseils, matériel et meilleurs spots (2026)":
        ("Photo Safari in Nepal: Tips, Camera Gear & Best Spots (2026)",
         "Discover the ultimate wildlife photography guide for Nepal. Bengal tigers, one-horned rhinos, and camera techniques for Terai jungles."),

    "Safari au Népal en famille : guide complet et conseils de sécurité":
        ("Family Safari in Nepal: Complete Guide & Safety Tips",
         "Planning a family safari in Nepal? Discover safe routes, kid-friendly eco-lodges, walking safari advice, and best seasons for children."),

    "Prix d'un safari à Bardia : forfaits, tarifs et ce qui est inclus":
        ("Bardia Safari Prices: Packages, Costs & What's Included",
         "Complete pricing breakdown for safaris in Bardia National Park. Understand guide fees, park permits, lodge packages, and hidden costs."),

    "Bivouac & Camping Safari à Bardia : Nuits sauvages en jungle au Népal":
        ("Bivouac & Camping Safari in Bardia: Wild Nights in Nepal's Jungle",
         "Spend the night under the stars deep inside Bardia National Park. Camping safaris, campfire meals, and nighttime jungle sounds."),

    "Traquer la panthère des neiges au Népal : expédition en haute altitude":
        ("Tracking the Snow Leopard in Nepal: High Altitude Expedition",
         "Embark on an expedition to find the ghost of the Himalayas. Best regions, optimal seasons, equipment, and tracking snow leopards in Nepal."),

    "Pourquoi choisir une agence locale francophone pour votre safari au Népal ?":
        ("Why Choose a Local Eco-Tourism Agency for Your Nepal Safari?",
         "Discover the benefits of booking directly with a certified local agency in Nepal: expert native trackers, fair prices, and 100% tailor-made safaris."),

    "Le safari éthique au Népal : pourquoi privilégier la marche et l'éco-responsabilité":
        ("Ethical Safari in Nepal: Why Walking & Eco-Responsibility Matter",
         "Learn how walking safaris protect wildlife habitats, empower local Tharu communities, and offer an authentic, eco-friendly adventure."),

    "Combien de jours consacrer à un safari au Népal ? Formules de 3 à 15 jours":
        ("How Many Days for a Nepal Safari? 3 to 15-Day Itinerary Options",
         "Find the ideal duration for your wildlife trip in Nepal. From 3-day Bardia express packages to 15-day complete jungle and trek circuits."),

    "Quand partir au Népal pour un safari ? Climat, saisons et faune":
        ("Best Time for a Nepal Safari: Climate, Seasons & Wildlife Viewing",
         "Detailed month-by-month guide to visiting Bardia and Chitwan. Understand dry season advantages, tiger sighting periods, and monsoon weather."),

    "Parc National de Bardia vs Chitwan : quel parc choisir pour votre safari ?":
        ("Bardia vs Chitwan National Park: Which Safari Destination to Choose?",
         "Detailed comparison between Bardia and Chitwan: wildlife density, tourist numbers, walking safari opportunities, and access."),
}

def translate_post(post):
    en_post = dict(post)
    
    # Translate Title & Description if mapped, or provide clean English default
    if post["title"] in TITLE_DESC_MAP:
        en_title, en_desc = TITLE_DESC_MAP[post["title"]]
        en_post["title"] = en_title
        en_post["description"] = en_desc
    else:
        # Fallback string transforms
        title = post["title"].replace("au Népal", "in Nepal").replace("à Bardia", "in Bardia").replace("à Chitwan", "in Chitwan")
        en_post["title"] = title
    
    # Translate category
    cat_map = {
        "Ornithologie & Birdwatching": "Ornithology & Birdwatching",
        "Safaris à pied": "Walking Safaris",
        "Photographie animalière": "Wildlife Photography",
        "Voyage en famille": "Family Travel",
        "Budget & Tarifs": "Pricing & Budget",
        "Expéditions": "Expeditions",
        "Écotourisme": "Eco-Tourism",
        "Conseils de voyage": "Travel Tips"
    }
    en_post["category"] = cat_map.get(post.get("category"), "Wildlife & Safaris")
    
    # Translate author role
    en_post["authorRole"] = "Founder & Expedition Leader"
    
    # Replace links inside HTML content
    content = post.get("content", "")
    content = content.replace('href="/blog', 'href="/en/blog')
    content = content.replace('href="/tours', 'href="/en/tours')
    content = content.replace('href="/destinations', 'href="/en/destinations')
    content = content.replace('href="/a-propos.html"', 'href="/en/about.html"')
    content = content.replace('href="/contact.html"', 'href="/en/contact.html"')
    content = content.replace('https://junglenepal.com/nos-aventures/', 'https://junglenepal.com/en/#prochains-departs')
    content = content.replace('Découvrir nos expéditions', 'Discover Our Expeditions')
    content = content.replace('Explorer Nos Séjours', 'Explore Our Trips')
    content = content.replace('Jours', 'days').replace('jours', 'days')
    
    en_post["content"] = content
    return en_post

en_posts = [translate_post(p) for p in posts]

with open(EN_JSON, 'w', encoding='utf-8') as f:
    json.dump(en_posts, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {EN_JSON} with {len(en_posts)} English blog posts.")
