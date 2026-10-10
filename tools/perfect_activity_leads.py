import re

UPDATES = {
    # 1. Safari Jeep Bardia FR
    'src/pages/tours/safari-jeep-bardia.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Explorez les zones reculées de Bardia en Jeep safari privatisée
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Privatisée pour votre groupe (jusqu'à 6 personnes) au tarif de <strong>190 € la journée complète</strong>, cette exploration motorisée en 4x4 tout-terrain est le moyen idéal d'atteindre les secteurs les plus profonds et préservés du <strong>parc national de Bardia</strong> (secteurs de Baghaura, berges de la Karnali). Encadrée par un chauffeur chevronné et un guide naturaliste certifié, l'excursion inclut l'intégralité des permis du parc ainsi que le panier-repas en brousse pour couvrir de grandes distances et maximiser vos chances de croiser le tigre du Bengale.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              À bord d’un véhicule 4x4 spécialement adapté et totalement ouvert sur l’extérieur, vous sillonnez les pistes forestières et les plaines alluviales en traquant les empreintes fraîches de la nuit et en interprétant chaque cri d’alerte de la canopée, accompagnés d'un guide jungle senior et d'un pisteur d’élite."""
    ),

    # 2. Safari Pied Bardia FR
    'src/pages/tours/safari-pied-bardia.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Partez à pied au cœur du parc national de Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Proposé au tarif de <strong>50 € par personne pour une journée complète</strong> (06h30–18h00), le <strong>safari à pied dans le parc national de Bardia</strong> est l'expérience d'immersion la plus pure et palpitante du Népal. Encadrée obligatoirement par <strong>deux pisteurs natifs certifiés</strong> armés de bâtons traditionnels en bambou, cette journée inclut le permis officiel d'entrée, le déjeuner pris au cœur de la jungle et offre un <strong>taux d'observation de 85%+ pour le tigre du Bengale</strong> en saison sèche.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Loin du bruit des moteurs, vous quittez les pistes classiques pour progresser silencieusement dans les sous-bois de sals et les hautes herbes à éléphants. Vos deux guides décryptent chaque empreinte fraîche de la nuit, les indices olfactifs et les cris d’alerte des cervidés pour vous positionner aux meilleurs points d'affût naturels."""
    ),

    # 3. Rafting Safari Bardia FR
    'src/pages/tours/rafting-safari-bardia.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Descendez la rivière Karnali en rafting safari privatisé au cœur de Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Accessible à <strong>120 € par personne la journée complète</strong>, cette descente en <strong>rafting safari sur la rivière Karnali</strong> (35 km de dérive silencieuse le long du parc national de Bardia) est l'approche la plus discrète et sauvage pour surprendre la grande faune. Encadrée par un barreur d'eau vive certifié, un guide naturaliste senior et un pisteur d’élite, la journée inclut l'équipement de sécurité complet, le transfert 4x4, les permis du parc et un déjeuner pique-nique dressé sur une plage fluviale isolée.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Portée par les courants calmes et cristallins de la Karnali et du bras Geruwa, l'embarcation dérive sans bruit le long des falaises boisées, des bancs de graviers et des îles fluviales inaccessibles par voie terrestre. Cette perspective unique terre-eau offre des opportunités rares d'observer le rare <strong>dauphin d'eau douce du Gange</strong>, le <strong>crocodile gavial</strong>, ainsi que des éléphants et des tigres venant s'abreuver sur les berges au grand jour."""
    ),

    # 4. Safari Pied Chitwan FR
    'src/pages/tours/safari-pied-chitwan.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Découvrez Chitwan autrement : à pied
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Proposé au tarif de <strong>70 € par personne pour une journée complète</strong>, le <strong>safari à pied à Chitwan</strong> vous plonge au plus près de la 2ème plus grande population mondiale de <strong>rhinocéros unicornes d’Asie</strong> (>690 individus protégés). Accompagnée de deux naturalistes locaux certifiés, cette exploration pédestre inclut les permis officiels, le déjeuner en brousse et garantit un taux d’observation du rhinocéros approchant 95% toute l'année, loin de la poussière des convois motorisés.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Départ à l'aube pour profiter de la fraîcheur matinale et du pic d'activité animale. Vos guides progressent silencieusement à travers les forêts communautaires, les clairières de Sal et le long des rivières pour déceler empreintes fraîches, bruits de mastication et cris d'alerte des singes, en quête de rhinocéros, d'ours lippus, de tigres du Bengale et d'oiseaux tropicaux."""
    ),

    # 5. Safari Jeep Chitwan FR
    'src/pages/tours/safari-jeep-chitwan.astro': (
        """<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">
            <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">
              Explorez les plaines et jungles de Chitwan en Jeep safari privatisée
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal not-prose">
              Privatisée pour votre groupe (jusqu'à 6 personnes) au tarif de <strong>190 € la journée complète</strong>, cette excursion en 4x4 tout-terrain s'enfonce profondément dans la zone cœur classée UNESCO du <strong>parc national de Chitwan</strong> (secteurs préservés de Kasara et Sukhibhar). Guidée par un chauffeur chevronné et un guide naturaliste senior, la formule inclut tous les permis du parc et le déjeuner en brousse pour maximiser l'observation des rhinocéros unicornes, ours lippus, gavials et tigres du Bengale.
            </p>
            <p>
              Plongez au cœur du plus ancien et célèbre parc national du Népal pour une journée complète d’exploration motorisée en totale immersion. Inscrit au patrimoine mondial de l'UNESCO, le parc national de Chitwan offre une mosaïque d'habitats exceptionnelle : vastes forêts de Sal, prairies alluviales géantes et méandres fluviaux propices à une densité de faune remarquable."""
    ),

    # 6. Safari Jeep Bardia EN
    'src/pages/en/tours/bardia-jeep-safari.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Explore remote wilderness corridors of Bardia by private 4x4 Jeep
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Privatized exclusively for your group (up to 6 guests) at <strong>€190 for a full day</strong>, this 4x4 open-jeep safari is the ultimate way to reach the most secluded, untamed sectors of <strong>Bardia National Park</strong> (including Baghaura and the Karnali floodplains). Escorted by an expert driver and a certified senior naturalist, this all-inclusive expedition covers national park entry permits and a freshly prepared bush lunch, allowing you to cover vast distances and maximize encounters with wild Bengal tigers.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Aboard a customized safari vehicle completely open to the wilderness, you navigate forest trails and alluvial grasslands alongside an elite tracking team, reading fresh night pugmarks and interpreting canopy alarm calls throughout the day."""
    ),

    # 7. Safari Pied Bardia EN
    'src/pages/en/tours/bardia-walking-safari.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Head into the deep wilderness of Bardia National Park on foot
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Offered at <strong>€50 per person for a full day</strong> (6:30 AM – 6:00 PM), the <strong>walking safari in Bardia National Park</strong> is Nepal's purest, most thrilling wildlife encounter. Escorted by <strong>two licensed native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, this tour includes park permits, a jungle bush lunch, and boasts an <strong>85%+ sighting probability for wild Bengal tigers</strong> during the peak dry season.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Free from the noise of vehicle engines, you leave conventional tracks to tread quietly through towering Sal forests and elephant grasslands. Your guides read fresh pugmarks, scent markings, and canopy alarm calls to position you at strategic riverside watchpoints throughout the day."""
    ),

    # 8. Rafting Safari Bardia EN
    'src/pages/en/tours/bardia-rafting-safari.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Float Down the Karnali River on a Private Rafting Safari in Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Available at <strong>€120 per person for a full day</strong>, this <strong>Karnali River rafting safari</strong> (a 35 km silent drift along Bardia National Park) is the quietest and most stealthy way to observe wild Asian wildlife. Guided by a certified whitewater captain, senior naturalist, and elite tracker, the tour includes complete safety equipment, 4x4 transfers, national park permits, and a freshly prepared picnic lunch on an isolated river island.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Carried by gentle, clear currents through the Karnali and Geruwa channels, your raft drifts silently alongside forested bluffs and gravel banks. This rare water-level perspective offers unmatched opportunities to witness freshwater Gangetic dolphins, critically endangered gharials, and wild elephants or Bengal tigers emerging to drink along the riverbanks."""
    ),

    # 9. Safari Pied Chitwan EN
    'src/pages/en/tours/chitwan-walking-safari.astro': (
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Discover Chitwan differently: on foot
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Priced at <strong>€70 per person for a full day</strong>, the <strong>guided walking safari in Chitwan National Park</strong> gets you up close to the world's second-largest population of <strong>greater one-horned rhinos</strong> (>690 protected individuals). Led by two certified native naturalists, this expedition includes park permits, a wilderness picnic lunch, and boasts a near-guaranteed 95% rhino sighting rate year-round, far from motorized tourist routes.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Setting off early in the morning to catch peak wildlife activity, your team tracks pugmarks, feeding traces, and primate alarm calls through Sal forests, tall grassland corridors, and quiet river bends in search of rhinos, sloth bears, Bengal tigers, and rare tropical birds."""
    ),

    # 10. Safari Jeep Chitwan EN
    'src/pages/en/tours/chitwan-jeep-safari.astro': (
        """<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">
            <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">
              Explore the floodplains and wild jungles of Chitwan by private safari 4x4
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal not-prose">
              Privatized exclusively for your group (up to 6 passengers) at <strong>€190 for a full day</strong>, this open 4x4 expedition penetrates deep into the UNESCO World Heritage core sectors of <strong>Chitwan National Park</strong> (including Kasara and Sukhibhar). Guided by an expert driver and a certified senior naturalist, this all-inclusive tour covers national park permits and a bush lunch to maximize encounters with greater one-horned rhinos, sloth bears, gharials, and Bengal tigers.
            </p>
            <p>
              Immerse yourself into Nepal's oldest and most renowned national park for a full day of motorized exploration in total wilderness. A UNESCO World Heritage site, Chitwan National Park boasts an extraordinary mosaic of habitats: vast Sal tree forests, gigantic elephant-grass floodplains, and meandering river bends fostering remarkable wildlife density."""
    )
}

