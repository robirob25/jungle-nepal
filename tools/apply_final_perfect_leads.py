import re

BLOCKS = {
    'src/pages/tours/safari-jeep-bardia.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- AVERTISSEMENT)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Explorez les zones reculées de Bardia en Jeep safari privatisée
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Privatisée pour votre groupe (jusqu'à 6 personnes) au tarif de <strong>190 € la journée complète</strong>, cette exploration motorisée en 4x4 tout-terrain est le moyen idéal d'atteindre les secteurs les plus profonds et préservés du <strong>parc national de Bardia</strong> (secteurs de Baghaura, berges de la Karnali). Encadrée par un chauffeur chevronné et un guide naturaliste certifié, l'excursion inclut l'intégralité des permis du parc ainsi que le panier-repas en brousse pour couvrir de grandes distances et maximiser vos chances de croiser le tigre du Bengale.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              À bord d’un véhicule 4x4 spécialement adapté et totalement ouvert sur l’extérieur, vous sillonnez les pistes forestières et les plaines alluviales en traquant les empreintes fraîches de la nuit et en interprétant chaque cri d’alerte de la canopée, accompagnés d'un guide jungle senior et d'un pisteur d’élite.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              <strong>L’objectif majeur :</strong> maximiser vos chances d'observer le seigneur des lieux, le <strong>tigre du Bengale</strong>. La mobilité de la jeep permet de rejoindre rapidement des points stratégiques éloignés (comme les berges reculées de la rivière Karnali ou les miradors profonds) et d'augmenter significativement les opportunités de croiser le <strong>rhinocéros unicorne</strong>, les <strong>éléphants sauvages</strong>, le <strong>léopard</strong>, les hardes de <strong>cerfs axis et sambars</strong>, ainsi que les crocodiles gavials le long des bancs de sable.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Le déjeuner pique-nique est partagé en pleine nature, à l’abri d’un mirador sécurisé surplombant une clairière ou un point d’eau stratégique. Formule 100 % clé en main : tous les permis d'entrée et autorisations gouvernementales sont intégralement pris en charge.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/bardia-jeep-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- ETHICAL & WILD NATURE)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Explore remote wilderness corridors of Bardia by private 4x4 Jeep
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Privatized exclusively for your group (up to 6 guests) at <strong>€190 for a full day</strong>, this 4x4 open-jeep safari is the ultimate way to reach the most secluded, untamed sectors of <strong>Bardia National Park</strong> (including Baghaura and the Karnali floodplains). Escorted by an expert driver and a certified senior naturalist, this all-inclusive expedition covers national park entry permits and a freshly prepared bush lunch, allowing you to cover vast distances and maximize encounters with wild Bengal tigers.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Aboard a customized safari vehicle completely open to the wilderness, you navigate forest trails and alluvial grasslands alongside an elite tracking team, reading fresh night pugmarks and interpreting canopy alarm calls throughout the day.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              <strong>Primary objective:</strong> maximize your chances of encountering the apex ruler of Bardia, the <strong>Bengal tiger</strong>. The vehicle's swift mobility lets you access distant prime hotspots (such as the far banks of the Karnali River or deep jungle watchtowers), dramatically increasing opportunities to spot <strong>greater one-horned rhinos</strong>, <strong>wild elephants</strong>, <strong>leopards</strong>, herds of <strong>chital and sambar deer</strong>, and basking gharials along sandbanks.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              A bush lunch is shared in the wild, shaded inside a secured viewing machan overlooking a waterhole. Fully turn-key: all park permits and local entry permissions are fully handled.
            </p>
          </div>\n\n          """
    ),

    'src/pages/tours/safari-pied-bardia.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- Avertissement Faune Sauvage)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Partez à pied au cœur du parc national de Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Proposé au tarif de <strong>50 € par personne pour une journée complète</strong> (06h30–18h00), le <strong>safari à pied dans le parc national de Bardia</strong> est l'expérience d'immersion la plus pure et palpitante du Népal. Encadrée obligatoirement par <strong>deux pisteurs natifs certifiés</strong> armés de bâtons traditionnels en bambou, cette journée inclut le permis officiel d'entrée, le déjeuner pris au cœur de la jungle et offre un <strong>taux d'observation de 85%+ pour le tigre du Bengale</strong> en saison sèche.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Loin du bruit des moteurs, vous quittez les pistes classiques pour progresser silencieusement dans les sous-bois de sals et les hautes herbes à éléphants. Vos deux guides décryptent chaque empreinte fraîche de la nuit, les indices olfactifs et les cris d’alerte des cervidés pour vous positionner aux meilleurs points d'affût naturels.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              <strong>L’objectif principal de la journée : le tigre du Bengale</strong>. Son observation ne peut naturellement jamais être garantie. Mais la journée est également l’occasion de rechercher le <strong>rhinocéros unicorne d'Asie</strong>, les <strong>troupeaux d’éléphants sauvages</strong>, les cervidés (cerfs axis, cerfs sambar), les singes entelles et les très nombreuses espèces d’oiseaux présentes à Bardia.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Le déjeuner est pris directement dans la jungle sous les arbres géants, afin de profiter de chaque instant de la journée sans jamais quitter le parc.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/bardia-walking-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- Wildlife Tracking Safety Notice)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Head into the deep wilderness of Bardia National Park on foot
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Offered at <strong>€50 per person for a full day</strong> (6:30 AM – 6:00 PM), the <strong>walking safari in Bardia National Park</strong> is Nepal's purest, most thrilling wildlife encounter. Escorted by <strong>two licensed native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, this tour includes park permits, a jungle bush lunch, and boasts an <strong>85%+ sighting probability for wild Bengal tigers</strong> during the peak dry season.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Free from the noise of vehicle engines, you leave conventional tracks to tread quietly through towering Sal forests and elephant grasslands. Your guides read fresh pugmarks, scent markings, and canopy alarm calls to position you at strategic riverside watchpoints throughout the day.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              <strong>The primary quest: Bengal tigers.</strong> While sightings can never be 100% guaranteed in true wilderness, foot tracking also brings opportunities to observe <strong>greater one-horned Asian rhinos</strong>, <strong>wild elephant herds</strong>, chital and sambar deer, langur monkeys, and hundreds of bird species.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Bush lunch is enjoyed under ancient riverine canopy, maximizing every minute deep inside the national park.
            </p>
          </div>\n\n          """
    ),

    'src/pages/tours/rafting-safari-bardia.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- AVERTISSEMENT)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Descendez la rivière Karnali en rafting safari privatisé au cœur de Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Accessible à <strong>120 € par personne la journée complète</strong>, cette descente en <strong>rafting safari sur la rivière Karnali</strong> (35 km de dérive silencieuse le long du parc national de Bardia) est l'approche la plus discrète et sauvage pour surprendre la grande faune. Encadrée par un barreur d'eau vive certifié, un guide naturaliste senior et un pisteur d’élite, la journée inclut l'équipement de sécurité complet, le transfert 4x4, les permis du parc et un déjeuner pique-nique dressé sur une plage fluviale isolée.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Portée par les courants calmes et cristallins de la Karnali et du bras Geruwa, l'embarcation dérive sans bruit le long des falaises boisées, des bancs de graviers et des îles fluviales inaccessibles par voie terrestre. C'est le biotope exclusif du rare <strong>dauphin d'eau douce du Gange</strong>, que l'on guette dans les fosses profondes, ainsi que des deux espèces de sauriens emblématiques : le majestueux <strong>crocodile gavial du Gange</strong> et le <strong>crocodile des marais</strong>.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Sur les rives, la progression furtive offre des opportunités uniques de surprendre des éléphants sauvages, des rhinocéros unicornes venus se baigner, des hardes de cervidés et parfois même le <strong>tigre du Bengale</strong> traversant les bancs de sable au grand jour. La journée comprend plusieurs escales avec de courtes traques à pied et un déjeuner sur une plage déserte.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/bardia-rafting-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- ETHICAL & WILD NATURE)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Float Down the Karnali River on a Private Rafting Safari in Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Available at <strong>€120 per person for a full day</strong>, this <strong>Karnali River rafting safari</strong> (a 35 km silent drift along Bardia National Park) is the quietest and most stealthy way to observe wild Asian wildlife. Guided by a certified whitewater captain, senior naturalist, and elite tracker, the tour includes complete safety equipment, 4x4 transfers, national park permits, and a freshly prepared picnic lunch on an isolated river island.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Carried by gentle, crystal-clear currents through the Karnali and Geruwa channels, your raft drifts silently alongside forested bluffs and gravel banks. This unique water-level vantage point offers rare views into the habitat of the endangered <strong>Gangetic river dolphin</strong>, as well as two prehistoric crocodilian species: the slender-snouted <strong>gharial</strong> and the marsh mugger.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Along the shoreline, silent drifting often yields spectacular sightings of wild elephants bathing, greater one-horned rhinos grazing, deer herds, and occasionally a <strong>Bengal tiger</strong> crossing gravel bars in broad daylight. Includes bush stopovers for short tracking walks and an isolated beach lunch.
            </p>
          </div>\n\n          """
    ),

    'src/pages/tours/safari-pied-chitwan.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- Avertissement Faune Sauvage)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Découvrez Chitwan autrement : à pied
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Proposé au tarif de <strong>70 € par personne pour une journée complète</strong>, le <strong>safari à pied à Chitwan</strong> vous plonge au plus près de la 2ème plus grande population mondiale de <strong>rhinocéros unicornes d’Asie</strong> (>690 individus protégés). Accompagnée de deux naturalistes locaux certifiés, cette exploration pédestre inclut les permis officiels, le déjeuner en brousse et garantit un taux d’observation du rhinocéros approchant 95% toute l'année, loin de la poussière des convois motorisés.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Départ à l'aube pour profiter de la fraîcheur matinale et du pic d'activité animale. Vos guides progressent silencieusement à travers les forêts communautaires, les clairières de Sal et le long des rivières pour déceler empreintes fraîches, bruits de mastication et cris d'alerte des singes, en quête de rhinocéros, d'ours lippus, de tigres du Bengale et d'oiseaux tropicaux.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              <strong>Le tigre du Bengale constitue notre recherche la plus prestigieuse</strong>, mais Chitwan offre également d’importantes possibilités d’observation de l'ours lippu, des hardes de cervidés, des gavials du Gange et de plus de 500 espèces d'oiseaux. Le déjeuner est pris directement en pleine nature à l’ombre de la canopée.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/chitwan-walking-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- Wildlife Warning)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Discover Chitwan differently: on foot
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Priced at <strong>€70 per person for a full day</strong>, the <strong>guided walking safari in Chitwan National Park</strong> gets you up close to the world's second-largest population of <strong>greater one-horned rhinos</strong> (>690 protected individuals). Led by two certified native naturalists, this expedition includes park permits, a wilderness picnic lunch, and boasts a near-guaranteed 95% rhino sighting rate year-round, far from motorized tourist routes.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Setting off early in the morning to catch peak wildlife activity, your team tracks pugmarks, feeding traces, and primate alarm calls through Sal forests, tall grassland corridors, and quiet river bends in search of rhinos, sloth bears, Bengal tigers, and rare tropical birds.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              <strong>Bengal tigers remain the ultimate quest</strong>, while Chitwan's mosaic of riverbanks and community buffer zones also provides exceptional encounters with sloth bears, wild deer, marsh muggers, and endangered gharials. A hot picnic lunch is enjoyed directly in the jungle.
            </p>
          </div>\n\n          """
    ),

    'src/pages/tours/safari-jeep-chitwan.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">.*?</div>\s*(?=<!-- Avertissement)',
        """<section id="apercu" class="scroll-mt-28 space-y-6">
          <div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">
            <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">
              Explorez les plaines et jungles de Chitwan en Jeep safari privatisée
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal not-prose">
              Privatisée pour votre groupe (jusqu'à 6 personnes) au tarif de <strong>190 € la journée complète</strong>, cette excursion en 4x4 tout-terrain s'enfonce profondément dans la zone cœur classée UNESCO du <strong>parc national de Chitwan</strong> (secteurs préservés de Kasara et Sukhibhar). Guidée par un chauffeur chevronné et un guide naturaliste senior, la formule inclut tous les permis du parc et le déjeuner en brousse pour maximiser l'observation des rhinocéros unicornes, ours lippus, gavials et tigres du Bengale.
            </p>
            <p>
              Plongez au cœur du plus ancien et célèbre parc national du Népal pour une journée complète d’exploration motorisée en totale immersion. Inscrit au patrimoine mondial de l'UNESCO, le parc national de Chitwan offre une mosaïque d'habitats exceptionnelle : vastes forêts de Sal, prairies alluviales géantes et méandres fluviaux propices à une remarquable densité de faune.
            </p>
            <p>
              À bord d’un véhicule 4x4 privatisé et ouvert, vous êtes accompagné par un chauffeur chevronné, un guide naturaliste senior spécialiste du Terai et un pisteur d’élite. L'itinérance en jeep permet de s'éloigner des circuits courts touristiques pour s'enfoncer dans les secteurs calmes du parc, franchir les cours d'eau et guetter les passages d'animaux le long des corridors de forêt primaire.
            </p>
            <p>
              Le déjeuner pique-nique est partagé en pleine jungle, à l’abri d’un mirador sécurisé dominant un point d’eau ou une boucle fluviale. Formule 100 % clé en main : tous les permis d'entrée et taxes gouvernementales sont intégralement inclus.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/chitwan-jeep-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">.*?</div>\s*(?=<!-- Ethical & Wild Nature Warning)',
        """<section id="apercu" class="scroll-mt-28 space-y-6">
          <div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">
            <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">
              Explore the floodplains and wild jungles of Chitwan by private safari 4x4
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal not-prose">
              Privatized exclusively for your group (up to 6 passengers) at <strong>€190 for a full day</strong>, this open 4x4 expedition penetrates deep into the UNESCO World Heritage core sectors of <strong>Chitwan National Park</strong> (including Kasara and Sukhibhar). Guided by an expert driver and a certified senior naturalist, this all-inclusive tour covers national park permits and a bush lunch to maximize encounters with greater one-horned rhinos, sloth bears, gharials, and Bengal tigers.
            </p>
            <p>
              Immerse yourself into Nepal's oldest and most renowned national park for a full day of motorized exploration in total wilderness. A UNESCO World Heritage site, Chitwan National Park boasts an extraordinary mosaic of habitats: vast Sal tree forests, gigantic elephant-grass floodplains, and meandering river bends fostering remarkable wildlife density.
            </p>
            <p>
              Aboard a private, open-sided 4x4 safari vehicle, you are accompanied by a veteran driver, a senior naturalist guide specialized in the Terai biome, and an elite native tracker. Traveling by jeep allows you to escape standard tourist circuits, venture into the quietest sectors of the park, cross waterways, and watch for predator passages along primary forest corridors.
            </p>
            <p>
              Bush lunch is enjoyed deep in the jungle inside a secured observation watchtower overlooking a river curve or waterhole. Fully turn-key: all park permits, vehicle fees, and guide licenses are completely included.
            </p>
          </div>\n\n          """
    )
}

for path, (pattern, replacement) in BLOCKS.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 1:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Perfectly rewritten aperçu in {path}")
    else:
        print(f"✗ Regex count {count} for {path}")
