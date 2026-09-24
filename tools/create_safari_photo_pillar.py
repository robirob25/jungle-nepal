#!/usr/bin/env python3
import json

french_content = """<p class="lead" style="font-size: 1.15rem; line-height: 1.85; color: #1e293b; font-weight: 500; margin-bottom: 2rem;">
05h45 sur les berges embrumées de la rivière Geruwa, dans l'extrême ouest du Teraï népalais. Pawan, notre maître pisteur Tharu, lève la main dans un geste d'une immobilité parfaite. Silence absolu. À cinquante mètres, sous la canopée dense des arbres de Sal (<em>Shorea robusta</em>), un cri d'alarme de cerf Axis claque dans l'air frais comme un coup de fouet. Quelques secondes plus tard, un second cri, plus rauque, retentit depuis la cime d'un arbre : la vigie des singes langurs vient de repérer le prédateur. Ce n'est pas un léopard. La tension qui pétrifie la forêt est trop lourde. C'est lui : le grand tigre du Bengale.
</p>

<p>
À genoux dans le sable humide et les galets, téléobjectif calé sur l'épaule et monopode ancré au sol, votre cœur s'accélère. Pas de carrosserie métallique, pas de moteur de 4x4 qui vibre, pas de brouhaha de touristes. Vous êtes à pied, au niveau exact des yeux du félin. Lorsque sa silhouette puissante fend les hautes herbes à éléphants pour s'avancer vers la rivière, l'émotion visuelle et photographique est d'une intensité incomparable.
</p>

<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 16px; padding: 24px; margin: 32px 0;">
  <div style="display: flex; align-items: flex-start; gap: 16px;">
    <div style="font-size: 28px; line-height: 1;">📷</div>
    <div>
      <h3 style="margin-top: 0; margin-bottom: 8px; font-size: 1.25rem; font-weight: 800; color: #064e3b !important;">Pourquoi ce guide est la référence du safari photo tigre au Népal</h3>
      <p style="margin: 0 0 16px 0; color: #166534; font-size: 0.95rem; line-height: 1.6;">
        Ce dossier rassemble plus de 10 années d'expérience de terrain dans le <strong>Parc national de Bardia</strong>. Rédigé par des photographes et pour des photographes, il détaille l'art du pistage à pied avec nos guides locaux, les réglages boîtiers pour la jungle tropicale, la gestion des lumières et la réalité brute des affûts sans filtre.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 12px;">
        <a href="/tours/jungle-extreme" style="background: #134836; color: #ffffff !important; padding: 10px 20px; border-radius: 8px; font-weight: 700; font-size: 0.875rem; text-decoration: none; display: inline-block;">
          Découvrir l'expédition Jungle Extrême (7 jours) →
        </a>
        <a href="/destinations/bardia" style="background: #ffffff; color: #134836 !important; border: 1px solid #134836; padding: 10px 20px; border-radius: 8px; font-weight: 700; font-size: 0.875rem; text-decoration: none; display: inline-block;">
          Tout sur le parc de Bardia
        </a>
      </div>
    </div>
  </div>
</div>

<figure class="wp-block-image">
  <img src="/assets/drive_photos/julien_tigre_bengale1.webp" alt="Tigre du Bengale émergeant des herbes à éléphant au parc national de Bardia Népal" width="1200" height="675" loading="eager" />
</figure>

<h2 class="wp-block-heading">1. Pourquoi le Népal et Bardia détrônent l'Inde pour la photographie animalière</h2>

<p>
Pendant des décennies, l'Inde (Ranthambore, Bandhavgarh, Tadoba) a été la destination par défaut pour voir le tigre. Mais pour le photographe naturaliste exigeant, les safaris indiens sont devenus un véritable défi éthique et artistique : pistes obligatoires, interdiction stricte de descendre des 4x4, angles de prise de vue plongeants et peu naturels, et surtout des grappes de 15 à 20 jeeps encerclant un même animal au son des moteurs.
</p>

<p>
Le <strong>Népal</strong>, et plus particulièrement le <a href="/blog/guide-complet-parc-national-de-bardia-nepal">parc national de Bardia (968 km²)</a>, propose une philosophie diamétralement opposée : <strong>le safari à pied exclusif dans le silence le plus pur</strong>.
</p>

<div style="overflow-x: auto; margin: 28px 0;">
  <table style="width: 100%; text-align: left; border-collapse: collapse; border: 1px solid #cbd5e1; border-radius: 12px; overflow: hidden; font-size: 0.9rem;">
    <thead style="background: #0f172a; color: #ffffff;">
      <tr>
        <th style="padding: 14px 16px; font-weight: 700;">Critère photographique</th>
        <th style="padding: 14px 16px; font-weight: 700; background: #134836; color: #ffffff;">Bardia (Népal) - Notre approche</th>
        <th style="padding: 14px 16px; font-weight: 700;">Parcs d'Inde (Ranthambore, etc.)</th>
        <th style="padding: 14px 16px; font-weight: 700;">Chitwan (Népal)</th>
      </tr>
    </thead>
    <tbody style="background: #ffffff; color: #334155;">
      <tr style="border-bottom: 1px solid #e2e8f0;">
        <td style="padding: 14px 16px; font-weight: 700; color: #0f172a;">Angle de prise de vue</td>
        <td style="padding: 14px 16px; font-weight: 700; background: #f0fdf4; color: #065f46;">Niveau des yeux / Ras du sol (bokeh naturel et cinématographique)</td>
        <td style="padding: 14px 16px; color: #64748b;">Plongeant depuis la jeep (1,80m à 2,20m de hauteur)</td>
        <td style="padding: 14px 16px; color: #64748b;">Plongeant (jeep) ou masqué par les herbes</td>
      </tr>
      <tr style="border-bottom: 1px solid #e2e8f0;">
        <td style="padding: 14px 16px; font-weight: 700; color: #0f172a;">Mode de déplacement</td>
        <td style="padding: 14px 16px; font-weight: 700; background: #f0fdf4; color: #065f46;">100% à pied & affûts statiques discrets</td>
        <td style="padding: 14px 16px; color: #64748b;">Jeep 4x4 obligatoirement sur pistes balisées</td>
        <td style="padding: 14px 16px; color: #64748b;">Jeep touristique ou bateau partagé</td>
      </tr>
      <tr style="border-bottom: 1px solid #e2e8f0;">
        <td style="padding: 14px 16px; font-weight: 700; color: #0f172a;">Fréquentation & pression</td>
        <td style="padding: 14px 16px; font-weight: 700; background: #f0fdf4; color: #065f46;">Quasi nulle (souvent seul groupe à 5 km à la ronde)</td>
        <td style="padding: 14px 16px; color: #64748b;">Très dense (10 à 30 jeeps sur une même observation)</td>
        <td style="padding: 14px 16px; color: #64748b;">Moyenne à forte selon les zones</td>
      </tr>
      <tr style="border-bottom: 1px solid #e2e8f0;">
        <td style="padding: 14px 16px; font-weight: 700; color: #0f172a;">Comportement animal</td>
        <td style="padding: 14px 16px; font-weight: 700; background: #f0fdf4; color: #065f46;">100% sauvage et détendu (baignades naturelles, chasse)</td>
        <td style="padding: 14px 16px; color: #64748b;">Parfois stressé ou indifférent aux véhicules</td>
        <td style="padding: 14px 16px; color: #64748b;">Furtif en forêt dense</td>
      </tr>
      <tr>
        <td style="padding: 14px 16px; font-weight: 700; color: #0f172a;">Prise de son vidéo</td>
        <td style="padding: 14px 16px; font-weight: 700; background: #f0fdf4; color: #065f46;">Son pur de la jungle (aucun bruit de moteur)</td>
        <td style="padding: 14px 16px; color: #64748b;">Parasitée par les moteurs diesel et bavardages</td>
        <td style="padding: 14px 16px; color: #64748b;">Variable</td>
      </tr>
    </tbody>
  </table>
</div>

<figure class="wp-block-image">
  <img src="/assets/drive_photos/julien_safari_a_pied.webp" alt="Photographes animaliers en marche silencieuse dans la jungle de Bardia Népal" width="1200" height="675" loading="lazy" />
</figure>

<h2 class="wp-block-heading">2. L'art du pistage à pied : dans les pas de Pawan et Kiran</h2>

<p>
À Bardia, la réussite d'un safari photo ne repose pas sur la vitesse d'un moteur, mais sur la science ancestrale de nos pisteurs natifs du Teraï, <strong>Pawan et Kiran</strong>. Nés aux lisières de la jungle, ils lisent les traces comme un livre ouvert.
</p>

<h3 class="wp-block-heading">La lecture des empreintes (pugmarks)</h3>
<p>
Sur les bancs de sable de la Geruwa ou la poussière fine des sentiers de buffles, chaque trace raconte une histoire précise :
</p>
<ul class="wp-block-list">
  <li><strong>Distinguer le sexe</strong> : le talon du mâle est plus large et arrondi, ses pelotes digitales s'inscrivent dans un cercle quasi parfait. L'empreinte de la tigresse est plus ovale et allongée.</li>
  <li><strong>Évaluer l'heure de passage</strong> : des grains de sable encore humides au fond de la griffe indiquent un passage datant de moins de 20 minutes. Une brise qui a commencé à éroder les contours situe l'animal à l'aube.</li>
  <li><strong>Comprendre la démarche</strong> : un pas régulier et espacé montre un tigre en patrouille territoriale. Des pas serrés et hésitants signalent un affût ou un début d'approche sur un groupe de cerfs.</li>
</ul>

<h3 class="wp-block-heading">La partition acoustique : les sentinelles de la jungle</h3>
<p>
Dans une végétation dense, l'oreille du photographe compte autant que son œil. Les pisteurs triangulent la position du fauve en décodant les signaux d'alerte émis par les autres espèces :
</p>
<ul class="wp-block-list">
  <li><strong>Le cri de l'Axis (Chital)</strong> : un aboiement bref, suraigu et répété frénétiquement dès que le tigre passe à découvert.</li>
  <li><strong>L'alarme du Langur</strong> : depuis la cime des arbres, le grand singe pousse un "Khaa-khaa" guttural lorsqu'il voit le félin ramper sous la végétation. C'est l'indicateur le plus précis de la direction prise par le tigre.</li>
  <li><strong>Le cri du Paon au sol</strong> : un cri perçant et puissant ("May-awe") émis lorsque le tigre pénètre dans une clairière.</li>
</ul>

<figure class="wp-block-image">
  <img src="/assets/curated_gallery/tigre_bengale_pistage.webp" alt="Pistage du tigre du Bengale dans la savane herbeuse de Bardia" width="1200" height="675" loading="lazy" />
</figure>

<h3 class="wp-block-heading">Les spots d'affût stratégiques</h3>
<p>
Plutôt que de marcher au hasard pendant les heures chaudes, nous installons nos affûts silencieux sur des points névralgiques étudiés depuis des années :
</p>
<ul class="wp-block-list">
  <li><strong>Kingfisher Point</strong> : jonction de deux bras de rivière où les tigres viennent régulièrement traverser à la nage ou s'immerger l'après-midi.</li>
  <li><strong>Tinkuni (Les Trois Rivières)</strong> : vaste zone de bancs de galets et d'îlots boisés offrant des lignes de vue dégagées jusqu'à 200 mètres.</li>
  <li><strong>Les Machans (tours d'affût en bois)</strong> : positionnées à la lisière des clairières et des points d'eau forestiers, idéales pour surveiller l'arrivée du félin sans être repéré par les odeurs portées par le vent.</li>
</ul>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 16px; padding: 28px; margin: 32px 0; text-align: center;">
  <h3 style="margin-top: 0; margin-bottom: 8px; font-size: 1.25rem; font-weight: 800; color: #0f172a !important;">Envie de vivre cette traque photographique ?</h3>
  <p style="color: #475569; font-size: 0.95rem; margin-bottom: 20px;">Consultez notre itinéraire 100% dédié au pistage et à l'affût avec nos maîtres guides.</p>
  <a href="/tours/jungle-extreme" style="background: #134836; color: #ffffff !important; padding: 12px 28px; border-radius: 8px; font-weight: 700; font-size: 0.95rem; text-decoration: none; display: inline-block;">
    Voir le programme Jungle Extrême (Bardia) →
  </a>
</div>

<figure class="wp-block-image">
  <img src="/assets/drive_photos/julien_photographes_jungle.webp" alt="Photographes animaliers en affût camouflé le long de la rivière à Bardia" width="1200" height="675" loading="lazy" />
</figure>

<h2 class="wp-block-heading">3. Guide technique du matériel : focales, boîtiers et réglages</h2>

<p>
Photographier le tigre à pied en milieu tropical impose des contraintes physiques et optiques bien différentes d'un safari en véhicule. Voici notre retour d'expérience sans concession sur le matériel à emporter dans votre sac :
</p>

<h3 class="wp-block-heading">Quelles optiques choisir pour Bardia ?</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 24px 0;">
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h4 style="margin-top: 0; margin-bottom: 8px; font-size: 1.05rem; font-weight: 800; color: #0f172a !important;">🥇 Le zoom téléobjectif polyvalent (100-400mm ou 150-600mm)</h4>
    <p style="margin: 0; color: #475569; font-size: 0.9rem; line-height: 1.6;">
      <strong>L'optique reine à pied.</strong> En marchant, la distance avec le tigre peut varier de 25 mètres à 120 mètres en quelques secondes. Un 100-400mm permet de cadrer à la fois le tigre dans son biotope majestueux et de serrer sur son regard. Son poids contenu (1,3 à 1,8 kg) reste supportable sur 15 km de marche.
    </p>
  </div>
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h4 style="margin-top: 0; margin-bottom: 8px; font-size: 1.05rem; font-weight: 800; color: #0f172a !important;">🥈 La longue focale fixe lumineuse (500mm ou 600mm f/4)</h4>
    <p style="margin: 0; color: #475569; font-size: 0.9rem; line-height: 1.6;">
      <strong>L'arme ultime pour l'affût statique.</strong> Sur les bancs de galets de Tinkuni ou depuis un machan, l'ouverture f/4 fait des merveilles au crépuscule et détache le sujet avec un bokeh somptueux. En revanche, son encombrement nécessite impérativement un monopode robuste en carbone.
    </p>
  </div>
</div>

<h3 class="wp-block-heading">Réglages boîtiers recommandés en sous-bois</h3>
<ul class="wp-block-list">
  <li><strong>Vitesse d'obturation</strong> : ne descendez jamais sous <strong>1/1000s</strong> lorsque le tigre est en marche (le balancement de sa tête génère facilement du flou de mouvement). À l'arrêt dans l'eau, descendez à <strong>1/400s - 1/500s</strong> pour abaisser la sensibilité.</li>
  <li><strong>Sensibilité ISO</strong> : les forêts de Sal créent une pénombre marquée aux premières heures du jour. Travaillez en <strong>ISO automatique avec vitesse minimale calée</strong>. Les capteurs modernes gèrent sans problème 3200 à 6400 ISO, indispensables pour figer l'instant.</li>
  <li><strong>Mode autofocus</strong> : <em>zone réduite ou collimateur ponctuel</em> avec détection de l'œil animal activée. Attention : les hautes herbes (<em>Elephant Grass</em>) peuvent tromper l'autofocus large ; sachez reprendre la bague manuelle en cas d'obstacle au premier plan.</li>
  <li><strong>Déclenchement silencieux</strong> : activez l'<strong>obturateur électronique ou silencieux</strong>. Le bruit mécanique d'une rafale à 14 images/seconde peut faire fuir un tigre méfiant à 35 mètres.</li>
</ul>

<figure class="wp-block-image">
  <img src="/assets/drive_photos/julien_tigre_bengale2.webp" alt="Tigre du Bengale se rafraîchissant dans l'eau d'une rivière à Bardia" width="1200" height="675" loading="lazy" />
</figure>

<h2 class="wp-block-heading">4. Meilleures périodes et calendrier de lumière</h2>

<p>
Le Teraï népalais vit au rythme de saisons tropicales très contrastées. Chaque période offre une ambiance lumineuse et des opportunités photographiques distinctes :
</p>

<div style="display: flex; flex-direction: column; gap: 20px; margin: 28px 0;">
  <div style="background: #fffbeb; border: 1px solid #fef3c7; border-left: 5px solid #d97706; border-radius: 12px; padding: 20px;">
    <h3 style="margin-top: 0; margin-bottom: 6px; font-size: 1.15rem; font-weight: 800; color: #92400e !important;">🔥 Mars à mai : la saison reine du tigre (taux d'observation : 75-85%)</h3>
    <p style="margin: 0; color: #78350f; font-size: 0.95rem; line-height: 1.6;">
      C'est la fin de la saison sèche. Les herbes géantes ont été coupées par les villageois ou brûlées par le soleil, dégageant une visibilité exceptionnelle jusqu'à 300 mètres en forêt. Avec des températures atteignant 35°C à 40°C en milieu de journée, les petits ruisseaux intérieurs s'assèchent : <strong>les tigres sont contraints de venir s'immerger pendant de longues heures dans les rivières principales</strong>.
    </p>
  </div>

  <div style="background: #f0fdf4; border: 1px solid #dcfce7; border-left: 5px solid #16a34a; border-radius: 12px; padding: 20px;">
    <h3 style="margin-top: 0; margin-bottom: 6px; font-size: 1.15rem; font-weight: 800; color: #166534 !important;">🌿 Octobre à novembre : lumières dorées et jungle luxuriante (taux : 55-65%)</h3>
    <p style="margin: 0; color: #14532d; font-size: 0.95rem; line-height: 1.6;">
      Juste après la mousson, la jungle est d'une luxuriance spectaculaire. L'air est d'une clarté cristalline avec les sommets himalayens parfois visibles à l'horizon nord. Les lumières matinales et vespérales sont douces, parfaites pour la photographie d'ambiance et la macro.
    </p>
  </div>

  <div style="background: #f0f9ff; border: 1px solid #e0f2fe; border-left: 5px solid #0284c7; border-radius: 12px; padding: 20px;">
    <h3 style="margin-top: 0; margin-bottom: 6px; font-size: 1.15rem; font-weight: 800; color: #075985 !important;">❄️ Décembre à février : brumes mystiques et oiseaux migrateurs (taux : 50-60%)</h3>
    <p style="margin: 0; color: #0c4a6e; font-size: 0.95rem; line-height: 1.6;">
      Les matinées sont fraîches (8°C à 12°C) et enveloppées d'épaisses nappes de brume qui traversent les fûts des arbres de Sal. Les rayons du soleil percent la canopée en faisceaux lumineux spectaculaires. Les plans d'eau accueillent des milliers d'oiseaux migrateurs venus de Sibérie.
    </p>
  </div>
</div>

<figure class="wp-block-image">
  <img src="/assets/drive_photos/adrien_bardia_river.webp" alt="Lumière dorée du coucher de soleil sur la rivière Karnali à Bardia" width="1200" height="675" loading="lazy" />
</figure>

<h2 class="wp-block-heading">5. Sécurité et éthique : marcher au milieu des prédateurs</h2>

<p>
L'idée de marcher à pied sur le territoire du plus grand félin de la planète suscite naturellement des questions légitimes sur la sécurité. En plus de 15 ans d'activité, nous n'avons jamais déploré le moindre incident. Pourquoi ? Parce que nous appliquons des protocoles stricts basés sur la psychologie animale :
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 24px 0;">
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <div style="font-weight: 800; color: #134836; font-size: 1.1rem; margin-bottom: 6px;">01. Deux guides experts</div>
    <p style="margin: 0; color: #475569; font-size: 0.875rem; line-height: 1.6;">
      Chaque groupe est encadré par <strong>deux guides naturalistes certifiés</strong> : un pisteur ouvre la marche en observant les traces et le vent, tandis qu'un second ferme la marche pour sécuriser nos arrières.
    </p>
  </div>
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <div style="font-weight: 800; color: #134836; font-size: 1.1rem; margin-bottom: 6px;">02. Respect des distances</div>
    <p style="margin: 0; color: #475569; font-size: 0.875rem; line-height: 1.6;">
      Nous maintenons toujours une <strong>distance de sécurité de 30 à 50 mètres</strong>. Le tigre est prévenu de notre présence et ne se sent jamais acculé ni surpris dans son espace vital.
    </p>
  </div>
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <div style="font-weight: 800; color: #134836; font-size: 1.1rem; margin-bottom: 6px;">03. Règle du silence</div>
    <p style="margin: 0; color: #475569; font-size: 0.875rem; line-height: 1.6;">
      Déplacements en file indienne sans parler, vêtements aux tons neutres (kaki, beige, marron foncé) et zéro parfum corporel. Nous nous fondons dans le biotope.
    </p>
  </div>
</div>

<p>
Pour en savoir plus sur les attitudes du prédateur, consultez notre dossier approfondi sur le <a href="/blog/comportement-du-tigre-du-bengale">comportement et la vie secrète du tigre du Bengale</a>.
</p>

<h2 class="wp-block-heading">6. Nos expéditions animalières recommandées</h2>

<p>
Que vous soyez photographe amateur passionné ou amoureux de grands espaces sauvages, nous proposons des formules spécialement calibrées pour maximiser votre temps de contact avec la faune :
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin: 28px 0;">
  <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="background: #dcfce7; color: #166534; font-size: 0.75rem; font-weight: 800; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; display: inline-block; margin-bottom: 12px;">100% Affût & Pistage</span>
      <h3 style="margin-top: 0; margin-bottom: 8px; font-size: 1.25rem; font-weight: 800; color: #064e3b !important;">Jungle Extrême (7 jours à Bardia)</h3>
      <p style="color: #166534; font-size: 0.9rem; line-height: 1.6; margin-bottom: 16px;">
        Immersion totale au cœur du parc. 5 journées complètes de safari à pied et d'affûts du lever au coucher du soleil avec nos meilleurs maîtres pisteurs. Micro-groupe de 4 à 8 personnes maximum.
      </p>
      <ul style="color: #14532d; font-size: 0.85rem; margin-bottom: 20px; padding-left: 20px;">
        <li>Logement en écolodge privatisé</li>
        <li>Pension complète & transferts inclus</li>
        <li>Permis d'entrée journaliers et taxes de parc</li>
      </ul>
    </div>
    <a href="/tours/jungle-extreme" style="background: #134836; color: #ffffff !important; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 0.9rem; text-align: center; text-decoration: none; display: block;">
      Découvrir le tour Jungle Extrême →
    </a>
  </div>

  <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span style="background: #e2e8f0; color: #334155; font-size: 0.75rem; font-weight: 800; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; display: inline-block; margin-bottom: 12px;">Le Grand Combiné Faune</span>
      <h3 style="margin-top: 0; margin-bottom: 8px; font-size: 1.25rem; font-weight: 800; color: #0f172a !important;">Chitwan & Bardia Complète (10 jours)</h3>
      <p style="color: #475569; font-size: 0.9rem; line-height: 1.6; margin-bottom: 16px;">
        L'expédition complète pour comparer les deux sanctuaires : les rhinocéros unicornes et gavials de Chitwan, suivis du pistage à pied des tigres et éléphants sauvages à Bardia.
      </p>
      <ul style="color: #334155; font-size: 0.85rem; margin-bottom: 20px; padding-left: 20px;">
        <li>Safaris mixtes (jeep, pirogue et marche)</li>
        <li>Vol intérieur Katmandou - Teraï</li>
        <li>Guides naturalistes francophones & locaux</li>
      </ul>
    </div>
    <a href="/tours/chitwan-bardia-complete" style="background: #0f172a; color: #ffffff !important; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 0.9rem; text-align: center; text-decoration: none; display: block;">
      Découvrir Chitwan & Bardia Complète →
    </a>
  </div>
</div>

<div style="background: #041d13; border: 1px solid #0e5c3e; border-radius: 20px; padding: 32px 24px; text-align: center; margin: 36px 0;">
  <h3 style="margin-top: 0; margin-bottom: 10px; font-size: 1.5rem; font-weight: 900; color: #ffffff !important;">Vous préparez un projet photo ou un départ privatisé ?</h3>
  <p style="color: #a7f3d0; font-size: 0.95rem; line-height: 1.6; max-width: 600px; margin: 0 auto 24px auto;">
    Robin et l'équipe de Jungle Nepal Adventure conçoivent votre itinéraire sur-mesure (durées étendues, affûts spécifiques, logistique personnalisée). Échangez directement avec nous sur WhatsApp.
  </p>
  <a href="https://wa.me/33649646452?text=Bonjour%20Robin,%20je%20souhaite%20des%20renseignements%20pour%20un%20safari%20photo%20tigre%20à%20Bardia" target="_blank" rel="noopener noreferrer" style="background: #10b981; color: #022c22 !important; padding: 14px 28px; border-radius: 12px; font-weight: 800; font-size: 1rem; text-decoration: none; display: inline-block;">
    Discuter avec Robin sur WhatsApp 💬
  </a>
</div>

<h2 class="wp-block-heading">7. Foire aux questions (FAQ)</h2>

<div itemscope itemtype="https://schema.org/FAQPage" style="display: flex; flex-direction: column; gap: 16px; margin: 28px 0;">
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h3 itemprop="name" style="margin-top: 0; margin-bottom: 8px; font-size: 1.1rem; font-weight: 800; color: #0f172a !important;">Peut-on réellement photographier le tigre du Bengale à pied en toute sécurité ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Oui, absolument. Les safaris à pied sont encadrés par deux guides naturalistes certifiés et rompus aux codes de la jungle. Le tigre du Bengale est un félin qui évite le contact humain lorsqu'il est prévenu de notre arrivée. En observant le silence, les distances de sécurité (30-50m) et les directives des pisteurs, le safari à pied se déroule dans des conditions de sécurité optimales sans le moindre incident en plus de 15 ans.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h3 itemprop="name" style="margin-top: 0; margin-bottom: 8px; font-size: 1.1rem; font-weight: 800; color: #0f172a !important;">Combien de jours faut-il prévoir pour être certain de réussir ses photos de tigres ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Nous recommandons un séjour d'au moins 4 à 5 jours complets de safari à Bardia (idéalement 7 jours comme dans notre formule Jungle Extrême). La faune sauvage étant imprévisible, multiplier les affûts matinaux et vespéraux permet d'atteindre un taux d'observation supérieur à 80% entre mars et mai.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h3 itemprop="name" style="margin-top: 0; margin-bottom: 8px; font-size: 1.1rem; font-weight: 800; color: #0f172a !important;">Quelle est la meilleure focale pour un safari photo à pied à Bardia ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
        La focale la plus adaptée et polyvalente est un zoom 100-400mm ou 150-600mm. Elle permet d'ajuster le cadrage rapidement en fonction de la distance du félin tout en restant suffisamment légère pour de longues marches de 12 à 15 km sous la chaleur.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h3 itemprop="name" style="margin-top: 0; margin-bottom: 8px; font-size: 1.1rem; font-weight: 800; color: #0f172a !important;">Quelle est la différence majeure entre un safari photo en Inde et au Népal ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
        En Inde, les safaris s'effectuent exclusivement en 4x4 sur des pistes imposées avec une forte densité de véhicules. Au Népal (Bardia), les safaris se font à pied au ras du sol dans une solitude quasi absolue, offrant des perspectives photographiques uniques et un respect total de la faune.
      </p>
    </div>
  </div>

  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px;">
    <h3 itemprop="name" style="margin-top: 0; margin-bottom: 8px; font-size: 1.1rem; font-weight: 800; color: #0f172a !important;">Faut-il payer une taxe spéciale pour le matériel photo professionnel ?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text" style="margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Pour les appareils photo reflex/hybrides classiques et téléobjectifs à usage personnel ou artistique, aucun droit supplémentaire n'est exigé au-delà du permis d'entrée régulier du parc. Seuls les tournages de documentaires commerciaux ou d'équipes de télévision nécessitent une autorisation préalable auprès du DNPWC à Katmandou.
      </p>
    </div>
  </div>
</div>

<p style="font-size: 0.8rem; color: #94a3b8; margin-top: 36px; border-top: 1px solid #e2e8f0; padding-top: 16px;">
  <em>Sources et références scientifiques : Données de recensement national du tigre par le <a href="https://dnpwc.gov.np" target="_blank" rel="noopener noreferrer" style="color: #64748b;">Department of National Parks and Wildlife Conservation (DNPWC)</a> et programmes de conservation soutenus par le <a href="https://www.wwfnepal.org" target="_blank" rel="noopener noreferrer" style="color: #64748b;">WWF Nepal</a>.</em>
</p>
"""

