#!/usr/bin/env python3
import os
import json
import re

BASE_DIR = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal"
DATA_DIR = os.path.join(BASE_DIR, "src/data")
PAGES_EN = os.path.join(BASE_DIR, "src/pages/en")
TOURS_EN = os.path.join(PAGES_EN, "tours")

TOUR_TRANSLATIONS = {
    "jungle-extreme": {
        "title": "Extreme Jungle – Wildlife Special",
        "badge": "Pro Wildlife Passion",
        "style": "Immersion & Photography",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "From sacred temples to silent jungles, every moment is crafted to capture wonder and serenity. Guided by expert naturalists, explore deep forests, cross peaceful rivers, and observe wildlife in its rawest, most poetic form.",
        "highlights": [
            "Early morning hides to capture first light in the jungle",
            "Silent walking safaris with trackers following fresh footprints",
            "River observation to approach wildlife undisturbed"
        ]
    },
    "nepal-sauvage": {
        "title": "Wild Nepal – From Jungle to Sacred Mountains",
        "badge": "Top Favorite",
        "style": "Full Discovery & Safari",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "This journey is not just a tour. It is a passage through three Nepals: the jungle of Bardia, hill temples, authentic Himalayan villages, and the raw energy of Kathmandu.",
        "highlights": [
            "Walking safaris tracking Bengal tigers in Bardia",
            "Himalayan mountain views and village encounters",
            "Sacred temples and heritage of Kathmandu Valley"
        ]
    },
    "chitwan-bardia-complete": {
        "title": "Chitwan + Bardia – Complete Jungle Adventure",
        "badge": "Best-seller",
        "style": "Safari & Exploration",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "This adventure offers the perfect balance between guided safaris and raw wilderness. Navigate the Karnali River and traverse Bardia and Chitwan jungles in search of tigers, rhinos, and wild elephants.",
        "highlights": [
            "Double park experience: Chitwan and Bardia National Parks",
            "Dugout canoe safari on Rapti river & Karnali river boat safari",
            "High density of one-horned rhinos and Bengal tigers"
        ]
    },
    "bardia-explorateur": {
        "title": "Bardia Explorer – 5 Days in the Wild Jungle",
        "badge": "100% Native Trackers",
        "style": "Intense Safari",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "5 days of total immersion in the pristine jungle of Bardia National Park. Daily walking and jeep safaris with native trackers who grew up in the Terai.",
        "highlights": [
            "100% walking safaris guided by native Tharu trackers",
            "Deep jungle hides at prime tiger drinking spots",
            "Stay in authentic eco-lodges near the park boundary"
        ]
    },
    "chitwan-culture": {
        "title": "Chitwan – Culture & Wild Jungle",
        "badge": "Culture & Nature",
        "style": "Family & Nature",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "Discover Chitwan National Park: traditional dugout canoe trip on Rapti River, immersion with the local Tharu community, and rhino watching.",
        "highlights": [
            "Close encounters with Greater One-Horned Rhinoceros",
            "Traditional Tharu cultural evening and village walks",
            "Peaceful river canoe safari watching aquatic birdlife"
        ]
    },
    "rafting-safari": {
        "title": "Wild Rivers & Hidden Heritage – Rafting Expedition",
        "badge": "Rafting & Adventure",
        "style": "Expedition & Whitewater",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "Multi-day rafting expedition down the Karnali River combined with wild jungle safaris and riverside camping under the Himalayan stars.",
        "highlights": [
            "Whitewater rafting on the emerald waters of Karnali River",
            "Wild riverside camping on pristine sandy beaches",
            "Jungle safaris entering Bardia from river access"
        ]
    },
    "bardia-nuit-sauvage": {
        "title": "Bardia Wild Night – Jungle Bivouac & Camping",
        "badge": "Wild Bivouac",
        "style": "Wild Camping & Trek",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "Spend unforgettable nights bivouacking in jungle treehouses and tented camps inside Bardia wilderness. Fall asleep to the sounds of nocturnal wildlife.",
        "highlights": [
            "Overnight bivouac in jungle observation towers",
            "Night wildlife tracking and nocturnal sounds of the Terai",
            "Campfires with local trackers sharing jungle folklore"
        ]
    },
    "rara-lake-bardia": {
        "title": "Rara Lake & Bardia – Ultimate Off-the-Beaten-Path Expedition",
        "badge": "Exclusive Expedition",
        "style": "High Trek & Safari",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "From the pristine turquoise waters of alpine Rara Lake down to the wild lowland jungles of Bardia: Nepal's ultimate remote wilderness crossing.",
        "highlights": [
            "Explore Rara Lake, Nepal's largest and most pristine mountain lake",
            "Trek through ancient pine forests and remote mountain passes",
            "Descend into Bardia National Park for tiger and rhino safaris"
        ]
    },
    "bardia-babai-camping": {
        "title": "Bardia Babai Valley – Wild Camping in Unspoiled Nature",
        "badge": "100% Wild",
        "style": "Extreme Bivouac",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "Traverse the secret Babai Valley in eastern Bardia. Camping under the stars far from civilization, tracking wild elephant herds and big cats.",
        "highlights": [
            "Exclusive access to the pristine Babai Valley ecosystem",
            "Wild camping along the Babai River bank",
            "Top sanctuary for wild Asian elephants and Bengal tigers"
        ]
    },
    "nepal-immersion-totale": {
        "title": "Nepal Total Immersion – Culture, Wildlife & Himalaya",
        "badge": "Grand Tour 360°",
        "style": "Complete Expedition",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "The ultimate 18-day grand tour of Nepal covering Kathmandu Valley, Pokhara lakes, Annapurna balconies, Chitwan rhinos, and Bardia tigers.",
        "highlights": [
            "Complete 360° overview of Nepal's culture, mountains, and jungles",
            "Pokhara & Annapurna sunrise panoramas",
            "Safaris in both Chitwan and Bardia National Parks"
        ]
    },
    "babai-special": {
        "title": "Deep into the Wild: Babai Special Experience – 5 Days",
        "badge": "Exclusive Experience",
        "style": "Deep Wilderness",
        "category_tag": "Wild Nepal • Eco-Safari",
        "overview": "An intense 5-day deep wilderness trek in Babai Valley. Ideal for seasoned naturalists seeking total solitude and prime tiger tracking.",
        "highlights": [
            "Unmatched solitude in Babai River sanctuary",
            "Guided by veteran Tharu head trackers",
            "High frequency of big cat and elephant sightings"
        ]
    },
    "tiji-mustang": {
        "title": "Tiji Festival in Upper Mustang – Culture & High Trek",
        "badge": "Culture & High Trek",
        "style": "Tibetan Culture Trek",
        "category_tag": "Himalaya & Mustang",
        "overview": "Witness the ancient Tiji Festival in the walled kingdom of Lo Manthang. Experience Tibetan Buddhist rituals, sacred mask dances, and dramatic canyon landscapes.",
        "highlights": [
            "3-day Tiji Festival celebration in Lo Manthang",
            "Explore the ancient cliff caves and monasteries of Mustang",
            "Breathtaking views of Dhaulagiri and Annapurna ranges"
        ]
    },
    "carnet-de-voyage": {
        "title": "Nepal Sketchbook & Travel Journal – 15 Days",
        "badge": "Creative & Nature",
        "style": "Artistic & Discovery",
        "category_tag": "Creative Expedition",
        "overview": "An artistic voyage through Nepal's jungles and mountain villages. Capture landscapes, wildlife, and portraits in your personal travel journal.",
        "highlights": [
            "Guided sketching workshops in heritage sites & jungle hides",
            "Slow travel pace focused on observation and creativity",
            "Unique souvenir notebook crafted throughout the journey"
        ]
    },
    "immersion-spirituelle": {
        "title": "Spiritual & Nature Immersion in the Himalayas",
        "badge": "Serenity & Meditation",
        "style": "Mindfulness & Nature",
        "category_tag": "Spiritual Trek",
        "overview": "Reconnect with nature through Himalayan monastery stays, sunrise meditation, yoga sessions, and gentle walks in sacred valleys.",
        "highlights": [
            "Stay in authentic Buddhist monastery guest houses",
            "Daily meditation and breathwork facing snow-capped peaks",
            "Blessing ceremonies with senior Himalayan monks"
        ]
    },
    "panthere-des-neiges": {
        "title": "Snow Leopard Expedition – Himalayan High Altitude (17 Days)",
        "badge": "Extreme Himalaya",
        "style": "High Altitude Expedition",
        "category_tag": "Himalayan Wildlife",
        "overview": "Track the 'Ghost of the Mountains' in the high snow-covered valleys of Manang. A rare expedition guided by elite high-altitude trackers.",
        "highlights": [
            "Dedicated snow leopard tracking in prime winter habitats",
            "High-power spotting scope stations in high valleys",
            "Encounters with blue sheep, Himalayan ibex, and golden eagles"
        ]
    }
}

