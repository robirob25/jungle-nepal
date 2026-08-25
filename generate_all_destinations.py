import os
import json
import re

os.makedirs('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations', exist_ok=True)

# Load scraped data
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/scraped_destinations_raw.json', 'r', encoding='utf-8') as f:
    scraped = json.load(f)

# Load all tours
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

# Definition of all 5 Destinations with rich text from junglenepal.com
destinations_info = {
    "bardia": {
        "title": "Parc national de Bardia",
        "badge": "🐅 Sanctuaire Suprême du Tigre du Bengale",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
        "intro": "Avant sa création officielle en 1988, le parc national de Bardia était une réserve de chasse royale dédiée à la monarchie népalaise. Sa transformation en sanctuaire protégé a permis de préserver l'un des écosystèmes les plus sauvages et intacts d'Asie.",
        "description_p1": "Aujourd'hui, le parc national de Bardia est le véritable sanctuaire de la faune sauvage au Népal. S'étendant sur 968 km² de forêts de sals denses, de savanes herbeuses et de méandres fluviaux le long de la rivière Karnali, il abrite la plus dense population de tigres du Bengale en liberté du pays.",
        "description_p2": "Contrairement aux parcs touristiques bondés, Bardia se découvre principalement à pied, accompagné de deux maîtres pisteurs natifs. Vous pisterez le tigre, le grand rhinocéros indien, les hardes d'éléphants sauvages, les cerfs chitals et le discret léopard dans un silence absolu.",
        "tharu_title": "La communauté Tharu & l'harmonie avec la forêt",
        "tharu_text": "Les Tharus sont les gardiens indigènes de Bardia. Vivant en lisière du sanctuaire depuis des siècles, ils possèdent une connaissance intime des plantes médicinales, des pistes animales et des équilibres sacrés de la jungle. Nos séjours intègrent des nuits chez l'habitant et des repas traditionnels cuisinés au feu de bois.",
        "best_season": "D'octobre à mai (Pic d'observation des tigres aux points d'eau entre mars et mai).",
        "fauna_highlight": ["Tigre royal du Bengale", "Grand Rhinocéros unicorne", "Éléphant sauvage d'Asie", "Cerf des marais", "Dauphin du Gange", "Crocodile Gavial"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Tharu-danse.png"
        ],
        "related_tours": ["nepal-sauvage", "babai-special", "bardia-babai-camping", "bardia-explorateur", "bardia-nuit-sauvage", "jungle-extreme"]
    },
    "chitwan": {
        "title": "Parc national de Chitwan",
        "badge": "🦏 Patrimoine Mondial de l'UNESCO",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "intro": "Classé au patrimoine mondial de l’UNESCO depuis 1984, le parc national de Chitwan abrite l'une des biodiversités les plus spectaculaires et foisonnantes du continent asiatique.",
        "description_p1": "Le parc national de Chitwan est mondialement reconnu comme le meilleur endroit pour observer le grand rhinocéros indien à une corne (Rhinoceros unicornis) dans son habitat naturel. Les plaines inondables et les hautes herbes à éléphants offrent des scènes animalières d'une rare intensité.",
        "description_p2": "Entre safaris en jeep ouverte, marches silencieuses dans la jungle avec nos guides experts et descentes douces en canoë traditionnel sur la rivière Rapti au milieu des gavials et des oiseaux migrateurs, Chitwan allie aventure brute et confort d'écolodges chaleureux.",
        "tharu_title": "Culture Tharu & artisanat du Terai",
        "tharu_text": "Les villages bordant Chitwan perpétuent des traditions millénaires : maisons en torchis ornées de motifs sacrés, danses des bâtons et gastronomie locale. Chaque séjour contribue au développement durable de ces communautés.",
        "best_season": "D'octobre à avril (Climat doux et herbes coupées favorisant l'observation de la grande faune).",
        "fauna_highlight": ["Grand Rhinocéros unicorne", "Tigre du Bengale", "Ours lippu (Sloth Bear)", "Crocodile Gavial du Gange", "Cerf sambar", "Plus de 500 espèces d'oiseaux"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/ours-lippu-chitwan.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/tharu-1.jpg"
        ],
        "related_tours": ["chitwan-culture", "chitwan-bardia-complete", "nepal-immersion-totale"]
    },
    "suklaphanta": {
        "title": "Parc national de Suklaphanta",
        "badge": "🦌 L'Éden Sauvage Hors des Sentiers Battus",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg",
        "intro": "Situé à l'extrême ouest du Népal, à la frontière de l'Inde, le parc national de Suklaphanta est l'un des territoires les plus sauvages, préservés et secrets de tout l'Himalaya.",
        "description_p1": "Suklaphanta est mondialement réputé pour abriter la plus grande harde de cerfs des marais (Barasingha) au monde, comptant plus de 2 000 individus qui évoluent librement dans d'immenses prairies herbeuses dorées.",
        "description_p2": "Le parc constitue également un corridor biologique vital pour le tigre du Bengale, le léopard, les hardes d'éléphants sauvages et plus de 420 espèces d'oiseaux aquatiques et migrateurs. C'est l'expérience safari ultime pour les explorateurs en quête de solitude totale.",
        "tharu_title": "L'Ouest sauvage du Népal",
        "tharu_text": "Loin de toute agitation touristique, Suklaphanta offre un contact authentique et émouvant avec les ethnies Rana Tharu de l'extrême ouest, réputées pour leurs costumes colorés et leur accueil légendaire.",
        "best_season": "De novembre à mai (Période sèche idéale pour les traversées des grandes plaines).",
        "fauna_highlight": ["Cerf des marais (Barasingha)", "Tigre du Bengale", "Léopard indien", "Éléphant sauvage", "Florican du Bengale (oiseau rare)", "Chacal doré"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Elephant-sauvage-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/2-1.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png"
        ],
        "related_tours": ["jungle-extreme", "rara-lake-bardia", "bardia-explorateur"]
    },
    "annapurna": {
        "title": "Les Annapurna & Pokhara",
        "badge": "🏔️ Sommets Sacrés & Treks Mythiques",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/himalayas-5817277_1920.jpg",
        "intro": "La région de l'Annapurna offre des contrastes géographiques et culturels vertigineux : des forêts tropicales luxuriantes jusqu'aux parois de glace flirtant avec les 8 000 mètres.",
        "description_p1": "Située au nord de la paisible ville lacustre de Pokhara, la région de l'Annapurna permet de vivre une randonnée alpine d'exception adaptée à tous les niveaux : balades contemplatives sur les balcons de l'Himalaya, traversées de forêts de rhododendrons géants ou ascensions vers les sanctuaires sacrés.",
        "description_p2": "Combiner un trek dans les Annapurna avec un safari animalier dans le Terai (Bardia ou Chitwan) permet de vivre l'intégralité du Népal : la verticalité des géants de neige et la luxuriance mystique de la jungle.",
        "tharu_title": "Villages Gurung & Magar",
        "tharu_text": "Au fil des sentiers de pierre, vous ferez étape dans des villages suspendus où les peuples Gurung et Magar perpétuent l'hospitalité montagnarde autour d'un thé brûlant et d'un Dal Bhat réconfortant.",
        "best_season": "D'octobre à décembre (Ciel d'un bleu cristallin) et de mars à mai (Floraison des rhododendrons).",
        "fauna_highlight": ["Monal de l'Himalaya (oiseau national)", "Mouton bleu (Bharal)", "Cerf porte-musc", "Tahr de l'Himalaya", "Vautour de l'Himalaya", "Léopard des neiges (en haute altitude)"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2026/01/Machapuchare-himalaya-montagne.png",
            "https://junglenepal.com/wp-content/uploads/2026/01/Himalaya-haut-sommet.png",
            "https://junglenepal.com/wp-content/uploads/2026/01/Nepal-Himalaya-hiver.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/1.png"
        ],
        "related_tours": ["tiji-mustang", "nepal-sauvage", "immersion-spirituelle", "carnet-de-voyage"]
    },
    "katmandou": {
        "title": "Katmandou & la Vallée des Rois",
        "badge": "🕉️ Cité Millénaire & Temples Sacrés",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/03/79.png",
        "intro": "Au premier abord, Katmandou peut sembler déroutante et bouillonnante. Mais laissez-lui quelques heures, et elle finit par vous enchanter par sa ferveur spirituelle et sa poésie intemporelle.",
        "description_p1": "Véritable musée à ciel ouvert classé par l'UNESCO, la vallée de Katmandou abrite les cités royales de Patan et Bhaktapur, le grand stûpa bouddhiste de Bodnath aux yeux bienveillants et le sanctuaire hindou de Pashupatinath au bord de la rivière sacrée Bagmati.",
        "description_p2": "C'est à Katmandou que commence chaque aventure avec Jungle Nepal Adventure. Nous y assurons un accueil francophone personnalisé, le briefing d'expédition avec l'équipe et la découverte des ruelles historiques à l'écart des foules.",
        "tharu_title": "Art Newar & Spiritualité Vivante",
        "tharu_text": "Les artisans newars sculptent le bois et le bronze avec le même génie depuis des siècles. Les toits de pagodes, les cours intérieures secrètes et les moulins à prières créent une atmosphère de sérénité inoubliable.",
        "best_season": "Accessible toute l'année (Climat particulièrement doux et ensoleillé d'octobre à mai).",
        "fauna_highlight": ["Singes sacrés de Swayambhunath", "Oiseaux de la vallée", "Jardins botaniques historiques", "Rizières en terrasses de Nagarkot"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/03/79.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2026/01/Groupe-touriste-Nagarkot-Nepal.jpg"
        ],
        "related_tours": ["nepal-sauvage", "nepal-immersion-totale", "immersion-spirituelle", "carnet-de-voyage"]
    }
}