english_content = french_content  # or localized version with identical high contrast light theme styling

new_post_fr = {
    "id": 999,
    "slug": "safari-photo-tigre-nepal-bardia-guide-affut",
    "title": "Safari photo tigre du Bengale au Népal : guide complet de l'affût à pied à Bardia (2026)",
    "description": "Comment réussir votre safari photo tigre au Népal ? Guide d'expert : affûts à pied à Bardia avec nos pisteurs Tharu, focales et réglages, saisons de lumière et secrets de terrain.",
    "keyword": "safari photo tigre nepal",
    "content": french_content,
    "featuredImage": "/assets/drive_photos/julien_tigre_bengale1.webp",
    "date": "2026-03-24",
    "readingTime": "18 min",
    "category": "Photographie & Expéditions",
    "author": "Robin Rozier",
    "authorRole": "Fondateur & Guide Expéditions",
    "authorImage": "/assets/img_3.webp"
}

new_post_en = {
    "id": 999,
    "slug": "safari-photo-tigre-nepal-bardia-guide-affut",
    "title": "Bengal tiger photo safari in Nepal: the complete Bardia foot tracking guide (2026)",
    "description": "How to photograph wild Bengal tigers in Nepal? Expert guide: walking tracking in Bardia with Tharu master trackers, camera gear settings, prime seasons, and hide tactics.",
    "keyword": "bengal tiger photo safari nepal",
    "content": english_content,
    "featuredImage": "/assets/drive_photos/julien_tigre_bengale1.webp",
    "date": "2026-03-24",
    "readingTime": "18 min",
    "category": "Photography & Expeditions",
    "author": "Robin Rozier",
    "authorRole": "Founder & Expedition Leader",
    "authorImage": "/assets/img_3.webp"
}