CATEGORY_REPLACEMENTS = [
    ("Mixe jungle et montagne (5)", "Jungle & Mountain Blend (5)"),
    ("Safaris et grands félins (11)", "Safaris & Big Cats (11)"),
    ("Bivouacs et nuits sauvages (5)", "Jungle Bivouacs & Wild Nights (5)"),
    ("Rhinocéros et Chitwan (3)", "Rhinos & Chitwan (3)"),
    ("Rafting et expéditions rivières (3)", "Rafting & River Expeditions (3)"),
    ("Himalaya, Mustang et spiritualité (6)", "Himalaya, Mustang & Spirituality (6)"),
    ("Népal Sauvage • Éco-Safari", "Wild Nepal • Eco-Safari"),
]

COMMON_TOUR_PHRASES = [
    ("Jour 1 –", "Day 1 –"),
    ("Jour 2 –", "Day 2 –"),
    ("Jour 3 –", "Day 3 –"),
    ("Jour 4 –", "Day 4 –"),
    ("Jour 5 –", "Day 5 –"),
    ("Jour 6 –", "Day 6 –"),
    ("Jour 7 –", "Day 7 –"),
    ("Jour 8 –", "Day 8 –"),
    ("Jour 9 –", "Day 9 –"),
    ("Jour 10 –", "Day 10 –"),
    ("Jour 11 –", "Day 11 –"),
    ("Jour 12 –", "Day 12 –"),
    ("Jour 13 –", "Day 13 –"),
    ("Jour 14 –", "Day 14 –"),
    ("Jour 15 –", "Day 15 –"),
    ("Jour 16 –", "Day 16 –"),
    ("Jour 17 –", "Day 17 –"),
    ("Jour 18 –", "Day 18 –"),
    ("Jour 1 :", "Day 1:"),
    ("Jour 2 :", "Day 2:"),
    ("Jour 3 :", "Day 3:"),
    ("Jour 4 :", "Day 4:"),
    ("Jour 5 :", "Day 5:"),
    ("Jour 6 :", "Day 6:"),
    ("Jour 7 :", "Day 7:"),
    ("Jour 8 :", "Day 8:"),
    ("Jour 9 :", "Day 9:"),
    ("Jour 10 :", "Day 10:"),
    ("Jour 11 :", "Day 11:"),
    ("Jour 12 :", "Day 12:"),
    ("Jour 13 :", "Day 13:"),
    ("Jour 14 :", "Day 14:"),
    ("Jour 15 :", "Day 15:"),
    ("Ce qui vous attend", "What to Expect"),
    ("Points forts du séjour", "Expedition Highlights"),
    ("Itinéraire détaillé", "Detailed Itinerary"),
    ("Itinéraire Jour par Jour", "Day-by-Day Itinerary"),
    ("Ce qui est inclus", "What's Included"),
    ("Ce qui n'est pas inclus", "What's Not Included"),
    ("Foire aux questions", "Frequently Asked Questions"),
    ("Réserver ce séjour", "Book This Expedition"),
    ("Demander un devis sur-mesure", "Request a Custom Quote"),
    ("Discuter avec Robin sur WhatsApp", "Chat with Robin on WhatsApp"),
    ("Départs garantis", "Guaranteed Departures"),
    ("Petit groupe (4 à 10 max)", "Small Groups (4-10 max)"),
    ("Pisteurs natifs 100%", "100% Native Trackers"),
    ("Durée :", "Duration:"),
    ("Prix par personne :", "Price per person:"),
    ("Niveau :", "Difficulty:"),
    ("Style :", "Style:"),
    ("Avis voyageurs", "Traveler Reviews"),
    ("Informations pratiques", "Practical Information"),
    ("Conseils d'équipement", "Packing & Gear Tips"),
    ("Période idéale :", "Best Season:"),
    ("Toute l'année", "All Year Round"),
    ("Automne et Printemps", "Autumn & Spring"),
]

