import json
import os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    all_tours = json.load(f)

# Load the destination articles
destinations_data = {
    "bardia": {
        "slug": "bardia",
        "name": "Parc national de Bardia",
        "name_en": "Bardia National Park",
        "tagline": "Tigres du Bengale, éléphants sauvages et safaris à pied exclusifs",
        "tagline_en": "Bengal Tigers, Wild Elephants & Exclusive Walking Safaris",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
        "intro_p1": "Avant sa création officielle en 1988, le parc national de Bardia était une réserve de chasse royale dédiée à la monarchie népalaise. Sa transformation en parc national a marqué une étape clé dans la protection de la biodiversité du Teraï occidental. Aujourd'hui, Bardia est le sanctuaire le plus vaste et le plus intact du Népal, offrant une nature brute et préservée, loin du tourisme de masse.",
        "intro_p2": "Aujourd’hui, le parc national de Bardia est un véritable sanctuaire de la faune sauvage au Népal. Il abrite des espèces emblématiques comme le tigre du Bengale, l'éléphant d'Asie sauvage, le rhinocéros unicorne, ainsi que le rare dauphin d'eau douce du Gange (sur les rivières Karnali et Geruwa). On y recense également plus de 400 espèces d’oiseaux, des léopards, des cerfs axis et de grands gavials préhistoriques.",
        "intro_p3": "Vivre une expérience immersive au cœur de la jungle de Bardia se fait à travers différents modes d'approche respectueux : safaris à pied silencieux avec nos maîtres pisteurs natifs (tracking du tigre du Bengale), safaris en jeep 4x4 ouverte pour explorer les zones profondes et la vallée secrète de Babai, balades en canoë traditionnel sur les rivières pour observer les gavials, et bivouacs sauvages sous tente en jungle.",
        "fiche_technique": [
            {"label": "Meilleure période", "value": "D'octobre à mai (Pic d'observation des tigres aux points d'eau entre mars et mai)"},
            {"label": "Mode d'exploration", "value": "Safaris silencieux à pied (walking safari), affûts, jeep 4x4 ouverte et canoë traditionnel"},
            {"label": "Encadrement d'élite", "value": "2 maîtres pisteurs natifs certifiés par groupe (dont Pawan & Kiran, ex-BBC Wildlife)"},
            {"label": "Format de groupe", "value": "Micro-groupes exclusifs de 4 à 8 explorateurs max pour garantir le silence"},
            {"label": "Hébergement", "value": "Éco-lodges de brousse en bordure de parc & campements sauvages en tente à Babai"}
        ],
        "culture_badge": "Gardiens de la forêt",
        "culture_title": "La communauté Tharu & l'harmonie ancestrale avec la jungle",
        "culture_desc": "Les Tharus sont les gardiens indigènes de Bardia. Vivant en lisière du sanctuaire depuis des siècles, ils possèdent une connaissance intime des plantes médicinales, des pistes animales et des équilibres sacrés de la forêt. Leurs maisons traditionnelles, bâties en terre, paille et bambou, s'intègrent parfaitement dans les paysages. Nos séjours soutiennent directement ces villages locaux.",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Tharu-danse.png"
        ],
        "matching_slugs": ["bardia-explorateur", "babai-special", "bardia-babai-camping", "bardia-nuit-sauvage", "jungle-extreme", "nepal-sauvage", "chitwan-bardia-complete", "rara-lake-bardia", "rafting-safari", "nepal-immersion-totale"]
    },
    "chitwan": {
        "slug": "chitwan",
        "name": "Parc national de Chitwan",
        "name_en": "Chitwan National Park",
        "tagline": "Rhinocéros unicornes, pirogues sur la Rapti et culture Tharu",
        "tagline_en": "One-Horned Rhinos, Rapti River Canoes & Tharu Culture",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "intro_p1": "Classé au patrimoine mondial de l’UNESCO en 1984, le parc national de Chitwan abrite l’une des faunes sauvages les plus impressionnantes d’Asie. C'est le premier parc national créé au Népal en 1973. Il est considéré mondialement comme le meilleur endroit pour observer le grand rhinocéros indien à une corne (Rhinoceros unicornis) évoluant librement dans son habitat naturel de forêts de sal et de hautes prairies alluviales.",
        "intro_p2": "Entre safaris en jeep, marches guidées d'observation dans la jungle et descentes paisibles en pirogue traditionnelle sur la rivière Rapti au lever du soleil, chaque activité offre une immersion directe au contact de la faune. Ce décor sauvage et préservé fait de Chitwan un lieu magique où vous croiserez des hardes de cervidés, des crocodiles gavials se chauffant sur les berges de sable, ainsi que des martins-pêcheurs et calaos colorés.",
        "intro_p3": "L’un des grands atouts du parc national de Chitwan est son accessibilité idéale. Situé à seulement quelques heures de route de Katmandou ou de Pokhara (et desservi par l'aéroport de Bharatpur), il permet une halte nature de qualité sans longs trajets éprouvants. Grâce à nos éco-lodges de charme partenaires et à nos guides naturalistes, Chitwan est parfait aussi bien pour les familles que pour les explorateurs avides de grands espaces.",
        "fiche_technique": [
            {"label": "Meilleure période", "value": "D'octobre à avril (Climat très doux, excellente visibilité sur la faune)"},
            {"label": "Mode d'exploration", "value": "Pirogues traditionnelles sur la Rapti, jeeps 4x4 ouvertes et safaris à pied"},
            {"label": "Espèces phares", "value": "Rhinocéros unicorne (+690 individus), gavials du Gange, tigres, calaos"},
            {"label": "Format de groupe", "value": "Micro-groupes de 4 à 8 personnes (ou départs privatisés famille)"},
            {"label": "Hébergement", "value": "Éco-lodges de charme Tharu éco-responsables avec piscine et jardin tropical"}
        ],
        "culture_badge": "Traditions du Teraï",
        "culture_title": "La culture Tharu & la vie rurale au bord des rivières",
        "culture_desc": "La communauté Tharu de Chitwan vit en symbiose avec les cours d'eau et les forêts de sal. Leurs danses rituelles au bâton, leurs fresques murales décoratives et leurs méthodes de pêche artisanale à la nasse témoignent d'un patrimoine vivant exceptionnel que nous découvrons lors de nos haltes culturelles.",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png"
        ],
        "matching_slugs": ["chitwan-culture", "chitwan-bardia-complete", "nepal-immersion-totale"]
    },
    "suklaphanta": {
        "slug": "suklaphanta",
        "name": "Parc national de Suklaphanta",
        "name_en": "Suklaphanta National Park",
        "tagline": "Les plus grandes hardes de cerfs des marais au monde & ouest sauvage",
        "tagline_en": "The World's Largest Swamp Deer Herds & Untamed Wild West",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
        "intro_p1": "Situé dans l’extrême ouest du Népal, à la frontière de l’Inde, le parc national de Suklaphanta est l’un des joyaux les plus sauvages et les moins fréquentés du pays. Encore totalement préservé des circuits touristiques classiques, Suklaphanta offre une expérience de safari pur, paisible et authentique.",
        "intro_p2": "La renommée de Suklaphanta repose avant tout sur sa vaste prairie ouverte (Phanta), la plus grande d'Asie du Sud (54 km²). C'est ici que vit la plus importante harde de cerfs des marais (Barasingha) au monde, comptant plus de 2 000 individus. Voir des centaines de grands mâles aux bois majestueux traverser la brume matinale est un spectacle inoubliable. Le parc est également un habitat vital pour le tigre du Bengale, le léopard d'Asie, les éléphants sauvages et le rare florican du Bengale.",
        "intro_p3": "Explorer Suklaphanta, c’est faire le choix d’un safari brut, hors des sentiers battus. Accompagnés de guides locaux expérimentés, vous découvrez une nature où le silence n'est rompu que par les bruits de la jungle. Visiter Suklaphanta, c'est aussi soutenir concrètement un modèle de conservation communautaire pionnier au Népal.",
        "fiche_technique": [
            {"label": "Meilleure période", "value": "De novembre à mai (Prairies dégagées, grands rassemblements d'animaux)"},
            {"label": "Mode d'exploration", "value": "Pistes 4x4 ouvertes, tours d'affût panoramiques et marches guidées"},
            {"label": "Faune exceptionnelle", "value": "+2000 cerfs des marais, hardes d'éléphants sauvages, tigres et léopards"},
            {"label": "Fréquentation", "value": "Quasi-nulle (Sanctuaire 100% exclusif sans aucune foule touristique)"},
            {"label": "Hébergement", "value": "Campements de brousse confortables & lodges locaux authentiques"}
        ],
        "culture_badge": "Ouest Sauvage",
        "culture_title": "Villages ruraux du Teraï Occidental",
        "culture_desc": "L'extrême ouest népalais est resté fidèle aux rythmes agricoles traditionnels. Les communautés locales perpétuent un mode de vie respectueux des cycles de la nature et vous accueillent avec une bienveillance sincère et chaleureuse.",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
        ],
        "matching_slugs": ["nepal-sauvage", "nepal-immersion-totale", "jungle-extreme"]
    },
    "annapurna": {
        "slug": "annapurna",
        "name": "Les Annapurna & Pokhara",
        "name_en": "Annapurna Range & Pokhara",
        "tagline": "Des treks mythiques entre hauts sommets, lacs sacrés et cultures montagnardes",
        "tagline_en": "Mythical Treks Between Sacred Peaks, Lakes & Alpine Villages",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
        "intro_p1": "La région de l’Annapurna est l’une des zones de trekking les plus spectaculaires et variées de la planète. Située à courte distance de la charmante ville de Pokhara, elle permet de passer en quelques jours des vallées subtropicales luxuriantes peuplées de bananiers aux forêts de rhododendrons géants, avant d'atteindre les balcons alpins face aux géants himalayens comme le Machapuchare (le célèbre mont Fish Tail), le Dhaulagiri et l'Annapurna Sud.",
        "intro_p2": "Le trekking dans la région de l’Annapurna ne se résume pas aux panoramas vertigineux — il est avant tout une rencontre humaine chaleureuse. Au fil des sentiers ancestraux, les nuits se passent dans de confortables tea houses familiales ou chez l’habitant. On y partage le traditionnel Dal Bhat réparateur au coin du poêle tout en découvrant les coutumes et la générosité des montagnards Gurung.",
        "intro_p3": "Les deux périodes privilégiées pour arpenter l'Annapurna sont l'automne (octobre à décembre), avec une visibilité cristalline sur les sommets enneigés après la mousson, et le printemps (mars à mai), période magique où les rhododendrons fleurissent en rouge et rose sur les pentes des montagnes.",
        "fiche_technique": [
            {"label": "Meilleure période", "value": "Octobre à Décembre (Ciel limpide) & Mars à Mai (Floraison rhododendrons)"},
            {"label": "Niveau de marche", "value": "4 à 7 heures de marche par jour à un rythme régulier et accessible"},
            {"label": "Points de vue", "value": "Poon Hill, Balcons des Annapurna, Vallée sacrée de Pokhara & Lac Phewa"},
            {"label": "Hébergement", "value": "Tea houses familiales de montagne chaleureuses & hôtels confortables à Pokhara"},
            {"label": "Encadrement", "value": "Guides francophones diplômés et porteurs locaux respectés et assurés"}
        ],
        "culture_badge": "Himalaya Sacré",
        "culture_title": "Villages Gurung & Sérénité de Pokhara",
        "culture_desc": "Perchés sur les crêtes verdoyantes, les villages Gurung de Ghandruk et Landruk dévoilent leurs maisons de pierre sèche aux toits d'ardoise. À Pokhara, les rives du lac Phewa offrent une halte apaisante face aux reflets du mont Machapuchare.",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg"
        ],
        "matching_slugs": ["rara-lake-bardia", "immersion-spirituelle", "carnet-de-voyage"]
    },
    "katmandou": {
        "slug": "katmandou",
        "name": "Vallée de Katmandou",
        "name_en": "Kathmandu Valley",
        "tagline": "Un chaos vivant et fascinant, temples sacrés et cités royales classées UNESCO",
        "tagline_en": "A Living & Spiritual Marvel, Sacred Temples & UNESCO Royal Cities",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "intro_p1": "Au premier abord, Katmandou peut sembler déroutante et vibrante. Mais laissez-lui un peu de temps, et elle finit par vous happer totalement. Entre ruelles pavées millénaires chargées d’histoire, senteurs d'encens de santal et toits-terrasses avec vue sur les stupas dorés, Katmandou est une ville brute et profondément vivante où le sacré côtoie le quotidien à chaque coin de rue.",
        "intro_p2": "La vallée de Katmandou abrite sept sites classés au patrimoine mondial de l’UNESCO : le grand stupa blanc de Boudhanath, cœur spirituel des bouddhistes tibétains ; la colline sacrée de Swayambhunath (le Monkey Temple) ; le temple hindou millénaire de Pashupatinath ; et les trois places royales historiques de Durbar Square (Katmandou, Patan et la cité médiévale préservée de Bhaktapur).",
        "intro_p3": "Pour tous nos voyageurs, Katmandou est bien plus qu’une simple escale technique. C’est ici que Robin et nos équipes vous accueillent dès votre atterrissage à l'aéroport international pour un briefing personnalisé autour d'un thé népalais, avant de vous équiper et de vous lancer vers les grands territoires sauvages du Népal.",
        "fiche_technique": [
            {"label": "Meilleure période", "value": "Accessible et agréable toute l'année (Climat doux à 1 400 m d'altitude)"},
            {"label": "Trésors culturels", "value": "7 sites UNESCO : Boudhanath, Swayambhunath, Pashupatinath, Bhaktapur, Patan"},
            {"label": "Expériences clés", "value": "Méditation matinale, artisanat Newar, toits-terrasses et marchés aux épices"},
            {"label": "Accueil exclusif", "value": "Prise en charge personnalisée à l'aéroport par Robin & briefing privé"},
            {"label": "Hébergement", "value": "Hôtels de charme traditionnels au cœur des quartiers historiques calmes"}
        ],
        "culture_badge": "Cœur Spirituel",
        "culture_title": "L'artisanat Newar & les cités royales médiévales",
        "culture_desc": "La vallée de Katmandou est le berceau du peuple Newar, maîtres sculpteurs sur bois, fondeurs de bronze et bâtisseurs de pagodes. Flâner dans les cours intérieures de Patan et Bhaktapur est un véritable voyage dans le temps.",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
        ],
        "matching_slugs": ["tiji-mustang", "immersion-spirituelle", "carnet-de-voyage", "nepal-sauvage", "nepal-immersion-totale", "rafting-safari"]
    }
}