# Regex to match the section beginning down to where the content continues
# In each file, we replace from '<div class="space-y-4">\n            <h2' (or prose) down to the matching anchor
PATTERNS = {
    'src/pages/tours/safari-jeep-bardia.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base text-slate-700 leading-relaxed font-normal">\s*À bord d’un véhicule 4x4 spécialement adapté',
        UPDATES['src/pages/tours/safari-jeep-bardia.astro']
    ),
    'src/pages/tours/safari-pied-bardia.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\s*Accompagné d’un <strong>guide jungle expérimenté</strong>',
        UPDATES['src/pages/tours/safari-pied-bardia.astro']
    ),
    'src/pages/tours/rafting-safari-bardia.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base text-slate-700 leading-relaxed font-normal">\s*À bord d\'un raft tout équipé et sécurisé',
        UPDATES['src/pages/tours/rafting-safari-bardia.astro']
    ),
    'src/pages/tours/safari-pied-chitwan.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\s*Départ tôt le matin',
        UPDATES['src/pages/tours/safari-pied-chitwan.astro']
    ),
    'src/pages/tours/safari-jeep-chitwan.astro': (
        r'<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">\s*<h2[^>]*>.*?</h2>\s*<p>.*?</p>\s*<p>.*?</p>\s*<p>\s*À bord d’un véhicule 4x4 privatisé',
        UPDATES['src/pages/tours/safari-jeep-chitwan.astro'] + '\n            <p>\n              À bord d’un véhicule 4x4 privatisé'
    ),
    'src/pages/en/tours/bardia-jeep-safari.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base text-slate-700 leading-relaxed font-normal">\s*Aboard a specialized 4x4 safari vehicle',
        UPDATES['src/pages/en/tours/bardia-jeep-safari.astro']
    ),
    'src/pages/en/tours/bardia-walking-safari.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\s*Accompanied by an <strong>experienced jungle guide</strong>',
        UPDATES['src/pages/en/tours/bardia-walking-safari.astro']
    ),
    'src/pages/en/tours/bardia-rafting-safari.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base text-slate-700 leading-relaxed font-normal">\s*Aboard a private, fully equipped raft',
        UPDATES['src/pages/en/tours/bardia-rafting-safari.astro']
    ),
    'src/pages/en/tours/chitwan-walking-safari.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\s*Starting early in the morning',
        UPDATES['src/pages/en/tours/chitwan-walking-safari.astro']
    ),
    'src/pages/en/tours/chitwan-jeep-safari.astro': (
        r'<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">\s*<h2[^>]*>.*?</h2>\s*<p>.*?</p>\s*<p>.*?</p>\s*<p>\s*Aboard a private, open-sided 4x4',
        UPDATES['src/pages/en/tours/chitwan-jeep-safari.astro'] + '\n            <p>\n              Aboard a private, open-sided 4x4'
    )
}

for filepath, (pattern, replacement) in PATTERNS.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 1:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Flawlessly updated {filepath}")
    else:
        print(f"✗ Regex count {count} for {filepath}")