TITLE_PAIRS = [
    ("Jungle extrême – spécial faune sauvage", "Extreme Jungle – Wildlife Special"),
    ("Népal sauvage – de la jungle aux montagnes sacrées", "Wild Nepal – From Jungle to Sacred Mountains"),
    ("Chitwan + Bardia – l’aventure jungle complète", "Chitwan + Bardia – Complete Jungle Adventure"),
    ("Chitwan + Bardia – l'aventure jungle complète", "Chitwan + Bardia – Complete Jungle Adventure"),
    ("Bardia explorateur – 5 jours dans la jungle", "Bardia Explorer – 5 Days in the Wild Jungle"),
    ("Chitwan – culture et jungle sauvage", "Chitwan – Culture & Wild Jungle"),
    ("Rivières sauvages et patrimoines cachés – expédition et rafting", "Wild Rivers & Hidden Heritage – Rafting Expedition"),
    ("Bardia – aventure immersive en jungle et camping sauvage", "Bardia Wild Night – Jungle Bivouac & Camping"),
    ("Rara Lake & Bardia expedition – l’ultime aventure hors sentiers battus", "Rara Lake & Bardia Expedition – Ultimate Off-the-Beaten-Path Expedition"),
    ("Rara Lake & Bardia expedition – l'ultime aventure hors sentiers battus", "Rara Lake & Bardia Expedition – Ultimate Off-the-Beaten-Path Expedition"),
    ("Bardia Babai vallée – camping sauvage au cœur d’une nature vierge et isolée", "Bardia Babai Valley – Wild Camping in Unspoiled Nature"),
    ("Bardia Babai vallée – camping sauvage au cœur d'une nature vierge et isolée", "Bardia Babai Valley – Wild Camping in Unspoiled Nature"),
    ("Népal – immersion totale : culture, vie sauvage et aventure", "Nepal Total Immersion – Culture, Wildlife & Himalaya"),
    ("Deep into the wild : Babai spécial experience – 5 jours", "Deep into the Wild: Babai Special Experience – 5 Days"),
    ("Tiji Festival – Upper Mustang", "Tiji Festival in Upper Mustang – Culture & High Trek"),
    ("Népal – carnet de dessin et de voyage – 15 jours", "Nepal Sketchbook & Travel Journal – 15 Days"),
    ("Immersion spirituelle en Himalaya", "Spiritual & Nature Immersion in the Himalayas"),
    ("Expédition : panthère des neiges exclusive (17 jours)", "Snow Leopard Expedition – Himalayan High Altitude (17 Days)"),
]

