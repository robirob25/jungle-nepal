import json
import os
import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/all_tours_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Metadata mapping for each of the 14 tours
meta_map = {
    "bardia-explorateur-5-jours-dans-la-jungle": {
        "short_id": "bardia-explorateur",
        "badge": "⭐ Best-Seller",
        "badge_color": "bg-jungle-800",
        "rating": "4.8",
        "reviews": 56,
        "difficulty": "Accessible à tous",
        "style": "Safari & Lodge Confort",
        "category": "safari",
        "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}
    },
    "chitwan-culture-et-jungle-sauvage": {
        "short_id": "chitwan-culture",
        "badge": "🦏 Rhinos & Tharu",
        "badge_color": "bg-emerald-700",
        "rating": "4.9",
        "reviews": 28,
        "difficulty": "Facile",
        "style": "Safari & Culture Locale",
        "category": "chitwan culture",
        "radar": {"wildlife": 4, "nature": 4, "culture": 5, "relax": 3, "nightlife": 1}
    },
    "rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting": {
        "short_id": "rafting-safari",
        "badge": "🚣 Rafting & Safari",
        "badge_color": "bg-sky-700",
        "rating": "5.0",
        "reviews": 15,
        "difficulty": "Sportif",
        "style": "Aventure & Eaux Vives",
        "category": "rafting safari",
        "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}
    },
    "bardia-aventure-immersive-en-jungle-et-camping-sauvage": {
        "short_id": "bardia-nuit-sauvage",
        "badge": "🌙 Micro-Aventure",
        "badge_color": "bg-amber-600",
        "rating": "4.9",
        "reviews": 31,
        "difficulty": "Accessible",
        "style": "Bivouac Express",
        "category": "bivouac safari",
        "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 2, "nightlife": 0}
    },
    "rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus": {
        "short_id": "rara-lake-bardia",
        "badge": "🏔️ Expédition 4x4 & Lac Sacré",
        "badge_color": "bg-indigo-800",
        "rating": "5.0",
        "reviews": 18,
        "difficulty": "Aventurier",
        "style": "Grand Trek & 4x4",
        "category": "trek safari",
        "radar": {"wildlife": 4, "nature": 5, "culture": 4, "relax": 2, "nightlife": 0}
    },
    "bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee": {
        "short_id": "bardia-babai-camping",
        "badge": "⛺ Bivouac Sauvage",
        "badge_color": "bg-jungle-700",
        "rating": "4.9",
        "reviews": 24,
        "difficulty": "Aventure",
        "style": "Expédition Bivouac",
        "category": "bivouac safari",
        "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 2, "nightlife": 0}
    },
    "nepal-immersion-totale-culture-vie-sauvage-et-aventure": {
        "short_id": "nepal-immersion-totale",
        "badge": "🔥 Promo -300€",
        "badge_color": "bg-fire-600",
        "rating": "4.9",
        "reviews": 42,
        "difficulty": "Dynamique",
        "style": "Immersion 360°",
        "category": "safari chitwan culture",
        "radar": {"wildlife": 5, "nature": 5, "culture": 5, "relax": 2, "nightlife": 1}
    },
    "deep-into-the-wild-babai-special-experience-5-jours": {
        "short_id": "babai-special",
        "badge": "⚡ Aventure ++",
        "badge_color": "bg-emerald-700",
        "rating": "5.0",
        "reviews": 19,
        "difficulty": "Aventurier",
        "style": "Tracking Tigre & Bivouac",
        "category": "safari bivouac",
        "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 1, "nightlife": 0}
    },
    "chitwan-bardia-laventure-jungle-complete": {
        "short_id": "chitwan-bardia-complete",
        "badge": "🌿 Double Safari Parcs",
        "badge_color": "bg-jungle-800",
        "rating": "4.9",
        "reviews": 33,
        "difficulty": "Modéré",
        "style": "Le Grand Safari Népalais",
        "category": "safari chitwan",
        "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}
    },
    "tiji-festival-tour-upper-mustang": {
        "short_id": "tiji-mustang",
        "badge": "🕉️ Spécial Culture",
        "badge_color": "bg-purple-800",
        "rating": "5.0",
        "reviews": 12,
        "difficulty": "Modéré",
        "style": "Himalaya & Culture Sacrée",
        "category": "trek culture",
        "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 2, "nightlife": 0}
    },
    "nepal-special-carnet-de-voyage": {
        "short_id": "carnet-de-voyage",
        "badge": "🎨 Spécial Dessin & Carnet",
        "badge_color": "bg-amber-700",
        "rating": "5.0",
        "reviews": 16,
        "difficulty": "Accessible",
        "style": "Art, Nature & Croquis",
        "category": "culture art",
        "radar": {"wildlife": 4, "nature": 5, "culture": 5, "relax": 4, "nightlife": 1}
    },
    "jungle-extreme-special-faune-sauvage": {
        "short_id": "jungle-extreme",
        "badge": "🐅 Passion Faune Pro",
        "badge_color": "bg-fire-700",
        "rating": "5.0",
        "reviews": 21,
        "difficulty": "Intense",
        "style": "Immersion & Photographie",
        "category": "safari bivouac",
        "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 1, "nightlife": 0}
    },
    "nepal-sauvage-de-la-jungle-aux-montagnes-sacrees": {
        "short_id": "nepal-sauvage",
        "badge": "❤️ Coup de cœur",
        "badge_color": "bg-jungle-800",
        "rating": "4.9",
        "reviews": 38,
        "difficulty": "Modéré",
        "style": "Safari 360° & Culture",
        "category": "safari culture trek",
        "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}
    },
    "immersion-spirituelle-en-himalaya": {
        "short_id": "immersion-spirituelle",
        "badge": "🧘 Retraite & Méditation",
        "badge_color": "bg-teal-800",
        "rating": "4.9",
        "reviews": 17,
        "difficulty": "Doux",
        "style": "Retraite Spirituelle & Yoga",
        "category": "culture spiritualite",
        "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 5, "nightlife": 0}
    }
}