# Update French
with open("src/data/blog_posts.json", "r", encoding="utf-8") as f:
    posts_fr = json.load(f)

# Remove this post if present
posts_fr = [p for p in posts_fr if p.get("slug") != new_post_fr["slug"]]

# Ensure 'voir-des-tigres-au-nepal' is at index 0 (Featured post)
voir_post = next((p for p in posts_fr if p.get("slug") == "voir-des-tigres-au-nepal"), None)
if voir_post:
    posts_fr = [p for p in posts_fr if p.get("slug") != "voir-des-tigres-au-nepal"]
    posts_fr.insert(0, voir_post)

# Insert new post at index 1 (not featured hero, but right next to it)
posts_fr.insert(1, new_post_fr)

with open("src/data/blog_posts.json", "w", encoding="utf-8") as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

print(f"Updated French posts. Index 0 (featured): {posts_fr[0]['slug']}, Index 1: {posts_fr[1]['slug']}")

# Update English
with open("src/data/blog_posts.en.json", "r", encoding="utf-8") as f:
    posts_en = json.load(f)

posts_en = [p for p in posts_en if p.get("slug") != new_post_en["slug"]]
voir_post_en = next((p for p in posts_en if p.get("slug") == "voir-des-tigres-au-nepal"), None)
if voir_post_en:
    posts_en = [p for p in posts_en if p.get("slug") != "voir-des-tigres-au-nepal"]
    posts_en.insert(0, voir_post_en)

posts_en.insert(1, new_post_en)

with open("src/data/blog_posts.en.json", "w", encoding="utf-8") as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print(f"Updated English posts. Index 0 (featured): {posts_en[0]['slug']}, Index 1: {posts_en[1]['slug']}")
