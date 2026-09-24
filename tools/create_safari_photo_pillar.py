#!/usr/bin/env python3
import json
import os

french_content = """<p class="lead text-xl text-slate-200 font-medium leading-relaxed mb-8">
05h45 sur les berges embrumées de la rivière Geruwa, dans l'extrême ouest du Teraï népalais. Pawan, notre maître pisteur Tharu, lève la main dans un geste d'une immobilité parfaite. Silence absolu. À cinquante mètres, sous la canopée dense des arbres de Sal (<em>Shorea robusta</em>), un cri d'alarme de cerf Axis claque dans l'air frais comme un coup de fouet. Quelques secondes plus tard, un second cri, plus rauque, retentit depuis la cime d'un arbre : la vigie des singes langurs vient de repérer le prédateur. Ce n'est pas un léopard. La tension qui pétrifie la forêt est trop lourde. C'est lui : le grand tigre du Bengale.
</p>

<p>
À genoux dans le sable humide et les galets, téléobjectif calé sur l'épaule et monopode ancré au sol, votre cœur s'accélère. Pas de carrosserie métallique, pas de moteur de 4x4 qui vibre, pas de brouhaha de touristes. Vous êtes à pied, au niveau exact des yeux du félin. Lorsque sa silhouette puissante fend les hautes herbes à éléphants pour s'avancer vers la rivière, l'émotion visuelle et photographique est d'une intensité incomparable.
</p>

<div class="my-10 p-6 sm:p-8 rounded-2xl bg-gradient-to-br from-emerald-950/80 to-slate-900/90 border border-emerald-500/30 shadow-2xl backdrop-blur-md">
  <div class="flex items-start gap-4">
    <div class="p-3 bg-emerald-500/20 text-emerald-400 rounded-xl text-2xl">📷</div>
    <div>
      <h3 class="text-xl font-bold text-emerald-300 mb-2 mt-0">Pourquoi ce guide est la référence du safari photo tigre au Népal</h3>
      <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
        Ce dossier rassemble plus de 10 années d'expérience de terrain dans le <strong>Parc National de Bardia</strong>. Rédigé par des photographes et pour des photographes, il détaille l'art du pistage à pied avec nos guides locaux, les réglages boîtiers pour la jungle tropicale, la gestion des lumières et la réalité brute des affûts sans filtre.
      </p>
      <div class="flex flex-wrap gap-3">
        <a href="/tours/jungle-extreme" class="inline-flex items-center gap-2 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-xs sm:text-sm font-semibold rounded-lg transition-colors">
          <span>Découvrir l'Expédition Jungle Extrême (7 jours)</span> →
        </a>
        <a href="/destinations/bardia" class="inline-flex items-center gap-2 px-4 py-2 bg-white/10 hover:bg-white/20 text-slate-200 text-xs sm:text-sm font-medium rounded-lg transition-colors border border-white/10">
          <span>Tout sur le Parc de Bardia</span>
        </a>
      </div>
    </div>
  </div>
</div>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_tigre_bengale1.webp" alt="Tigre du Bengale émergeant des herbes à éléphant au parc national de Bardia Népal" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="eager" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Rencontre au ras du sol avec un grand mâle tigre du Bengale sur les berges de la rivière Geruwa (Photo : Expédition Jungle Nepal Adventure).</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">1. Pourquoi le Népal et Bardia détrônent l'Inde pour la photographie animalière</h2>

<p>
Pendant des décennies, l'Inde (Ranthambore, Bandhavgarh, Tadoba) a été la destination par défaut pour voir le tigre. Mais pour le photographe naturaliste exigeant, les safaris indiens sont devenus un véritable défi éthique et artistique : pistes obligatoires, interdiction stricte de descendre des 4x4, angles de prise de vue plongeants et peu naturels, et surtout des grappes de 15 à 20 jeeps encerclant un même animal au son des moteurs.
</p>

<p>
Le <strong>Népal</strong>, et plus particulièrement le <a href="/blog/guide-complet-parc-national-de-bardia-nepal" class="text-emerald-400 underline hover:text-emerald-300">Parc National de Bardia (968 km²)</a>, propose une philosophie diamétralement opposée : <strong>le safari à pied exclusif dans le silence le plus pur</strong>.
</p>

<div class="overflow-x-auto my-8">
  <table class="w-full text-left text-sm text-slate-300 border-collapse border border-slate-800 rounded-xl overflow-hidden">
    <thead class="bg-slate-900 text-emerald-400 font-semibold border-b border-slate-800">
      <tr>
        <th class="p-4">Critère Photographique</th>
        <th class="p-4 bg-emerald-950/40 text-white font-bold border-x border-emerald-800/40">Bardia (Népal) - Notre approche</th>
        <th class="p-4">Parcs d'Inde (Ranthambore, etc.)</th>
        <th class="p-4">Chitwan (Népal)</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800/60 bg-slate-950/40">
      <tr class="hover:bg-slate-900/40">
        <td class="p-4 font-medium text-white">Angle de prise de vue</td>
        <td class="p-4 bg-emerald-950/20 text-emerald-300 font-semibold border-x border-emerald-800/30"><strong>Niveau des yeux / Ras du sol</strong> (fond flou naturel, bokeh cinématique)</td>
        <td class="p-4 text-slate-400">Plongeant depuis la jeep (1,80m à 2,20m de hauteur)</td>
        <td class="p-4 text-slate-400">Plongeant (jeep) ou masqué par les herbes</td>
      </tr>
      <tr class="hover:bg-slate-900/40">
        <td class="p-4 font-medium text-white">Mode de déplacement</td>
        <td class="p-4 bg-emerald-950/20 text-emerald-300 font-semibold border-x border-emerald-800/30"><strong>100% à pied & affûts statiques discrets</strong></td>
        <td class="p-4 text-slate-400">Jeep 4x4 obligatoirement sur pistes balisées</td>
        <td class="p-4 text-slate-400">Jeep touristique ou bateau partagé</td>
      </tr>
      <tr class="hover:bg-slate-900/40">
        <td class="p-4 font-medium text-white">Fréquentation & Pression</td>
        <td class="p-4 bg-emerald-950/20 text-emerald-300 font-semibold border-x border-emerald-800/30"><strong>Quasi nulle</strong> (souvent seul groupe à 5 km à la ronde)</td>
        <td class="p-4 text-slate-400">Très dense (10 à 30 jeeps sur une même observation)</td>
        <td class="p-4 text-slate-400">Moyenne à forte selon les zones</td>
      </tr>
      <tr class="hover:bg-slate-900/40">
        <td class="p-4 font-medium text-white">Comportement animal</td>
        <td class="p-4 bg-emerald-950/20 text-emerald-300 font-semibold border-x border-emerald-800/30"><strong>100% sauvage et détendu</strong> (baignades naturelles, chasse)</td>
        <td class="p-4 text-slate-400">Parfois stressé ou indifférent aux véhicules</td>
        <td class="p-4 text-slate-400">Furtif en forêt dense</td>
      </tr>
      <tr class="hover:bg-slate-900/40">
        <td class="p-4 font-medium text-white">Possibilité de vidéo sonore</td>
        <td class="p-4 bg-emerald-950/20 text-emerald-300 font-semibold border-x border-emerald-800/30"><strong>Son pur de la jungle</strong> (aucun bruit de moteur)</td>
        <td class="p-4 text-slate-400">Parasitée par les moteurs diesel et bavardages</td>
        <td class="p-4 text-slate-400">Variable</td>
      </tr>
    </tbody>
  </table>
</div>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_safari_a_pied.webp" alt="Photographes animaliers en marche silencieuse dans la jungle de Bardia Népal" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Progression silencieuse en file indienne sous la conduite de nos pisteurs Tharus au cœur de la forêt de Sal.</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">2. L'Art du Pistage à Pied : Dans les pas de Pawan & Kiran</h2>

<p>
À Bardia, la réussite d'un safari photo ne repose pas sur la vitesse d'un moteur, mais sur la science ancestrale de nos pisteurs natifs du Teraï, <strong>Pawan et Kiran</strong>. Nés aux lisières de la jungle, ils lisent les traces comme un livre ouvert.
</p>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">La lecture des empreintes (Pugmarks)</h3>
<p>
Sur les bancs de sable de la Geruwa ou la poussière fine des sentiers de buffles, chaque trace raconte une histoire précise :
</p>
<ul class="list-disc pl-6 space-y-2 text-slate-300">
  <li><strong>Distinguer le sexe</strong> : Le talon du mâle est plus large et arrondi, ses pelotes digitales s'inscrivent dans un cercle quasi parfait. L'empreinte de la tigresse est plus ovale et allongée.</li>
  <li><strong>Évaluer l'heure de passage</strong> : Des grains de sable encore humides au fond de la griffe indiquent un passage datant de moins de 20 minutes. Une brise qui a commencé à éroder les contours situe l'animal à l'aube.</li>
  <li><strong>Comprendre la démarche</strong> : Un pas régulier et espacé montre un tigre en patrouille territoriale. Des pas serrés et hésitants signalent un affût ou un début d'approche sur un groupe de cerfs.</li>
</ul>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">La partition acoustique : les sentinelles de la jungle</h3>
<p>
Dans une végétation dense, l'oreille du photographe compte autant que son œil. Les pisteurs triangulent la position du fauve en décodant les signaux d'alerte émis par les autres espèces :
</p>
<ul class="list-disc pl-6 space-y-2 text-slate-300">
  <li><strong>Le cri de l'Axis (Chital)</strong> : Un aboiement bref, suraigu et répété frénétiquement dès que le tigre passe à découvert.</li>
  <li><strong>L'alarme du Langur</strong> : Depuis la cime des arbres, le grand singe pousse un "Khaa-khaa" guttural lorsqu'il voit le félin ramper sous la végétation. C'est l'indicateur le plus précis de la direction prise par le tigre.</li>
  <li><strong>Le cri du Paon au sol</strong> : Un cri perçant et puissant ("May-awe") émis lorsque le tigre pénètre dans une clairière.</li>
</ul>

<figure class="wp-block-image my-8">
  <img src="/assets/curated_gallery/tigre_bengale_pistage.webp" alt="Pistage du tigre du Bengale dans la savane herbeuse de Bardia" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Traces fraîches de tigre du Bengale relevées à l'aube le long des chenaux de la Karnali.</figcaption>
</figure>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">Les spots d'affût stratégiques</h3>
<p>
Plutôt que de marcher au hasard pendant les heures chaudes, nous installons nos affûts silencieux sur des points névralgiques étudiés depuis des années :
</p>
<ul class="list-disc pl-6 space-y-2 text-slate-300">
  <li><strong>Kingfisher Point</strong> : Jonction de deux bras de rivière où les tigres viennent régulièrement traverser à la nage ou s'immerger l'après-midi.</li>
  <li><strong>Tinkuni (Les Trois Rivières)</strong> : Vaste zone de bancs de galets et d'îlots boisés offrant des lignes de vue dégagées jusqu'à 200 mètres.</li>
  <li><strong>Les Machans (Tours d'affût en bois)</strong> : Positionnées à la lisière des clairières et des points d'eau forestiers, idéales pour surveiller l'arrivée du félin sans être repéré par les odeurs portées par le vent.</li>
</ul>

<div class="my-10 p-6 rounded-2xl bg-slate-900 border border-emerald-500/20 text-center">
  <p class="text-lg font-bold text-white mb-2">Envie de vivre cette traque photographique ?</p>
  <p class="text-slate-300 text-sm mb-4">Consultez notre itinéraire 100% dédié au pistage et à l'affût avec nos maîtres guides.</p>
  <a href="/tours/jungle-extreme" class="inline-block px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl transition-colors shadow-lg">
    Voir le programme Jungle Extrême (Bardia) →
  </a>
</div>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_photographes_jungle.webp" alt="Photographes animaliers en affût camouflé le long de la rivière à Bardia" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Affût statique camouflé au bord de l'eau : la patience récompensée par des lumières rasantes magiques.</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">3. Guide Technique du Matériel : Focales, Boîtiers & Réglages</h2>

<p>
Photographier le tigre à pied en milieu tropical impose des contraintes physiques et optiques bien différentes d'un safari en véhicule. Voici notre retour d'expérience sans concession sur le matériel à emporter dans votre sac :
</p>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">Quelles optiques choisir pour Bardia ?</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
  <div class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h4 class="text-lg font-bold text-amber-400 mb-2 mt-0">🥇 Le Zoom Téléobjectif Polyvalent (100-400mm ou 150-600mm)</h4>
    <p class="text-slate-300 text-sm leading-relaxed">
      <strong>L'optique reine à pied.</strong> Pourquoi ? Parce qu'en marchant, la distance avec le tigre peut varier de 25 mètres à 120 mètres en quelques secondes. Un 100-400mm f/4.5-5.6 (ou équivalent 70-200mm f/2.8 + doubleur) permet de cadrer à la fois le tigre dans son biotope majestueux et de serrer sur son regard. Son poids contenu (1,3 à 1,8 kg) reste supportable sur 15 km de marche.
    </p>
  </div>
  <div class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h4 class="text-lg font-bold text-amber-400 mb-2 mt-0">🥈 La Longue Focale Fixe Lumineuse (500mm ou 600mm f/4)</h4>
    <p class="text-slate-300 text-sm leading-relaxed">
      <strong>L'arme ultime pour l'affût statique.</strong> Sur les bancs de galets de Tinkuni ou depuis un machan, l'ouverture f/4 fait des merveilles au crépuscule et détache le sujet avec un bokeh somptueux. En revanche, son encombrement nécessite impérativement un monopode robuste en carbone et devient très contraignant lors des marches dynamiques en forêt dense.
    </p>
  </div>
</div>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">Réglages boîtiers recommandés en sous-bois</h3>
<ul class="list-disc pl-6 space-y-3 text-slate-300">
  <li><strong>Vitesse d'obturation</strong> : Ne descendez jamais sous <strong>1/1000s</strong> lorsque le tigre est en marche (le balancement de sa tête génère facilement du flou de mouvement). À l'arrêt dans l'eau, descendez à <strong>1/400s - 1/500s</strong> pour abaisser la sensibilité.</li>
  <li><strong>Sensibilité ISO</strong> : Les forêts de Sal créent une pénombre marquée aux premières heures du jour. Travaillez en <strong>ISO automatique avec vitesse minimale calée</strong>. Les capteurs modernes gèrent sans problème 3200 à 6400 ISO, indispensables pour figer l'instant.</li>
  <li><strong>Mode Autofocus</strong> : <em>Zone réduite ou collimateur ponctuel</em> avec détection de l'œil animal activée. Attention : les hautes herbes (<em>Elephant Grass</em>) peuvent tromper l'autofocus large ; sachez reprendre la bague manuelle en cas d'obstacle au premier plan.</li>
  <li><strong>Déclenchement Silencieux</strong> : Activez l'<strong>obturateur électronique ou silencieux</strong>. Le bruit mécanique d'une rafale à 14 images/seconde peut faire tourner bride à un tigre méfiant à 35 mètres.</li>
</ul>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_tigre_bengale2.webp" alt="Tigre du Bengale se rafraîchissant dans l'eau d'une rivière à Bardia" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Tigre immergé dans la rivière Geruwa lors des fortes chaleurs d'avril (Photo : Julien - Voyageur Jungle Nepal).</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">4. Meilleures Périodes & Calendrier de Lumière</h2>

<p>
Le Teraï népalais vit au rythme de saisons tropicales très contrastées. Chaque période offre une ambiance lumineuse et des opportunités photographiques distinctes :
</p>

<div class="space-y-6 my-8">
  <div class="p-6 rounded-2xl bg-slate-900/80 border-l-4 border-amber-500">
    <h3 class="text-xl font-bold text-amber-300 mb-2 mt-0">🔥 Mars à Mai : La Saison Reine du Tigre (Taux d'observation : 75-85%)</h3>
    <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-2">
      C'est la fin de la saison sèche. Les herbes géantes ont été coupées par les villageois ou brûlées par le soleil, dégageant une visibilité exceptionnelle jusqu'à 300 mètres en forêt. Avec des températures atteignant 35°C à 40°C en milieu de journée, les petits ruisseaux intérieurs s'assèchent : <strong>les tigres sont contraints de venir s'immerger pendant de longues heures dans les rivières principales</strong>.
    </p>
    <span class="inline-block text-xs font-semibold px-2.5 py-1 bg-amber-500/20 text-amber-300 rounded">Meilleur spot : Affûts de berge & baignades</span>
  </div>

  <div class="p-6 rounded-2xl bg-slate-900/80 border-l-4 border-emerald-500">
    <h3 class="text-xl font-bold text-emerald-300 mb-2 mt-0">🌿 Octobre à Novembre : Lumières Dorées & Festival de Dashain (Taux : 55-65%)</h3>
    <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-2">
      Juste après la mousson, la jungle est d'une luxuriance spectaculaire. L'air est d'une clarté cristalline avec les sommets himalayens parfois visibles à l'horizon nord. Les lumières matinales et vespérales sont douces, parfaites pour la photographie d'ambiance et la macro. C'est également la période idéale pour coupler safari faune et immersion culturelle lors du grand festival hindou de Dashain.
    </p>
    <span class="inline-block text-xs font-semibold px-2.5 py-1 bg-emerald-500/20 text-emerald-300 rounded">
      Circuit recommandé : <a href="/tours/dashain-immersion-culturelle" class="underline text-emerald-200">Dashain Immersion Culturelle & Safari</a>
    </span>
  </div>

  <div class="p-6 rounded-2xl bg-slate-900/80 border-l-4 border-cyan-500">
    <h3 class="text-xl font-bold text-cyan-300 mb-2 mt-0">❄️ Décembre à Février : Brumes Mystiques & Oiseaux Migrateurs (Taux : 50-60%)</h3>
    <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-2">
      Les matinées sont fraîches (8°C à 12°C) et enveloppées d'épaisses nappes de brume qui traversent les fûts des arbres de Sal. Les rayons du soleil percent la canopée en faisceaux lumineux spectaculaires (effet Tyndall). Les plans d'eau accueillent des milliers d'oiseaux migrateurs venus de Sibérie.
    </p>
    <span class="inline-block text-xs font-semibold px-2.5 py-1 bg-cyan-500/20 text-cyan-300 rounded">Ambiance cinématographique & ornithologie</span>
  </div>
</div>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/adrien_bardia_river.webp" alt="Lumière dorée du coucher de soleil sur la rivière Karnali à Bardia" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Coucher de soleil sur la Karnali : l'heure magique où les prédateurs s'activent pour la chasse nocturne.</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">5. Sécurité & Éthique : Comment nous marchons au milieu des prédateurs</h2>

<p>
L'idée de marcher à pied sur le territoire du plus grand félin de la planète suscite naturellement des questions légitimes sur la sécurité. En plus de 15 ans d'activité, nous n'avons jamais déploré le moindre incident. Pourquoi ? Parce que nous appliquons des protocoles stricts basés sur la psychologie animale :
</p>

<div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-6">
  <div class="p-5 rounded-xl bg-slate-900 border border-slate-800">
    <div class="text-emerald-400 text-2xl font-bold mb-2">01. Deux guides experts</div>
    <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
      Chaque groupe est encadré par <strong>deux guides naturalistes certifiés</strong> : un pisteur ouvre la marche en observant les traces et le vent, tandis qu'un second ferme la marche pour sécuriser nos arrières.
    </p>
  </div>
  <div class="p-5 rounded-xl bg-slate-900 border border-slate-800">
    <div class="text-emerald-400 text-2xl font-bold mb-2">02. Respect des distances</div>
    <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
      Nous maintenons toujours une <strong>distance de sécurité de 30 à 50 mètres</strong>. Le tigre est prévenu de notre présence et ne se sent jamais acculé ni surpris dans son espace vital.
    </p>
  </div>
  <div class="p-5 rounded-xl bg-slate-900 border border-slate-800">
    <div class="text-emerald-400 text-2xl font-bold mb-2">03. Règle du silence</div>
    <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
      Déplacements en file indienne sans parler, vêtements aux tons neutres (kaki, beige, marron foncé) et zéro parfum corporel. Nous nous fondons dans le biotope.
    </p>
  </div>
</div>

<p>
Pour en savoir plus sur les attitudes du prédateur, consultez notre dossier approfondi sur le <a href="/blog/comportement-du-tigre-du-bengale" class="text-emerald-400 underline hover:text-emerald-300">comportement et la vie secrète du tigre du Bengale</a>.
</p>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">6. Nos Expéditions Photo Clés en Main</h2>

<p>
Que vous soyez photographe amateur passionné ou professionnel aguerri, nous proposons des formules spécialement calibrées pour maximiser votre temps de prise de vue sur le terrain :
</p>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  <div class="p-6 rounded-2xl bg-gradient-to-br from-slate-900 to-emerald-950/60 border border-emerald-500/30 flex flex-col justify-between">
    <div>
      <span class="inline-block px-3 py-1 bg-emerald-500/20 text-emerald-300 text-xs font-bold rounded-full mb-3">Le circuit 100% Affût & Pistage</span>
      <h3 class="text-xl font-bold text-white mb-2 mt-0">Jungle Extrême (7 Jours à Bardia)</h3>
      <p class="text-slate-300 text-sm mb-4 leading-relaxed">
        Immersion totale au cœur du parc. 5 journées complètes de safari à pied et d'affûts du lever au coucher du soleil avec nos meilleurs maîtres pisteurs. Micro-groupe de 4 à 8 personnes maximum.
      </p>
      <ul class="text-xs text-slate-300 space-y-1 mb-6">
        <li>✓ Logement en écolodge privatisé</li>
        <li>✓ Pension complète & transferts inclus</li>
        <li>✓ Permis d'entrée journaliers et taxes de parc</li>
      </ul>
    </div>
    <a href="/tours/jungle-extreme" class="w-full text-center py-3 bg-emerald-600 hover:bg-emerald-500 text-white text-sm font-bold rounded-xl transition-colors">
      Découvrir le Tour Jungle Extrême →
    </a>
  </div>

  <div class="p-6 rounded-2xl bg-gradient-to-br from-slate-900 to-amber-950/40 border border-amber-500/30 flex flex-col justify-between">
    <div>
      <span class="inline-block px-3 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-full mb-3">Culture Tharu & Faune Sauvage</span>
      <h3 class="text-xl font-bold text-white mb-2 mt-0">Dashain Immersion & Safari (10 Jours)</h3>
      <p class="text-slate-300 text-sm mb-4 leading-relaxed">
        Une aventure unique combinant le grand festival de Dashain dans les villages traditionnels Tharu et 4 jours de traque photographique intensive du tigre et du rhinocéros à Bardia.
      </p>
      <ul class="text-xs text-slate-300 space-y-1 mb-6">
        <li>✓ Célébrations familiales exclusives</li>
        <li>✓ Safaris à pied et en jeep privée</li>
        <li>✓ Encadrement bilingue francophone</li>
      </ul>
    </div>
    <a href="/tours/dashain-immersion-culturelle" class="w-full text-center py-3 bg-amber-600 hover:bg-amber-500 text-white text-sm font-bold rounded-xl transition-colors">
      Découvrir l'Immersion Dashain →
    </a>
  </div>
</div>

<div class="my-10 p-8 rounded-3xl bg-emerald-950 border border-emerald-500/40 text-center relative overflow-hidden shadow-2xl">
  <div class="relative z-10 max-w-2xl mx-auto">
    <h3 class="text-2xl sm:text-3xl font-extrabold text-white mb-3 mt-0">Vous préparez un projet photo ou un départ privatisé ?</h3>
    <p class="text-emerald-200 text-sm sm:text-base leading-relaxed mb-6">
      Robin et l'équipe de Jungle Nepal Adventure conçoivent votre itinéraire sur-mesure (durées étendues, affûts spécifiques, mise à disposition de porteurs pour matériel lourd). Échangez directement avec nous sur WhatsApp.
    </p>
    <a href="https://wa.me/33649646452?text=Bonjour%20Robin,%20je%20souhaite%20des%20renseignements%20pour%20un%20safari%20photo%20tigre%20à%20Bardia" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-8 py-4 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold text-base rounded-2xl shadow-xl transition-all hover:scale-105">
      <span>Discuter avec Robin sur WhatsApp</span> 💬
    </a>
  </div>
</div>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">7. FAQ : Vos questions fréquentes sur le safari photo tigre</h2>

<div itemscope itemtype="https://schema.org/FAQPage" class="space-y-6 my-8">
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">Peut-on réellement photographier le tigre du Bengale à pied en toute sécurité ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        Oui, absolument. Les safaris à pied sont encadrés par deux guides naturalistes certifiés et rompus aux codes de la jungle. Le tigre du Bengale est un félin qui évite le contact humain lorsqu'il est prévenu de notre arrivée. En observant le silence, les distances de sécurité (30-50m) et les directives des pisteurs, le safari à pied se déroule dans des conditions de sécurité optimales sans le moindre incident en plus de 15 ans.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">Combien de jours faut-il prévoir pour être certain de réussir ses photos de tigres ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        Nous recommandons un séjour d'au moins 4 à 5 jours complets de safari à Bardia (idéalement 7 jours comme dans notre formule Jungle Extrême). La faune sauvage étant imprévisible, multiplier les affûts matinaux et vespéraux permet d'atteindre un taux d'observation supérieur à 80% entre mars et mai.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">Quelle est la meilleure focale pour un safari photo à pied à Bardia ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        La focale la plus adaptée et polyvalente est un zoom 100-400mm ou 150-600mm. Elle permet d'ajuster le cadrage rapidement en fonction de la distance du félin tout en restant suffisamment légère pour de longues marches de 12 à 15 km sous la chaleur.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">Quelle est la différence majeure entre un safari photo en Inde et au Népal ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        En Inde, les safaris s'effectuent exclusivement en 4x4 sur des pistes imposées avec une forte densité de véhicules. Au Népal (Bardia), les safaris se font à pied au ras du sol dans une solitude quasi absolue, offrant des perspectives photographiques uniques et un respect total de la faune.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">Faut-il payer une taxe spéciale pour le matériel photo professionnel ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        Pour les appareils photo reflex/hybrides classiques et téléobjectifs à usage personnel ou artistique, aucun droit supplémentaire n'est exigé au-delà du permis d'entrée régulier du parc. Seuls les tournages de documentaires commerciaux ou d'équipes de télévision nécessitent une autorisation préalable auprès du DNPWC à Katmandou.
      </p>
    </div>
  </div>
</div>

<p class="text-xs text-slate-400 mt-10 border-t border-slate-800 pt-4">
  <em>Sources et références scientifiques : Données de recensement national du tigre par le <a href="https://dnpwc.gov.np" target="_blank" rel="noopener noreferrer" class="underline text-slate-300">Department of National Parks and Wildlife Conservation (DNPWC)</a> et programmes de conservation soutenus par le <a href="https://www.wwfnepal.org" target="_blank" rel="noopener noreferrer" class="underline text-slate-300">WWF Nepal</a>.</em>
</p>
"""