for slug, d in destinations_data.items():
    # Build FR
    fiche_rows_fr = "\n".join([f"""        <div>
          <p class="text-xs font-bold uppercase tracking-wider text-slate-400">{item['label']}</p>
          <p class="font-bold text-slate-900 mt-0.5">{item['value']}</p>
        </div>""" for item in d['fiche_technique']])

    gallery_cols_fr = "\n".join([f"""        <div onclick="openLightbox({i})" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="{img}" alt="{d['name']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>""" for i, img in enumerate(d['gallery'])])

    matching_slugs_json = json.dumps(d['matching_slugs'])

    fr_astro = f"""---
import Layout from '../../layouts/Layout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import toursData from '../../data/tours.json';

const matchingTours = toursData.filter(t => {matching_slugs_json}.includes(t.slug));
---

<Layout 
  title="{d['name']} | Destinations Jungle Nepal Adventure"
  description="{d['intro_p1'][:150]}"
  image="{d['hero_image']}"
  lang="fr"
  isDarkHeader={{true}}
>
  <Header lang="fr" currentPath="/destinations/{slug}.html" />

  <!-- HERO BANNER DESTINATION -->
  <div class="relative min-h-[50vh] flex items-center justify-center pt-32 pb-20 px-4 bg-slate-950 text-white overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img src="{d['hero_image']}" alt="{d['name']}" class="w-full h-full object-cover opacity-35 scale-105 filter brightness-85" />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/40"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center space-y-4">
      <nav class="flex items-center justify-center gap-2 text-xs text-slate-300 font-semibold mb-2">
        <a href="/index.html" class="hover:text-white">Accueil</a>
        <span>›</span>
        <a href="/destinations.html" class="hover:text-white">Destinations</a>
        <span>›</span>
        <span class="text-amber-300 font-bold">{d['name']}</span>
      </nav>

      <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/20 text-[#10b981] border border-emerald-500/30 text-xs font-black uppercase tracking-widest">
        <span>🇳🇵</span> Territoire Sauvage du Népal
      </span>
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-tight">
        {d['name']}
      </h1>
      <p class="text-base sm:text-xl text-slate-200 max-w-2xl mx-auto font-medium leading-relaxed drop-shadow">
        {d['tagline']}
      </p>
    </div>
  </div>

  <!-- MAIN CONTAINER (LAYOUT D'ORIGINE AVEC FICHE TECHNIQUE À DROITE) -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 font-sans space-y-16">
    
    <!-- 1. GRILLE 2 COLONNES : TEXTE COMPLET (GAUCHE) & FICHE TECHNIQUE (DROITE) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
      
      <!-- Colonne Gauche : 100% Contenu Texte Officiel junglenepal.com -->
      <div class="lg:col-span-7 space-y-6">
        <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">Immersion Sauvage</span>
        <h2 class="text-2xl sm:text-4xl font-black text-slate-950 tracking-tight leading-tight">
          Explorer {d['name']}
        </h2>
        <div class="text-slate-700 text-base leading-relaxed space-y-4 font-normal">
          <p>{d['intro_p1']}</p>
          <p>{d['intro_p2']}</p>
          <p>{d['intro_p3']}</p>
        </div>
      </div>

      <!-- Colonne Droite : Fiche Pratique / Fiche Technique du Lieu -->
      <div class="lg:col-span-5 bg-white rounded-3xl p-7 sm:p-8 border border-slate-200/90 shadow-xl space-y-6 sticky top-28">
        <h3 class="font-black text-xl text-slate-950 pb-3 border-b border-slate-100 flex items-center gap-2">
          <svg class="w-5 h-5 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <span>Fiche pratique & technique</span>
        </h3>
        
        <div class="space-y-4 text-sm">
{fiche_rows_fr}
        </div>

        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20{d['name']}" target="_blank" rel="noopener noreferrer" class="block w-full text-center py-3.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/30 hover:scale-[1.02] active:scale-95 transition-all">
          Poser une question sur {d['name']} →
        </a>
      </div>

    </div>

    <!-- 2. ENCART CULTURE LOCALE & POPULATIONS -->
    <div class="p-8 sm:p-12 rounded-3xl bg-safari-100 border border-slate-200 space-y-4">
      <div class="max-w-3xl space-y-3">
        <span class="inline-block text-xs font-black uppercase tracking-widest text-[#0e8354] bg-white px-3.5 py-1 rounded-full border border-slate-200 shadow-sm">
          {d['culture_badge']}
        </span>
        <h3 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">
          {d['culture_title']}
        </h3>
        <p class="text-slate-700 text-sm sm:text-base leading-relaxed font-normal">
          {d['culture_desc']}
        </p>
      </div>
    </div>

    <!-- 3. GALERIE PHOTO IMMERSIVE (4 PHOTOS HD AVEC LIGHTBOX) -->
    <div class="space-y-6">
      <div>
        <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Photographies du terrain</span>
        <h3 class="font-black text-2xl sm:text-3xl text-slate-950">Aperçu visuel de {d['name']}</h3>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
{gallery_cols_fr}
      </div>
    </div>

    <!-- 4. CIRCUITS ASSOCIÉS À CETTE DESTINATION -->
    <div class="space-y-8 pt-8 border-t border-slate-200">
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Saison 2026/2027</span>
          <h3 class="font-black text-2xl sm:text-4xl text-slate-950">Les séjours immersifs à {d['name']}</h3>
          <p class="text-slate-600 text-sm mt-1">Départs garantis en micro-groupes. Cliquez sur un circuit pour consulter le programme jour par jour.</p>
        </div>
        <a href="/index.html#prochains-departs" class="text-xs font-black text-[#0e8354] hover:underline shrink-0">
          Voir tous les 14 séjours →
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {{matchingTours.map((tour) => (
          <div 
            class="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col group cursor-pointer"
            onclick={{`window.location.href='/tours/${{tour.slug}}.html'`}}
          >
            <!-- Photo Hero -->
            <div class="relative h-60 overflow-hidden bg-slate-900">
              <img 
                src={{tour.images[0]}} 
                alt={{tour.title}} 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-black/20"></div>

              <div class="absolute top-4 left-4 right-4 flex items-center justify-between">
                <span class="px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-300 border border-amber-300/30 text-xs font-black">
                  {{tour.badge}}
                </span>
                <span class="px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white text-xs font-bold">
                  4–8 pers.
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 text-white">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-200">
                  <span>🕒 {{tour.duration}}</span>
                  <span>•</span>
                  <span class="text-amber-300">★ {{tour.rating}} ({{tour.reviews}} avis)</span>
                </div>
              </div>
            </div>

            <!-- Card Body -->
            <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">{{tour.style}}</span>
                <h3 class="font-black text-xl text-slate-950 mt-1 leading-snug group-hover:text-[#0e8354] transition-colors">
                  {{tour.title}}
                </h3>
                <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed font-normal">
                  {{tour.overview}}
                </p>
              </div>

              <!-- Price & CTA -->
              <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <span class="text-[10px] font-extrabold uppercase text-slate-400 block">À partir de</span>
                  <div class="flex items-baseline gap-2">
                    <span class="font-black text-2xl text-slate-950 tracking-tight">{{tour.price}}</span>
                    {{tour.originalPrice && (
                      <span class="text-xs text-slate-400 line-through font-bold">{{tour.originalPrice}}</span>
                    )}}
                  </div>
                </div>

                <a 
                  href={{`/tours/${{tour.slug}}.html`}}
                  class="px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/30 group-hover:shadow-lg hover:scale-105 transition-all"
                >
                  Voir le séjour →
                </a>
              </div>

            </div>
          </div>
        ))}}
      </div>
    </div>

  </main>

  <Footer lang="fr" />

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 bg-black/95 backdrop-blur-xl z-50 hidden opacity-0 transition-opacity duration-300 flex items-center justify-center p-4">
    <div class="absolute top-6 left-6 right-6 flex items-center justify-between text-white z-10">
      <div id="lightbox-counter" class="bg-white/10 backdrop-blur-md px-4 py-1.5 rounded-full text-xs font-extrabold border border-white/20">
        1 / 4
      </div>
      <button onclick="closeLightbox()" class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center text-white transition-all hover:scale-105 active:scale-95 cursor-pointer">
        ✕
      </button>
    </div>

    <button onclick="prevLightboxImage(event)" class="absolute left-4 sm:left-8 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-20 shadow-2xl cursor-pointer">
      ‹
    </button>
    <button onclick="nextLightboxImage(event)" class="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-20 shadow-2xl cursor-pointer">
      ›
    </button>

    <div class="relative max-w-5xl max-h-[85vh] flex items-center justify-center">
      <img id="lightbox-image" src="" alt="Photo agrandie" class="max-w-full max-h-[85vh] object-contain rounded-2xl shadow-2xl transition-all duration-300" />
    </div>
  </div>

  <script is:inline>
    const galleryImages = {json.dumps(d['gallery'])};
    let currentImageIndex = 0;

    window.openLightbox = function(index) {{
      currentImageIndex = index;
      updateLightboxContent();
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('hidden');
      setTimeout(() => {{
        modal.classList.remove('opacity-0');
        modal.classList.add('opacity-100');
      }}, 10);
      document.body.style.overflow = 'hidden';
    }};

    window.closeLightbox = function() {{
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('opacity-100');
      modal.classList.add('opacity-0');
      setTimeout(() => {{
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }}, 300);
    }};

    function updateLightboxContent() {{
      const img = document.getElementById('lightbox-image');
      const counter = document.getElementById('lightbox-counter');
      if (img && galleryImages[currentImageIndex]) {{
        img.src = galleryImages[currentImageIndex];
      }}
      if (counter) {{
        counter.textContent = (currentImageIndex + 1) + ' / ' + galleryImages.length;
      }}
    }}

    window.prevLightboxImage = function(e) {{
      if (e) e.stopPropagation();
      currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length;
      updateLightboxContent();
    }};

    window.nextLightboxImage = function(e) {{
      if (e) e.stopPropagation();
      currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
      updateLightboxContent();
    }};

    document.addEventListener('keydown', (e) => {{
      const modal = document.getElementById('lightbox-modal');
      if (modal && !modal.classList.contains('hidden')) {{
        if (e.key === 'ArrowLeft') window.prevLightboxImage();
        if (e.key === 'ArrowRight') window.nextLightboxImage();
        if (e.key === 'Escape') window.closeLightbox();
      }}
    }});
  </script>
</Layout>
"""

    with open(f"/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/{slug}.astro", 'w', encoding='utf-8') as f:
        f.write(fr_astro)

    # Build EN
    en_astro = fr_astro.replace("lang=\"fr\"", "lang=\"en\"").replace("currentPath=\"/destinations/", "currentPath=\"/en/destinations/")
    en_astro = en_astro.replace("from '../../", "from '../../../")
    en_astro = en_astro.replace("Accueil", "Home")
    en_astro = en_astro.replace("Territoire Sauvage du Népal", "Wild Sanctuary of Nepal")
    en_astro = en_astro.replace("Explorer ", "Explore ")
    en_astro = en_astro.replace("Fiche pratique & technique", "Key Practical Facts")
    en_astro = en_astro.replace("Poser une question sur ", "Ask a question about ")
    en_astro = en_astro.replace("Photographies du terrain", "Photos from the Wild")
    en_astro = en_astro.replace("Aperçu visuel de ", "Visual Overview of ")
    en_astro = en_astro.replace("Saison 2026/2027", "Season 2026/2027")
    en_astro = en_astro.replace("Les séjours immersifs à ", "Immersive Expeditions to ")
    en_astro = en_astro.replace("Départs garantis en micro-groupes. Cliquez sur un circuit pour consulter le programme jour par jour.", "Guaranteed small group departures. Click on an expedition to view the day-by-day itinerary.")
    en_astro = en_astro.replace("Voir tous les 14 séjours →", "View all 14 trips →")
    en_astro = en_astro.replace("À partir de", "Starting from")
    en_astro = en_astro.replace("Voir le séjour →", "View expedition →")
    en_astro = en_astro.replace("<Footer lang=\"fr\" />", "<Footer lang=\"en\" />")
    en_astro = en_astro.replace("/destinations.html", "/en/destinations.html")
    en_astro = en_astro.replace("/index.html", "/en/index.html")
    en_astro = en_astro.replace("/tours/", "/en/tours/")

    with open(f"/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/destinations/{slug}.astro", 'w', encoding='utf-8') as f:
        f.write(en_astro)

print("Generated all 5 destination pages with exact original design + sidebar Fiche Technique + 100% full text!")