def update_tours_json():
    fr_json_path = os.path.join(DATA_DIR, "tours.json")
    en_json_path = os.path.join(DATA_DIR, "tours.en.json")

    with open(fr_json_path, "r", encoding="utf-8") as f:
        tours = json.load(f)

    for tour in tours:
        slug = tour["slug"]
        if slug in TOUR_TRANSLATIONS:
            t = TOUR_TRANSLATIONS[slug]
            tour["title"] = t["title"]
            tour["badge"] = t["badge"]
            tour["style"] = t["style"]
            tour["overview"] = t["overview"]
            tour["highlights"] = t["highlights"]

    with open(en_json_path, "w", encoding="utf-8") as f:
        json.dump(tours, f, ensure_ascii=False, indent=2)
    print(f"Updated {en_json_path}")

def update_index_astro():
    index_path = os.path.join(PAGES_EN, "index.astro")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    for fr, en in CATEGORY_REPLACEMENTS:
        content = content.replace(fr, en)

    for fr_t, en_t in TITLE_PAIRS:
        content = content.replace(fr_t, en_t)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {index_path}")

def update_tour_pages():
    for file in os.listdir(TOURS_EN):
        if not file.endswith(".astro"):
            continue
        
        file_path = os.path.join(TOURS_EN, file)
        slug = file.replace(".astro", "")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        for fr, en in COMMON_TOUR_PHRASES:
            content = content.replace(fr, en)

        for fr_t, en_t in TITLE_PAIRS:
            content = content.replace(fr_t, en_t)

        content = re.sub(r'lang="fr"', 'lang="en"', content)
        content = re.sub(r"lang='fr'", "lang='en'", content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Updated EN tour page: {file}")

if __name__ == "__main__":
    update_tours_json()
    update_index_astro()
    update_tour_pages()