english_content = """<p class="lead text-xl text-slate-200 font-medium leading-relaxed mb-8">
05:45 AM on the misty banks of the Geruwa River in the deep west of Nepal's Terai. Pawan, our Tharu master tracker, raises his hand in absolute stillness. Complete silence. Fifty meters away, beneath the dense canopy of Sal trees (<em>Shorea robusta</em>), a Spotted Deer (Chital) alarm call snaps through the crisp morning air like a whip. Seconds later, a deeper, guttural bark echoes from a tree crown: the Langur sentry has spotted the apex predator. This is no leopard. The tension freezing the forest is too heavy. It is him: the great Bengal Tiger.
</p>

<p>
Kneeling in the damp sand and river pebbles, telephoto lens braced on your shoulder, monopod set into the riverbed, your pulse quickens. No metal chassis, no vibrating 4x4 engine, no tourist chatter. You are on foot, at the exact eye-level of the wild feline. When his massive silhouette breaks through the tall elephant grass toward the water, the photographic and emotional impact is beyond compare.
</p>

<div class="my-10 p-6 sm:p-8 rounded-2xl bg-gradient-to-br from-emerald-950/80 to-slate-900/90 border border-emerald-500/30 shadow-2xl backdrop-blur-md">
  <div class="flex items-start gap-4">
    <div class="p-3 bg-emerald-500/20 text-emerald-400 rounded-xl text-2xl">📷</div>
    <div>
      <h3 class="text-xl font-bold text-emerald-300 mb-2 mt-0">Why this guide is the definitive reference for Tiger Photo Safaris in Nepal</h3>
      <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-4">
        This comprehensive dossier compiles over 10 years of intensive field experience in <strong>Bardia National Park</strong>. Written by photographers for photographers, it details the art of walking tracking with native guides, camera gear settings for tropical canopies, lighting seasons, and unfiltered hide tactics.
      </p>
      <div class="flex flex-wrap gap-3">
        <a href="/en/tours/jungle-extreme" class="inline-flex items-center gap-2 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-xs sm:text-sm font-semibold rounded-lg transition-colors">
          <span>Explore Jungle Extreme Expedition (7 Days)</span> →
        </a>
        <a href="/en/destinations/bardia" class="inline-flex items-center gap-2 px-4 py-2 bg-white/10 hover:bg-white/20 text-slate-200 text-xs sm:text-sm font-medium rounded-lg transition-colors border border-white/10">
          <span>All about Bardia National Park</span>
        </a>
      </div>
    </div>
  </div>
</div>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_tigre_bengale1.webp" alt="Bengal Tiger emerging from elephant grass in Bardia National Park Nepal" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="eager" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Eye-level ground encounter with a dominant male Bengal tiger along the Geruwa River (Photo: Jungle Nepal Adventure Expedition).</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">1. Why Nepal and Bardia Surpass India for Wildlife Photography</h2>

<p>
For decades, India (Ranthambore, Bandhavgarh, Tadoba) was the default destination for tiger sightings. But for demanding wildlife photographers, Indian safaris have become an ethical and creative compromise: restricted tracks, mandatory vehicle confinement, steep high-angle shots, and clusters of 15 to 20 jeeps surrounding a single animal.
</p>

<p>
<strong>Nepal</strong>, and specifically <a href="/en/blog/guide-complet-parc-national-de-bardia-nepal" class="text-emerald-400 underline hover:text-emerald-300">Bardia National Park (968 km²)</a>, champions an entirely different philosophy: <strong>pure walking tracking in total wilderness silence</strong>.
</p>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_safari_a_pied.webp" alt="Wildlife photographers on a walking safari in Bardia jungle Nepal" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Silent single-file walking tracking guided by native Tharu trackers in the Sal forest.</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">2. The Art of Foot Tracking with Pawan & Kiran</h2>

<p>
In Bardia, successful photography does not rely on vehicle horsepower, but on the ancestral woodcraft of our native Terai trackers, <strong>Pawan and Kiran</strong>.
</p>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">Reading Pugmarks (Footprints)</h3>
<p>
On river sandbanks or soft dust trails, every footprint tells a precise story:
</p>
<ul class="list-disc pl-6 space-y-2 text-slate-300">
  <li><strong>Sex Identification</strong>: Male tiger pad tracks fit into a square/circular box with broad rounded heels, whereas female prints are distinctly more oval.</li>
  <li><strong>Time Estimation</strong>: Damp sand grains at the edge of claw indentations reveal a passage within 20 minutes.</li>
  <li><strong>Behavioral Pace</strong>: Even stride lengths signify a boundary patrol; compressed, deliberate paces indicate hunting stalking mode.</li>
</ul>

<figure class="wp-block-image my-8">
  <img src="/assets/curated_gallery/tigre_bengale_pistage.webp" alt="Tracking Bengal Tiger footprints in Bardia grassland" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Fresh tiger pugmarks identified at dawn along the Karnali river channel.</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">3. Technical Camera Gear Guide for Jungle Photography</h2>

<h3 class="wp-block-heading text-xl font-bold text-emerald-400 mt-8 mb-4">Lenses: What to Pack in Your Bag</h3>
<ul class="list-disc pl-6 space-y-3 text-slate-300">
  <li><strong>The Versatile Telephoto Zoom (100-400mm or 150-600mm)</strong>: The uncontested king on foot. Maneuverable, lightweight (1.4-1.8 kg), and allows switching from environmental habitat portraits to tight headshots.</li>
  <li><strong>The Fast Prime (500mm or 600mm f/4)</strong>: Outstanding for static hides on wooden Machans or riverbank waits, delivering unmatched creamy bokeh at twilight.</li>
</ul>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/julien_tigre_bengale2.webp" alt="Bengal tiger bathing in river pool in Bardia National Park" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Tiger cooling off in the Geruwa River during April heat (Photo: Julien - Jungle Nepal Traveler).</figcaption>
</figure>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">4. Best Seasons & Lighting Calendar</h2>

<ul class="list-disc pl-6 space-y-3 text-slate-300">
  <li><strong>March to May (The Peak Tiger Season - 75-85% Sightings)</strong>: Dry heat, cut grass, water pools dry up, forcing tigers into prolonged river baths daily.</li>
  <li><strong>October to November (Golden Post-Monsoon Light & Dashain)</strong>: Crystal clear air, lush emerald jungle, comfortable temperatures (24-28°C), and sacred Dashain festivities.</li>
  <li><strong>December to February (Mystic Fogs & Bird Migration)</strong>: Atmospheric god rays filtering through Sal trees and thousands of migratory waterfowl.</li>
</ul>

<figure class="wp-block-image my-8">
  <img src="/assets/drive_photos/adrien_bardia_river.webp" alt="Golden sunset over Karnali river in Bardia Nepal" class="w-full rounded-2xl border border-white/10 shadow-2xl object-cover" width="1200" height="675" loading="lazy" />
  <figcaption class="text-xs text-center text-slate-400 mt-2 italic">Sunset on the Karnali: the magic hour when apex predators initiate their nocturnal hunts.</figcaption>
</figure>

<div class="my-10 p-8 rounded-3xl bg-emerald-950 border border-emerald-500/40 text-center shadow-2xl">
  <h3 class="text-2xl font-extrabold text-white mb-3 mt-0">Planning a private photo expedition in Nepal?</h3>
  <p class="text-emerald-200 text-sm sm:text-base leading-relaxed mb-6">
    Contact Robin and the Jungle Nepal Adventure field team on WhatsApp to tailor your expedition dates, dedicated hides, and master tracker logistics.
  </p>
  <a href="https://wa.me/33649646452?text=Hello%20Robin,%20I%20am%20interested%20in%20a%20private%20tiger%20photo%20safari%20in%20Bardia" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-8 py-4 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold text-base rounded-2xl shadow-xl transition-all">
    <span>Chat with Robin on WhatsApp</span> 💬
  </a>
</div>

<h2 class="wp-block-heading text-2xl sm:text-3xl font-bold text-white mt-12 mb-6">5. Frequently Asked Questions (FAQ)</h2>

<div itemscope itemtype="https://schema.org/FAQPage" class="space-y-6 my-8">
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">Can you safely photograph Bengal Tigers on foot in Nepal?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        Yes, absolutely. Walking safaris are led by two certified native naturalists with decades of experience. Bengal tigers avoid human conflict when given space (30-50m safety perimeter) and approached quietly under tracker supervision. In over 15 years, Jungle Nepal has maintained a 100% incident-free safety record.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">How many days should I plan for a tiger photo safari in Bardia?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        We recommend a minimum of 4 to 5 full safari days in Bardia (ideally 7 days as in our Jungle Extreme itinerary). This provides multiple dawn and dusk hide sessions, achieving sighting rates above 80% during the March-May peak window.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" class="p-5 rounded-xl bg-slate-900/90 border border-slate-800">
    <h3 itemprop="name" class="text-lg font-bold text-emerald-300 mb-2 mt-0">What is the difference between a tiger photo safari in India and Nepal?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" class="text-slate-300 text-sm sm:text-base leading-relaxed">
        In India, safaris are strictly conducted in 4x4 vehicles on designated tracks alongside dozens of other jeeps. In Nepal (Bardia), safaris are on foot at ground eye-level in near-total solitude, providing unique natural bokeh, low-angle framing, and zero engine disturbance.
      </p>
    </div>
  </div>
</div>
"""

