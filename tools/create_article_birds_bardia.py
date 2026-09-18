import json, re

# Read current blog posts
with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

slug = "oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis"

# Check if slug already exists
posts_fr = [p for p in posts_fr if p['slug'] != slug]
posts_en = [p for p in posts_en if p['slug'] != slug]

# French Article Content (> 2200 words)
title_fr = "Nos oiseaux préférés de Bardia : les calaos et joyaux ailés du Teraï (2026)"
desc_fr = "Guide naturaliste complet de nos oiseaux préférés à Bardia : calao bicorne géant, rollier indien et tchitrec de paradis. Secrets d'observation, biomes et photographie ornithologique."

content_fr = """<p class="lead text-lg sm:text-xl text-slate-300 font-normal leading-relaxed mb-8">
Quand on évoque le <strong>parc national de Bardia</strong>, l'imaginaire collectif s'enflamme instantanément pour les prédateurs terrestres : le pas feutré du tigre du Bengale, la silhouette préhistorique du rhinocéros unicorne ou la force tranquille de l'éléphant sauvage. Pourtant, dès que le premier rayon de soleil perce les brumes de la forêt de sals et embrase la canopée, une tout autre féerie s'éveille. Les cimes résonnent du battement d'ailes puissant des calaos, les clairières s'illuminent des éclats bleu cobalt du rollier indien, et les sous-bois ombragés voient tournoyer le vol spectral du tchitrec de paradis.
</p>

<p>
Avec plus de <strong>500 espèces d'oiseaux recensées</strong> au fil de ses corridors fluviaux, ses savanes inondables et ses forêts vierges primaires, Bardia est l'un des plus prestigieux sanctuaires ornithologiques de toute l'Asie du Sud. Dans ce guide de terrain exclusif, notre équipe de guides naturalistes locaux partage ses coups de cœur absolus, ses secrets de repérage et les anecdotes intimes vécues au contact des trois plus spectaculaires joyaux ailés du Teraï népalais.
</p>

<figure class="my-10">
  <img src="/assets/curated_gallery/calao_bicorne_canopee.webp" alt="Calao bicorne perché dans la canopée de Bardia" class="rounded-2xl shadow-xl w-full object-cover border border-white/10" loading="lazy" />
  <figcaption class="text-xs sm:text-sm text-center text-slate-400 mt-3 italic">Le majestueux calao bicorne (Buceros bicornis), seigneur ailé de la forêt de sals à Bardia.</figcaption>
</figure>

<h2>1. Le calao bicorne géant (Buceros bicornis) : le seigneur préhistorique de la canopée</h2>
<p>
Entendre un calao bicorne avant de le voir est une expérience inoubliable pour tout voyageur en safari à pied. Son vol lourd et puissant produit un vrombissement rythmique, semblable au passage à basse altitude d'une locomotive à vapeur ou d'un petit aéronef. Ce bruit caractéristique s'explique par l'anatomie de ses rémiges : contrairement à la plupart des oiseaux dont le plumage étouffe les frottements de l'air, les rémiges du grand calao laissent passer l'air entre leurs bases nues, créant une onde sonore unique perceptible à plusieurs centaines de mètres.
</p>
<p>
Mesurant jusqu'à <strong>1,30 mètre de long</strong> pour une envergure spectaculaire pouvant dépasser <strong>1,60 mètre</strong>, le calao bicorne (<em>Buceros bicornis</em>) est le géant absolu des cimes du Teraï. Son élément anatomique le plus remarquable est sans conteste son volumineux casque corné, une protubérance dorée surmontant un bec incurvé massif. Contrairement à une idée reçue tenace, ce casque n'est pas en os plein : il s'agit d'une structure kératinisée alvéolaire ultra-légère, qui sert à la fois de caisse de résonance pour ses cris rauques et gutturaux, d'amplificateur visuel pour la parade nuptiale et d'outil pour creuser les écorces tendres.
</p>
<p>
À Bardia, les calaos bicornes jouent un rôle écologique fondamental : ce sont les « jardiniers en chef » de la jungle tropicale. Frugivores spécialisés friands de figues sauvages (<em>Ficus benghalensis</em> et <em>Ficus religiosa</em>), ils ingèrent les fruits entiers et dispersent les graines intactes sur des dizaines de kilomètres carrés lors de leurs vols au-dessus des canopées. Sans le travail quotidien des calaos, la régénération naturelle des essences nobles de la forêt de feuillus serait gravement compromise.
</p>
<p>
Leur cycle de reproduction compte parmi les merveilles comportementales du monde animal. Au printemps, la femelle s'enferme volontairement à l'intérieur d'une cavité d'arbre séculaire située entre 15 et 30 mètres de hauteur. Avec l'aide du mâle qui lui apporte des boulettes de boue, de pulpe végétale et de déjections, elle mure l'entrée du nid ne laissant subsister qu'une étroite fente verticale de quelques millimètres. Durant toute la période d'incubation et d'élevage précoce des oisillons — soit près de 3 à 4 mois consécutifs —, le mâle assure seul le ravitaillement, effectuant jusqu'à 15 allers-retours quotidiens pour régurgiter des centaines de figues et de petits insectes à sa partenaire emmurée.
</p>

<h2>2. Le rollier indien (Coracias benghalensis) : l'éclair turquoise des savanes alluviales</h2>
<p>
Dès que l'on quitte la pénombre de la grande forêt de sals pour déboucher sur les vastes prairies alluviales (<em>phantas</em>) bordant la rivière Karnali, un éclair de lumière bleu céleste captive immédiatement le regard. Le <strong>rollier indien</strong> (<em>Coracias benghalensis</em>) est le maître incontesté du contraste chromatique dans le Teraï népalais.
</p>
<p>
Au repos, perché sur un piquet de bois mort, une branche d'acacia ou un buisson épineux, le rollier paraît étonnamment discret : son dos arbore des nuances de brun cannelle, de vert olive terne et de beige sable qui le camouflent parfaitement contre les écorces sèches. Mais dès qu'il prend son essor pour intercepter un insecte au sol, une métamorphose spectaculaire s'opère : ses ailes déployées révèlent un dégradé étincelant de <strong>bleu turquoise, d'outremer profond et de cyan iridescent</strong> qui vibre sous le soleil subtropical.
</p>

<figure class="my-10">
  <img src="/assets/curated_gallery/rollier_indien_envol_turquoise.webp" alt="Rollier indien déployant ses ailes turquoise à Bardia" class="rounded-2xl shadow-xl w-full object-cover border border-white/10" loading="lazy" />
  <figcaption class="text-xs sm:text-sm text-center text-slate-400 mt-3 italic">L'explosion de couleurs du rollier indien (Coracias benghalensis) en plein envol au-dessus des phantas de Bardia.</figcaption>
</figure>

<p>
Son nom français de « rollier » (comme son appellation anglaise de <em>Roller</em>) fait directement référence à ses spectaculaires parades aériennes de séduction. Durant la saison des amours, de mars à mai, les mâles effectuent de vertigineuses acrobaties dans le ciel : ascensions verticales suivies de piqués vertigineux en vrille et de tonneaux serrés, accompagnés de cris rauques et gutturaux très sonores. Ces prouesses de voltige servent à délimiter leur territoire de chasse et à séduire les femelles perchées sur les hauteurs.
</p>
<p>
Chasseur d'affût redoutablement efficace, le rollier se nourrit d'une grande variété de proies terrestres : scarabées géants, sauterelles de savane, mantes religieuses, scorpions et petits lézards. Il plonge en piqué direct sur sa cible, la saisit de son bec robuste et retourne immédiatement sur son perchoir pour assommer la proie contre le bois avant de l'avaler d'un trait. Dans la culture népalaise et hindoue, le rollier indien (souvent associé à la divinité Shiva sous le nom local de <em>Nilkanth</em>) est considéré comme un messager de bon augure et un symbole sacré de protection pour les voyageurs.
</p>

<h2>3. Le tchitrec de paradis (Terpsiphone paradisi) : le danseur fantomatique des sous-bois</h2>
<p>
Parmi tous les passereaux qui peuplent la jungle humide de Bardia, le <strong>tchitrec de paradis</strong> (<em>Terpsiphone paradisi</em>, ou gobe-mouches du paradis asiatique) suscite l'émerveillement le plus pur. Cet oiseau d'une grâce absolue semble tout droit sorti d'une estampe d'art asiatique ancienne.
</p>
<p>
Le mâle adulte en livrée nuptiale présente un dimorphisme morphologique hors du commun. Il arbore deux très longues plumes caudales centrales (rectrices) qui peuvent mesurer jusqu'à <strong>30 à 40 centimètres de longueur</strong>, soit plus de trois fois la taille de son propre corps ! Lorsqu'il voltige à travers les sous-bois ombragés, entre les lianes et les fougères arborescentes pour capturer des moustiques et des libellules en plein vol, ces longs rubans soyeux ondulent et flottent dans l'air avec une légèreté hypnotique qui évoque le ruban d'une gymnaste rythmique.
</p>

<figure class="my-10">
  <img src="/assets/curated_gallery/tchitrec_paradis_longues_rectrices.webp" alt="Tchitrec de paradis mâle aux longues rectrices blanches dans la jungle de Bardia" class="rounded-2xl shadow-xl w-full object-cover border border-white/10" loading="lazy" />
  <figcaption class="text-xs sm:text-sm text-center text-slate-400 mt-3 italic">Le gracieux tchitrec de paradis (Terpsiphone paradisi), reconnaissable à ses spectaculaires rectrices flottantes.</figcaption>
</figure>

<p>
Ce passereau présente également un phénomène de <strong>polymorphisme chromatique</strong> fascinant chez les mâles : on observe des individus en phase rousse (corps châtain vif et calotte bleu-nuit métallique) et des individus plus âgés en phase blanche pure (corps blanc neige immaculé, calotte noire brillante aux reflets bleu cobalt et bec bleu outremer). Les femelles, quant à elles, conservent une robe rousse avec une queue de longueur standard et sans longues plumes caudales.
</p>
<p>
Le tchitrec affectionne particulièrement les forêts galeries humides bordant les cours d'eau calmes de la rivière Babai et les petits ruisseaux forestiers ombragés. C'est un migrateur partiel qui s'installe à Bardia pour nicher entre avril et août, tissant un nid minuscule en forme de cône suspendu à une fourche de branche basse, habilement décoré de mousse verte et consolidé avec des fils de toiles d'araignées.
</p>

<h2>4. Les autres joyaux ailés incontournables de la jungle de Bardia</h2>
<p>
Si le grand calao, le rollier et le tchitrec constituent le trio de tête des observateurs, la biodiversité aviaire de Bardia réserve d'innombrables autres surprises visuelles :
</p>
<ul class="space-y-3 my-6 list-disc list-inside text-slate-300">
  <li><strong>Le calao pie oriental (Anthracoceros albirostris) :</strong> Plus petit et plus sociable que le calao bicorne, souvent observé en petits groupes bruyants de 4 à 8 individus dans les vergers et à la lisière des villages Tharu.</li>
  <li><strong>Le martin-chasseur gurial (Pelargopsis capensis) :</strong> Un colosse parmi les martins-pêcheurs, doté d'un bec rouge carmin géant capable de transpercer poissons, grenouilles et crabes d'eau douce le long des bras morts de la Karnali.</li>
  <li><strong>Le martin-chasseur de Smyrne (Halcyon smyrnensis) :</strong> Magnifique oiseau au dos turquoise électrique, à la poitrine chocolat et au plastron blanc pur, très fréquent dans les rizières et fossés inondés.</li>
  <li><strong>La perruche à tête prune (Psittacula cyanocephala) :</strong> Un perroquet miniature aux couleurs éclatantes, dont les mâles arborent une tête rose violacé semblable à une fleur tropicale éclose.</li>
  <li><strong>Le guêpier d'Orient (Merops orientalis) :</strong> Acrobaties aériennes permanentes au crépuscule au-dessus des bancs de sable pour capturer abeilles et papillons.</li>
  <li><strong>Le trogon à tête rouge (Harpactes erythrocephalus) :</strong> Joyau timide et discret des forêts primaires denses, aux tons rouge cramoisi et brun doré.</li>
</ul>

<h2>Tableau comparatif : morphologie, habitat et meilleure saison d'observation</h2>
<div class="my-8 overflow-x-auto">
  <table class="w-full text-left text-sm text-slate-300 border border-white/10 rounded-xl overflow-hidden">
    <thead class="bg-white/10 text-white uppercase text-xs">
      <tr>
        <th class="p-3">Espèce</th>
        <th class="p-3">Envergure / Taille</th>
        <th class="p-3">Biome de prédilection</th>
        <th class="p-3">Période optimale</th>
        <th class="p-3">Niveau de rareté</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/10 bg-slate-900/60">
      <tr>
        <td class="p-3 font-semibold text-emerald-300">Calao bicorne géant</td>
        <td class="p-3">120 - 130 cm</td>
        <td class="p-3">Canopée des forêts de sals et figuiers sauvages</td>
        <td class="p-3">Novembre à Mai</td>
        <td class="p-3">Vulnérable (commun à Bardia)</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-cyan-300">Rollier indien</td>
        <td class="p-3">30 - 34 cm</td>
        <td class="p-3">Prairies alluviales ouvertes (phantas), lisères</td>
        <td class="p-3">Toute l'année (pic de parade en Mars-Mai)</td>
        <td class="p-3">Très commun</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-amber-300">Tchitrec de paradis</td>
        <td class="p-3">20 cm (+ 30 cm de queue)</td>
        <td class="p-3">Forêts galeries ombragées, sous-bois humides</td>
        <td class="p-3">Avril à Septembre (reproduction)</td>
        <td class="p-3">Fréquent mais discret</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-rose-300">Martin-chasseur gurial</td>
        <td class="p-3">35 - 38 cm</td>
        <td class="p-3">Berges fluviales, bras morts de la Karnali</td>
        <td class="p-3">Octobre à Juin</td>
        <td class="p-3">Assez commun</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-purple-300">Perruche à tête prune</td>
        <td class="p-3">33 - 35 cm</td>
        <td class="p-3">Arbres fruitiers, bosquets ouverts, canopée</td>
        <td class="p-3">Octobre à Mai</td>
        <td class="p-3">Très commun</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>5. Les meilleurs spots d'observation ornithologique à Bardia</h2>
<p>
Observer les oiseaux à Bardia ne nécessite pas d'affronter des foules de jeeps. Grâce à la possibilité unique au Népal de réaliser des <strong>safaris pédestres accompagnés de guides naturalistes</strong>, vous pouvez évoluer en silence absolu au cœur des biotopes les plus préservés :
</p>
<ol class="space-y-4 my-6 list-decimal list-inside text-slate-300">
  <li><strong>La tour d'affût de Baghaura Phanta :</strong> Idéale aux premières lueurs de l'aube pour observer les rolliers indiens, les perruches, les engoulevents et les rapaces postés sur les grands arbres isolés de la plaine.</li>
  <li><strong>Les berges de la rivière Geruwa (bras est de la Karnali) :</strong> Un paradis aquatique où se croisent calaos pies, martins-pêcheurs pies, sternes, vanneaux du Bengale et ibis à tête noire.</li>
  <li><strong>La forêt primaire de la vallée de la Babai :</strong> La zone la plus sauvage et préservée de Bardia, où les figuiers géants centenaires attirent des familles entières de calaos bicornes et de pigeons verts à cou rose.</li>
  <li><strong>Les corridors forestiers bordant les villages Tharu :</strong> Parfait pour une promenade ornithologique de fin d'après-midi, à la rencontre des passereaux, coucous koëls et souimangas éclatants butinant les fleurs d'hibiscus.</li>
</ol>

<h2>6. Conseils photo et réglages boîtier pour la photo d'oiseaux en jungle</h2>
<p>
Photographier les oiseaux en forêt tropicale représente un défi technique passionnant en raison des contrastes de lumière extrêmes entre le sous-bois sombre et le ciel lumineux :
</p>
<ul class="space-y-3 my-6 list-disc list-inside text-slate-300">
  <li><strong>Focale recommandée :</strong> Un téléobjectif de 400 mm à 600 mm (équivalent plein format) est indispensable pour isoler les petits passereaux dans la végétation. Un zoom polyvalent 100-400mm ou 150-600mm offre le meilleur compromis maniabilité/poids pour la marche à pied.</li>
  <li><strong>Vitesse d'obturation :</strong> Pour figer le vol foudroyant d'un rollier ou les ondulations de queue d'un tchitrec, maintenez une vitesse minimale de <strong>1/2000s</strong> voire <strong>1/3200s</strong>. Pour un calao perché dans la canopée, 1/800s suffit.</li>
  <li><strong>Gestion des ISO :</strong> N'ayez pas peur de monter à 3200 ou 6400 ISO sous la frondaison épaisse. Les capteurs modernes et les logiciels de débruitage gèrent parfaitement ce niveau de bruit.</li>
  <li><strong>Mode autofocus :</strong> Utilisez le suivi AF sur l'œil des oiseaux (Bird Eye AF) désormais disponible sur les boîtiers modernes (Sony A7IV/A1, Canon R5/R6, Nikon Z8/Z9), ou un collimateur spot ponctuel pour faire la mise au point à travers les branchages.</li>
</ul>

<div class="blog-cta-card">
  <h3>Envie d'un safari ornithologique sur mesure à Bardia ?</h3>
  <p>Nos guides naturalistes expérimentés repèrent les oiseaux au chant et vous conduisent dans les meilleurs affûts secrets loin de toute foule.</p>
  <a href="/contact" class="btn-cta">Organiser mon safari à Bardia</a>
</div>

<h2>Foire aux questions (FAQ) — oiseaux et birdwatching à Bardia</h2>
<div class="space-y-6 my-8">
  <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
    <h3 class="text-emerald-400 font-bold text-base mb-2">Quelle est la meilleure période de l'année pour observer les oiseaux à Bardia ?</h3>
    <p class="text-slate-300 text-sm leading-relaxed">
      La période allant de <strong>novembre à avril</strong> est idéale. Les oiseaux résidents sont très actifs et le parc accueille des milliers d'oiseaux migrateurs venus de Sibérie et du plateau tibétain (canards, rapaces, oies à tête barrée). D'avril à juin, les migrateurs d'été comme le tchitrec de paradis et les coucous arrivent pour la nidification.
    </p>
  </div>
  <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
    <h3 class="text-emerald-400 font-bold text-base mb-2">Faut-il être un ornithologue expérimenté pour apprécier le safari oiseaux ?</h3>
    <p class="text-slate-300 text-sm leading-relaxed">
      Absolument pas ! Les couleurs flamboyantes du rollier indien, l'envergure impressionnante du calao bicorne et la beauté des martins-pêcheurs émerveillent petits et grands dès les premières minutes. Nos guides naturalistes partagent leurs jumelles professionnelles et vous expliquent chaque comportement de manière vivante et passionnante.
    </p>
  </div>
  <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
    <h3 class="text-emerald-400 font-bold text-base mb-2">Peut-on combiner safari tigres et observation des oiseaux lors d'une même sortie ?</h3>
    <p class="text-slate-300 text-sm leading-relaxed">
      Oui, et c'est précisément la magie de Bardia ! Lors des marches d'affût au tigre ou au rhinocéros le long des rivières et des clairières, les oiseaux sont omniprésents. De plus, les cris d'alarme de certains oiseaux (comme le vanneau du Bengale ou le coucou) sont de précieux indices que nos pisteurs utilisent pour localiser les grands fauves.
    </p>
  </div>
</div>
"""

