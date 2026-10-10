import json

with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

# Find post in FR
p_fr = next(x for x in posts_fr if x.get('slug') == 'pistage-a-pied-nepal-journee-type-pisteurs-tharu')

# Construct the enhanced FR content with elite UI/UX blocks and rich internal links
new_content_fr = """<p class="wp-block-paragraph">Il est 05h45 du matin. Une nappe de brume laiteuse s'élève lentement au-dessus des rizières endormies de Thakurdwara. Dans la cour de notre lodge, Pawan et Kiran vérifient une dernière fois leurs gourdes métalliques et ajustent leur sac de toile. Dans leurs mains, pas de fusil ni d'épieu : un simple <strong>bâton en bambou robuste</strong>, poli par des décennies d'immersion au cœur de la jungle.</p>

<p class="wp-block-paragraph">Faire un <strong>safari à pied au Népal</strong> (walking safari) suscite immanquablement chez les voyageurs un mélange d'excitation intense et de vertige légitime : <em>est-ce bien raisonnable de marcher sur le même territoire qu'un tigre du Bengale de 220 kg, qu'un rhinocéros unicorne cuirassé ou qu'un éléphant sauvage ?</em></p>

<p class="wp-block-paragraph">La réponse est sans équivoque : oui, car le pistage pédestre dans le <a href="/destinations/bardia">parc national de Bardia</a> n'est ni une bravade téméraire ni un spectacle improvisé. C'est un art séculaire rigoureusement codifié, transmis de génération en génération par le peuple indigène Tharu. Pour explorer l'histoire et les coutumes de nos guides, lisez notre dossier sur la <a href="/blog/culture-tharu-nepal-immersion-jungle">culture Tharu et l'immersion en jungle au Népal</a>.</p>

<div class="blog-cta-card my-8">
  <div>
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">Activité phare à la journée</span>
    <h3>Safari à pied à Bardia (Walking Safari 1 Jour)</h3>
    <p>50 € / personne • 2 guides naturalistes certifiés • Briefing sécurité et pistage éthique au ras du sol.</p>
  </div>
  <a href="/tours/safari-pied-bardia" class="cta-btn">Réserver l'activité à pied (50 €) →</a>
</div>

<p class="wp-block-paragraph">Voici le récit minute par minute d'une journée type de pistage à pied dans le sanctuaire sauvage le plus préservé d'Asie.</p>

<hr />

<h2 class="wp-block-heading">06h15 : Le franchissement de la frontière végétale et le briefing de sécurité</h2>
<p class="wp-block-paragraph">Après un court trajet pour rejoindre le poste des gardes forestiers de l'armée népalaise à l'entrée du parc, l'expédition commence par le contrôle scrupuleux des permis de conservation. Avant que la semelle de votre chaussure ne touche le premier sentier sablonneux, nos deux guides réunissent le groupe pour le briefing obligatoire de sécurité.</p>

<p class="wp-block-paragraph">Les <strong>quatre règles d'or du pistage pédestre</strong> sont énoncées avec calme mais fermeté :</p>
<ol class="wp-block-list">
  <li><strong>Silence absolu en déplacement :</strong> Les branches mortes, les feuilles sèches de Sal et le bruissement des vêtements sont nos premiers ennemis. Le tigre possède une ouïe cinq fois supérieure à la nôtre ; notre sécurité dépend de notre capacité à entendre la forêt avant qu'elle ne nous repère.</li>
  <li><strong>La marche en file indienne compacte :</strong> Jamais de dispersion. Le premier guide ouvre la marche pour scruter le sol et l'horizon ; le second guide ferme le rang pour surveiller les arrières. Aux yeux des prédateurs, un groupe soudé et compact forme une silhouette intimidante, là où un marcheur isolé représente une proie vulnérable.</li>
  <li><strong>Le bâton de bambou (<em>Lathi</em>) :</strong> Symbole du pisteur Tharu, ce bâton sert de troisième point d'appui pour sonder les rivières, écarter les ronces sans bruit, mais aussi de barrière visuelle en cas de confrontation rapprochée.</li>
  <li><strong>La règle d'or universelle : NE JAMAIS COURIR.</strong> Dans le règne animal, seule la proie détale à toute allure. Face à un grand prédateur, la course déclenche instantanément le réflexe prédateur d'attaque. Pour un tour d'horizon complet des protocoles, consultez notre guide : <a href="/blog/safari-a-pied-nepal-danger-regles-securite-guide">Le safari à pied est-il dangereux au Népal ?</a>.</li>
</ol>

<!-- ENHANCED SAFETY PROTOCOL CARDS (PERFECT UI/UX) -->
<div class="my-8 space-y-4">
  <div class="p-5 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-slate-800">
    <div class="flex items-center gap-2 mb-2">
      <span class="text-xl">🐅</span>
      <h3 class="text-base font-black text-amber-950 uppercase tracking-tight">Protocole face au Tigre du Bengale</h3>
    </div>
    <p class="text-xs sm:text-sm leading-relaxed text-slate-700">
      <strong>Arrêt net immédiat.</strong> Le groupe se serre épaule contre épaule pour former un bloc imposant. On maintient un <strong>contact visuel direct et ininterrompu</strong> sans jamais baisser les yeux, sans crier, et on recule pas à pas très lentement. <strong>Ne jamais courir ni tourner le dos.</strong> Dans 99 % des cas, le félin jauge le groupe et s'éclipse silencieusement dans le sous-bois. Pour comprendre la psychologie du félin, découvrez notre étude sur le <a href="/blog/comportement-du-tigre-du-bengale" class="text-emerald-700 font-bold underline">comportement du tigre du Bengale</a>.
    </p>
  </div>

  <div class="p-5 rounded-2xl bg-slate-100 border border-slate-300/80 text-slate-800">
    <div class="flex items-center gap-2 mb-2">
      <span class="text-xl">🦏</span>
      <h3 class="text-base font-black text-slate-900 uppercase tracking-tight">Protocole face au Rhinocéros unicorne</h3>
    </div>
    <p class="text-xs sm:text-sm leading-relaxed text-slate-700">
      Si l'animal charge, la consigne absolue est de <strong>grimper immédiatement sur un arbre robuste</strong> à 2 ou 3 mètres de hauteur grâce aux indications des guides. En terrain ouvert sans arbre accessible, on court en <strong>zig-zag rapide</strong> pour déjouer sa vision périphérique très réduite, ou l'on jette son sac à dos ou un vêtement au sol pour détourner sa charge. Approfondissez ces réflexes dans notre dossier sur le <a href="/blog/comportement-du-rhinoceros-unicornis" class="text-emerald-700 font-bold underline">comportement du rhinocéros unicorne</a>.
    </p>
  </div>

  <div class="p-5 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
    <div class="flex items-center gap-2 mb-2">
      <span class="text-xl">🐘</span>
      <h3 class="text-base font-black text-emerald-300 uppercase tracking-tight">Protocole face à l'Éléphant sauvage</h3>
    </div>
    <p class="text-xs sm:text-sm leading-relaxed text-slate-200">
      <strong>L'anticipation et l'esquive priment sur tout.</strong> L'éléphant sauvage ne tolère aucune proximité. Les guides détectent sa présence à l'odeur musquée, aux branches brisées et aux vibrations du sol. On s'écarte immédiatement <strong>sous le vent à très grande distance</strong> (plus de 300 mètres) en libérant systématiquement ses corridors de passage vers la rivière. Retrouvez nos conseils dans le guide sur <a href="/blog/elephant-sauvage-nepal-guide-safari" class="text-amber-300 font-bold underline">l'éléphant sauvage au Népal</a>.
    </p>
  </div>
</div>

<hr />

<h2 class="wp-block-heading">07h30 : La lecture des "Pugmarks" et les premiers indices de la nuit</h2>
<p class="wp-block-paragraph">Le soleil commence à percer la canopée des arbres de Sal (<em>Shorea robusta</em>). Le sol meuble d'un chemin de patrouille révèle les secrets des heures sombres.</p>

<p class="wp-block-paragraph">Pawan s'accroupit brusquement. Du bout des doigts, il effleure une empreinte circulaire nette imprimée dans le sable humide : un <strong>pugmark</strong> de tigre.</p>
<ul class="wp-block-list">
  <li><strong>Le décryptage du pisteur :</strong> La largeur du coussinet plantaire (9,5 cm) indique un mâle adulte territorial. Les grains de sable sur les crêtes de l'empreinte sont encore humides et la rosée n'a pas encore coulé dans le creux : l'animal est passé ici il y a moins de 45 minutes.</li>
  <li><strong>Les griffures territoriales :</strong> Quelques mètres plus loin, le tronc d'un Sal porte des entailles verticales profondes à plus de deux mètres de hauteur, mêlées à une odeur musquée persistante de pop-corn beurré : le félin a marqué son territoire avant de descendre vers l'eau. Pour percer tous ces secrets, lisez notre guide : <a href="/blog/art-du-pistage-jungle-nepal-traces-cris-alarme">L'art du pistage en jungle au Népal : traces, cris d'alarme et secrets</a>.</li>
</ul>

<hr />

<h2 class="wp-block-heading">09h00 : La symphonie des cris d'alarme dans la canopée</h2>
<p class="wp-block-paragraph">Tandis que nous nous enfonçons vers les corridors alluviaux, la jungle s'anime. En safari à pied, nos guides ne cherchent pas l'animal avec leurs yeux, mais avec leurs oreilles :</p>

<blockquote>
  <p class="wp-block-paragraph"><em>« Écoutez le chital ! »</em> chuchote Kiran.</p>
</blockquote>

<p class="wp-block-paragraph">À trois cents mètres sur notre gauche, l'aboiement strident et métallique d'un cerf axis (<em>Axis axis</em>) déchire le sous-bois. Un deuxième cri répond immédiatement. Quelques secondes plus tard, un cri rauque, violent et saccadé retentit depuis les cimes : l'alarme d'un mâle dominant <a href="/blog/singes-nepal-langurs-macaques-guide">singe langur de l'Himalaya</a>.</p>

<p class="wp-block-paragraph">Perchés à vingt mètres de hauteur, les singes bénéficient d'un angle de vue plongeant imprenable sur les herbes d'éléphant. Leur alarme ne trompe jamais : un félin est en mouvement. Le pisteur calcule la direction du vent, estime la trajectoire du prédateur et nous guide d'un pas feutré vers un promontoire naturel surplombant le cours d'eau.</p>

<hr />

<h2 class="wp-block-heading">11h30 : L'affût silencieux au bord de la rivière Geruwa</h2>
<p class="wp-block-paragraph">Aux heures les plus chaudes de la journée (spécialement entre mars et mai lorsque le thermomètre frôle les 38°C), les tigres quittent la fournaise des herbes sèches pour venir se baigner et réguler leur température corporelle dans les eaux fraîches de la rivière. Découvrez les meilleures périodes d'affût dans notre article : <a href="/blog/tigre-bardia-observation-chances-spots">Tigre à Bardia : chances d'observation et spots stratégiques</a>.</p>

<p class="wp-block-paragraph">Nous nous installons sur les bancs de galets de <strong>Tinkuni</strong>, un confluent réputé où la rivière forme des méandres paisibles bordés de falaises alluviales :</p>
<ul class="wp-block-list">
  <li>Nous nous adossons à de grands galets ou sous l'ombrage d'un buisson d'épineux.</li>
  <li>Pas un mot n'est prononcé. Les chuchotements sont remplacés par des signaux manuels précis.</li>
  <li>Pendant deux à trois heures, nous guettons l'eau miroitante. Un <a href="/blog/gavial-du-gange-crocodiles-nepal-guide">crocodile gavial du Gange</a> flotte immobile à la surface, tandis qu'une troupe de loutres plonge bruyamment.</li>
  <li>Soudain, à l'orée des herbes dorées de la rive opposée, une silhouette rousse aux rayures noires fait son apparition : le tigre s'avance à pas lents, boit posément et s'immerge jusqu'au cou. L'émotion d'observer ce spectacle au ras du sol, sans vitre de 4x4 ni barrière métallique, reste gravée à jamais.</li>
</ul>

<hr />

<h2 class="wp-block-heading">14h00 : Pique-nique en jungle dans un mirador en bois (<em>Machan</em>)</h2>
<p class="wp-block-paragraph">La pause déjeuner s'effectue dans un <em>machan</em>, une tour d'observation traditionnelle en bois surélevée à 6 mètres du sol, construite par les gardes forestiers du parc. C'est le moment de relâcher la tension musculaire, de déguster le déjeuner chaud préparé par le lodge (riz népalais, dal bhat, légumes sautés du potager et fruits frais) tout en continuant à balayer la plaine aux jumelles.</p>

<hr />

<h2 class="wp-block-heading">16h30 : Rencontre avec le colosse cuirassé : le rhinocéros unicorne</h2>
<p class="wp-block-paragraph">En fin d'après-midi, nous amorçons la boucle retour à travers les prairies humides. Le vent tourne. Soudain, une masse grise imposante se détache à cinquante mètres dans une clairière : un rhinocéros unicorne d'Asie (<em>Rhinoceros unicornis</em>), broutant paisiblement des jacinthes d'eau.</p>

<p class="wp-block-paragraph">Pawan teste la direction de l'air en laissant filer une pincée de sable entre ses doigts. Le vent souffle vers nous : le colosse ne nous a pas sentis. Avec sa mauvaise vue mais son ouïe aiguisée, l'animal mastique avec force. Les guides nous font progresser pas à pas derrière un alignement d'arbres protecteurs. Nous contemplons les replis de sa peau cuirassée couverte de boue séchée, véritable armure préhistorique vivante. Retrouvez l'inventaire complet des espèces dans notre guide : <a href="/blog/animaux-bardia-faune-parc-national">Les animaux de Bardia : guide de la faune du parc</a>.</p>

<hr />

<h2 class="wp-block-heading">18h30 : Retour au lodge et débriefing au coin du feu</h2>
<p class="wp-block-paragraph">Le soleil rougeoie et disparaît derrière les contreforts des montagnes de Siwalik. Nous franchissons à nouveau la porte du parc, les chaussures couvertes de poussière fine, les sens encore en alerte.</p>

<p class="wp-block-paragraph">Autour du feu de camp du lodge, une tasse de thé masala chaud ou une bière népalaise à la main, Pawan déplie la carte topographique du parc. Avec un feutre, nous retraçons les 14 kilomètres parcourus, les trois relevés d'empreintes fraîches, les oiseaux cochés et les minutes magiques passées face au grand félin.</p>

<hr />

<h2 class="wp-block-heading">Le safari à pied est-il fait pour vous ?</h2>
<p class="wp-block-paragraph">Le safari pédestre ne requiert pas une condition physique d'athlète de haut niveau : le rythme de marche est lent, ponctué de nombreuses haltes d'affût statique. Pour évaluer votre niveau, consultez notre article : <a href="/blog/condition-physique-safari-a-pied-nepal">Quelle condition physique pour un safari à pied au Népal ?</a>. De plus, si vous terminez une randonnée himalayenne, notre nouveau guide vous explique en détail <a href="/blog/comment-organiser-un-safari-a-bardia-apres-un-trek">comment organiser un safari à Bardia après un trek</a>.</p>

<p class="wp-block-paragraph">Loin du tourisme de masse et des jeeps bondées, cette immersion au ras du sol est la plus belle preuve de respect que l'on puisse offrir à la faune souveraine du Teraï.</p>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">Activité 1 Jour ou Expédition Complète</span>
    <h3 class="text-xl font-bold text-white">Vivez une journée de pistage à pied avec nos maîtres pisteurs Tharu</h3>
    <p class="text-slate-300 text-xs">Vous êtes déjà au Népal à Katmandou ou Pokhara ? Rejoignez nos guides d'élite pour une journée d'immersion 100% à pied dans le parc de Bardia ou un séjour complet de 5 jours.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/tours/safari-pied-bardia" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Réserver le Safari 1 Jour à Pied (50€) →</a>
    <a href="/tours/bardia-explorateur" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Expédition Bardia Explorateur (5 jours) →</a>
    <a href="/contact" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs shadow-md transition-all">Demander un conseil direct à Robin →</a>
  </div>
</div>
"""

