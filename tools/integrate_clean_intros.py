import re

# Precise insertions for each activity page
PAGES = {
    # 1. Safari Jeep Bardia FR
    'src/pages/tours/safari-jeep-bardia.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explorez les zones reculées de Bardia en Jeep safari privatisée\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explorez les zones reculées de Bardia en Jeep safari privatisée\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              Privatiser un <strong>safari en jeep d’une journée complète à Bardia</strong> coûte <strong>190 € par véhicule</strong> (jusqu’à 6 passagers). Il permet d’explorer les secteurs reculés du parc inaccessibles à pied (Baghaura, berges de la Karnali). L’excursion inclut le 4x4 tout-terrain avec chauffeur expérimenté, un guide naturaliste certifié, les permis d’entrée et le panier repas en brousse.\n            </p>'
    },

    # 2. Safari Pied Bardia FR
    'src/pages/tours/safari-pied-bardia.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Partez à pied au cœur du parc national de Bardia\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Partez à pied au cœur du parc national de Bardia\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              Un <strong>safari à pied dans le parc national de Bardia</strong> coûte <strong>50 € par personne</strong> avec Jungle Nepal Adventure. Encadré obligatoirement par <strong>deux pisteurs natifs certifiés</strong> armés de bâtons traditionnels en bambou, il dure une journée complète (6h30–18h00) et inclut le permis du parc, le déjeuner en jungle et un <strong>taux d’observation de 85%+ pour le tigre du Bengale</strong> au printemps. Les marches sans deux guides agréés sont strictement interdites par les autorités du parc.\n            </p>'
    },

    # 3. Rafting Safari Bardia FR
    'src/pages/tours/rafting-safari-bardia.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Descendez la rivière Karnali en rafting safari privatisé au cœur de Bardia\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Descendez la rivière Karnali en rafting safari privatisé au cœur de Bardia\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              Une journée de <strong>rafting et safari sur la rivière Karnali à Bardia</strong> coûte <strong>120 € par personne</strong>. Cette descente silencieuse de 35 km offre des observations exceptionnelles de dauphins d’eau douce du Gange, crocodiles gavials et tigres venant s’abreuver sur les bancs de galets, avec équipement de sécurité certifié et déjeuner sur une plage isolée.\n            </p>'
    },

    # 4. Safari Pied Chitwan FR
    'src/pages/tours/safari-pied-chitwan.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Découvrez Chitwan autrement : à pied\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Découvrez Chitwan autrement : à pied\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              Un <strong>safari à pied dans le parc national de Chitwan</strong> coûte <strong>70 € par personne</strong>. Guidé par deux naturalistes locaux, il se déroule dans les forêts communautaires et zones tampons réputées pour abriter la 2ème plus grande population mondiale de <strong>rhinocéros unicornes d’Asie</strong> (>690 individus), avec des chances d’observation à pied approchant 95% toute l’année.\n            </p>'
    },

    # 5. Safari Jeep Chitwan FR
    'src/pages/tours/safari-jeep-chitwan.astro': {
        'target': '<h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">\n              Explorez les plaines et jungles de Chitwan en Jeep safari privatisée\n            </h2>',
        'insert': '<h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">\n              Explorez les plaines et jungles de Chitwan en Jeep safari privatisée\n            </h2>\n            <p>\n              Privatiser un <strong>safari en jeep à Chitwan</strong> pour une journée complète coûte <strong>190 € pour le véhicule</strong> (jusqu’à 6 personnes). Il s’enfonce profondément dans la zone cœur classée UNESCO (Kasara, Sukhibhar) pour observer rhinocéros unicornes, ours lippus, crocodiles gavials et tigres du Bengale sous la conduite d’un guide naturaliste agréé.\n            </p>'
    },

    # 6. Safari Jeep Bardia EN
    'src/pages/en/tours/bardia-jeep-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explore Remote Bardia via Private Jeep Safari\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explore Remote Bardia via Private Jeep Safari\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>private full-day 4x4 open jeep safari in Bardia costs €190 per vehicle</strong> (accommodating up to 6 guests). It allows exploring remote park sectors inaccessible on foot (Baghaura, Karnali riverbanks). The tour includes the customized safari vehicle, expert driver, licensed senior naturalist guide, national park entry fees, and a freshly prepared bush lunch.\n            </p>'
    },

    # 7. Safari Pied Bardia EN
    'src/pages/en/tours/bardia-walking-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explore Bardia National Park on Foot\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explore Bardia National Park on Foot\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>full-day walking safari in Bardia National Park costs €50 per person</strong> with Jungle Nepal Adventure. Escorted by <strong>two certified native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, it runs from 6:30 AM to 6:00 PM and includes park permits, a jungle bush lunch, and an <strong>85%+ sighting probability for wild Bengal tigers</strong> during spring. Walking without two licensed guides is strictly illegal under Nepalese park law.\n            </p>'
    },

    # 8. Rafting Safari Bardia EN
    'src/pages/en/tours/bardia-rafting-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Drift Down the Karnali River on a Private Rafting Safari in Bardia\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Drift Down the Karnali River on a Private Rafting Safari in Bardia\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>full-day rafting safari on the Karnali River in Bardia costs €120 per person</strong>. This silent 35 km river drift offers rare views of freshwater Gangetic river dolphins, critically endangered gharial crocodiles, and riverbank tigers, accompanied by certified river guides with safety gear and riverside lunch included.\n            </p>'
    },

    # 9. Safari Pied Chitwan EN
    'src/pages/en/tours/chitwan-walking-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Discover Chitwan on Foot\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Discover Chitwan on Foot\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>guided walking safari in Chitwan National Park costs €70 per person</strong>. Led by two certified naturalists through community buffer forests, it offers a near-guaranteed <strong>95% sighting probability for greater one-horned rhinos</strong> (>690 recorded individuals), sloth bears, and river crocodilians without the disruption of motor vehicles.\n            </p>'
    },

    # 10. Safari Jeep Chitwan EN
    'src/pages/en/tours/chitwan-jeep-safari.astro': {
        'target': '<h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">\n              Explore Chitwan Plains and Forests via Private Jeep Safari\n            </h2>',
        'insert': '<h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">\n              Explore Chitwan Plains and Forests via Private Jeep Safari\n            </h2>\n            <p>\n              A <strong>full-day private jeep safari in Chitwan National Park costs €190 per vehicle</strong> (accommodating up to 6 passengers). The itinerary penetrates deep into the UNESCO World Heritage core sectors (Kasara and Sukhibhar) to track greater one-horned rhinos, sloth bears, wild elephants, and Bengal tigers alongside a licensed senior naturalist.\n            </p>'
    }
}

for path, data in PAGES.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize whitespace for matching if needed
    if data['target'] in content:
        content = content.replace(data['target'], data['insert'], 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated intro in {path}")
    else:
        print(f"✗ Target not found in {path}")