def generate_dots(val):
    dots = ""
    for i in range(5):
        if i < val:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-jungle-800"></span>'
        else:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-slate-300"></span>'
    return dots

# WeRoad Page Template
template_str = """<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Jungle Nepal Adventure</title>
  <meta name="description" content="{overview}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title} | Jungle Nepal Adventure">
  <meta property="og:description" content="{overview}">
  <meta property="og:image" content="{hero_img}">
  <meta property="og:type" content="website">

  <!-- Google Fonts: Plus Jakarta Sans + Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Inter"', 'sans-serif'],
            heading: ['"Plus Jakarta Sans"', 'sans-serif'],
          }},
          colors: {{
            jungle: {{
              50: '#f2f8f5',
              100: '#e1efe8',
              200: '#c5dfd3',
              300: '#9ac5b5',
              400: '#6aa692',
              500: '#468974',
              600: '#346f5e',
              700: '#2a594c',
              800: '#165c45',
              900: '#0f4332',
              950: '#08261d',
            }},
            fire: {{
              50: '#fff7ed',
              100: '#ffedd5',
              200: '#fed7aa',
              300: '#fdba74',
              400: '#fb923c',
              500: '#f97316',
              600: '#ea580c',
              700: '#c2410c',
              800: '#9a3412',
            }},
            sand: {{
              50: '#faf8f5',
              100: '#f4ede4',
              200: '#e8dbca',
              300: '#d7c2a7',
              400: '#c4a682',
            }}
          }},
          boxShadow: {{
            'weroad': '0 12px 32px -4px rgba(8, 38, 29, 0.12), 0 4px 12px -2px rgba(8, 38, 29, 0.06)',
            'weroad-hover': '0 20px 40px -4px rgba(8, 38, 29, 0.2), 0 8px 16px -2px rgba(8, 38, 29, 0.1)',
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-white text-slate-800 font-sans antialiased selection:bg-jungle-800 selection:text-white">

  <!-- TOP ANNOUNCEMENT BAR -->
  <aside aria-label="Bannière promo" class="bg-gradient-to-r from-jungle-950 via-jungle-900 to-jungle-800 text-white text-xs sm:text-sm py-2 px-4 sticky top-0 z-50 border-b border-white/10">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span class="inline-flex items-center justify-center bg-fire-600 text-white text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full animate-pulse">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-200 hidden sm:inline">
          🇳🇵 <strong>Dernières places disponibles</strong> pour ce départ !
        </span>
        <span class="text-amber-300 font-semibold">
          -100€ avec le code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs">
        <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
        <span>WhatsApp direct : <strong>+33 6 95 41 32 27</strong></span>
      </a>
    </div>
  </aside>

  <!-- NAVBAR STICKY -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-9 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
      
      <!-- Logo -->
      <a href="../index.html" class="flex items-center gap-3 group">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-jungle-700 to-jungle-950 flex items-center justify-center text-emerald-400 border border-emerald-500/30 group-hover:scale-105 transition-transform shadow-md">
          <i data-lucide="footprints" class="w-5 h-5"></i>
        </div>
        <div class="flex flex-col">
          <span class="font-heading font-black text-base sm:text-lg tracking-tight text-jungle-950 leading-none">
            JUNGLE NEPAL
          </span>
          <span class="text-[9px] font-bold tracking-widest text-emerald-700 uppercase mt-0.5">
            Adventure • Retour accueil
          </span>
        </div>
      </a>

      <!-- Quick Nav Links -->
      <nav class="hidden md:flex items-center gap-6 text-sm font-heading font-semibold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-jungle-800 transition-colors">Tous les 14 circuits</a>
        <a href="#itineraire" class="hover:text-jungle-800 transition-colors">Itinéraire</a>
        <a href="#inclus" class="hover:text-jungle-800 transition-colors">Inclus & Extras</a>
        <a href="#avis" class="hover:text-jungle-800 transition-colors">Avis voyageurs</a>
        <a href="#faq" class="hover:text-jungle-800 transition-colors">FAQ</a>
      </nav>

      <!-- Right Action CTA -->
      <div class="flex items-center gap-3">
        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-fire-600 hover:bg-fire-500 text-white text-xs sm:text-sm font-heading font-bold px-4 sm:px-5 py-2.5 rounded-full shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <i data-lucide="calendar" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN TOUR CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-slate-500 font-medium mb-4 overflow-x-auto whitespace-nowrap">
      <a href="../index.html" class="hover:text-jungle-800 flex items-center gap-1">
        <i data-lucide="home" class="w-3.5 h-3.5"></i>
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="../index.html#prochains-departs" class="hover:text-jungle-800">Nos 14 Séjours</a>
      <span>›</span>
      <span class="text-slate-800 font-bold truncate">{title}</span>
    </nav>

    <!-- Header Title & Badges Row -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6">
      <div>
        <h1 class="font-heading font-black text-2xl sm:text-4xl lg:text-5xl text-jungle-950 tracking-tight leading-tight">
          {title}
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-slate-700 bg-sand-100 px-3 py-1 rounded-full">
            <i data-lucide="sun" class="w-4 h-4 text-amber-500"></i>
            <span>{duration}</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-800 font-bold px-3 py-1 rounded-full border border-emerald-200">
            <div class="flex text-amber-400">
              <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400"></i>
            </div>
            <span>{rating} ({reviews} avis vérifiés)</span>
          </div>
          <span class="text-xs font-bold {badge_color} text-white px-3 py-1 rounded-full">
            {badge}
          </span>
        </div>
      </div>

      <!-- Action Share / Wishlist Buttons -->
      <div class="flex items-center gap-2 shrink-0">
        <button onclick="navigator.clipboard.writeText(window.location.href); alert('Lien copié dans le presse-papiers !');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition-colors">
          <i data-lucide="share-2" class="w-4 h-4 text-slate-500"></i>
          <span>Partager</span>
        </button>
        <button onclick="this.classList.toggle('text-fire-600'); this.classList.toggle('bg-fire-50');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition-colors">
          <i data-lucide="heart" class="w-4 h-4 text-slate-500"></i>
          <span>Favoris</span>
        </button>
      </div>
    </div>

    <!-- PHOTO MOSAIC GALLERY (WeRoad Style) -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[440px] mb-8 relative">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="{hero_img}" alt="{title}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="{gallery_img_1}" alt="{title}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="{gallery_img_2}" alt="{title}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="{gallery_img_3}" alt="{title}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-heading font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105">
        <i data-lucide="images" class="w-4 h-4 text-jungle-800"></i>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- STICKY SUB-NAV -->
    <div class="sticky top-[73px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-heading font-bold text-slate-600">
        <a href="#apercu" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Aperçu</a>
        <a href="#pour-moi" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Profil Voyage</a>
        <a href="#itineraire" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Itinéraire Jour par Jour ({days_count} jours)</a>
        <a href="#inclus" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Inclus & Extras</a>
        <a href="#avis" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">Avis</a>
        <a href="#faq" class="hover:text-jungle-800 transition-colors pb-1 border-b-2 border-transparent hover:border-jungle-800">FAQ</a>
      </div>
    </div>

    <!-- 2-COLUMN MAIN GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT COLUMN -->
      <div class="lg:col-span-8 space-y-12">
        
        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
            {overview}
          </p>

          <!-- Key Highlights Box -->
          <div class="bg-sand-50 rounded-3xl p-6 sm:p-8 border border-sand-200">
            <h3 class="font-heading font-bold text-lg text-jungle-950 mb-4 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-5 h-5 text-amber-500"></i>
              <span>Les temps forts du voyage</span>
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-slate-700">
              {highlights_html}
            </ul>
          </div>
        </section>

        <!-- SECTION 2: CE VOYAGE EST POUR MOI ? -->
        <section id="pour-moi" class="pt-6 border-t border-slate-200">
          <h2 class="font-heading font-extrabold text-2xl text-jungle-950 mb-6">
            Ce voyage est-il fait pour moi ?
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200/80">
            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🐅</span> Faune & Pistage</span>
                <div class="flex gap-1.5">{radar_wildlife}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🌿</span> Nature & Aventure</span>
                <div class="flex gap-1.5">{radar_nature}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🛕</span> Culture & Vie locale</span>
                <div class="flex gap-1.5">{radar_culture}</div>
              </div>
            </div>

            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🧘</span> Relax & Contemplation</span>
                <div class="flex gap-1.5">{radar_relax}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🎉</span> Fête & Soirée</span>
                <div class="flex gap-1.5">{radar_nightlife}</div>
              </div>
              <div class="pt-2 border-t border-slate-200 flex items-center justify-between text-sm font-semibold">
                <span class="text-slate-500">Effort physique :</span>
                <span class="text-jungle-800 bg-emerald-50 px-2.5 py-0.5 rounded-full">{difficulty}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION 3: ITINÉRAIRE -->
        <section id="itineraire" class="pt-6 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-heading font-extrabold text-2xl sm:text-3xl text-jungle-950">
                Itinéraire détaillé ({days_count} jours)
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Programme jour par jour conçu et encadré par nos pisteurs et guides natifs.
              </p>
            </div>
            <button onclick="toggleAllDays()" class="text-xs font-bold text-jungle-800 hover:text-fire-600 transition-colors">
              Tout déplier / replier
            </button>
          </div>

          <div class="space-y-3">
            {days_html}
          </div>
        </section>

        <!-- SECTION 4: INCLUS & EXTRAS -->
        <section id="inclus" class="pt-8 border-t border-slate-200">
          <h2 class="font-heading font-extrabold text-2xl sm:text-3xl text-jungle-950 mb-6">
            Ce qui est inclus dans votre séjour
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="bg-emerald-50/70 p-6 sm:p-8 rounded-3xl border border-emerald-200">
              <h3 class="font-heading font-bold text-base text-emerald-900 mb-4 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600"></i>
                <span>Inclus dans le prix</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-emerald-950">
                <li class="flex items-start gap-2"><span>✓</span><span>Tous les hébergements (lodges traditionnels ou tentes de bivouac)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Pension complète en jungle (3 repas sains et locaux par jour)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Vols intérieurs & transports privés mentionnés au programme</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Permis d'entrée aux Parcs Nationaux et taxes de conservation</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Accompagnement par des pisteurs d'élite certifiés (Pawan / Kiran)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Assistance et coordination 24h/24 en français (Robin)</span></li>
              </ul>
            </div>

            <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200">
              <h3 class="font-heading font-bold text-base text-slate-800 mb-4 flex items-center gap-2">
                <i data-lucide="x-circle" class="w-5 h-5 text-slate-400"></i>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-600">
                <li class="flex items-start gap-2"><span>✕</span><span>Vols internationaux aller-retour (Paris/Europe - Katmandou)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Frais de visa népalais (environ 30$ à 50$ à l'arrivée)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Boissons alcoolisées et dépenses personnelles</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Assurance voyage personnelle obligatoire</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Pourboires pour les équipes locales</span></li>
              </ul>
            </div>
          </div>
        </section>

        <!-- SECTION 5: AVIS -->
        <section id="avis" class="pt-8 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-heading font-extrabold text-2xl sm:text-3xl text-jungle-950">
                Avis sur ce circuit
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Note globale <strong>{rating} / 5</strong> sur Google Reviews ({reviews} avis)
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="bg-sand-50 p-5 rounded-2xl border border-slate-200 text-xs sm:text-sm space-y-3">
              <div class="flex text-amber-400 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
              </div>
              <p class="italic text-slate-700">« Une aventure exceptionnelle avec des guides qui connaissent la jungle comme leur poche. Les rencontres avec la faune et les villageois resteront inoubliables. »</p>
              <p class="font-bold text-jungle-950">— Voyageur vérifié Google Reviews</p>
            </div>

            <div class="bg-sand-50 p-5 rounded-2xl border border-slate-200 text-xs sm:text-sm space-y-3">
              <div class="flex text-amber-400 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
              </div>
              <p class="italic text-slate-700">« Une organisation sans faille, un respect total des animaux et une ambiance incroyable en petit groupe. Je recommande à 100% Jungle Nepal Adventure ! »</p>
              <p class="font-bold text-jungle-950">— Explorateur Népal 2025/2026</p>
            </div>
          </div>
        </section>

        <!-- SECTION 6: FAQ -->
        <section id="faq" class="pt-8 border-t border-slate-200">
          <h2 class="font-heading font-extrabold text-2xl text-jungle-950 mb-6">
            Questions fréquentes sur ce voyage
          </h2>

          <div class="space-y-3 text-sm">
            <details class="group bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <summary class="font-heading font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment se passe la réservation et le paiement ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
                Pour bloquer votre place, un acompte de 30% est demandé par carte bancaire ou virement sécurisé. Le solde restant est réglé avant le départ ou à votre arrivée à Katmandou.
              </p>
            </details>

            <details class="group bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <summary class="font-heading font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment sont composés les groupes ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
                Nos séjours sont exclusivement limités à 4 à 8 personnes pour préserver le silence en forêt, maximiser les chances d'observer les animaux et garantir une cohésion chaleureuse.
              </p>
            </details>

            <details class="group bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <summary class="font-heading font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Quel est le niveau physique requis ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
                Ce circuit est classé <strong>{difficulty}</strong>. Nos guides adaptent le rythme pour que chacun profite pleinement de l'expérience en toute sécurité.
              </p>
            </details>
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: STICKY BOOKING CARD -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-28 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-weroad space-y-6">
          
          <div>
            <span class="text-[11px] font-heading font-bold uppercase tracking-wider text-jungle-800">{style}</span>
            <h3 class="font-heading font-extrabold text-xl text-jungle-950 mt-1">
              {title}
            </h3>
            <p class="text-xs text-slate-500 mt-1">{duration} • Petit groupe (4 à 8 pers)</p>
          </div>

          <!-- Price Row -->
          <div class="pt-4 border-t border-slate-100 flex items-baseline justify-between">
            <div>
              <p class="text-[11px] font-semibold uppercase text-slate-400">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-heading font-black text-3xl text-jungle-950">{price_display}</span>
                {original_price_html}
              </div>
            </div>
            {discount_badge_html}
          </div>

          <!-- Departures Selector List -->
          <div class="space-y-2.5">
            <label class="block text-xs font-heading font-bold uppercase tracking-wider text-slate-600">
              Sélectionnez une date de départ :
            </label>
            <div class="space-y-2">
              <label class="flex items-center justify-between p-3 rounded-2xl border border-jungle-800 bg-emerald-50/50 cursor-pointer transition-all text-xs">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Automne 2026" checked class="text-jungle-800 focus:ring-jungle-700">
                  <div>
                    <p class="font-bold text-slate-800">10 Oct - 24 Oct 2026</p>
                    <p class="text-[10px] text-slate-500">4 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-emerald-800">Confirmé</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all text-xs">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Novembre 2026" class="text-jungle-800 focus:ring-jungle-700">
                  <div>
                    <p class="font-bold text-slate-800">07 Nov - 21 Nov 2026</p>
                    <p class="text-[10px] text-slate-500">2 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-fire-700">Dernières places</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all text-xs">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Printemps 2027" class="text-jungle-800 focus:ring-jungle-700">
                  <div>
                    <p class="font-bold text-slate-800">15 Mars - 29 Mars 2027</p>
                    <p class="text-[10px] text-slate-500">6 places disponibles</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-emerald-800">Saison tigres</span>
              </label>
            </div>
          </div>

          <!-- Primary CTA Button -->
          <button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-heading font-black text-base shadow-xl shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all text-center">
            Réserver ma place →
          </button>

          <!-- Reassurance Micro-Copy -->
          <div class="space-y-2 text-xs text-slate-500 pt-2 border-t border-slate-100">
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Acompte de 30% seulement à la réservation</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Annulation sans frais jusqu'à 30 jours</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Paiement 100% sécurisé (CB / Virement)</span>
            </div>
          </div>

          <!-- Extra Quick Links -->
          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2.5 text-xs">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20j'ai%20une%20question%20sur%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-emerald-50 text-emerald-800 font-bold hover:bg-emerald-100 transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4 text-emerald-600"></i>
              <span>Poser une question sur WhatsApp</span>
            </a>
            <a href="tel:+33695413227" class="flex items-center justify-center gap-2 py-2 rounded-xl text-slate-600 hover:text-slate-900 font-semibold transition-colors">
              <i data-lucide="phone" class="w-3.5 h-3.5"></i>
              <span>Appeler Robin au +33 6 95 41 32 27</span>
            </a>
          </div>

        </div>
      </div>

    </div>

  </main>

  <!-- MODAL: BOOKING -->
  <div id="booking-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative animate-fade-in text-slate-900 max-h-[90vh] overflow-y-auto">
      <button onclick="closeBookingForm()" class="absolute top-5 right-5 p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-2xl bg-fire-100 text-fire-600 flex items-center justify-center">
          <i data-lucide="ticket" class="w-5 h-5"></i>
        </div>
        <div>
          <h3 class="font-heading font-black text-xl text-jungle-950">
            Réservation • {title}
          </h3>
          <p class="text-xs text-slate-500">À partir de {price_display} / personne</p>
        </div>
      </div>

      <form onsubmit="handleBookingSubmit(event)" class="space-y-4 text-sm mt-4">
        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Date choisie</label>
          <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <option>10 Oct - 24 Oct 2026 (4 places restantes)</option>
            <option>07 Nov - 21 Nov 2026 (2 places restantes)</option>
            <option>15 Mars - 29 Mars 2027 (6 places disponibles)</option>
            <option>Dates sur-mesure / privatisé</option>
          </select>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Voyageurs</label>
            <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
              <option>1 voyageur</option>
              <option selected>2 voyageurs</option>
              <option>3 voyageurs</option>
              <option>4 voyageurs et +</option>
            </select>
          </div>
          <div>
            <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Chambre</label>
            <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
              <option>Double / Twin (inclus)</option>
              <option>Individuelle (+ supplément)</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Vos coordonnées</label>
          <div class="grid grid-cols-2 gap-3 mb-3">
            <input type="text" placeholder="Prénom & Nom" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <input type="tel" placeholder="Téléphone / WhatsApp" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
          </div>
          <input type="email" placeholder="Adresse email" required class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
        </div>

        <button type="submit" class="w-full py-4 rounded-2xl bg-fire-600 hover:bg-fire-500 text-white font-heading font-black text-base shadow-xl shadow-fire-600/30">
          Confirmer ma pré-réservation (Sans frais) →
        </button>
      </form>
    </div>
  </div>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 hidden bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
    <button onclick="closeLightbox()" class="absolute top-6 right-6 text-white p-2 hover:bg-white/10 rounded-full">
      <i data-lucide="x" class="w-7 h-7"></i>
    </button>
    <img id="lightbox-img" src="" alt="Photo agrandie" class="max-w-4xl max-h-[85vh] object-contain rounded-2xl shadow-2xl">
  </div>

  <script>
    lucide.createIcons();

    const allImages = [
      "{hero_img}",
      "{gallery_img_1}",
      "{gallery_img_2}",
      "{gallery_img_3}"
    ];

    function openLightbox(index) {{
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      img.src = allImages[index] || allImages[0];
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      document.getElementById('lightbox-modal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function toggleAllDays() {{
      const accordions = document.querySelectorAll('details.day-accordion');
      const allOpen = Array.from(accordions).every(a => a.open);
      accordions.forEach(a => a.open = !allOpen);
    }}

    function scrollToBooking() {{
      document.getElementById('booking-widget').scrollIntoView({{ behavior: 'smooth' }});
    }}

    function openBookingForm() {{
      document.getElementById('booking-modal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeBookingForm() {{
      document.getElementById('booking-modal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function handleBookingSubmit(e) {{
      e.preventDefault();
      alert('🎉 Pré-réservation enregistrée avec succès ! Robin et Pawan prennent contact avec vous sous 24h.');
      closeBookingForm();
    }}
  </script>
</body>
</html>
"""