p_fr['content'] = new_content_fr
print("FR post updated successfully!")

# Now let's update EN post with the exact same structure, formatting and internal links
p_en = next(x for x in posts_en if x.get('slug') == 'pistage-a-pied-nepal-journee-type-pisteurs-tharu')

new_content_en = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: A Day with Native Tharu Trackers in Bardia</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>Ancestral Ethology:</strong> Tharu master trackers read the jungle like an open book—decoding fresh pugmarks, soil moisture, claw scratches on bark, and complex avian alarm calls.</li>
    <li><strong>Dawn Departure (6:00 AM):</strong> Entering the park at first light when nocturnal predators are returning to day hides along the Geruwa and Khauraha riverbeds.</li>
    <li><strong>Midday Riverbank Stakeouts:</strong> Setting up silent vantage points under shaded trees overlooking active watering holes during the heat of the day.</li>
    <li><strong>The Bush Lunch:</strong> Enjoying hot fresh dahl bhat or parathas in an elevated wooden watchtower (<em>machan</em>) overlooking the grassland savannah.</li>
    <li><strong>Two Licensed Guides Required:</strong> Every walking safari in <a href="/en/destinations/bardia" class="text-emerald-800 font-bold underline">Bardia National Park</a> is led by two licensed naturalists carrying traditional bamboo lathis (staffs).</li>
  </ul>