# English Article Content (> 2000 words)
title_en = "Our Favorite Birds of Bardia: Great Hornbill, Indian Roller & Paradise Flycatcher (2026)"
desc_en = "Complete naturalist guide to our favorite birds in Bardia National Park: Great Hornbill, Indian Roller, Asian Paradise Flycatcher. Habitats, behavior, birdwatching spots."

content_en = """<p class="lead text-lg sm:text-xl text-slate-300 font-normal leading-relaxed mb-8">
When travelers think of <strong>Bardia National Park</strong>, their minds immediately conjure images of majestic terrestrial apex predators: the silent stride of the Bengal tiger, the prehistoric armor of the greater one-horned rhinoceros, or the ancient power of wild Asian elephants. Yet, the moment dawn breaks through the sal forest mist and illuminates the jungle canopy, an entirely different kind of enchantment takes flight. The treetop canopy vibrates with the rhythmic thunder of giant hornbills, open grasslands erupt in electric turquoise flashes as rollers hunt, and dim, shaded understories host the ghost-like ribbons of paradise flycatchers.
</p>

<p>
Boasting over <strong>500 recorded bird species</strong> across its riverine corridors, alluvial floodplains, and dense tropical hardwood forests, Bardia stands among South Asia's premier avian havens. In this in-depth field guide, our resident local naturalist guides share their top favorite species, field tracking secrets, and intimate encounters with the three most iconic winged treasures of the Nepalese Terai.
</p>

<figure class="my-10">
  <img src="/assets/curated_gallery/calao_bicorne_canopee.webp" alt="Great hornbill perched in the sal canopy of Bardia" class="rounded-2xl shadow-xl w-full object-cover border border-white/10" loading="lazy" />
  <figcaption class="text-xs sm:text-sm text-center text-slate-400 mt-3 italic">The magnificent Great Hornbill (Buceros bicornis), prehistoric monarch of Bardia's sal forest canopy.</figcaption>
</figure>

<h2>1. The Great Hornbill (Buceros bicornis): prehistoric monarch of the canopy</h2>
<p>
Hearing a Great Hornbill before sighting it is an unforgettable milestone of any foot safari in Nepal. Its heavy, deliberate flight produces a deep, rhythmic whooshing resonance akin to a low-altitude steam locomotive or a vintage radial propeller engine. This acoustic signature is due to its specialized feather structure: unlike most birds whose plumage muffles air friction, the flight feathers of the Great Hornbill lack basal coverts, forcing air through the open primary quills and generating a low-frequency hum audible over half a kilometer away.
</p>
<p>
Measuring up to <strong>1.3 meters (4.3 feet) in length</strong> with a commanding wingspan surpassing <strong>1.6 meters (5.2 feet)</strong>, the Great Hornbill (<em>Buceros bicornis</em>) is the undisputed heavyweight ruler of the Terai treetops. Its most striking feature is the enormous golden-yellow casque resting atop its massive curved bill. Contrary to popular belief, this casque is not solid bone; it is an ultra-light honeycombed keratin structure that acts as a resonating chamber for deep, resonant territorial barks, an optical cue for courtship displays, and a functional tool for chiseling soft wood.
</p>
<p>
In Bardia's ecosystem, hornbills serve as the vital "chief foresters" of the tropical canopy. As obligate frugivores with a voracious appetite for wild figs (<em>Ficus benghalensis</em>, <em>Ficus religiosa</em>), they ingest fruits whole and disperse viable seeds across vast distances during their cross-canopy journeys. Without their daily dispersal services, the natural regeneration of major hardwood and fruit-bearing trees would suffer catastrophic declines.
</p>
<p>
Their reproductive biology is one of the most astonishing marvels in the animal kingdom. In spring, the breeding female voluntarily seals herself inside a natural tree cavity 15 to 30 meters above the forest floor. Aided by the male, who delivers pellets of mud, fruit pulp, and droppings, she bricks up the nest entrance until only a slender vertical slit remains. Throughout the entire 3 to 4-month incubation and brooding cycle, the male single-handedly delivers food, making up to 15 daily roundtrips to regurgitate hundreds of wild figs and protein-rich insects directly to his cloistered family.
</p>

<h2>2. The Indian Roller (Coracias benghalensis): the electric turquoise flash of the savannas</h2>
<p>
The moment you emerge from the shadowy sal woodland into the expansive alluvial grasslands (<em>phantas</em>) bordering the Karnali River, a sudden burst of brilliant azure and turquoise commands your gaze. The <strong>Indian Roller</strong> (<em>Coracias benghalensis</em>) is the undisputed master of optical contrast in the Nepalese lowlands.
</p>
<p>
At rest upon a dead branch, fence post, or thorny acacia bush, the roller appears deceptively modest: its back displays muted cinnamon-brown, dull olive, and sandy-buff tones that blend seamlessly against parched tree bark. However, the instant it launches into the air to ambush a terrestrial insect, a breathtaking metamorphosis unfolds: its wings reveal brilliant bands of <strong>ultramarine, radiant turquoise, and glowing cyan</strong> that shimmer brilliantly beneath the subtropical sun.
</p>

<figure class="my-10">
  <img src="/assets/curated_gallery/rollier_indien_envol_turquoise.webp" alt="Indian roller showing brilliant turquoise wings in flight at Bardia" class="rounded-2xl shadow-xl w-full object-cover border border-white/10" loading="lazy" />
  <figcaption class="text-xs sm:text-sm text-center text-slate-400 mt-3 italic">The dazzling plumage display of the Indian Roller (Coracias benghalensis) in mid-flight over Bardia's open savannas.</figcaption>
</figure>

<p>
The name "roller" derives from its acrobatic courtship displays during breeding season between March and May. Courting males execute dramatic aerial performances: steep vertical rocket ascents followed by dizzying tumbling dives, lateral barrel-rolls, and twisting somersaults, all accompanied by harsh, grating territorial calls that carry across open meadows.
</p>
<p>
As a sit-and-wait predatory specialist, the Indian Roller feeds upon an eclectic menu of terrestrial invertebrates: heavy ground beetles, locusts, mantids, scorpions, and small agamid lizards. Dropping from its elevated perch with pinpoint accuracy, it snaps up prey in its stout hooked beak and returns to batter the victim against the wood before swallowing it whole. In Nepalese and Hindu folklore, the Indian Roller (revered as <em>Nilkanth</em> and associated with Lord Shiva) is cherished as a sacred herald of good fortune and safe travels.
</p>

<h2>3. The Asian Paradise Flycatcher (Terpsiphone paradisi): the spectral dancer of the understory</h2>
<p>
Among all the songbirds and insectivores inhabiting Bardia's lush riparian jungles, the <strong>Asian Paradise Flycatcher</strong> (<em>Terpsiphone paradisi</em>) inspires the most profound wonder. This bird possesses an ethereal elegance reminiscent of classical Asian silk paintings.
</p>
<p>
Breeding adult males exhibit extraordinary morphological dimorphism. They develop two extended central tail streamers (rectrices) that can stretch up to <strong>30 to 40 centimeters (12 to 16 inches) in length</strong>—more than three times their entire body length! As the male flits through dim, dappled understories and hanging lianas in pursuit of flying insects, these ribbon-like plumes twist, flutter, and flow behind him like the silk ribbons of a rhythmic gymnast.
</p>

<figure class="my-10">
  <img src="/assets/curated_gallery/tchitrec_paradis_longues_rectrices.webp" alt="Asian paradise flycatcher male with long white tail streamers in Bardia jungle" class="rounded-2xl shadow-xl w-full object-cover border border-white/10" loading="lazy" />
  <figcaption class="text-xs sm:text-sm text-center text-slate-400 mt-3 italic">The ethereal Asian Paradise Flycatcher (Terpsiphone paradisi), renowned for its magnificent flowing tail streamers.</figcaption>
</figure>

<p>
Furthermore, males display remarkable <strong>color polymorphism</strong>: younger adult males sport a vibrant rufous-chestnut plumage with a glossy blue-black crest, while mature males transition into a striking pure white morph, featuring snowy white bodies, glossy crests, and vivid cobalt-blue orbital eye rings and beaks. Females consistently retain the rufous morph with standard-length tail feathers.
</p>
<p>
Paradise flycatchers thrive in humid riverine galleries alongside the Babai River and shady jungle tributaries. As summer breeding migrants arriving in Bardia between April and August, they build tiny, exquisite cone-shaped cup nests in low tree forks, carefully bound with sticky spiderwebs and camouflaged with fresh green moss.
</p>

<h2>4. Other must-see feathered treasures in Bardia National Park</h2>
<p>
Beyond the iconic trio of hornbills, rollers, and flycatchers, Bardia hosts an extraordinary variety of avian wonders:
</p>
<ul class="space-y-3 my-6 list-disc list-inside text-slate-300">
  <li><strong>Oriental Pied Hornbill (Anthracoceros albirostris):</strong> Smaller, highly vocal, and frequently spotted in lively flocks of 4 to 8 individuals foraging along buffer zone orchards and Tharu village outskirts.</li>
  <li><strong>Stork-billed Kingfisher (Pelargopsis capensis):</strong> A giant among kingfishers boasting a massive crimson dagger-bill capable of spearing fish, freshwater crabs, and frogs along quiet river oxbows.</li>
  <li><strong>White-throated Kingfisher (Halcyon smyrnensis):</strong> Electric turquoise-blue wings with chocolate-brown plumage, widely seen perching near wetlands, paddy fields, and irrigation canals.</li>
  <li><strong>Plum-headed Parakeet (Psittacula cyanocephala):</strong> A vividly colored parrot whose males sport an extraordinary purplish-pink head resembling an exotic jungle flower.</li>
  <li><strong>Little Green Bee-eater (Merops orientalis):</strong> Elegant aerial acrobats darting from exposed twigs to catch dragonflies and bees in mid-air over sandy riverbanks.</li>
  <li><strong>Red-headed Trogon (Harpactes erythrocephalus):</strong> A shy, reclusive gem of dense primary canopies, displaying deep crimson-red underparts and golden-olive backs.</li>
</ul>

<h2>Comparative field guide: morphology, habitat & prime viewing seasons</h2>
<div class="my-8 overflow-x-auto">
  <table class="w-full text-left text-sm text-slate-300 border border-white/10 rounded-xl overflow-hidden">
    <thead class="bg-white/10 text-white uppercase text-xs">
      <tr>
        <th class="p-3">Species</th>
        <th class="p-3">Length / Wingspan</th>
        <th class="p-3">Primary Habitat</th>
        <th class="p-3">Best Viewing Season</th>
        <th class="p-3">Rarity Status</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/10 bg-slate-900/60">
      <tr>
        <td class="p-3 font-semibold text-emerald-300">Great Hornbill</td>
        <td class="p-3">120 - 130 cm / 160 cm</td>
        <td class="p-3">Sal forest canopy, emergent wild fig trees</td>
        <td class="p-3">November to May</td>
        <td class="p-3">Vulnerable (healthy in Bardia)</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-cyan-300">Indian Roller</td>
        <td class="p-3">30 - 34 cm / 65 cm</td>
        <td class="p-3">Open alluvial grasslands (phantas), scrub borders</td>
        <td class="p-3">Year-round (courtship displays March-May)</td>
        <td class="p-3">Very common</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-amber-300">Asian Paradise Flycatcher</td>
        <td class="p-3">20 cm (+ 35 cm streamers)</td>
        <td class="p-3">Shaded riverine galleries, dense understory</td>
        <td class="p-3">April to September (summer breeding)</td>
        <td class="p-3">Fairly common but secretive</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-rose-300">Stork-billed Kingfisher</td>
        <td class="p-3">35 - 38 cm / 60 cm</td>
        <td class="p-3">Riverbanks, quiet oxbow lakes, Karnali backwaters</td>
        <td class="p-3">October to June</td>
        <td class="p-3">Common resident</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-purple-300">Plum-headed Parakeet</td>
        <td class="p-3">33 - 35 cm / 45 cm</td>
        <td class="p-3">Fruiting trees, open woodlands, canopy edges</td>
        <td class="p-3">October to May</td>
        <td class="p-3">Abundant resident</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>5. Premier birdwatching locations inside Bardia National Park</h2>
<p>
Birding in Bardia is unlike anywhere else in South Asia. Thanks to the park's exclusive focus on <strong>guided walking safaris</strong>, birdwatchers can explore prime bird habitats on foot without noisy engine rumble:
</p>
<ol class="space-y-4 my-6 list-decimal list-inside text-slate-300">
  <li><strong>Baghaura Phanta Watchtower:</strong> Essential at dawn to observe rollers, parakeets, nightjars, and raptors perching on dead snags across the open grassland.</li>
  <li><strong>Geruwa Riverbanks (Eastern Karnali Branch):</strong> A dynamic aquatic highway hosting pied kingfishers, lapwings, black-headed ibises, and great thick-knees along gravel bars.</li>
  <li><strong>Babai Valley Primary Hardwood Forests:</strong> The most untouched sector of the park, where massive old-growth fig trees attract large congregations of Great Hornbills and green pigeons.</li>
  <li><strong>Tharu Village Buffer Corridors:</strong> Ideal for gentle afternoon walks to spot sunbirds, drongos, Asian koels, and munias among flowering hedges and orchards.</li>
</ol>

<h2>6. Expert bird photography tips & camera settings in tropical forests</h2>
<p>
Capturing sharp bird photographs in dense subtropical jungles requires technical precision to balance deep tree shadows against bright canopy skylight:
</p>
<ul class="space-y-3 my-6 list-disc list-inside text-slate-300">
  <li><strong>Focal length recommendation:</strong> A 400mm to 600mm telephoto lens (full-frame equivalent) is vital for small passerines. High-quality 100-400mm or 150-600mm zooms offer the optimal balance between reach, portability, and walking endurance.</li>
  <li><strong>Shutter speed thresholds:</strong> To freeze the explosive flight of a roller or the fluttering streamers of a flycatcher, shoot at <strong>1/2000s to 1/3200s</strong>. For a perched hornbill in the canopy, 1/800s provides excellent stability.</li>
  <li><strong>ISO handling:</strong> Do not hesitate to shoot at ISO 3200 or 6400 under heavy canopy cover. Modern camera sensors and AI noise-reduction software handle high-ISO grains effortlessly.</li>
  <li><strong>Autofocus modes:</strong> Enable Bird-Eye AF tracking on modern mirrorless systems (Sony, Canon, Nikon) or use pinpoint single-point AF to focus through dense jungle foliage without hunting.</li>
</ul>

<div class="blog-cta-card">
  <h3>Ready for a tailored birdwatching safari in Bardia?</h3>
  <p>Our expert naturalist guides track bird calls and take you to private viewing blinds away from tourist crowds.</p>
  <a href="/en/contact" class="btn-cta">Plan my Bardia bird safari</a>
</div>

<h2>Frequently Asked Questions (FAQ) — Bardia birdwatching</h2>
<div class="space-y-6 my-8">
  <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
    <h3 class="text-emerald-400 font-bold text-base mb-2">When is the best time of year for birdwatching in Bardia?</h3>
    <p class="text-slate-300 text-sm leading-relaxed">
      The prime season runs from <strong>November through April</strong>. Resident species are active, and the park welcomes thousands of Palearctic migratory waterfowl and raptors from Siberia and the Tibetan Plateau. From April to June, summer breeding migrants like the Asian Paradise Flycatcher and cuckoos arrive.
    </p>
  </div>
  <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
    <h3 class="text-emerald-400 font-bold text-base mb-2">Do I need to be an expert birder to enjoy a bird safari?</h3>
    <p class="text-slate-300 text-sm leading-relaxed">
      Not at all! The striking colors of the Indian roller, the giant presence of the Great Hornbill, and the beauty of kingfishers captivate every nature lover. Our guides share premium binoculars and bring bird behavior to life through engaging field storytelling.
    </p>
  </div>
  <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
    <h3 class="text-emerald-400 font-bold text-base mb-2">Can tiger tracking and birdwatching be combined during the same safari?</h3>
    <p class="text-slate-300 text-sm leading-relaxed">
      Yes! That is the defining magic of Bardia. While walking along river channels and waiting at wildlife hides for tigers or rhinos, bird activity is continuous. Furthermore, bird alarm calls (such as from lapwings and drongos) are essential clues our trackers use to pinpoint big cat movements.
    </p>
  </div>
</div>
"""

# New Post Objects
new_post_fr = {
    "title": title_fr,
    "slug": slug,
    "date": "2026-05-18",
    "readingTime": "12 min",
    "category": "Faune & Safari",
    "featuredImage": "/assets/curated_gallery/calao_bicorne_canopee.webp",
    "description": desc_fr,
    "content": content_fr
}

new_post_en = {
    "title": title_en,
    "slug": slug,
    "date": "2026-05-18",
    "readingTime": "12 min",
    "category": "Wildlife & Safari",
    "featuredImage": "/assets/curated_gallery/calao_bicorne_canopee.webp",
    "description": desc_en,
    "content": content_en
}

# Insert strategically at position 18 (right among top wildlife guides)
insert_pos = 18
posts_fr.insert(insert_pos, new_post_fr)
posts_en.insert(insert_pos, new_post_en)

# Save updated files
with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print(f"Added '{slug}' at position {insert_pos} in both FR and EN datasets!")
print(f"Total FR posts: {len(posts_fr)} | Total EN posts: {len(posts_en)}")
