import json
import os

# Complete rich destination data from junglenepal.com
destinations_full = {
    "bardia": {
        "slug": "bardia",
        "name": "Parc national de Bardia",
        "name_en": "Bardia National Park",
        "tagline": "Tigres du Bengale, éléphants sauvages et safaris à pied exclusifs",
        "tagline_en": "Bengal Tigers, Wild Elephants & Exclusive Walking Safaris",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
        "stats": [
            {"label": "Superficie", "value": "968 km²", "sub": "Territoire 100% sauvage"},
            {"label": "Tigres du Bengale", "value": "+125", "sub": "Forte densité en Asie"},
            {"label": "Espèces d'oiseaux", "value": "400+", "sub": "Paradis ornithologique"},
            {"label": "Spécificité", "value": "À pied", "sub": "Safaris exclusifs sans foule"}
        ],
        "sections": [
            {
                "title": "Histoire et origines du Parc de Bardia",
                "content": """Avant sa création officielle en 1988, le parc national de Bardia était une réserve de chasse royale dédiée à la monarchie népalaise. Sa transformation en parc national a marqué une étape clé dans la protection de la biodiversité du Teraï occidental. Aujourd'hui, Bardia est le sanctuaire le plus vaste et le plus intact du Népal, offrant une nature brute et préservée, loin du tourisme de masse."""
            },
            {
                "title": "Le paradis des animaux sauvages en liberté",
                "content": """Aujourd’hui, le parc national de Bardia est un véritable sanctuaire de la faune sauvage au Népal. Il abrite des espèces emblématiques comme le tigre du Bengale, l'éléphant d'Asie sauvage, le rhinocéros unicorne, ainsi que le rare dauphin d'eau douce du Gange (sur les rivières Karnali et Geruwa). On y recense également plus de 400 espèces d’oiseaux, des léopards, des cerfs axis et de grands gavials préhistoriques."""
            },
            {
                "title": "Comment explorer le parc national de Bardia ?",
                "content": """Vivre une expérience immersive au cœur de la jungle de Bardia se fait à travers différents modes d'approche respectueux :
• Safaris à pied avec maîtres pisteurs natifs (tracking silencieux du tigre du Bengale).
• Safaris en jeep 4x4 ouverte pour explorer les zones profondes et la vallée secrète de Babai.
• Balades en canoë traditionnel sur les rivières pour observer les gavials et les oiseaux d'eau.
• Bivouac sauvage sous tente au cœur de la vallée isolée de Babai pour vivre la nuit en jungle."""
            },
            {
                "title": "La communauté Tharu : Gardiens ancestraux de la forêt",
                "content": """Au-delà de la faune sauvage et des paysages luxuriants, Bardia abrite l’une des cultures les plus fascinantes et résilientes du Népal : le peuple Tharu. Présente dans les plaines du Terai depuis des siècles, cette ethnie autochtone a développé une relation intime et respectueuse avec son environnement naturel.

Leur lien profond avec la nature est à la fois spirituel et ancré dans le quotidien. Les maisons traditionnelles Tharu, construites en terre, paille et bambou, s'intègrent harmonieusement dans les paysages ruraux. Ce qui rend la communauté Tharu unique, c’est sa connaissance intime de la forêt de Bardia : ils savent lire chaque empreinte, interpréter les cris d'alarme des cerfs et comprendre les mouvements de la faune. En séjournant à Bardia, vous soutenez directement cette communauté locale."""
            }
        ],
        "matching_slugs": ["bardia-explorateur", "babai-special", "bardia-babai-camping", "bardia-nuit-sauvage", "jungle-extreme", "nepal-sauvage"]
    },
    "chitwan": {
        "slug": "chitwan",
        "name": "Parc national de Chitwan",
        "name_en": "Chitwan National Park",
        "tagline": "Rhinocéros unicornes, pirogues sur la Rapti et culture Tharu",
        "tagline_en": "One-Horned Rhinos, Rapti River Canoes & Tharu Culture",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "stats": [
            {"label": "Statut", "value": "UNESCO", "sub": "Classé depuis 1984"},
            {"label": "Superficie", "value": "952 km²", "sub": "Premier parc du Népal"},
            {"label": "Rhinocéros", "value": "+690", "sub": "Habitat numéro 1 en Asie"},
            {"label": "Accessibilité", "value": "Facile", "sub": "Proche Pokhara & Katmandou"}
        ],
        "sections": [
            {
                "title": "Chitwan, paradis de la faune sauvage dans les plaines du Terai",
                "content": """Classé au patrimoine mondial de l’UNESCO en 1984, le parc national de Chitwan abrite l’une des faunes sauvages les plus impressionnantes d’Asie. C'est le premier parc national créé au Népal en 1973. Il est considéré mondialement comme le meilleur endroit pour observer le grand rhinocéros indien à une corne (Rhinoceros unicornis) évoluant librement dans son habitat naturel de forêts de sal et de hautes prairies alluviales."""
            },
            {
                "title": "Activités et immersions en pleine jungle",
                "content": """Entre safaris en jeep, marches guidées d'observation dans la jungle et descentes paisibles en pirogue traditionnelle sur la rivière Rapti au lever du soleil, chaque activité offre une immersion directe au contact de la faune.
Ce décor sauvage et préservé fait de Chitwan un lieu magique où vous croiserez des hardes de cervidés, des crocodiles gavials se chauffant sur les berges de sable, ainsi que des martins-pêcheurs et calaos colorés."""
            },
            {
                "title": "Accessibilité et confort des éco-lodges",
                "content": """L’un des grands atouts du parc national de Chitwan est son accessibilité idéale. Situé à seulement quelques heures de route de Katmandou ou de Pokhara (et desservi par l'aéroport de Bharatpur), il permet une halte nature de qualité sans longs trajets éprouvants.
Grâce à nos éco-lodges de charme partenaires, à la présence de nos guides naturalistes et à une logistique rodée, Chitwan est parfait aussi bien pour les familles que pour les explorateurs avides de grands espaces."""
            }
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
        "stats": [
            {"label": "Prairies", "value": "54 km²", "sub": "Plus vaste prairie d'Asie"},
            {"label": "Cerfs des marais", "value": "+2000", "sub": "Record mondial unique"},
            {"label": "Fréquentation", "value": "Ultra-faible", "sub": "Aucun tourisme de masse"},
            {"label": "Faune", "value": "Tigres & Éléphants", "sub": "Écosystème préservé"}
        ],
        "sections": [
            {
                "title": "Un sanctuaire naturel unique dans l'extrême ouest du Népal",
                "content": """Situé dans l’extrême ouest du Népal, à la frontière de l’Inde, le parc national de Suklaphanta est l’un des joyaux les plus sauvages et les moins fréquentés du pays. Encore totalement préservé des circuits touristiques classiques, Suklaphanta offre une expérience de safari pur, paisible et authentique."""
            },
            {
                "title": "La plus grande population de cerfs des marais (Barasingha) au monde",
                "content": """La renommée de Suklaphanta repose avant tout sur sa vaste prairie ouverte (Phanta), la plus grande d'Asie du Sud. C'est ici que vit la plus importante harde de cerfs des marais (Barasingha) au monde, comptant plus de 2 000 individus. Voir des centaines de grands mâles aux bois majestueux traverser la brume matinale est un spectacle inoubliable.
Le parc est également un habitat vital pour le tigre du Bengale, le léopard d'Asie, les hardes d'éléphants sauvages, le chacal doré et le rare florican du Bengale."""
            },
            {
                "title": "Pourquoi choisir l'expédition à Suklaphanta ?",
                "content": """Explorer Suklaphanta, c’est faire le choix d’un safari brut, hors des sentiers battus. Accompagnés de guides locaux expérimentés, vous découvrez une nature où le silence n'est rompu que par les bruits de la jungle. Visiter Suklaphanta, c'est aussi soutenir concrètement un modèle de conservation communautaire pionnier au Népal."""
            }
        ],
        "matching_slugs": ["nepal-sauvage", "nepal-immersion-totale"]
    },
    "annapurna": {
        "slug": "annapurna",
        "name": "Les Annapurna & Pokhara",
        "name_en": "Annapurna Range & Pokhara",
        "tagline": "Des treks mythiques entre hauts sommets, lacs sacrés et cultures montagnardes",
        "tagline_en": "Mythical Treks Between Sacred Peaks, Lakes & Alpine Villages",
        "hero_image": "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
        "stats": [
            {"label": "Sommets", "value": "+8000 m", "sub": "Annapurna I, Dhaulagiri"},
            {"label": "Camp de base", "value": "Pokhara", "sub": "Au bord du lac Phewa"},
            {"label": "Heures de marche", "value": "4 à 7h / jour", "sub": "Rythme accessible"},
            {"label": "Saison", "value": "Oct-Nov / Mar-Mai", "sub": "Ciels limpides"}
        ],
        "sections": [
            {
                "title": "Annapurna, des treks mythiques entre hauts sommets et vallées",
                "content": """La région de l’Annapurna est l’une des zones de trekking les plus spectaculaires et variées de la planète. Située à courte distance de la charmante ville de Pokhara, elle permet de passer en quelques jours des vallées subtropicales luxuriantes peuplées de bananiers aux forêts de rhododendrons géants, avant d'atteindre les balcons alpins face aux géants himalayens comme le Machapuchare (le célèbre mont Fish Tail), le Dhaulagiri et l'Annapurna Sud."""
            },
            {
                "title": "Rencontre humaine avec les peuples Gurung et Magar",
                "content": """Le trekking dans la région de l’Annapurna ne se résume pas aux panoramas vertigineux — il est avant tout une rencontre humaine chaleureuse. Au fil des sentiers ancestraux, les nuits se passent dans de confortables tea houses familiales ou chez l’habitant. On y partage le traditionnel Dal Bhat réparateur au coin du poêle tout en découvrant les coutumes et la générosité des montagnards Gurung."""
            },
            {
                "title": "Les meilleures saisons pour explorer l'Annapurna",
                "content": """Les deux périodes privilégiées pour arpenter l'Annapurna sont l'automne (octobre à décembre), avec une visibilité cristalline sur les sommets enneigés après la mousson, et le printemps (mars à mai), période magique où les rhododendrons fleurissent en rouge et rose sur les pentes des montagnes."""
            }
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
        "stats": [
            {"label": "Patrimoine UNESCO", "value": "7 sites", "sub": "Concentration unique au monde"},
            {"label": "Altitude", "value": "1400 m", "sub": "Climat tempéré toute l'année"},
            {"label": "Ambiance", "value": "Spirituelle", "sub": "Bouddhisme & Hindouisme"},
            {"label": "Accueil", "value": "Sur-mesure", "sub": "Briefing direct avec Robin"}
        ],
        "sections": [
            {
                "title": "Katmandou, un chaos vivant, spirituel et fascinant",
                "content": """Au premier abord, Katmandou peut sembler déroutante et vibrante. Mais laissez-lui un peu de temps, et elle finit par vous happer totalement. Entre ruelles pavées millénaires chargées d’histoire, senteurs d'encens de santal et toits-terrasses avec vue sur les stupas dorés, Katmandou est une ville brute et profondément vivante où le sacré côtoie le quotidien à chaque coin de rue."""
            },
            {
                "title": "Les 7 joyaux de la Vallée classés au Patrimoine Mondial de l'UNESCO",
                "content": """La vallée de Katmandou abrite une concentration monumentale unique au monde :
• Le grand stupa blanc de Boudhanath, cœur spirituel des bouddhistes tibétains.
• La colline sacrée de Swayambhunath (le Monkey Temple) surplombant toute la vallée.
• Le temple hindou millénaire de Pashupatinath sur les rives sacrées de la Bagmati.
• Les trois places royales historiques de Durbar Square : Katmandou, Patan et la cité médiévale préservée de Bhaktapur."""
            },
            {
                "title": "Votre porte d'entrée personnalisée vers l'aventure",
                "content": """Pour tous nos voyageurs, Katmandou est bien plus qu’une simple escale technique. C’est ici que Robin et nos équipes vous accueillent dès votre atterrissage à l'aéroport international pour un briefing personnalisé autour d'un thé népalais, avant de vous équiper et de vous lancer vers les grands territoires sauvages du Népal."""
            }
        ],
        "matching_slugs": ["nepal-sauvage", "tiji-mustang", "carnet-de-voyage"]
    }
}

def build_dest_astro(dest, lang='fr'):
    is_en = lang == 'en'
    slug = dest['slug']
    title = f"{dest['name']} – Guide Complet & Safaris" if not is_en else f"{dest['name_en']} – Complete Travel Guide & Safaris"
    desc = dest['tagline'] if not is_en else dest['tagline_en']
    dest_name = dest['name'] if not is_en else dest['name_en']
    dest_tagline = dest['tagline'] if not is_en else dest['tagline_en']
    
    current_path = f"/destinations/{slug}.html" if not is_en else f"/en/destinations/{slug}.html"
    home_url = "/index.html" if not is_en else "/en/index.html"
    all_dest_url = "/destinations.html" if not is_en else "/en/destinations.html"
    all_tours_url = "/index.html#prochains-departs" if not is_en else "/en/index.html#prochains-departs"
    tours_prefix = "/tours/" if not is_en else "/en/tours/"

    # Sections HTML
    sections_html = ""
    for s in dest['sections']:
        s_title = s['title'] if not is_en else s.get('title_en', s['title'])
        s_content = s['content'] if not is_en else s.get('content_en', s['content'])
        formatted_content = "<br/><br/>".join([f"<p class='leading-relaxed'>{p.strip()}</p>" for p in s_content.split('\n\n') if p.strip()])
        formatted_content = formatted_content.replace('•', '<br/>•')
        sections_html += f"""
        <div class="bg-white p-7 sm:p-9 rounded-3xl border border-slate-200/90 shadow-sm space-y-4">
          <h2 class="text-xl sm:text-2xl font-black text-slate-950 tracking-tight flex items-center gap-2.5">
            <span class="w-3 h-3 rounded-full bg-[#0e8354] shrink-0"></span>
            <span>{s_title}</span>
          </h2>
          <div class="text-sm sm:text-base text-slate-700 font-normal space-y-3">
            {formatted_content}
          </div>
        </div>
        """

    # Key stats HTML
    stats_html = ""
    for st in dest['stats']:
        stats_html += f"""
        <div class="bg-white p-5 rounded-2xl border border-slate-200/90 shadow-sm text-center">
          <p class="text-[10px] font-black uppercase tracking-wider text-slate-400">{st['label']}</p>
          <p class="text-2xl font-black text-[#0e8354] mt-1">{st['value']}</p>
          <p class="text-xs text-slate-500 mt-0.5">{st['sub']}</p>
        </div>
        """

    import_prefix = '../../' if is_en else '../'
    matching_slugs_json = json.dumps(dest['matching_slugs'])

    breadcrumb_home = 'Accueil' if not is_en else 'Home'
    badge_label = 'Territoire Sauvage du Népal' if not is_en else 'Wild Sanctuary of Nepal'
    sidebar_top = 'Organiser votre voyage' if not is_en else 'Plan Your Journey'
    sidebar_heading = f"Envie d'explorer {dest_name} ?" if not is_en else f"Explore {dest_name} ?"
    sidebar_desc = "Nos séjours sont organisés en micro-groupes de 4 à 8 personnes avec maîtres pisteurs natifs certifiés." if not is_en else "Our expeditions are strictly limited to small groups of 4 to 8 with certified native trackers."
    sidebar_wa = "Discuter avec Robin (WhatsApp)" if not is_en else "Chat with Robin (WhatsApp)"
    sidebar_quote = "Demander un devis sur-mesure" if not is_en else "Request a custom quote"
    quote_link = "/contact.html" if not is_en else "/en/contact.html"
    r1 = "Acompte de 30% à la réservation" if not is_en else "30% deposit upon booking"
    r2 = "Coordinateur francophone dédié" if not is_en else "Dedicated personal coordinator"
    r3 = "Zéro safari à dos d'éléphant (Éthique 100%)" if not is_en else "100% Ethical safari (No elephant rides)"
    circuits_badge = "Circuits recommandés" if not is_en else "Recommended Expeditions"
    circuits_heading = f"Les séjours explorant {dest_name}" if not is_en else f"Expeditions visiting {dest_name}"
    view_all = "Voir tous les 14 séjours →" if not is_en else "View all 14 trips →"
    start_from = "À PARTIR DE" if not is_en else "STARTING FROM"
    explore_btn = "Découvrir →" if not is_en else "Explore →"

    return f"""---
import Layout from '{import_prefix}layouts/Layout.astro';
import Header from '{import_prefix}components/Header.astro';
import Footer from '{import_prefix}components/Footer.astro';
import toursData from '{import_prefix}data/tours.json';

const matchingTours = toursData.filter(t => {matching_slugs_json}.includes(t.slug)).slice(0, 3);
---

<Layout 
  title="{title}"
  description="{desc}"
  image="{dest['hero_image']}"
  lang="{lang}"
  isDarkHeader={{true}}
>
  <Header lang="{lang}" currentPath="{current_path}" />

  <!-- HERO DESTINATION -->
  <div class="relative min-h-[55vh] flex items-center justify-center pt-32 pb-20 px-4 bg-slate-950 text-white overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img src="{dest['hero_image']}" alt="{dest_name}" class="w-full h-full object-cover opacity-40 scale-105 filter brightness-90" />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/40"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center space-y-4">
      <nav class="flex items-center justify-center gap-2 text-xs text-slate-300 font-semibold mb-2">
        <a href="{home_url}" class="hover:text-white">{breadcrumb_home}</a>
        <span>›</span>
        <a href="{all_dest_url}" class="hover:text-white">Destinations</a>
        <span>›</span>
        <span class="text-amber-300 font-bold">{dest_name}</span>
      </nav>

      <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/20 text-[#10b981] border border-emerald-500/30 text-xs font-black uppercase tracking-widest">
        <span>🇳🇵</span> {badge_label}
      </span>
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-tight">
        {dest_name}
      </h1>
      <p class="text-base sm:text-xl text-slate-200 max-w-2xl mx-auto font-medium leading-relaxed drop-shadow">
        {dest_tagline}
      </p>
    </div>
  </div>

  <!-- KEY STATS BAR -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-10 relative z-20">
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      {stats_html}
    </div>
  </section>

  <!-- MAIN ARTICLE CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 font-sans space-y-16">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT ARTICLE COLUMN (100% CONTENU TEXTE OFFICIEL) -->
      <div class="lg:col-span-8 space-y-8">
        {sections_html}
      </div>

      <!-- RIGHT SIDEBAR: SÉJOURS & CONTACT DIRECT -->
      <div class="lg:col-span-4 space-y-8">
        
        <!-- Booking / Info Card -->
        <div class="sticky top-28 bg-white p-7 rounded-3xl border border-slate-200/90 shadow-lg space-y-6">
          <div class="space-y-2">
            <span class="text-[11px] font-black uppercase tracking-wider text-[#0e8354]">{sidebar_top}</span>
            <h3 class="text-xl font-black text-slate-950">{sidebar_heading}</h3>
            <p class="text-xs text-slate-600 leading-relaxed font-normal">
              {sidebar_desc}
            </p>
          </div>

          <div class="space-y-3 pt-3 border-t border-slate-100 text-xs">
            <a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="w-full py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black flex items-center justify-center gap-2 shadow-md hover:scale-105 transition-all">
              <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
              <span>{sidebar_wa}</span>
            </a>
            <a href="{quote_link}" class="w-full py-3 rounded-2xl bg-slate-950 hover:bg-slate-800 text-white font-bold flex items-center justify-center gap-2 transition-colors">
              <span>{sidebar_quote}</span>
            </a>
          </div>

          <div class="pt-3 border-t border-slate-100 text-[11px] text-slate-500 space-y-1.5 font-medium">
            <p>✓ {r1}</p>
            <p>✓ {r2}</p>
            <p>✓ {r3}</p>
          </div>
        </div>

      </div>

    </div>

    <!-- SÉJOURS PASSANT PAR CETTE DESTINATION -->
    <div class="pt-12 border-t border-slate-200 space-y-8">
      <div class="flex items-end justify-between">
        <div>
          <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">{circuits_badge}</span>
          <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight mt-1">
            {circuits_heading}
          </h2>
        </div>
        <a href="{all_tours_url}" class="text-xs font-black text-[#0e8354] hover:underline">
          {view_all}
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {{matchingTours.map((t) => (
          <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col group">
            <div class="relative h-48 overflow-hidden bg-slate-900">
              <img src={{t.images[0]}} alt={{t.title}} class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
              <span class="absolute top-3 left-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-300 text-xs font-bold border border-amber-300/30">
                {{t.badge}}
              </span>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <p class="text-xs font-bold text-slate-500">{{t.duration}} • ★ {{t.rating}} ({{t.reviews}} avis)</p>
                <h3 class="font-bold text-base text-slate-900 mt-1 leading-snug group-hover:text-[#0e8354] transition-colors">
                  {{t.title}}
                </h3>
              </div>
              <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <span class="text-[10px] text-slate-400 block font-bold">{start_from}</span>
                  <span class="font-black text-xl text-slate-950">{{t.price}}</span>
                </div>
                <a href={{`{tours_prefix}${{t.slug}}.html`}} class="px-4 py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white text-xs font-bold transition-colors">
                  {explore_btn}
                </a>
              </div>
            </div>
          </div>
        ))}}
      </div>
    </div>

  </main>

  <Footer lang="{lang}" />
</Layout>
"""

# Generate for all 5 destinations (FR and EN)
for key, dest in destinations_full.items():
    # FR
    fr_code = build_dest_astro(dest, lang='fr')
    fr_path = f"/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/{key}.astro"
    with open(fr_path, 'w', encoding='utf-8') as f:
        f.write(fr_code)

    # EN
    en_code = build_dest_astro(dest, lang='en')
    en_path = f"/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/destinations/{key}.astro"
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(en_code)

print("Generated full rich destination pages with 100% official texts for all 5 destinations (FR + EN)!")