</div>

<p class="wp-block-paragraph">It is 5:45 AM. A diaphanous veil of mist hovers over the sleeping paddies of Thakurdwara. In the courtyard of our eco-lodge, Pawan and Kiran double-check their canteens and shoulder their canvas daypacks. In their hands, you will see no firearms, darts, or spears: only a stout, polished <strong>bamboo walking staff (<em>lathi</em>)</strong>, burnished by decades of intimate jungle travel.</p>

<p class="wp-block-paragraph">Embarking on a <strong>walking safari in Nepal</strong> stirs an instinctive blend of awe and heart-pounding respect: <em>is it truly safe to tread on foot across the very realm of a 220 kg Royal Bengal tiger, an armored greater one-horned rhino, or a wild bull elephant?</em></p>

<p class="wp-block-paragraph">The answer from experienced naturalists is an emphatic yes—provided you follow the ancestral tracking codes developed across centuries by the indigenous Tharu people. Learn more about our team and heritage in our feature on <a href="/en/blog/culture-tharu-traditions-cuisine-festival-dashain-bardia">Tharu culture and jungle life in Bardia</a>.</p>

<div class="blog-cta-card my-8">
  <div>
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">Top Day Activity</span>
    <h3>Bardia Walking Safari (1-Day Tiger Tracking)</h3>
    <p>€50 / person • 2 certified naturalist guides • Complete safety briefing and silent on-foot immersion.</p>
  </div>
  <a href="/en/tours/bardia-walking-safari" class="cta-btn">Book Walking Safari (€50) →</a>