processed_tours = []

for tour in raw_data:
    slug = tour["slug"]
    meta = meta_map.get(slug, {
        "short_id": slug,
        "badge": "Circuit Immersif",
        "badge_color": "bg-jungle-800",
        "rating": "4.9",
        "reviews": 20,
        "difficulty": "Modéré",
        "style": "Immersion & Faune",
        "category": "safari",
        "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}
    })

    # Images
    default_imgs = [
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920-600x800.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ]
    imgs = tour.get("images", [])
    while len(imgs) < 4:
        imgs.append(default_imgs[len(imgs) % len(default_imgs)])

    # Highlights
    hl_list = tour.get("highlights", [])
    if not hl_list:
        hl_list = [
            "Accompagnement exclusif par nos guides et pisteurs natifs certifiés",
            "Petits groupes de 4 à 8 voyageurs maximum pour une discrétion absolue en milieu sauvage",
            "Immersion authentique et respectueuse des populations locales et de la faune"
        ]
    highlights_html = "".join([f'<li class="flex items-start gap-2.5"><i data-lucide="check-circle" class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5"></i><span>{h}</span></li>' for h in hl_list])

    # Days
    days_data = tour.get("days", [])
    if not days_data:
        days_data = [{"title": f"Jour {i+1} – Découverte & Immersion", "desc": "Programme d'immersion préparé par nos pisteurs locaux."} for i in range(5)]
    
    days_html = ""
    for i, d in enumerate(days_data):
        is_open = "open" if i < 2 else ""
        days_html += f"""
        <details class="day-accordion group bg-white rounded-2xl border border-slate-200/90 shadow-sm p-4 sm:p-5 transition-all" {is_open}>
          <summary class="font-heading font-bold text-sm sm:text-base text-jungle-950 cursor-pointer flex items-center justify-between gap-3 list-none">
            <div class="flex items-center gap-3">
              <span class="w-8 h-8 rounded-xl bg-sand-100 text-jungle-800 font-black text-xs flex items-center justify-center shrink-0 border border-sand-200">
                {i+1}
              </span>
              <span>{d['title']}</span>
            </div>
            <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 group-open:rotate-180 transition-transform shrink-0"></i>
          </summary>
          <div class="mt-4 pl-11 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
            <p>{d['desc']}</p>
          </div>
        </details>
        """

    # Price
    price_val = tour.get("price_discount") or tour.get("price_original") or "Sur devis"
    orig_val = tour.get("price_original") if tour.get("price_discount") else None

    orig_html = f'<span class="text-sm text-slate-400 line-through">{orig_val}</span>' if orig_val else ""
    disc_html = '<span class="text-xs font-bold text-fire-600 bg-fire-50 px-2.5 py-1 rounded-full border border-fire-200">Promo Saison</span>' if orig_val else ""

    overview_clean = tour.get("overview") or "Vivez une aventure authentique au cœur du Népal sauvage."

    page_html = template_str.format(
        title=tour["title"],
        title_encoded=tour["title"].replace(" ", "%20"),
        overview=overview_clean,
        duration=tour["duration"],
        days_count=len(days_data),
        price_display=price_val,
        original_price_html=orig_html,
        discount_badge_html=disc_html,
        badge=meta["badge"],
        badge_color=meta["badge_color"],
        rating=meta["rating"],
        reviews=meta["reviews"],
        difficulty=meta["difficulty"],
        style=meta["style"],
        hero_img=imgs[0],
        gallery_img_1=imgs[1],
        gallery_img_2=imgs[2],
        gallery_img_3=imgs[3],
        highlights_html=highlights_html,
        days_html=days_html,
        radar_wildlife=generate_dots(meta["radar"]["wildlife"]),
        radar_nature=generate_dots(meta["radar"]["nature"]),
        radar_culture=generate_dots(meta["radar"]["culture"]),
        radar_relax=generate_dots(meta["radar"]["relax"]),
        radar_nightlife=generate_dots(meta["radar"]["nightlife"])
    )

    # Save to short_id.html and slug.html
    short_filename = f"{meta['short_id']}.html"
    slug_filename = f"{slug}.html"

    out_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
    with open(os.path.join(out_dir, short_filename), 'w', encoding='utf-8') as f:
        f.write(page_html)
    
    if short_filename != slug_filename:
        with open(os.path.join(out_dir, slug_filename), 'w', encoding='utf-8') as f:
            f.write(page_html)

    processed_tours.append({
        "slug": slug,
        "short_id": meta["short_id"],
        "title": tour["title"],
        "duration": tour["duration"],
        "price": price_val,
        "original_price": orig_val,
        "badge": meta["badge"],
        "badge_color": meta["badge_color"],
        "rating": meta["rating"],
        "reviews": meta["reviews"],
        "category": meta["category"],
        "hero_img": imgs[0],
        "overview": overview_clean,
        "link": f"tours/{meta['short_id']}.html"
    })

print(f"Generated all {len(processed_tours)} tour pages!")

# Save metadata for index generator
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'w', encoding='utf-8') as f:
    json.dump(processed_tours, f, indent=2, ensure_ascii=False)