# Template for individual Destination Page
def build_destination_page(dest_key, d):
    # Find matching tour cards
    matching_cards_html = ""
    for t in tours:
        short_id = t["short_id"]
        if short_id in d["related_tours"]:
            matching_cards_html += f"""
            <article class="bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
              <a href="../tours/{short_id}.html" class="relative h-64 overflow-hidden block group">
                <img src="{t.get('hero_img', d['hero_img'])}" alt="{t['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
                <span class="absolute top-4 left-4 bg-slate-950/80 backdrop-blur-md text-amber-300 text-xs font-black px-3 py-1 rounded-full border border-amber-400/30">
                  {t['badge']}
                </span>
                <span class="absolute bottom-4 left-4 text-white font-black text-sm">
                  {t['duration']} • {t['price']}
                </span>
              </a>
              <div class="p-6 flex-1 flex flex-col justify-between">
                <div>
                  <h3 class="font-black text-lg text-slate-900 hover:text-[#0e8354] transition-colors leading-snug">
                    <a href="../tours/{short_id}.html">{t['title']}</a>
                  </h3>
                  <p class="mt-2 text-xs text-slate-600 line-clamp-2 font-normal">
                    {t['overview']}
                  </p>
                </div>
                <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
                  <span class="text-xs font-bold text-[#0e8354]">Départs garantis 2026/2027</span>
                  <a href="../tours/{short_id}.html" class="px-4 py-2 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-extrabold text-xs shadow transition-all">
                    Voir le séjour →
                  </a>
                </div>
              </div>
            </article>
            """

    fauna_badges_html = "".join([f'<span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-emerald-50 text-[#0e8354] text-xs font-extrabold border border-emerald-200 shadow-sm"><i data-lucide="check" class="w-3.5 h-3.5"></i><span>{f}</span></span>' for f in d["fauna_highlight"]])

    gallery_html = "".join([f'<div class="rounded-2xl overflow-hidden shadow-md h-60 group"><img src="{img}" alt="{d["title"]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/></div>' for img in d["gallery"]])

    return f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']} | Destinations Jungle Nepal Adventure</title>
  <meta name="description" content="{d['intro'][:160]}">

  <!-- WeRoad Exact Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
          }},
          colors: {{
            jungle: {{
              50: '#f1f7f4',
              500: '#109363',
              600: '#0e8354',
              950: '#041d13',
            }},
            safari: {{
              50: '#faf8f5',
              100: '#f4efe6',
            }}
          }}
        }}
      }}
    }}
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style> body {{ font-family: 'Plus Jakarta Sans', sans-serif; }} </style>
</head>
<body class="bg-safari-50 text-slate-800 antialiased selection:bg-slate-950 selection:text-white">

  <!-- TOP BANNER -->
  <aside class="bg-gradient-to-r from-[#073021] via-[#0e5c3e] to-[#073021] text-white text-xs py-2.5 px-4 font-bold text-center border-b border-emerald-500/20 shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="w-6 hidden sm:block"></div>
      <div class="flex-1 text-center whitespace-nowrap overflow-hidden text-ellipsis">
        <span>🐅 <strong>Saison 2026-2027</strong> : Départs garantis en micro-groupes • <strong>-100€</strong> avec le code <span class="bg-white/15 px-2 py-0.5 rounded text-amber-300 font-black">JUNGLE100</span></span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/80 hover:text-white">✕</button>
    </div>
  </aside>

  <!-- NAVBAR SUR FOND BLANC AVEC LOGO NOIR TRANSPARENT -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between">
      
      <a href="../index.html" class="flex items-center gap-2 group shrink-0">
        <img src="../assets/logo_dark.png" alt="Jungle Nepal Adventure Logo" class="h-14 sm:h-16 w-auto object-contain group-hover:scale-105 transition-transform duration-300" />
      </a>

      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>
        <a href="index.html" class="text-[#0e8354] font-black border-b-2 border-[#0e8354] pb-0.5">Destinations</a>
        <a href="../index.html#concept" class="hover:text-[#0e8354] transition-colors">L'esprit safari</a>
        <a href="../a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="{exact_google_url}" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors flex items-center gap-1"><span class="text-[#00b67a]">★</span> Avis 5.0</a>
        <a href="../contact.html" class="hover:text-[#0e8354] transition-colors">Contacte-nous</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20informations%20sur%20{d['title']}" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-extrabold text-xs sm:text-[13px] shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>WhatsApp direct</span>
        </a>
      </div>

    </div>
  </header>

  <!-- HERO DESTINATION -->
  <section class="relative min-h-[60vh] sm:min-h-[70vh] flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">
    <div class="absolute inset-0 z-0">
      <img src="{d['hero_img']}" alt="{d['title']}" class="w-full h-full object-cover object-center filter brightness-75 contrast-105"/>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/50 to-black/40"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/25 text-amber-300 text-xs font-black uppercase tracking-wider mb-6">
        <span>{d['badge']}</span>
      </div>

      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-2xl">
        {d['title']}
      </h1>

      <p class="mt-6 text-base sm:text-xl text-slate-200 max-w-2xl font-medium leading-relaxed drop-shadow">
        {d['intro']}
      </p>
    </div>
  </section>

  <!-- CONTENU DÉTAILLÉ DE LA DESTINATION -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24 space-y-20">
    
    <!-- 1. PRÉSENTATION & FAUNE -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-7 space-y-6">
        <div class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wider text-[#0e8354] bg-emerald-50 px-3.5 py-1 rounded-full border border-emerald-200">
          <span>Sanctuaire sauvage</span>
        </div>
        <h2 class="font-black text-3xl sm:text-4xl text-slate-950 tracking-tight leading-tight">
          Une immersion brute au cœur de la vie sauvage
        </h2>
        <p class="text-slate-600 text-base leading-relaxed font-normal">
          {d['description_p1']}
        </p>
        <p class="text-slate-600 text-base leading-relaxed font-normal">
          {d['description_p2']}
        </p>

        <!-- Faune Highlights -->
        <div class="pt-4 space-y-3">
          <p class="font-black text-xs uppercase tracking-wider text-slate-400">Espèces emblématiques observées :</p>
          <div class="flex flex-wrap gap-2">
            {fauna_badges_html}
          </div>
        </div>
      </div>

      <!-- Quick Info Card -->
      <div class="lg:col-span-5 bg-white rounded-3xl p-8 border border-slate-200/90 shadow-xl space-y-6">
        <h3 class="font-black text-xl text-slate-950 pb-3 border-b border-slate-100 flex items-center gap-2">
          <i data-lucide="info" class="w-5 h-5 text-[#0e8354]"></i>
          <span>Fiche pratique</span>
        </h3>
        
        <div class="space-y-4 text-sm">
          <div>
            <p class="text-xs font-bold uppercase text-slate-400">Meilleure période</p>
            <p class="font-bold text-slate-900 mt-0.5">{d['best_season']}</p>
          </div>
          <div>
            <p class="text-xs font-bold uppercase text-slate-400">Mode d'exploration</p>
            <p class="font-bold text-slate-900 mt-0.5">Safaris à pied avec double pisteur, canoë et 4x4 d'accès</p>
          </div>
          <div>
            <p class="text-xs font-bold uppercase text-slate-400">Format de groupe</p>
            <p class="font-bold text-slate-900 mt-0.5">Micro-groupes exclusifs de 4 à 8 explorateurs max</p>
          </div>
          <div>
            <p class="text-xs font-bold uppercase text-slate-400">Encadrement</p>
            <p class="font-bold text-slate-900 mt-0.5">Maîtres pisteurs natifs (Pawan) & coordination française (Robin)</p>
          </div>
        </div>

        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20{d['title']}" target="_blank" class="block w-full text-center py-3.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow hover:scale-[1.02] active:scale-95 transition-all">
          Poser une question sur cette destination →
        </a>
      </div>
    </div>

    <!-- 2. CULTURE LOCALE & THARU -->
    <div class="p-8 sm:p-12 rounded-3xl bg-safari-100 border border-slate-200">
      <div class="max-w-3xl space-y-4">
        <span class="inline-block text-xs font-black uppercase tracking-widest text-[#0e8354] bg-white px-3.5 py-1 rounded-full border border-slate-200">
          Immersion locale
        </span>
        <h3 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">
          {d['tharu_title']}
        </h3>
        <p class="text-slate-700 text-sm sm:text-base leading-relaxed font-medium">
          {d['tharu_text']}
        </p>
      </div>
    </div>

    <!-- 3. GALERIE PHOTO IMMERSIVE -->
    <div class="space-y-6">
      <div class="flex items-end justify-between">
        <div>
          <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Photographies du terrain</span>
          <h3 class="font-black text-2xl sm:text-3xl text-slate-950">Aperçu visuel de {d['title']}</h3>
        </div>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        {gallery_html}
      </div>
    </div>

    <!-- 4. CIRCUITS ASSOCIÉS À CETTE DESTINATION -->
    <div class="space-y-8 pt-8 border-t border-slate-200">
      <div>
        <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Saison 2026/2027</span>
        <h3 class="font-black text-2xl sm:text-4xl text-slate-950">Les séjours immersifs à {d['title']}</h3>
        <p class="text-slate-600 text-sm mt-1">Départs garantis en micro-groupes. Cliquez sur un circuit pour consulter le programme jour par jour.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {matching_cards_html}
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-300 pt-16 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6 pb-12 border-b border-white/10 text-xs">
        <a href="../index.html"><img src="../assets/logo.png" alt="Logo" class="h-16 w-auto object-contain"/></a>
        <div class="flex flex-wrap gap-6 text-slate-400 font-bold">
          <a href="../index.html#prochains-departs" class="hover:text-white">Tous les 14 séjours</a>
          <a href="index.html" class="hover:text-white">Toutes les destinations</a>
          <a href="../a-propos.html" class="hover:text-white">À propos</a>
          <a href="../contact.html" class="hover:text-white">Contact</a>
        </div>
      </div>
      <p class="pt-8 text-xs text-slate-500 text-center">© 2026 Jungle Nepal Adventure • Tous droits réservés.</p>
    </div>
  </footer>

  <!-- BOUTON RETOUR EN HAUT ÉLÉGANT & GRAPHIQUE -->
  <button id="back-to-top" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 z-40 hidden sm:flex items-center justify-center w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-950/90 hover:bg-[#0e8354] text-white border border-white/25 shadow-[0_10px_30px_rgba(0,0,0,0.45)] backdrop-blur-xl transition-all duration-300 opacity-0 translate-y-4 pointer-events-none hover:scale-110 active:scale-95 group cursor-pointer" aria-label="Retour en haut">
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white group-hover:-translate-y-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
  </button>
  <script>
    lucide.createIcons();
    window.addEventListener('scroll', () => {{
      const btn = document.getElementById('back-to-top');
      if (!btn) return;
      if (window.scrollY > 300) {{
        btn.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }} else {{
        btn.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }}
    }});
  </script>
</body>
</html>
"""

# Generate all 5 individual destination pages
for dest_key, d in destinations_info.items():
    page_html = build_destination_page(dest_key, d)
    dest_path = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/{dest_key}.html'
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f'Generated destination page: {dest_path}')

# Build Destination Hub: destinations/index.html
destinations_cards_hub = ""
for dest_key, d in destinations_info.items():
    destinations_cards_hub += f"""
    <article class="group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
      <a href="{dest_key}.html" class="relative h-72 sm:h-80 overflow-hidden block">
        <img src="{d['hero_img']}" alt="{d['title']}" class="w-full h-full object-cover group-hover:scale-108 transition-transform duration-700 ease-out"/>
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/30 to-transparent"></div>
        <span class="absolute top-4 left-4 bg-slate-950/80 backdrop-blur-md text-amber-300 text-xs font-black px-3.5 py-1.5 rounded-full border border-amber-400/30">
          {d['badge']}
        </span>
        <div class="absolute bottom-4 left-4 right-4">
          <h2 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
            {d['title']}
          </h2>
        </div>
      </a>
      <div class="p-6 sm:p-7 flex-1 flex flex-col justify-between">
        <p class="text-sm text-slate-600 line-clamp-3 leading-relaxed font-normal">
          {d['intro']}
        </p>
        <div class="mt-6 pt-5 border-t border-slate-100 flex items-center justify-between">
          <span class="text-xs font-bold text-[#0e8354]">Explorer la région</span>
          <a href="{dest_key}.html" class="px-5 py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
            Découvrir la destination →
          </a>
        </div>
      </div>
    </article>
    """

hub_html = f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nos Destinations au Népal | Jungle Nepal Adventure</title>
  <meta name="description" content="Découvrez nos 5 grandes régions d'expédition au Népal : Parc national de Bardia, Parc de Chitwan, Suklaphanta, les Annapurna et la vallée de Katmandou.">

  <!-- WeRoad Exact Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
          }},
          colors: {{
            jungle: {{
              50: '#f1f7f4',
              500: '#109363',
              600: '#0e8354',
              950: '#041d13',
            }},
            safari: {{
              50: '#faf8f5',
              100: '#f4efe6',
            }}
          }}
        }}
      }}
    }}
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style> body {{ font-family: 'Plus Jakarta Sans', sans-serif; }} </style>
</head>
<body class="bg-safari-50 text-slate-800 antialiased selection:bg-slate-950 selection:text-white">

  <!-- TOP BANNER -->
  <aside class="bg-gradient-to-r from-[#073021] via-[#0e5c3e] to-[#073021] text-white text-xs py-2.5 px-4 font-bold text-center border-b border-emerald-500/20 shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="w-6 hidden sm:block"></div>
      <div class="flex-1 text-center whitespace-nowrap overflow-hidden text-ellipsis">
        <span>🐅 <strong>Saison 2026-2027</strong> : Départs garantis en micro-groupes • <strong>-100€</strong> avec le code <span class="bg-white/15 px-2 py-0.5 rounded text-amber-300 font-black">JUNGLE100</span></span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/80 hover:text-white">✕</button>
    </div>
  </aside>

  <!-- NAVBAR -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between">
      
      <a href="../index.html" class="flex items-center gap-2 group shrink-0">
        <img src="../assets/logo_dark.png" alt="Jungle Nepal Adventure Logo" class="h-14 sm:h-16 w-auto object-contain group-hover:scale-105 transition-transform duration-300" />
      </a>

      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>
        <a href="index.html" class="text-[#0e8354] font-black border-b-2 border-[#0e8354] pb-0.5">Destinations</a>
        <a href="../index.html#concept" class="hover:text-[#0e8354] transition-colors">L'esprit safari</a>
        <a href="../a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="{exact_google_url}" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors flex items-center gap-1"><span class="text-[#00b67a]">★</span> Avis 5.0</a>
        <a href="../contact.html" class="hover:text-[#0e8354] transition-colors">Contacte-nous</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20informations%20sur%20vos%20destinations" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-extrabold text-xs sm:text-[13px] shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>WhatsApp direct</span>
        </a>
      </div>

    </div>
  </header>

  <!-- HERO HUB -->
  <section class="relative min-h-[50vh] sm:min-h-[60vh] flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950 text-white">
    <div class="absolute inset-0 z-0">
      <img src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" alt="Tigre de Bardia" class="w-full h-full object-cover filter brightness-70 contrast-105"/>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/40"></div>
    </div>
    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/25 text-amber-300 text-xs font-black uppercase tracking-wider mb-6">
        <span>🇳🇵 Sanctuaires Sauvages du Népal</span>
      </div>
      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-2xl">
        Nos Destinations
      </h1>
      <p class="mt-6 text-base sm:text-xl text-slate-200 max-w-2xl font-medium leading-relaxed drop-shadow">
        Des sanctuaires inviolés du Terai aux sommets himalayens, découvrez les 5 grands territoires explorés avec nos maîtres pisteurs.
      </p>
    </div>
  </section>

  <!-- GRILLE DES 5 DESTINATIONS -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {destinations_cards_hub}
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-300 pt-16 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6 pb-12 border-b border-white/10 text-xs">
        <a href="../index.html"><img src="../assets/logo.png" alt="Logo" class="h-16 w-auto object-contain"/></a>
        <div class="flex flex-wrap gap-6 text-slate-400 font-bold">
          <a href="../index.html#prochains-departs" class="hover:text-white">Tous les 14 séjours</a>
          <a href="index.html" class="hover:text-white">Toutes les destinations</a>
          <a href="../a-propos.html" class="hover:text-white">À propos</a>
          <a href="../contact.html" class="hover:text-white">Contact</a>
        </div>
      </div>
      <p class="pt-8 text-xs text-slate-500 text-center">© 2026 Jungle Nepal Adventure • Tous droits réservés.</p>
    </div>
  </footer>

  <!-- BOUTON RETOUR EN HAUT ÉLÉGANT & GRAPHIQUE -->
  <button id="back-to-top" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 z-40 hidden sm:flex items-center justify-center w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-950/90 hover:bg-[#0e8354] text-white border border-white/25 shadow-[0_10px_30px_rgba(0,0,0,0.45)] backdrop-blur-xl transition-all duration-300 opacity-0 translate-y-4 pointer-events-none hover:scale-110 active:scale-95 group cursor-pointer" aria-label="Retour en haut">
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white group-hover:-translate-y-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
  </button>
  <script>
    lucide.createIcons();
    window.addEventListener('scroll', () => {{
      const btn = document.getElementById('back-to-top');
      if (!btn) return;
      if (window.scrollY > 300) {{
        btn.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }} else {{
        btn.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }}
    }});
  </script>
</body>
</html>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/index.html', 'w', encoding='utf-8') as f:
    f.write(hub_html)

print("Generated destinations/index.html hub and all 5 individual destination pages successfully!")