</div>

<hr />

<h2 class="wp-block-heading">06:15 AM: Entering the Green Frontier & Safety Briefing</h2>
<p class="wp-block-paragraph">After checking entry permits with the Nepal Army conservation outpost at the park boundary, your shoes touch the first sandy jungle track. Before advancing a single step into the Sal forest canopy, your two guides gather the group for a mandatory safety briefing.</p>

<p class="wp-block-paragraph">The <strong>four golden rules of foot tracking</strong> are delivered with quiet authority:</p>
<ol class="wp-block-list">
  <li><strong>Absolute silence while moving:</strong> Snapping dry twigs, crunching broad Sal leaves, and rustling synthetics are your primary obstacles. A tiger's hearing is five times sharper than a human's; your safety relies on hearing the jungle before it detects you.</li>
  <li><strong>Tight single-file formation:</strong> Never wander or fan out. The lead guide navigates the terrain and scans the horizon; the rear guide monitors your backtrail. In the eyes of apex predators, a tight unit presents a formidable collective silhouette, whereas a scattered walker mimics vulnerable prey.</li>
  <li><strong>The bamboo staff (<em>Lathi</em>):</strong> More than a hiking pole, this traditional Tharu staff tests river depths, parts thorny wait-a-minute vines silently, and serves as an imposing visual barrier in close encounters.</li>
  <li><strong>The universal rule: NEVER RUN.</strong> In the animal kingdom, only prey bolts in panic. Running instantly triggers a predator's innate predatory reflex. For an in-depth safety breakdown, see our guide: <a href="/en/blog/safari-a-pied-nepal-danger-regles-securite-guide">Is a walking safari dangerous in Nepal?</a>.</li>
