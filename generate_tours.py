import os

tours_data = [
    {
        "id": "nepal-sauvage",
        "title": "Népal sauvage – De la jungle aux montagnes sacrées",
        "subtitle": "Un passage à travers trois Népal. La jungle de Bardia, les villages himalayens et les temples sacrés de Katmandou.",
        "duration_days": "15 jours",
        "duration_nights": "14 nuits",
        "price": 2300,
        "original_price": None,
        "badge": "Coup de ❤️",
        "badge_color": "bg-jungle-800",
        "rating": "4.9",
        "review_count": 38,
        "difficulty": "Modéré",
        "style": "Safari 360° & Culture",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-27-at-13.17.14.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
        ],
        "radar": {
            "nightlife": 1,
            "relax": 2,
            "nature": 5,
            "culture": 4,
            "wildlife": 5
        },
        "highlights": [
            "3 jours d'immersion totale et de pistage du tigre à pied dans le Parc National de Bardia",
            "Séjour paisible et authentique dans le village de Ghachok, face aux sommets des Annapurnas",
            "Découvertes culturelles et spirituelles à Lumbini (naissance de Bouddha), Bhaktapur et Katmandou"
        ],
        "departures": [
            {"dates": "04 Oct - 18 Oct 2026", "spots": "4 places restantes", "status": "Confirmé"},
            {"dates": "18 Oct - 01 Nov 2026", "spots": "2 places restantes", "status": "Dernières places"},
            {"dates": "01 Nov - 15 Nov 2026", "spots": "6 places", "status": "Confirmé"},
            {"dates": "15 Mars - 29 Mars 2027", "spots": "5 places", "status": "Saison tigres"}
        ],
        "days": [
            {"day": "Jour 1", "title": "Arrivée à Katmandou et vol pour Bardia", "desc": "Accueil par notre équipe à Katmandou, vol intérieur pour Nepalgunj et transfert privé vers la jungle de Bardia. Installation dans votre lodge et première marche d'ambiance avec nos hôtes locaux."},
            {"day": "Jour 2", "title": "Bardia, royaume des tigres et des éléphants", "desc": "Safaris au lever du jour et marche silencieuse dans la forêt de Sal à la recherche des tigres du Bengale, des éléphants sauvages et d'oiseaux multicolores."},
            {"day": "Jour 3", "title": "Jeep safari 4x4 et canoë sur la rivière", "desc": "Départ matinal en jeep découverte à travers les plaines alluviales, suivi d'une descente paisible en canoë le long de la rivière pour approcher les gavials et les oiseaux d'eau."},
            {"day": "Jour 4", "title": "Immersion culturelle Tharu et affût tigre", "desc": "Marche avec les femmes du village Tharu à la cueillette de plantes sauvages, cours de cuisine traditionnelle au feu de bois. En fin d'après-midi, affût aux tigres au coucher du soleil."},
            {"day": "Jour 5", "title": "Dernier pistage matinal et spectacle de village", "desc": "Exploration matinale autour des points d'eau, visite du sanctuaire des éléphants et soirée festive avec danses traditionnelles Tharu."},
            {"day": "Jour 6", "title": "Pause sacrée à Lumbini", "desc": "Route vers le sud et halte à Lumbini, lieu de naissance historique de Bouddha. Visite du temple Maya Devi et méditation dans les jardins sacrés."},
            {"day": "Jour 7", "title": "En route pour l'Himalaya & Pokhara", "desc": "Ascension vers la vallée de Pokhara, temps libre au bord du lac Phewa puis installation dans le village paisible de Ghachok à 1 200m d'altitude face aux Annapurnas."},
            {"day": "Jour 8", "title": "Immersion dans la vie villageoise himalayenne", "desc": "Balade à travers les rizières en terrasses avec panoramas grandioses sur le Machapuchare (Queue de Poisson). Échanges chaleureux avec les familles locales."},
            {"day": "Jour 9", "title": "Cascades secrètes & observation des vautours", "desc": "Randonnée vers les cascades sauvages de Ghachok et observation des colonies de grands vautours de l'Himalaya planant au-dessus des gorges."},
            {"day": "Jour 10", "title": "Journée libre au pied des géants de glace", "desc": "Journée à votre rythme pour vous reposer, lire face aux montagnes, photographier ou randonner sur les crêtes environnantes."},
            {"day": "Jour 11", "title": "Route pittoresque vers Bandipur", "desc": "Traversée des collines népalaises en véhicule privé jusqu'à la cité newar de Bandipur, joyau architectural perché au coucher du soleil."},
            {"day": "Jour 12", "title": "La cité royale médiévale de Bhaktapur", "desc": "Découverte de Bhaktapur, véritable musée à ciel ouvert avec ses temples en bois sculpté, sa poterie artisanale et ses cérémonies hindouistes."},
            {"day": "Jour 13", "title": "L'énergie spirituelle de Katmandou", "desc": "Exploration guidée de Pashupatinath (bûchers sacrés), de la grande stupa de Boudhanath et de Swayambhunath avec nos guides spécialistes."},
            {"day": "Jour 14", "title": "Marchés secrets de Thamel & dîner d'adieu", "desc": "Dernières emplettes d'épices et d'artisanat dans les ruelles de Katmandou, suivi d'un banquet népalais convivial avec toute l'équipe."},
            {"day": "Jour 15", "title": "Vol retour vers l'Europe", "desc": "Transfert à l'aéroport international de Katmandou avec des souvenirs gravés à tout jamais. À bientôt au Népal !"}
        ]
    },
    {
        "id": "nepal-immersion-totale",
        "title": "Népal – Immersion Totale : Culture, Vie Sauvage et Aventure",
        "subtitle": "Le tour le plus complet : rafting sur la rivière Trisuli, rhinos à Chitwan, tigres à Bardia et spiritualité de Katmandou.",
        "duration_days": "14 jours",
        "duration_nights": "13 nuits",
        "price": 2300,
        "original_price": 2600,
        "badge": "🔥 Promo -300€",
        "badge_color": "bg-fire-600",
        "rating": "4.9",
        "review_count": 42,
        "difficulty": "Dynamique",
        "style": "Immersion 360°",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920-600x800.jpg",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
        ],
        "radar": {
            "nightlife": 1,
            "relax": 2,
            "nature": 5,
            "culture": 5,
            "wildlife": 5
        },
        "highlights": [
            "Lever de soleil inoubliable sur l'Himalaya depuis les hauteurs de Nagarkot",
            "Descente palpitante en rafting en eaux vives sur la rivière Trisuli",
            "Double safari jungle exclusif : rhinocéros unicornes à Chitwan et tigres du Bengale à Bardia",
            "Pèlerinage paisible à Lumbini, lieu de naissance sacré du Bouddha"
        ],
        "departures": [
            {"dates": "12 Sept - 25 Sept 2026", "spots": "3 places restantes", "status": "Promo"},
            {"dates": "10 Oct - 23 Oct 2026", "spots": "4 places", "status": "Confirmé"},
            {"dates": "07 Nov - 20 Nov 2026", "spots": "2 places restantes", "status": "Dernières places"},
            {"dates": "06 Mars - 19 Mars 2027", "spots": "6 places", "status": "Saison tigres"}
        ],
        "days": [
            {"day": "Jour 1", "title": "Arrivée à Katmandou", "desc": "Arrivée dans la capitale népalaise, accueil personnalisé par notre équipe francophone et transfert à l'hôtel. Repos et premier briefing de voyage."},
            {"day": "Jour 2", "title": "Les sanctuaires sacrés de Katmandou", "desc": "Visite de Pashupatinath, du temple des singes (Swayambhunath) et de l'immense stupa bouddhiste de Boudhanath avec notre guide érudit."},
            {"day": "Jour 3", "title": "Patan, Bhaktapur & Nuit panoramique à Nagarkot", "desc": "Cités royales aux palais de brique rouge et bois sculpté, puis montée vers Nagarkot pour assister au coucher de soleil sur les sommets enneigés."},
            {"day": "Jour 4", "title": "Rafting sur la Trisuli & Entrée à Chitwan", "desc": "3 heures d'adrénaline en rafting sur les rapides de la rivière Trisuli, puis route vers le parc national de Chitwan (UNESCO)."},
            {"day": "Jour 5", "title": "Journée safari 4x4 à Chitwan", "desc": "Safari journée complète au cœur de la jungle : observation des rhinocéros unicornes indiens, des hardes de cerfs et des crocodiles gavials."},
            {"day": "Jour 6", "title": "Marche jungle & Route vers Pokhara", "desc": "Marche matinale d'observation des oiseaux et des empreintes, puis route vers Pokhara et son atmosphère sereine au bord du lac."},
            {"day": "Jour 7", "title": "Merveilles de Pokhara", "desc": "Chutes de Davis, grottes sacrées, Musée international de la Montagne et balade en barque sur le lac Phewa face au mont Machapuchare."},
            {"day": "Jour 8", "title": "Pèlerinage à Lumbini", "desc": "Traversée des collines vers Lumbini, visite du temple Maya Devi et des monastères bouddhistes du monde entier."},
            {"day": "Jour 9", "title": "Arrivée à Bardia & Village Tharu", "desc": "Pénétration dans le Népal sauvage de Bardia. Déjeuner au Mowgli's Lodge et balade au cœur de la communauté Tharu."},
            {"day": "Jour 10", "title": "Safari 4x4 et pistage du tigre à Bardia", "desc": "Journée entière en immersion dans la jungle profonde à la recherche du tigre du Bengale et des éléphants sauvages avec nos pisteurs natifs."},
            {"day": "Jour 11", "title": "Deuxième journée safari & Pistage à pied", "desc": "Approche furtive à pied des clairières et des berges sablonneuses où les fauves viennent s'abreuver."},
            {"day": "Jour 12", "title": "Dernier safari & Soirée culturelle Tharu", "desc": "Derniers moments magiques en forêt et spectacle envoûtant de danses et percussions traditionnelles autour du feu."},
            {"day": "Jour 13", "title": "Vol pour Katmandou", "desc": "Vol intérieur vers la capitale, shopping d'artisanat et dîner de clôture avec les organisateurs."},
            {"day": "Jour 14", "title": "Vol retour", "desc": "Transfert à l'aéroport et vol retour avec des étoiles plein les yeux."}
        ]
    },
    {
        "id": "babai-special",
        "title": "Deep Into The Wild : Babai Spécial Expérience – 5 jours",
        "subtitle": "Une expédition exclusive au cœur de la vallée la plus isolée et dense en tigres du Népal.",
        "duration_days": "5 jours",
        "duration_nights": "4 nuits",
        "price": 750,
        "original_price": 900,
        "badge": "⚡ Aventure ++",
        "badge_color": "bg-emerald-700",
        "rating": "5.0",
        "review_count": 19,
        "difficulty": "Aventurier",
        "style": "Tracking Tigre & Bivouac",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route-600x800.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc-600x800.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01-600x800.jpeg"
        ],
        "radar": {
            "nightlife": 0,
            "relax": 1,
            "nature": 5,
            "culture": 2,
            "wildlife": 5
        },
        "highlights": [
            "Accès exclusif à la vallée ultra-préservée de Babai, inaccessible au tourisme de masse",
            "Descente silencieuse en bateau et pistage du tigre à pied avec Pawan (ex-guide BBC)",
            "Deux nuits inoubliables en campement mobile sauvage au bord de la rivière (Rhino Camp & Nilgai Camp)",
            "Plein tarif reversé à la protection du parc et aux communautés autochtones"
        ],
        "departures": [
            {"dates": "15 Oct - 19 Oct 2026", "spots": "2 places", "status": "Dernières places"},
            {"dates": "12 Nov - 16 Nov 2026", "spots": "4 places", "status": "Confirmé"},
            {"dates": "18 Fév - 22 Fév 2027", "spots": "3 places", "status": "Confirmé"},
            {"dates": "20 Mars - 24 Mars 2027", "spots": "2 places", "status": "Pic saison tigre"}
        ],
        "days": [
            {"day": "Jour 1", "title": "Bienvenue dans la nature sauvage & Rhino Camp", "desc": "Prise en charge à Nepalgunj et transfert aux rives de la rivière Babai à Chepang. Safari paisible en bateau au cœur du sanctuaire et installation au Rhino Camp au bord de l'eau."},
            {"day": "Jour 2", "title": "Sur les traces du tigre du Bengale & Nilgai Camp", "desc": "Thé matinal et départ pour une grande journée de pistage à pied des tigres et léopards. Pique-nique sauvage au bord de l'eau et installation au Nilgai Camp sous la voûte céleste."},
            {"day": "Jour 3", "title": "Descente de la rivière Babai & Retour au Lodge", "desc": "Marche guidée matinale dans les hautes herbes de Sal, descente en bateau au fil de l'eau puis transfert au lodge pour une douche chaude et un dîner réconfortant."},
            {"day": "Jour 4", "title": "Safari en jeep dans l'ouest de Bardia & Danse Tharu", "desc": "Journée complète en jeep 4x4 dans le secteur ouest du parc, suivi d'une performance culturelle traditionnelle Tharu en soirée."},
            {"day": "Jour 5", "title": "Derniers regards & Transfert", "desc": "Petit-déjeuner au lodge, adieux à l'équipe locale et transfert vers l'aéroport pour votre vol de continuation."}
        ]
    },
    {
        "id": "bardia-babai-camping",
        "title": "Bardia Babai Vallée – Camping sauvage au cœur d’une nature vierge",
        "subtitle": "8 jours d'immersion totale et de bivouac sous les étoiles dans les territoires les plus reculés de Bardia.",
        "duration_days": "8 jours",
        "duration_nights": "7 nuits",
        "price": 1200,
        "original_price": None,
        "badge": "⛺ Bivouac Sauvage",
        "badge_color": "bg-jungle-700",
        "rating": "4.9",
        "review_count": 24,
        "difficulty": "Aventure",
        "style": "Expédition Bivouac",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc-600x800.jpg",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route-600x800.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01-600x800.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg"
        ],
        "radar": {
            "nightlife": 0,
            "relax": 2,
            "nature": 5,
            "culture": 3,
            "wildlife": 5
        },
        "highlights": [
            "Immersion totale en campement mobile sur les berges vierges de la rivière Babai",
            "Observation nocturne des bruits de la jungle autour du feu de camp",
            "Pisteurs et cuisiniers natifs dédiés exclusivement à votre petit groupe",
            "Probabilité maximale d'observation des grands félins et rhinocéros"
        ],
        "departures": [
            {"dates": "08 Oct - 15 Oct 2026", "spots": "4 places", "status": "Confirmé"},
            {"dates": "05 Nov - 12 Nov 2026", "spots": "3 places", "status": "Confirmé"},
            {"dates": "10 Mars - 17 Mars 2027", "spots": "2 places restantes", "status": "Dernières places"}
        ],
        "days": [
            {"day": "Jour 1", "title": "Arrivée à Bardia et installation", "desc": "Arrivée au Mowgli's Lodge, briefing de sécurité sur la jungle par Pawan et préparatifs de l'expédition."},
            {"day": "Jour 2", "title": "Entrée dans la vallée secrète de Babai", "desc": "Départ en 4x4 jusqu'au point de départ, puis marche silencieuse et installation du premier campement sous tente."},
            {"day": "Jour 3", "title": "Journée de tracking approfondi du tigre", "desc": "Suivi des empreintes fraîches le long des points d'eau et des corridors de migration des animaux."},
            {"day": "Jour 4", "title": "Pirogue & observation des berges", "desc": "Descente paisible au fil de l'eau pour surprendre les hardes d'éléphants et les cerfs venant s'abreuver."},
            {"day": "Jour 5", "title": "Immersion au cœur de la forêt de Sal", "desc": "Marche sous la canopée géante, observation des oiseaux rares et des singes entelles."},
            {"day": "Jour 6", "title": "Bivouac sur banc de sable isolé", "desc": "Dernière nuit magique sous la Voie Lactée au son des rugissements lointains et du feu crépitant."},
            {"day": "Jour 7", "title": "Retour au lodge & Soirée villageoise", "desc": "Retour à la civilisation, repos bien mérité au lodge et dîner festif avec les villageois Tharu."},
            {"day": "Jour 8", "title": "Fin de l'expédition", "desc": "Transfert vers l'aéroport de Nepalgunj."}
        ]
    },
    {
        "id": "bardia-explorateur",
        "title": "Bardia Explorateur – 5 jours dans la jungle",
        "subtitle": "La formule préférée des amoureux de nature : safaris quotidiens à pied et en 4x4 au lodge de charme.",
        "duration_days": "5 jours",
        "duration_nights": "4 nuits",
        "price": 450,
        "original_price": None,
        "badge": "⭐ Best-Seller",
        "badge_color": "bg-jungle-800",
        "rating": "4.8",
        "review_count": 56,
        "difficulty": "Facile",
        "style": "Safari & Lodge",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01-600x800.jpeg",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920-600x800.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg"
        ],
        "radar": {
            "nightlife": 1,
            "relax": 3,
            "nature": 5,
            "culture": 4,
            "wildlife": 5
        },
        "highlights": [
            "Safaris à pied quotidiens encadrés par 2 pisteurs certifiés",
            "Hébergement chaleureux au Mowgli's Resort avec repas népalais traditionnels",
            "Observation des rhinocéros, chitals, singes et plus de 250 espèces d'oiseaux",
            "Tarif imbattable en direct avec l'agence locale sans intermédiaire"
        ],
        "departures": [
            {"dates": "Départs tous les lundis & jeudis", "spots": "Toute l'année", "status": "Disponible"}
        ],
        "days": [
            {"day": "Jour 1", "title": "Arrivée au lodge à Bardia", "desc": "Accueil chaleureux par Pawan et sa famille, installation dans les chambres confortables et visite du village Tharu."},
            {"day": "Jour 2", "title": "Safari à pied journée complète", "desc": "Une journée entière à pied dans la jungle, affûts stratégiques près des rivières et pique-nique sous les arbres."},
            {"day": "Jour 3", "title": "Safari en Jeep 4x4", "desc": "Exploration des zones plus reculées du parc en véhicule 4x4 tout-terrain ouvert pour maximiser les observations."},
            {"day": "Jour 4", "title": "Marche matinale & après-midi détente", "desc": "Pistage matinal des traces fraîches, baignade dans la rivière et coucher de soleil sur les digues."},
            {"day": "Jour 5", "title": "Dernier tour & Départ", "desc": "Petit-déjeuner copieux et transfert retour vers Nepalgunj."}
        ]
    },
    {
        "id": "rafting-safari",
        "title": "Rivières Sauvages : Expédition Rafting & Safari – 18 jours",
        "subtitle": "La grande aventure aquatique et sauvage : descente de canyons en eaux vives et safaris d'exception.",
        "duration_days": "18 jours",
        "duration_nights": "17 nuits",
        "price": 2190,
        "original_price": None,
        "badge": "🚣 Rafting & Safari",
        "badge_color": "bg-sky-700",
        "rating": "5.0",
        "review_count": 15,
        "difficulty": "Sportif",
        "style": "Aventure & Eaux Vives",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3-600x800.webp",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc-600x800.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
        ],
        "radar": {
            "nightlife": 1,
            "relax": 2,
            "nature": 5,
            "culture": 4,
            "wildlife": 5
        },
        "highlights": [
            "Descente en rafting en autonomie des impressionnantes gorges de la rivière Karnali",
            "Bivouacs sur les plages de sable blanc inaccessibles par la route",
            "Observation des rarissimes dauphins d'eau douce du Gange",
            "Grande immersion finale dans la jungle de Bardia"
        ],
        "departures": [
            {"dates": "15 Oct - 01 Nov 2026", "spots": "4 places", "status": "Confirmé"},
            {"dates": "10 Nov - 27 Nov 2026", "spots": "3 places", "status": "Confirmé"},
            {"dates": "01 Mars - 18 Mars 2027", "spots": "6 places", "status": "Ouvert"}
        ],
        "days": [
            {"day": "Jour 1-2", "title": "Katmandou & Préparatifs d'expédition", "desc": "Arrivée dans la capitale, briefing technique d'eaux vives et équipement."},
            {"day": "Jour 3-8", "title": "Descente des gorges de la Karnali en rafting", "desc": "Franchissement de rapides de classe III-IV, paysages vertigineux et nuits sous tente sur les bancs de sable."},
            {"day": "Jour 9-10", "title": "Arrivée aux plaines du Terai & Dauphins du Gange", "desc": "Navigation plus paisible dans les méandres où nagent les dauphins d'eau douce."},
            {"day": "Jour 11-15", "title": "Grande immersion safari à Bardia", "desc": "5 jours complets de pistage de tigres, éléphants et rhinos avec nos pisteurs natifs."},
            {"day": "Jour 16-17", "title": "Pokhara & Cités royales", "desc": "Détente au bord du lac Phewa et visite culturelle de Bhaktapur."},
            {"day": "Jour 18", "title": "Vol retour", "desc": "Transfert aéroport et retour en France."}
        ]
    },
    {
        "id": "bardia-nuit-sauvage",
        "title": "Bardia Aventure : Nuit Sauvage sous la Voûte Céleste",
        "subtitle": "2 jours et 1 nuit en bivouac secret au cœur de la jungle pour ressentir la nature à l'état pur.",
        "duration_days": "2 jours",
        "duration_nights": "1 nuit",
        "price": 350,
        "original_price": None,
        "badge": "🌙 Micro-Aventure",
        "badge_color": "bg-amber-600",
        "rating": "4.9",
        "review_count": 31,
        "difficulty": "Accessible",
        "style": "Bivouac Express",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-8.webp",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc-600x800.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01-600x800.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg"
        ],
        "radar": {
            "nightlife": 0,
            "relax": 2,
            "nature": 5,
            "culture": 2,
            "wildlife": 5
        },
        "highlights": [
            "Une nuitée inoubliable sous tente dans une zone protégée exclusive",
            "Dîner convivial préparé au feu de camp au cœur de la nature",
            "Affûts au coucher et au lever du soleil avec 2 pisteurs expérimentés",
            "Sensations garanties au milieu des bruits nocturnes de la faune"
        ],
        "departures": [
            {"dates": "Départs quotidiens sur demande (Oct - Juin)", "spots": "Sur mesure", "status": "Disponible"}
        ],
        "days": [
            {"day": "Jour 1", "title": "Pénétration dans la jungle & Installation du camp", "desc": "Départ en début d'après-midi, marche d'approche dans la forêt, affût au coucher du soleil pour observer les animaux venant s'abreuver, dîner au feu de camp et nuit sous tente étoilée."},
            {"day": "Jour 2", "title": "Pistage matinal dans la brume & Retour au lodge", "desc": "Réveil aux chants des oiseaux et bruits de pas d'animaux, recherche des empreintes fraîches dans la rosée du matin, petit-déjeuner sauvage et retour au lodge en milieu de matinée."}
        ]
    },
    {
        "id": "tiji-mustang",
        "title": "Tiji Festival & Haut-Mustang : Mystères de l'Himalaya",
        "subtitle": "12 jours dans l'ancien royaume tibétain interdit de Lo : danses rituelles millénaires et canyons grandioses.",
        "duration_days": "12 jours",
        "duration_nights": "11 nuits",
        "price": 3300,
        "original_price": 3500,
        "badge": "🕉️ Spécial Culture",
        "badge_color": "bg-purple-800",
        "rating": "5.0",
        "review_count": 12,
        "difficulty": "Modéré",
        "style": "Himalaya & Culture Sacrée",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/image_processing20200226-4-1spyx16-150x150.jpg",
        "gallery_imgs": [
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
        ],
        "radar": {
            "nightlife": 0,
            "relax": 2,
            "nature": 5,
            "culture": 5,
            "wildlife": 2
        },
        "highlights": [
            "Assister aux 3 jours sacrés du Tiji Festival dans la cité fortifiée de Lo Manthang",
            "Découverte des grottes troglodytiques et monastères secrets du Mustang",
            "Traversée des paysages désertiques d'altitude aux teintes ocres et pourpres",
            "Permis spécial restreint de Haut-Mustang inclus sans tracas"
        ],
        "departures": [
            {"dates": "02 Mai - 13 Mai 2027", "spots": "4 places restantes", "status": "Dates Festival Tiji"},
            {"dates": "16 Mai - 27 Mai 2027", "spots": "6 places", "status": "Printemps Mustang"}
        ],
        "days": [
            {"day": "Jour 1-2", "title": "Katmandou & Vol Pokhara", "desc": "Briefing et démarches pour le permis spécial de Mustang, vol scénique vers Pokhara."},
            {"day": "Jour 3", "title": "Vol vers Jomsom & Début de piste vers Kagbeni", "desc": "Vol au-dessus des gorges de la Kali Gandaki, entrée dans le royaume de Mustang à Kagbeni."},
            {"day": "Jour 4-5", "title": "Remontée des canyons vers Lo Manthang", "desc": "Passage des villages fortifiés de Chele, Syangboche et Tsarang aux monastères rouges."},
            {"day": "Jour 6-8", "title": "Les 3 jours grandioses du Tiji Festival", "desc": "Présence au festival au palais royal : danses masquées des moines, prières sacrées et célébration du triomphe du bien sur le mal."},
            {"day": "Jour 9-10", "title": "Grottes de Chhoser & Retour vers Jomsom", "desc": "Visite des habitations troglodytes taillées dans les falaises ocres et descente vers Jomsom."},
            {"day": "Jour 11-12", "title": "Retour Katmandou & Vol international", "desc": "Vols intérieurs Pokhara - Katmandou et vol retour vers l'Europe."}
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Jungle Nepal Adventure</title>
  <meta name="description" content="{subtitle}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title} | Jungle Nepal Adventure">
  <meta property="og:description" content="{subtitle}">
  <meta property="og:image" content="{hero_img}">
  <meta property="og:type" content="website">

  <!-- Google Fonts: Plus Jakarta Sans + Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN with configuration -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Inter"', 'sans-serif'],
            heading: ['"Plus Jakarta Sans"', 'sans-serif'],
          }},
          colors: {{
            jungle: {{
              50: '#f2f8f5',
              100: '#e1efe8',
              200: '#c5dfd3',
              300: '#9ac5b5',
              400: '#6aa692',
              500: '#468974',
              600: '#346f5e',
              700: '#2a594c',
              800: '#165c45',
              900: '#0f4332',
              950: '#08261d',
            }},
            fire: {{
              50: '#fff7ed',
              100: '#ffedd5',
              200: '#fed7aa',
              300: '#fdba74',
              400: '#fb923c',
              500: '#f97316',
              600: '#ea580c',
              700: '#c2410c',
              800: '#9a3412',
            }},
            sand: {{
              50: '#faf8f5',
              100: '#f4ede4',
              200: '#e8dbca',
              300: '#d7c2a7',
              400: '#c4a682',
            }}
          }},
          boxShadow: {{
            'weroad': '0 12px 32px -4px rgba(8, 38, 29, 0.12), 0 4px 12px -2px rgba(8, 38, 29, 0.06)',
            'weroad-hover': '0 20px 40px -4px rgba(8, 38, 29, 0.2), 0 8px 16px -2px rgba(8, 38, 29, 0.1)',
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-white text-slate-800 font-sans antialiased selection:bg-jungle-800 selection:text-white">

  <!-- ========================================================================= -->
  <!-- TOP ANNOUNCEMENT BAR (WeRoad Style) -->
  <!-- ========================================================================= -->
  <aside aria-label="Bannière promo" class="bg-gradient-to-r from-jungle-950 via-jungle-900 to-jungle-800 text-white text-xs sm:text-sm py-2 px-4 sticky top-0 z-50 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span class="inline-flex items-center justify-center bg-fire-600 text-white text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full animate-pulse">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-200 hidden sm:inline">
          🇳🇵 <strong>Dernières places disponibles</strong> pour ce départ !
        </span>
        <span class="text-amber-300 font-semibold">
          -100€ avec le code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20le%20circuit%20{title}" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs">
        <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
        <span>WhatsApp direct : <strong>+33 6 95 41 32 27</strong></span>
      </a>
    </div>
  </aside>

  <!-- ========================================================================= -->
  <!-- NAVBAR STICKY -->
  <!-- ========================================================================= -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-9 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
      
      <!-- Logo -->
      <a href="../index.html" class="flex items-center gap-3 group">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-jungle-700 to-jungle-950 flex items-center justify-center text-emerald-400 border border-emerald-500/30 group-hover:scale-105 transition-transform shadow-md">
          <i data-lucide="footprints" class="w-5 h-5"></i>
        </div>
        <div class="flex flex-col">
          <span class="font-heading font-black text-base sm:text-lg tracking-tight text-jungle-950 leading-none">
            JUNGLE NEPAL
          </span>
          <span class="text-[9px] font-bold tracking-widest text-emerald-700 uppercase mt-0.5">
            Adventure • Retour accueil
          </span>
        </div>
      </a>

      <!-- Quick Nav Links -->
      <nav class="hidden md:flex items-center gap-6 text-sm font-heading font-semibold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-jungle-800 transition-colors">Tous les départs</a>
        <a href="#itineraire" class="hover:text-jungle-800 transition-colors">Itinéraire</a>
        <a href="#inclus" class="hover:text-jungle-800 transition-colors">Inclus & Extras</a>
        <a href="#avis" class="hover:text-jungle-800 transition-colors">Avis voyageurs</a>
        <a href="#faq" class="hover:text-jungle-800 transition-colors">FAQ</a>
      </nav>

      <!-- Right Action CTA -->
      <div class="flex items-center gap-3">
        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-fire-600 hover:bg-fire-500 text-white text-xs sm:text-sm font-heading font-bold px-4 sm:px-5 py-2.5 rounded-full shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <i data-lucide="calendar" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- MAIN TOUR CONTENT (WeRoad 1:1 Page Structure) -->
  <!-- ========================================================================= -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24">
    
    <!-- Breadcrumbs (WeRoad Style) -->
    <nav class="flex items-center gap-2 text-xs text-slate-500 font-medium mb-4 overflow-x-auto whitespace-nowrap">
      <a href="../index.html" class="hover:text-jungle-800 flex items-center gap-1">
        <i data-lucide="home" class="w-3.5 h-3.5"></i>
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="../index.html#prochains-departs" class="hover:text-jungle-800">Voyages Népal</a>
      <span>›</span>
      <span class="text-slate-800 font-bold truncate">{title}</span>
    </nav>

    <!-- Header Title & Badges Row (WeRoad Style) -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6">
      <div>
        <h1 class="font-heading font-black text-2xl sm:text-4xl lg:text-5xl text-jungle-950 tracking-tight leading-tight">
          {title}
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-slate-700 bg-sand-100 px-3 py-1 rounded-full">
            <i data-lucide="sun" class="w-4 h-4 text-amber-500"></i>
            <span>{duration_days} • {duration_nights}</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-800 font-bold px-3 py-1 rounded-full border border-emerald-200">
            <div class="flex text-amber-400">
              <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400"></i>
            </div>
            <span>{rating} ({review_count} avis vérifiés)</span>
          </div>
          <span class="text-xs font-bold {badge_color} text-white px-3 py-1 rounded-full">
            {badge}
          </span>
        </div>
      </div>

      <!-- Action Share / Wishlist Buttons -->
      <div class="flex items-center gap-2 shrink-0">
        <button onclick="navigator.clipboard.writeText(window.location.href); alert('Lien copié dans le presse-papiers !');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition-colors">
          <i data-lucide="share-2" class="w-4 h-4 text-slate-500"></i>
          <span>Partager</span>
        </button>
        <button onclick="toggleWishlistTour(this)" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition-colors">
          <i data-lucide="heart" class="w-4 h-4 text-slate-500"></i>
          <span>Favoris</span>
        </button>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- PHOTO MOSAIC GALLERY (WeRoad 1:1 Signature Grid) -->
    <!-- ========================================================================= -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[440px] mb-8 relative">
      <!-- Main Hero (2 cols) -->
      <div class="md:col-span-2 h-full overflow-hidden">
        <img 
          src="{hero_img}" 
          alt="{title}" 
          class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
          onclick="openLightbox(0)"
        />
      </div>
      <!-- Middle photo (1 col) -->
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img 
          src="{gallery_img_1}" 
          alt="{title}" 
          class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
          onclick="openLightbox(1)"
        />
      </div>
      <!-- Right stacked photos (1 col) -->
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img 
            src="{gallery_img_2}" 
            alt="{title}" 
            class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
            onclick="openLightbox(2)"
          />
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img 
            src="{gallery_img_3}" 
            alt="{title}" 
            class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
            onclick="openLightbox(3)"
          />
        </div>
      </div>

      <!-- View All Photos Button Badge -->
      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-heading font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105">
        <i data-lucide="images" class="w-4 h-4 text-jungle-800"></i>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- ========================================================================= -->
    <!-- STICKY SUB-NAV (WeRoad Style) -->
    <!-- ========================================================================= -->
    <div class="sticky top-[73px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-heading font-bold text-slate-600">
        <a href="#apercu" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Aperçu</a>
        <a href="#pour-moi" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Profil Voyage</a>
        <a href="#itineraire" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Itinéraire Jour par Jour</a>
        <a href="#inclus" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Inclus & Extras</a>
        <a href="#avis" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Avis</a>
        <a href="#faq" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">FAQ</a>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- 2-COLUMN MAIN CONTENT (Content Left 8 cols + Sticky Card Right 4 cols) -->
    <!-- ========================================================================= -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT COLUMN (Main narrative & Itinerary) -->
      <div class="lg:col-span-8 space-y-12">
        
        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
            {subtitle}
          </p>

          <!-- Key Highlights Box -->
          <div class="bg-sand-50 rounded-3xl p-6 sm:p-8 border border-sand-200">
            <h3 class="font-heading font-bold text-lg text-jungle-950 mb-4 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-5 h-5 text-amber-500"></i>
              <span>Les temps forts du voyage</span>
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-slate-700">
              {highlights_html}
            </ul>
          </div>
        </section>

        <!-- SECTION 2: CE VOYAGE EST POUR MOI ? (WeRoad Profile Radar) -->
        <section id="pour-moi" class="pt-6 border-t border-slate-200">
          <h2 class="font-heading font-extrabold text-2xl text-jungle-950 mb-6">
            Ce voyage est-il fait pour moi ?
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/80">
            
            <div class="space-y-4">
              <!-- Wildlife Radar -->
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium">
                  <span>🐅</span> Faune & Pistage
                </span>
                <div class="flex gap-1.5">
                  {radar_wildlife}
                </div>
              </div>

              <!-- Nature Radar -->
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium">
                  <span>🌿</span> Nature & Aventure
                </span>
                <div class="flex gap-1.5">
                  {radar_nature}
                </div>
              </div>

              <!-- Culture Radar -->
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium">
                  <span>🛕</span> Culture & Vie locale
                </span>
                <div class="flex gap-1.5">
                  {radar_culture}
                </div>
              </div>
            </div>

            <div class="space-y-4">
              <!-- Relax Radar -->
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium">
                  <span>🧘</span> Relax & Contemplation
                </span>
                <div class="flex gap-1.5">
                  {radar_relax}
                </div>
              </div>

              <!-- Nightlife Radar -->
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium">
                  <span>🎉</span> Fête & Vie nocturne
                </span>
                <div class="flex gap-1.5">
                  {radar_nightlife}
                </div>
              </div>

              <!-- Effort & Style -->
              <div class="pt-2 border-t border-slate-200 flex items-center justify-between text-sm font-semibold">
                <span class="text-slate-500">Effort physique :</span>
                <span class="text-jungle-800 bg-emerald-50 px-2.5 py-0.5 rounded-full">{difficulty}</span>
              </div>
            </div>

          </div>
        </section>

        <!-- SECTION 3: ITINÉRAIRE (WeRoad Accordion) -->
        <section id="itineraire" class="pt-6 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-heading font-extrabold text-2xl sm:text-3xl text-jungle-950">
                Itinéraire détaillé
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Programme jour par jour conçu et encadré par nos pisteurs natifs.
              </p>
            </div>
            <button onclick="toggleAllDays()" class="text-xs font-bold text-jungle-800 hover:text-fire-600 transition-colors">
              Tout déplier / replier
            </button>
          </div>

          <!-- Day-by-Day Accordion Container -->
          <div class="space-y-3">
            {days_html}
          </div>
        </section>

        <!-- SECTION 4: INCLUS & EXTRAS (WeRoad Style) -->
        <section id="inclus" class="pt-8 border-t border-slate-200">
          <h2 class="font-heading font-extrabold text-2xl sm:text-3xl text-jungle-950 mb-6">
            Ce qui est inclus dans votre séjour
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            
            <!-- Inclus -->
            <div class="bg-emerald-50/70 p-6 sm:p-8 rounded-3xl border border-emerald-200">
              <h3 class="font-heading font-bold text-base text-emerald-900 mb-4 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600"></i>
                <span>Inclus dans le prix</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-emerald-950">
                <li class="flex items-start gap-2"><span>✓</span><span>Tous les hébergements (éco-lodges de charme et hôtels traditionnels sélectionnés)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Pension complète en jungle (3 repas sains et locaux par jour)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Vols intérieurs & transports privés mentionnés au programme</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Permis d'entrée aux Parcs Nationaux et taxes de conservation</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Accompagnement par des pisteurs d'élite certifiés (Pawan / Kiran)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Assistance et coordination 24h/24 en français (Robin)</span></li>
              </ul>
            </div>

            <!-- Non inclus -->
            <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200">
              <h3 class="font-heading font-bold text-base text-slate-800 mb-4 flex items-center gap-2">
                <i data-lucide="x-circle" class="w-5 h-5 text-slate-400"></i>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-600">
                <li class="flex items-start gap-2"><span>✕</span><span>Vols internationaux aller-retour (Paris/Europe - Katmandou)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Frais de visa népalais (environ 30$ à 50$ à l'arrivée)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Boissons alcoolisées et dépenses personnelles</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Assurance voyage personnelle obligatoire</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Pourboires pour les équipes locales</span></li>
              </ul>
            </div>

          </div>
        </section>

        <!-- SECTION 5: AVIS (WeRoad Social Proof) -->
        <section id="avis" class="pt-8 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-heading font-extrabold text-2xl sm:text-3xl text-jungle-950">
                Avis sur ce circuit
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Note globale <strong>4.9 / 5</strong> sur Google Reviews
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="bg-sand-50 p-5 rounded-2xl border border-slate-200 text-xs sm:text-sm space-y-3">
              <div class="flex text-amber-400 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
              </div>
              <p class="italic text-slate-700">« Une aventure exceptionnelle. Nous avons eu la chance de voir des tigres et des rhinos en pleine liberté. L'accompagnement de Pawan et Robin a rendu ce voyage magique. »</p>
              <p class="font-bold text-jungle-950">— Adrien N. (Voyageur vérifié)</p>
            </div>

            <div class="bg-sand-50 p-5 rounded-2xl border border-slate-200 text-xs sm:text-sm space-y-3">
              <div class="flex text-amber-400 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
              </div>
              <p class="italic text-slate-700">« Ce n'est pas un simple safari, c'est une véritable leçon d'humilité et de respect de la nature. Hébergements très confortables et ambiance géniale en petit groupe. »</p>
              <p class="font-bold text-jungle-950">— Samantha G. (Voyageuse vérifiée)</p>
            </div>
          </div>
        </section>

        <!-- SECTION 6: FAQ ACCORDION -->
        <section id="faq" class="pt-8 border-t border-slate-200">
          <h2 class="font-heading font-extrabold text-2xl text-jungle-950 mb-6">
            Questions fréquentes sur ce voyage
          </h2>

          <div class="space-y-3 text-sm">
            <details class="group bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <summary class="font-heading font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment se passe la réservation et le paiement ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
                Pour bloquer votre place, un acompte de 30% est demandé par carte bancaire ou virement sécurisé. Le solde restant est réglé avant le départ ou à votre arrivée à Katmandou.
              </p>
            </details>

            <details class="group bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <summary class="font-heading font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Est-il dangereux de faire un safari à pied face aux tigres ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
                Nos safaris à pied sont toujours encadrés par 2 pisteurs professionnels expérimentés (plus de 20 ans d'expérience). Ils connaissent parfaitement les comportements de la faune et les règles de sécurité strictes à respecter.
              </p>
            </details>

            <details class="group bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <summary class="font-heading font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Quel équipement dois-je emporter ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
                Des vêtements aux couleurs neutres (kaki, beige, marron), de bonnes chaussures de marche, un chapeau, une gourde, de la crème solaire, un répulsif anti-moustiques et des jumelles. Une liste complète vous sera envoyée dès votre inscription.
              </p>
            </details>
          </div>
        </section>

      </div>

      <!-- ========================================================================= -->
      <!-- RIGHT COLUMN: STICKY BOOKING CARD (WeRoad 1:1 Signature) -->
      <!-- ========================================================================= -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-28 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-weroad space-y-6">
          
          <div>
            <span class="text-[11px] font-heading font-bold uppercase tracking-wider text-jungle-800">{style}</span>
            <h3 class="font-heading font-extrabold text-xl text-jungle-950 mt-1">
              {title}
            </h3>
            <p class="text-xs text-slate-500 mt-1">{duration_days} • Petit groupe (4 à 8 pers)</p>
          </div>

          <!-- Price Row -->
          <div class="pt-4 border-t border-slate-100 flex items-baseline justify-between">
            <div>
              <p class="text-[11px] font-semibold uppercase text-slate-400">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-heading font-black text-3xl text-jungle-950">{price} €</span>
                {original_price_html}
              </div>
            </div>
            {discount_badge_html}
          </div>

          <!-- Departures Selector List (WeRoad Style) -->
          <div class="space-y-2.5">
            <label class="block text-xs font-heading font-bold uppercase tracking-wider text-slate-600">
              Sélectionnez une date de départ :
            </label>
            <div class="space-y-2">
              {departures_html}
            </div>
          </div>

          <!-- Primary CTA Button (WeRoad Coral/Orange) -->
          <button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-heading font-black text-base shadow-xl shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all text-center">
            Réserver ma place →
          </button>

          <!-- Reassurance Micro-Copy -->
          <div class="space-y-2 text-xs text-slate-500 pt-2 border-t border-slate-100">
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Acompte de 30% seulement à la réservation</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Annulation sans frais jusqu'à 30 jours</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Paiement 100% sécurisé (CB / Virement)</span>
            </div>
          </div>

          <!-- Extra Quick Links -->
          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2.5 text-xs">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20j'ai%20une%20question%20sur%20le%20circuit%20{title}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-emerald-50 text-emerald-800 font-bold hover:bg-emerald-100 transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4 text-emerald-600"></i>
              <span>Poser une question sur WhatsApp</span>
            </a>
            <a href="tel:+33695413227" class="flex items-center justify-center gap-2 py-2 rounded-xl text-slate-600 hover:text-slate-900 font-semibold transition-colors">
              <i data-lucide="phone" class="w-3.5 h-3.5"></i>
              <span>Appeler Robin au +33 6 95 41 32 27</span>
            </a>
          </div>

        </div>
      </div>

    </div>

  </main>

  <!-- ========================================================================= -->
  <!-- MODAL: BOOKING & ENQUIRY -->
  <!-- ========================================================================= -->
  <div id="booking-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative animate-fade-in text-slate-900 max-h-[90vh] overflow-y-auto">
      <button onclick="closeBookingForm()" class="absolute top-5 right-5 p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-2xl bg-fire-100 text-fire-600 flex items-center justify-center">
          <i data-lucide="ticket" class="w-5 h-5"></i>
        </div>
        <div>
          <h3 class="font-heading font-black text-xl text-jungle-950">
            Réservation • {title}
          </h3>
          <p class="text-xs text-slate-500">À partir de {price} € / personne</p>
        </div>
      </div>

      <form onsubmit="handleBookingSubmit(event)" class="space-y-4 text-sm mt-4">
        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Date choisie</label>
          <select id="modal-date-select" class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            {modal_departures_options}
          </select>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Voyageurs</label>
            <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
              <option>1 voyageur</option>
              <option selected>2 voyageurs</option>
              <option>3 voyageurs</option>
              <option>4 voyageurs et +</option>
            </select>
          </div>
          <div>
            <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Chambre</label>
            <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
              <option>Double / Twin (inclus)</option>
              <option>Individuelle (+ supplément)</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Vos coordonnées</label>
          <div class="grid grid-cols-2 gap-3 mb-3">
            <input type="text" placeholder="Prénom & Nom" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <input type="tel" placeholder="Téléphone / WhatsApp" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
          </div>
          <input type="email" placeholder="Adresse email" required class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
        </div>

        <button type="submit" class="w-full py-4 rounded-2xl bg-fire-600 hover:bg-fire-500 text-white font-heading font-black text-base shadow-xl shadow-fire-600/30">
          Confirmer ma pré-réservation (Sans frais) →
        </button>
      </form>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- LIGHTBOX GALLERY MODAL -->
  <!-- ========================================================================= -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 hidden bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
    <button onclick="closeLightbox()" class="absolute top-6 right-6 text-white p-2 hover:bg-white/10 rounded-full">
      <i data-lucide="x" class="w-7 h-7"></i>
    </button>
    <img id="lightbox-img" src="" alt="Photo agrandie" class="max-w-4xl max-h-[85vh] object-contain rounded-2xl shadow-2xl">
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT -->
  <!-- ========================================================================= -->
  <script>
    lucide.createIcons();

    const allImages = [
      "{hero_img}",
      "{gallery_img_1}",
      "{gallery_img_2}",
      "{gallery_img_3}"
    ];

    function openLightbox(index) {{
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      img.src = allImages[index] || allImages[0];
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      document.getElementById('lightbox-modal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function toggleAllDays() {{
      const accordions = document.querySelectorAll('details.day-accordion');
      const allOpen = Array.from(accordions).every(a => a.open);
      accordions.forEach(a => a.open = !allOpen);
    }}

    function scrollToBooking() {{
      document.getElementById('booking-widget').scrollIntoView({{ behavior: 'smooth' }});
    }}

    function openBookingForm() {{
      document.getElementById('booking-modal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeBookingForm() {{
      document.getElementById('booking-modal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function handleBookingSubmit(e) {{
      e.preventDefault();
      alert('🎉 Pré-réservation enregistrée avec succès ! Robin et Pawan prennent contact avec vous sous 24h.');
      closeBookingForm();
    }}

    function toggleWishlistTour(btn) {{
      btn.classList.toggle('bg-fire-50');
      btn.classList.toggle('text-fire-600');
      btn.classList.toggle('border-fire-300');
    }}
  </script>
</body>
</html>
"""

def generate_dots(val):
    dots = ""
    for i in range(5):
        if i < val:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-jungle-800"></span>'
        else:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-slate-300"></span>'
    return dots

for tour in tours_data:
    # Build Highlights HTML
    highlights_html = "".join([f'<li class="flex items-start gap-2.5"><i data-lucide="check-circle" class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5"></i><span>{h}</span></li>' for h in tour["highlights"]])
    
    # Build Departures HTML
    departures_html = ""
    modal_departures_options = ""
    for i, dep in enumerate(tour["departures"]):
        active_class = "border-jungle-800 bg-emerald-50/50" if i == 0 else "border-slate-200 hover:border-slate-300"
        departures_html += f"""
        <label class="flex items-center justify-between p-3 rounded-2xl border {active_class} cursor-pointer transition-all text-xs">
          <div class="flex items-center gap-2">
            <input type="radio" name="departure_date" value="{dep['dates']}" {"checked" if i==0 else ""} class="text-jungle-800 focus:ring-jungle-700">
            <div>
              <p class="font-bold text-slate-800">{dep['dates']}</p>
              <p class="text-[10px] text-slate-500">{dep['spots']}</p>
            </div>
          </div>
          <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-emerald-800">{dep['status']}</span>
        </label>
        """
        modal_departures_options += f"<option>{dep['dates']} ({dep['spots']})</option>"

    # Build Days Accordion HTML
    days_html = ""
    for i, d in enumerate(tour["days"]):
        is_open = "open" if i < 3 else ""
        days_html += f"""
        <details class="day-accordion group bg-white rounded-2xl border border-slate-200/90 shadow-sm p-4 sm:p-5 transition-all" {is_open}>
          <summary class="font-heading font-bold text-sm sm:text-base text-jungle-950 cursor-pointer flex items-center justify-between gap-3 list-none">
            <div class="flex items-center gap-3">
              <span class="w-8 h-8 rounded-xl bg-sand-100 text-jungle-800 font-black text-xs flex items-center justify-center shrink-0 border border-sand-200">
                {i+1}
              </span>
              <span>{d['day']} – {d['title']}</span>
            </div>
            <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 group-open:rotate-180 transition-transform shrink-0"></i>
          </summary>
          <div class="mt-4 pl-11 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
            <p>{d['desc']}</p>
          </div>
        </details>
        """

    # Price specifics
    original_price_html = f'<span class="text-sm text-slate-400 line-through">{tour["original_price"]} €</span>' if tour["original_price"] else ""
    discount_badge_html = f'<span class="text-xs font-bold text-fire-600 bg-fire-50 px-2.5 py-1 rounded-full border border-fire-200">Économisez {tour["original_price"] - tour["price"]} €</span>' if tour["original_price"] else ""

    content = template.format(
        title=tour["title"],
        subtitle=tour["subtitle"],
        duration_days=tour["duration_days"],
        duration_nights=tour["duration_nights"],
        price=tour["price"],
        original_price_html=original_price_html,
        discount_badge_html=discount_badge_html,
        badge=tour["badge"],
        badge_color=tour["badge_color"],
        rating=tour["rating"],
        review_count=tour["review_count"],
        difficulty=tour["difficulty"],
        style=tour["style"],
        hero_img=tour["hero_img"],
        gallery_img_1=tour["gallery_imgs"][0],
        gallery_img_2=tour["gallery_imgs"][1],
        gallery_img_3=tour["gallery_imgs"][2],
        highlights_html=highlights_html,
        departures_html=departures_html,
        modal_departures_options=modal_departures_options,
        days_html=days_html,
        radar_wildlife=generate_dots(tour["radar"]["wildlife"]),
        radar_nature=generate_dots(tour["radar"]["nature"]),
        radar_culture=generate_dots(tour["radar"]["culture"]),
        radar_relax=generate_dots(tour["radar"]["relax"]),
        radar_nightlife=generate_dots(tour["radar"]["nightlife"]),
    )

    out_file = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours', f'{tour["id"]}.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {out_file}")

print("All tour pages generated successfully!")