new_post_fr = {
    "id": 999,
    "slug": "safari-photo-tigre-nepal-bardia-guide-affut",
    "title": "Safari Photo Tigre du Bengale au Népal : Le Guide Ultime de l'Affût à Pied à Bardia (2026)",
    "description": "Comment réussir votre safari photo tigre au Népal ? Guide d'expert : affûts à pied à Bardia avec nos pisteurs Tharu, focales et réglages, saisons de lumière et secrets de terrain.",
    "keyword": "safari photo tigre nepal",
    "content": french_content,
    "featuredImage": "/assets/drive_photos/julien_tigre_bengale1.webp",
    "date": "2026-03-24",
    "readingTime": "22 min",
    "category": "Photographie & Expéditions",
    "author": "Robin Rozier",
    "authorRole": "Fondateur & Guide Expéditions",
    "authorImage": "/assets/img_3.webp"
}

new_post_en = {
    "id": 999,
    "slug": "safari-photo-tigre-nepal-bardia-guide-affut",
    "title": "Bengal Tiger Photo Safari in Nepal: The Ultimate Bardia Foot Tracking Guide (2026)",
    "description": "How to photograph wild Bengal tigers in Nepal? Expert guide: walking tracking in Bardia with Tharu master trackers, camera gear settings, prime seasons, and hide tactics.",
    "keyword": "bengal tiger photo safari nepal",
    "content": english_content,
    "featuredImage": "/assets/drive_photos/julien_tigre_bengale1.webp",
    "date": "2026-03-24",
    "readingTime": "22 min",
    "category": "Photography & Expeditions",
    "author": "Robin Rozier",
    "authorRole": "Founder & Expedition Leader",
    "authorImage": "/assets/img_3.webp"
}

# Update French
with open("src/data/blog_posts.json", "r", encoding="utf-8") as f:
    posts_fr = json.load(f)

# Filter out if already exists
posts_fr = [p for p in posts_fr if p.get("slug") != new_post_fr["slug"]]
posts_fr.insert(0, new_post_fr)

with open("src/data/blog_posts.json", "w", encoding="utf-8") as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

print(f"Updated French blog posts, total count: {len(posts_fr)}")

# Update English
with open("src/data/blog_posts.en.json", "r", encoding="utf-8") as f:
    posts_en = json.load(f)

posts_en = [p for p in posts_en if p.get("slug") != new_post_en["slug"]]
posts_en.insert(0, new_post_en)

with open("src/data/blog_posts.en.json", "w", encoding="utf-8") as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print(f"Updated English blog posts, total count: {len(posts_en)}")
