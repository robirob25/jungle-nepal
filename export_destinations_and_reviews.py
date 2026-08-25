import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/real_google_reviews.json', 'r', encoding='utf-8') as f:
    reviews = json.load(f)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews, f, ensure_ascii=False, indent=2)

destinations = [
    {
        "slug": "bardia",
        "name": "Parc national de Bardia",
        "icon": "🐅",
        "tagline": "Tigres du Bengale & Safaris à pied exclusifs",
        "heroImage": "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
        "desc": "Le sanctuaire le plus sauvage et préservé du Teraï népalais. Loin du tourisme de masse, Bardia abrite la plus forte densité de tigres du Bengale et d'éléphants sauvages d'Asie.",
        "highlights": [
            "Pistage des tigres du Bengale à pied avec nos guides natifs",
            "Bivouac sauvage dans la vallée secrète de Babai",
            "Micro-groupes limités à 4 à 8 explorateurs"
        ]
    },
    {
        "slug": "chitwan",
        "name": "Parc national de Chitwan",
        "icon": "🦏",
        "tagline": "Rhinocéros unicornes & Pirogues de la Rapti",
        "heroImage": "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "desc": "Premier parc national du Népal classé à l'UNESCO. Une mosaïque de jungle luxuriante, de rivières peuplées de gavials et de villages traditionnels Tharu.",
        "highlights": [
            "Observation des rhinocéros unicornes et gavials du Gange",
            "Descente en pirogue traditionnelle sur la rivière Rapti",
            "Immersion et nuits en écolodge Tharu éco-responsable"
        ]
    },
    {
        "slug": "suklaphanta",
        "name": "Parc national de Suklaphanta",
        "icon": "🦌",
        "tagline": "Cerfs des marais & Grands espaces vierges",
        "heroImage": "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
        "desc": "La plus grande prairie sauvage continue d'Asie du Sud. Un écosystème unique où paissent d'immenses hardes de cerfs des marais sous le regard des tigres.",
        "highlights": [
            "Les plus grandes hardes de cerfs des marais au monde",
            "Territoire ultra-préservé sans aucune foule touristique",
            "Observation d'oiseaux migrateurs rares et de léopards"
        ]
    },
    {
        "slug": "annapurna",
        "name": "Les Annapurna & Pokhara",
        "icon": "🏔️",
        "tagline": "Sommets mythiques & Balcons alpins",
        "heroImage": "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
        "desc": "Le royaume des géants de l'Himalaya. Des forêts de rhododendrons aux crêtes panoramiques avec vue imprenable sur le Machapuchare et le lac Phewa.",
        "highlights": [
            "Panoramas à 360° sur la chaîne des Annapurna et le Dhaulagiri",
            "Halte détente à Pokhara sur les rives du lac Phewa",
            "Rencontre avec les communautés Gurung de montagne"
        ]
    },
    {
        "slug": "katmandou",
        "name": "Vallée de Katmandou",
        "icon": "🕉️",
        "tagline": "Vallée des rois & Temples sacrés",
        "heroImage": "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "desc": "Le cœur culturel et spirituel du Népal. Temples bouddhistes millénaires, stupas dorés de Swayambhunath et ruelles vivantes de Patan et Bhaktapur.",
        "highlights": [
            "Les grands stupas sacrés de Boudhanath et Swayambhunath",
            "Cités royales de Patan et Bhaktapur classées UNESCO",
            "Accueil personnalisé et briefing de départ avec Robin"
        ]
    }
]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/destinations.json', 'w', encoding='utf-8') as f:
    json.dump(destinations, f, ensure_ascii=False, indent=2)

print("Exported destinations and reviews successfully!")