</ol>

<!-- ENHANCED SAFETY PROTOCOL CARDS (PERFECT UI/UX) -->
<div class="my-8 space-y-4">
  <div class="p-5 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-slate-800">
    <div class="flex items-center gap-2 mb-2">
      <span class="text-xl">🐅</span>
      <h3 class="text-base font-black text-amber-950 uppercase tracking-tight">Protocol: Confronting a Bengal Tiger</h3>
    </div>
    <p class="text-xs sm:text-sm leading-relaxed text-slate-700">
      <strong>Freeze immediately.</strong> The group links shoulder-to-shoulder to present an intimidating wall. Maintain <strong>unblinking, direct eye contact</strong> without shouting, and retreat step by deliberate step backwards. <strong>Never run and never turn your back.</strong> In 99% of encounters, the cat assesses the group and melts silently back into the tall grass. Read our behavioral dossier on <a href="/en/blog/comportement-du-tigre-du-bengale" class="text-emerald-700 font-bold underline">Bengal tiger behavior in the wild</a>.
    </p>
  </div>

  <div class="p-5 rounded-2xl bg-slate-100 border border-slate-300/80 text-slate-800">
    <div class="flex items-center gap-2 mb-2">
      <span class="text-xl">🦏</span>
      <h3 class="text-base font-black text-slate-900 uppercase tracking-tight">Protocol: Confronting a Greater One-Horned Rhino</h3>
    </div>
    <p class="text-xs sm:text-sm leading-relaxed text-slate-700">
      If a rhino charges, the absolute directive is to <strong>scramble up a sturdy tree</strong> at least 2 to 3 meters off the ground, following your guide's swift assistance. On open ground lacking trees, run in a <strong>sharp zig-zag pattern</strong> to exploit the rhino's notoriously weak peripheral eyesight, or drop a backpack to distract its momentum. Learn more in our guide to <a href="/en/blog/comportement-du-rhinoceros-unicornis" class="text-emerald-700 font-bold underline">rhino behavior and ecology</a>.
    </p>
  </div>

  <div class="p-5 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
    <div class="flex items-center gap-2 mb-2">
      <span class="text-xl">🐘</span>
      <h3 class="text-base font-black text-emerald-300 uppercase tracking-tight">Protocol: Confronting a Wild Bull Elephant</h3>
    </div>
    <p class="text-xs sm:text-sm leading-relaxed text-slate-200">
      <strong>Anticipation and avoidance override everything.</strong> Wild Asian bull elephants will not tolerate proximity. Trackers detect them early through pungent musky scent, snapping branches, and ground tremors. You immediately detour <strong>downwind at broad distance</strong> (over 300 meters), never blocking their migration corridors to the river. Review our safety tips on <a href="/en/blog/elephant-sauvage-nepal-guide-safari" class="text-amber-300 font-bold underline">wild elephants in Nepal</a>.
    </p>
  </div>
