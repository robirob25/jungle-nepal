import json

new_tour = {
    "slug": "panthere-des-neiges",
    "title": "Expédition : Panthère des Neiges Exclusive (17 jours)",
    "title_en": "Exclusive Snow Leopard Expedition (17 Days)",
    "duration": "17 Jours",
    "duration_en": "17 Days",
    "price": "4 300 €",
    "price_num": 4300,
    "group_size": "Micro-groupe 4 à 8 explorateurs",
    "group_size_en": "Small group 4 to 8 explorers",
    "rating": "5.0",
    "reviews_count": 10,
    "categories": ["mustang-himalaya", "culture", "grand-tour", "safari"],
    "badge": "🏔️ Himalaya, Mustang & Spiritualité",
    "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
    "image": "/assets/snow-leopard/snow_leopard_portrait.jpg",
    "images": [
        "/assets/snow-leopard/snow_leopard_portrait.jpg",
        "/assets/snow-leopard/snow_leopard_2.jpg",
        "/assets/snow-leopard/snow_leopard_cliffs.jpg",
        "/assets/snow-leopard/manang_gangapurna.jpg",
        "/assets/snow-leopard/annapurna_himalayas.jpg"
    ],
    "overview": "Partez sur les traces du félin le plus insaisissable et mythique de la planète : la Panthère des Neiges (Panthera uncia, le Fantôme des Montagnes). Au cœur de la haute vallée sauvage de Manang (3 600 m – 4 500 m) et des contreforts sacrés des Annapurnas, cette expédition exclusive de 17 jours allie acclimatation progressive, 9 jours intenses de pistage d'altitude avec nos maîtres pisteurs natifs, et immersion culturelle bouddhiste au monastère séculaire de Braka Gompa.",
    "overview_en": "Embark on an extraordinary 17-day expedition tracking the most elusive and legendary big cat on Earth: the Snow Leopard ('Ghost of the Mountains'). High in the remote wilderness of Manang (3,600m – 4,500m) and the Annapurnas, experience 9 full field days of intensive tracking alongside expert Himalayan trackers, progressive altitude acclimatization, and ancient Buddhist heritage at the 600-year-old Braka Gompa monastery.",
    "highlights": [
        "9 jours complets sur le terrain dédiés au suivi et à l’observation du Léopard des Neiges",
        "Pistage d'élite avec maîtres pisteurs himalayens et longues-vues professionnelles",
        "Acclimatation sécurisée en paliers (Chame 2 700 m, Manang 3 600 m et lac Gangapurna)",
        "Immersion culturelle à Bhaktapur, Bandipur et au monastère vieux de 600 ans de Braka Gompa",
        "Vol panoramique au-dessus de la chaîne des Annapurnas et sources chaudes naturelles"
    ],
    "highlights_en": [
        "9 full days in the field dedicated to tracking and observing the Snow Leopard",
        "Elite tracking with native Himalayan trackers and professional spotting scopes",
        "Safe stepwise altitude acclimatization (Chame 2,700m, Manang 3,600m, Gangapurna lake)",
        "Rich cultural discovery in Bhaktapur, Bandipur and the 600-year-old Braka Gompa monastery",
        "Panoramic flight over the Annapurna range and relaxing natural hot springs"
    ],
    "program": [
        {
            "day": "1",
            "title": "Arrivée à Katmandou – Transfert direct à la cité royale de Bhaktapur",
            "title_en": "Arrival in Kathmandu – Direct Transfer to Royal Bhaktapur",
            "desc": "Accueil à l'aéroport international et transfert direct vers la cité historique de Bhaktapur. Installation à l'hôtel et présentation de l'expédition. Ce choix permet une première immersion culturelle immédiate, à l'écart de l'agitation du centre de la capitale.",
            "desc_en": "Welcome at Kathmandu International Airport and direct transfer to the historic city of Bhaktapur. Check-in and expedition briefing. This allows immediate cultural immersion away from the bustling city center."
        },
        {
            "day": "2",
            "title": "Vol panoramique Katmandou – Pokhara & Préparatifs face aux Annapurnas",
            "title_en": "Scenic Flight Kathmandu – Pokhara & Expedition Briefing",
            "desc": "Vol domestique de 30 minutes vers Pokhara offrant un panorama unique sur la chaîne des Annapurnas. Temps libre l’après-midi pour explorer les abords du lac Phewa, visiter les temples, organiser les derniers préparatifs et profiter de la vue sur les montagnes. Nuit à l'hôtel.",
            "desc_en": "30-minute domestic flight to Pokhara with breathtaking views of the Annapurnas. Afternoon free time to stroll around Phewa Lake, visit temples, finalize gear, and enjoy mountain vistas. Overnight at hotel."
        },
        {
            "day": "3",
            "title": "Pokhara – Chame (2 700 m) : Remontée de la vallée et sources chaudes",
            "title_en": "Pokhara – Chame (2,700 m): Ascending the Valley & Hot Springs",
            "desc": "Départ en véhicule privatif 4x4 pour Chame (environ 6h de piste). Ce trajet spectaculaire marque le début de la remontée de la vallée et constitue le premier palier d'acclimatation à l'altitude. En fin de journée, accès aux sources d'eau chaude naturelles en bord de rivière. Nuit en lodge/hôtel.",
            "desc_en": "Private 4x4 departure for Chame (approx. 6h drive). This scenic route marks the start of the valley ascent and serves as the first altitude acclimatization stage. In the evening, relax in natural riverside hot springs. Overnight in lodge."
        },
        {
            "day": "4",
            "title": "Chame – Manang (3 600 m) & Randonnée d'acclimatation au Lac Gangapurna",
            "title_en": "Chame – Manang (3,600 m) & Acclimatization Hike to Gangapurna Lake",
            "desc": "Trajet de 2 heures en véhicule pour rejoindre Manang (3 600 m). Pour valider ce deuxième palier de contrôle d'acclimatation, une marche est programmée l'après-midi vers le lac glaciaire turquoise de Gangapurna. Nuit à l'hôtel/lodge à Manang.",
            "desc_en": "2-hour drive to reach Manang (3,600 m). To secure proper acclimatization, an afternoon hike is scheduled to the turquoise glacial Gangapurna Lake. Overnight in lodge in Manang."
        },
        {
            "day": "5 à 13 (9 jours)",
            "title": "Expédition Léopard des Neiges – 9 Jours de suivi et de pistage intensif",
            "title_en": "Snow Leopard Expedition – 9 Days of Intensive Field Tracking",
            "desc": "Neuf jours complets sur le terrain dédiés au suivi, à la recherche d'indices (empreintes, grattages, proies) et à l'observation du Léopard des neiges dans ses vallées refuges. Chaque jour, départ matinal avec nos pisteurs himalayens expérimentés munis de longues-vues HD. L'itinéraire intègre une flexibilité permettant d'effectuer une journée de césure et de transition culturelle au monastère de Braka Gompa, un site historique majeur vieux de 600 ans.",
            "desc_en": "Nine full days in the field dedicated to tracking, searching for signs (pugmarks, scrapes, kills), and observing the Snow Leopard in its high-altitude habitat. Daily early morning scouting with veteran Himalayan spotters and high-end scopes. Includes flexible schedule with a cultural transition day visiting the 600-year-old Braka Gompa monastery."
        },
        {
            "day": "14",
            "title": "Manang – Bandipur : Descente des hautes terres vers la cité Newar",
            "title_en": "Manang – Bandipur: Descending to the Preserved Newar Town",
            "desc": "Amorce de la descente des hautes altitudes. Trajet de 6 à 7 heures de route panoramique pour rejoindre Bandipur, un village traditionnel Newar piéton reconnu pour son architecture népalaise remarquablement préservée et son panorama splendide sur les sommets. Nuit sur place.",
            "desc_en": "Beginning the descent from high altitudes. 6-7 hours scenic drive to Bandipur, a charming, vehicle-free Newar village celebrated for its preserved 18th-century architecture and Himalayan sunset views. Overnight in Bandipur."
        },
        {
            "day": "15",
            "title": "Bandipur – Katmandou & Soirée libre à Thamel",
            "title_en": "Bandipur – Kathmandu & Free Evening in Thamel",
            "desc": "Route de retour vers la vallée de Katmandou (environ 4h de trajet). Installation à l'hôtel et fin de journée libre pour se reposer, flâner dans les ruelles animées du quartier de Thamel et savourer un dîner traditionnel népalais.",
            "desc_en": "Drive back to Kathmandu Valley (approx. 4h). Hotel check-in and free evening to relax, shop in Thamel's vibrant streets, and enjoy a celebratory farewell dinner."
        },
        {
            "day": "16",
            "title": "Katmandou : Joyaux du patrimoine mondial UNESCO & Thamel",
            "title_en": "Kathmandu: UNESCO World Heritage Highlights & Cultural Tour",
            "desc": "Journée consacrée à la découverte approfondie des grands sites culturels et spirituels de la vallée de Katmandou (stūpa de Swayambhunath, temple sacré de Pashupatinath ou grande place royale). Derniers achats d'artisanat local à Thamel.",
            "desc_en": "Comprehensive guided tour of Kathmandu Valley's UNESCO World Heritage gems (Swayambhunath Monkey Temple, sacred Pashupatinath, or Durbar Square). Final souvenir shopping in Thamel."
        },
        {
            "day": "17",
            "title": "Transfert aéroport & Vol retour",
            "title_en": "Airport Transfer & International Flight Home",
            "desc": "Transfert privatif à l'aéroport international de Katmandou selon l'horaire de votre vol pour votre départ, avec des souvenirs inoubliables du Fantôme des Montagnes.",
            "desc_en": "Private transfer to Kathmandu International Airport according to your flight schedule, departing with unforgettable memories of the Mountain Ghost."
        }
    ]
}

# Update src/data/tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Remove if already exists, then append
tours = [t for t in tours if t.get('slug') != 'panthere-des-neiges']
tours.append(new_tour)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

print(f"Successfully added Snow Leopard tour to src/data/tours.json! Total tours now: {len(tours)}")