</div>

<hr />

<h2 class="wp-block-heading">07:30 AM: Reading Pugmarks and Fresh Night Tracks</h2>
<p class="wp-block-paragraph">Early sunbeams filter through the towering canopy of Sal trees (<em>Shorea robusta</em>). The damp sand along an army patrol path reveals secrets carved in darkness.</p>

<p class="wp-block-paragraph">Pawan drops swiftly to one knee. With calloused fingertips, he gently traces the crisp circumference of a fresh <strong>pugmark</strong> pressed into the alluvial silt.</p>
<ul class="wp-block-list">
  <li><strong>The Tracker's Analysis:</strong> The 9.5 cm heel pad width identifies a dominant territorial male. The sand ridges remain moist and dawn dew has not yet settled into the indentations: the tiger passed here less than 45 minutes ago.</li>
  <li><strong>Territorial Markings:</strong> A few meters ahead, a stout Sal trunk displays vertical claw gashes over two meters high, accompanied by a musky scent resembling warm buttered popcorn: the cat marked his perimeter before heading down to the water. Master these signs in our field handbook: <a href="/en/blog/art-du-pistage-jungle-nepal-traces-cris-alarme">The Art of Jungle Tracking in Nepal: Tracks, Alarm Calls and Secrets</a>.</li>
</ul>

<hr />

<h2 class="wp-block-heading">09:00 AM: The Alarm Symphony in the Forest Canopy</h2>
<p class="wp-block-paragraph">As we push toward riverine corridors, the forest wakes up. On foot, trackers do not spot predators with their eyes first—they listen with tuned ears:</p>

<blockquote>
  <p class="wp-block-paragraph"><em>"Listen to the chital!"</em> whispers Kiran.</p>
</blockquote>

<p class="wp-block-paragraph">Three hundred meters to our flank, the sharp, metallic bark of a spotted deer (<em>Axis axis</em>) pierces the brush. Seconds later, a harsh, guttural cough echoes from the treetops: the alarm call of a dominant <a href="/en/blog/singes-nepal-langurs-macaques-guide">Tarai grey langur</a>.</p>

<p class="wp-block-paragraph">Perched twenty meters high, langurs possess an unhindered vantage over dense elephant grass. Their alarm never lies: a big cat is stalking. Testing wind direction with a pinch of dry dust, our guides steer us with feather-light steps toward a natural gravel ridge overlooking the riverbank.</p>

<hr />

<h2 class="wp-block-heading">11:30 AM: Silent River Stakeout Along the Geruwa</h2>
<p class="wp-block-paragraph">During the heat of the day (especially from March to May when midday mercury climbs to 38°C), tigers retreat from sweltering grasslands to soak in refreshing river shallows. Find the best seasons in our report: <a href="/en/blog/tigre-bardia-observation-chances-spots">Tigers in Bardia: Sighting Probabilities and Top Water Spots</a>.</p>

<p class="wp-block-paragraph">We settle into position on the boulder beaches of <strong>Tinkuni</strong>, a celebrated three-river junction where braided channels carve quiet pools below clay bluffs:</p>
<ul class="wp-block-list">
  <li>We nestle quietly against rounded boulders beneath thorny shade bushes.</li>
  <li>Not a single word is spoken; whispers are replaced by discreet hand gestures.</li>
  <li>For two to three hours, we watch the shimmer of the water. A prehistoric <a href="/en/blog/gavial-du-gange-crocodiles-nepal-guide">Gharial crocodile</a> drifts past while smooth-coated otters fish playfully.</li>
  <li>Suddenly, at the golden fringe of the opposite shore, a radiant orange and black silhouette materializes: the tiger advances with unhurried grace, drinks calmly, and wades in chest-deep. Witnessing this spectacle from ground level, without vehicle windows or metal cages, is an indelible privilege.</li>
</ul>

<hr />

<h2 class="wp-block-heading">02:00 PM: Bush Lunch in a Forest Watchtower (<em>Machan</em>)</h2>
<p class="wp-block-paragraph">Midday rest is spent inside a traditional wooden <em>machan</em> raised six meters off the ground. It is the time to unwind, relish a steaming lunch packed by the lodge (dahl bhat, fresh sautéed vegetables, and fruit), and scan the river flats with binoculars.</p>

<hr />

<h2 class="wp-block-heading">04:30 PM: Face-to-Face with an Armored Colossus: The Greater One-Horned Rhino</h2>
<p class="wp-block-paragraph">In the late afternoon, we loop back across floodplain marshlands. The wind shifts. Suddenly, a massive grey boulder seems to rise fifty meters away in a clearing: an immense Greater One-Horned Rhinoceros (<em>Rhinoceros unicornis</em>) grazing on water hyacinths.</p>

<p class="wp-block-paragraph">Pawan tests the breeze again. It blows toward us—the colossus has not scented our party. Despite feeble eyesight, its ears swivel like acoustic dishes. The guides maneuver our group behind an alignment of sturdy trees. We marvel at the armor-plated skin folds coated in dry mud—a true living prehistoric titan. Browse the full wildlife roster in our guide: <a href="/en/blog/animaux-bardia-faune-parc-national">Animals of Bardia: Complete Wildlife Guide</a>.</p>

<hr />

<h2 class="wp-block-heading">06:30 PM: Lodge Fireplace Debrief</h2>
<p class="wp-block-paragraph">The setting sun paints the Siwalik foothills crimson. We exit the park gates, boots coated in fine dust, senses still tingling.</p>

<p class="wp-block-paragraph">Around the evening campfire with hot masala chai in hand, Pawan unfolds the topographical map of Bardia. With a marker, we retrace the 14 kilometers walked, three fresh pugmark sets recorded, bird species ticked off, and magical minutes spent watching wild tigers.</p>

<hr />

<h2 class="wp-block-heading">Is a Walking Safari Right for You?</h2>
<p class="wp-block-paragraph">Tracking on foot does not require elite marathon fitness: the pace is measured, punctuated by extensive stationary hides. Check our fitness recommendations in: <a href="/en/blog/condition-physique-safari-a-pied-nepal">What Fitness Level is Needed for a Walking Safari in Nepal?</a>. If you are wrapping up a Himalayan mountain hike, see our new guide on <a href="/en/blog/comment-organiser-un-safari-a-bardia-apres-un-trek">how to organize a safari in Bardia after trekking</a>.</p>

<p class="wp-block-paragraph">Far removed from mass tourism, foot tracking is the ultimate gesture of humility and respect one can offer to the wild sovereigns of the Terai.</p>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">Day Activity or Multi-Day Expedition</span>
    <h3 class="text-xl font-bold text-white">Experience an authentic walking safari with our Tharu master trackers</h3>
    <p class="text-slate-300 text-xs">Already in Nepal or planning your trip? Join our elite local trackers for a 1-day walking safari or a complete 5-day Bardia wildlife expedition.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/bardia-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book 1-Day Walking Safari (€50) →</a>
    <a href="/en/tours/bardia-tiger-safari-5-days" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Bardia Tiger Safari 5 Days →</a>
    <a href="/en/contact" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs shadow-md transition-all">Contact Robin on WhatsApp →</a>
  </div>
</div>
"""

p_en['content'] = new_content_en
print("EN post updated successfully!")

with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Both JSON files saved!")
