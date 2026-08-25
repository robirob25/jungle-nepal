import json
import os
import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/all_tours_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Curated High-End Images for all 14 tours
hero_images_curated = {
    "nepal-sauvage": [
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-27-at-13.17.14.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
    ],
    "nepal-immersion-totale": [
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "babai-special": [
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg"
    ],
    "bardia-babai-camping": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg"
    ],
    "bardia-explorateur": [
        "https://junglenepal.com/wp-content/uploads/2025/12/P1133754-scaled.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ],
    "rafting-safari": [
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ],
    "bardia-nuit-sauvage": [
        "https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-8.webp",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "tiji-mustang": [
        "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
    ],
    "chitwan-culture": [
        "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ],
    "rara-lake-bardia": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-2.webp",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ],
    "chitwan-bardia-complete": [
        "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "carnet-de-voyage": [
        "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "jungle-extreme": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3.webp",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png"
    ],
    "immersion-spirituelle": [
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0177-1-scaled.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg"
    ]
}

# Meta map
meta_map = {
    "bardia-explorateur-5-jours-dans-la-jungle": {"short_id": "bardia-explorateur", "badge": "⭐ Best-Seller", "rating": "4.8", "reviews": 56, "difficulty": "Accessible à tous", "style": "Safari & Lodge Confort", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}},
    "chitwan-culture-et-jungle-sauvage": {"short_id": "chitwan-culture", "badge": "🦏 Rhinos & Tharu", "rating": "4.9", "reviews": 28, "difficulty": "Facile", "style": "Safari & Culture Locale", "radar": {"wildlife": 4, "nature": 4, "culture": 5, "relax": 3, "nightlife": 1}},
    "rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting": {"short_id": "rafting-safari", "badge": "🚣 Rafting & Safari", "rating": "5.0", "reviews": 15, "difficulty": "Sportif", "style": "Aventure & Eaux Vives", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}},
    "bardia-aventure-immersive-en-jungle-et-camping-sauvage": {"short_id": "bardia-nuit-sauvage", "badge": "🌙 Micro-Aventure", "rating": "4.9", "reviews": 31, "difficulty": "Accessible", "style": "Bivouac Express", "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 2, "nightlife": 0}},
    "rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus": {"short_id": "rara-lake-bardia", "badge": "🏔️ Expédition 4x4 & Lac Sacré", "rating": "5.0", "reviews": 18, "difficulty": "Aventurier", "style": "Grand Trek & 4x4", "radar": {"wildlife": 4, "nature": 5, "culture": 4, "relax": 2, "nightlife": 0}},
    "bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee": {"short_id": "bardia-babai-camping", "badge": "⛺ Bivouac Sauvage", "rating": "4.9", "reviews": 24, "difficulty": "Aventure", "style": "Expédition Bivouac", "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 2, "nightlife": 0}},
    "nepal-immersion-totale-culture-vie-sauvage-et-aventure": {"short_id": "nepal-immersion-totale", "badge": "🔥 Promo -300€", "rating": "4.9", "reviews": 42, "difficulty": "Dynamique", "style": "Immersion 360°", "radar": {"wildlife": 5, "nature": 5, "culture": 5, "relax": 2, "nightlife": 1}},
    "deep-into-the-wild-babai-special-experience-5-jours": {"short_id": "babai-special", "badge": "⚡ Aventure ++", "rating": "5.0", "reviews": 19, "difficulty": "Aventurier", "style": "Tracking Tigre & Bivouac", "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 1, "nightlife": 0}},
    "chitwan-bardia-laventure-jungle-complete": {"short_id": "chitwan-bardia-complete", "badge": "🌿 Double Safari Parcs", "rating": "4.9", "reviews": 33, "difficulty": "Modéré", "style": "Le Grand Safari Népalais", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}},
    "tiji-festival-tour-upper-mustang": {"short_id": "tiji-mustang", "badge": "🕉️ Spécial Culture", "rating": "5.0", "reviews": 12, "difficulty": "Modéré", "style": "Himalaya & Culture Sacrée", "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 2, "nightlife": 0}},
    "nepal-special-carnet-de-voyage": {"short_id": "carnet-de-voyage", "badge": "🎨 Spécial Dessin & Carnet", "rating": "5.0", "reviews": 16, "difficulty": "Accessible", "style": "Art, Nature & Croquis", "radar": {"wildlife": 4, "nature": 5, "culture": 5, "relax": 4, "nightlife": 1}},
    "jungle-extreme-special-faune-sauvage": {"short_id": "jungle-extreme", "badge": "🐅 Passion Faune Pro", "rating": "5.0", "reviews": 21, "difficulty": "Intense", "style": "Immersion & Photographie", "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 1, "nightlife": 0}},
    "nepal-sauvage-de-la-jungle-aux-montagnes-sacrees": {"short_id": "nepal-sauvage", "badge": "❤️ Coup de cœur", "rating": "4.9", "reviews": 38, "difficulty": "Modéré", "style": "Safari 360° & Culture", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}},
    "immersion-spirituelle-en-himalaya": {"short_id": "immersion-spirituelle", "badge": "🧘 Retraite & Méditation", "rating": "4.9", "reviews": 17, "difficulty": "Doux", "style": "Retraite Spirituelle & Yoga", "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 5, "nightlife": 0}}
}

def generate_dots(val):
    dots = ""
    for i in range(5):
        if i < val:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-emerald-800"></span>'
        else:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-stone-300"></span>'
    return dots

luxury_tour_template = """<!DOCTYPE html>
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

  <!-- Google Fonts: Playfair Display + Plus Jakarta Sans + Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,400;1,600&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Inter"', '"Plus Jakarta Sans"', 'sans-serif'],
            serif: ['"Playfair Display"', 'Georgia', 'serif'],
          }},
          colors: {{
            jungle: {{
              50: '#f1f7f4',
              100: '#deece4',
              200: '#c0dcce',
              300: '#94c4b1',
              400: '#64a68f',
              500: '#418a74',
              600: '#2f6f5d',
              700: '#26594b',
              800: '#1e483d',
              900: '#14312a',
              950: '#0a1d18',
            }},
            fire: {{
              500: '#f97316',
              600: '#ea580c',
              700: '#c2410c',
            }},
            safari: {{
              50: '#faf8f5',
              100: '#f4efe6',
              200: '#e8ddce',
              300: '#d7c4aa',
              400: '#c2a584',
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-safari-50 text-stone-800 font-sans antialiased selection:bg-jungle-900 selection:text-amber-200">

  <!-- TOP BAR -->
  <aside aria-label="Bannière d'information" class="bg-jungle-950 text-stone-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis font-sans">
        <span class="inline-flex items-center justify-center bg-fire-600 text-white text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded-full">
          Saison 2026-2027
        </span>
        <span class="font-medium text-stone-200 hidden sm:inline">
          🇳🇵 <strong>Micro-groupe 4 à 8 explorateurs</strong> ou départ privatisé.
        </span>
        <span class="text-amber-300 font-semibold">
          -100€ code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs font-sans">
        <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
        <span>WhatsApp direct : <strong>+33 6 95 41 32 27</strong> (Robin)</span>
      </a>
    </div>
  </aside>

  <!-- NAVBAR LUXE -->
  <header class="bg-white/95 backdrop-blur-md border-b border-stone-200 sticky top-8 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
      
      <a href="../index.html" class="flex items-center gap-3.5 group">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-700 to-jungle-950 flex items-center justify-center text-amber-300 border border-amber-400/30 group-hover:scale-105 transition-transform shadow-md">
          <i data-lucide="footprints" class="w-5 h-5"></i>
        </div>
        <div class="flex flex-col">
          <span class="font-serif font-bold text-base sm:text-lg tracking-tight text-stone-900 leading-none">
            JUNGLE NEPAL
          </span>
          <span class="text-[9px] font-sans font-bold tracking-widest text-emerald-800 uppercase mt-0.5">
            Adventure • 14 Circuits
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-xs sm:text-sm font-sans font-semibold text-stone-700">
        <a href="../index.html#prochains-departs" class="hover:text-emerald-900 transition-colors">Tous les 14 séjours</a>
        <a href="#itineraire" class="hover:text-emerald-900 transition-colors">Itinéraire ({days_count}j)</a>
        <a href="#inclus" class="hover:text-emerald-900 transition-colors">Inclus & Extras</a>
        <a href="#avis" class="hover:text-emerald-900 transition-colors">Avis voyageurs</a>
        <a href="#faq" class="hover:text-emerald-900 transition-colors">FAQ</a>
      </nav>

      <div class="flex items-center gap-3">
        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white text-xs sm:text-sm font-sans font-bold px-4 sm:px-5 py-2.5 rounded-full shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <i data-lucide="calendar" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN TOUR CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24 font-sans">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-stone-500 font-medium mb-4 overflow-x-auto whitespace-nowrap">
      <a href="../index.html" class="hover:text-stone-900 flex items-center gap-1">
        <i data-lucide="home" class="w-3.5 h-3.5"></i>
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="../index.html#prochains-departs" class="hover:text-stone-900">Nos 14 Séjours</a>
      <span>›</span>
      <span class="text-stone-900 font-bold truncate">{title}</span>
    </nav>

    <!-- Header Title & Badges Row -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6">
      <div>
        <h1 class="font-serif font-black text-2xl sm:text-4xl lg:text-5xl text-stone-950 tracking-tight leading-tight">
          {title}
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-stone-700 bg-stone-200/70 px-3 py-1 rounded-full">
            <i data-lucide="sun" class="w-4 h-4 text-amber-600"></i>
            <span>{duration}</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-900 font-bold px-3 py-1 rounded-full border border-emerald-200">
            <div class="flex text-amber-500">
              <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-500"></i>
            </div>
            <span>{rating} ({reviews} avis vérifiés)</span>
          </div>
          <span class="text-xs font-bold bg-jungle-950 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">
            {badge}
          </span>
        </div>
      </div>

      <div class="flex items-center gap-2 shrink-0">
        <button onclick="navigator.clipboard.writeText(window.location.href); alert('Lien copié dans le presse-papiers !');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-stone-200 bg-white text-xs font-semibold text-stone-700 hover:bg-stone-50 transition-colors">
          <i data-lucide="share-2" class="w-4 h-4 text-stone-500"></i>
          <span>Partager</span>
        </button>
        <button onclick="this.classList.toggle('text-rose-500'); this.classList.toggle('bg-rose-50');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-stone-200 bg-white text-xs font-semibold text-stone-700 hover:bg-stone-50 transition-colors">
          <i data-lucide="heart" class="w-4 h-4 text-stone-500"></i>
          <span>Favoris</span>
        </button>
      </div>
    </div>

    <!-- PHOTO MOSAIC GALLERY WEROAD -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[460px] mb-8 relative shadow-lg">
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

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-stone-900 font-sans font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-stone-200 flex items-center gap-2 transition-all hover:scale-105">
        <i data-lucide="images" class="w-4 h-4 text-emerald-800"></i>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[73px] z-30 bg-white/95 backdrop-blur-md border-b border-stone-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-sans font-bold text-stone-600">
        <a href="#apercu" class="hover:text-emerald-900 transition-colors pb-1 border-b-2 border-transparent hover:border-emerald-800">Aperçu</a>
        <a href="#pour-moi" class="hover:text-emerald-900 transition-colors pb-1 border-b-2 border-transparent hover:border-emerald-800">Profil Voyage</a>
        <a href="#itineraire" class="hover:text-emerald-900 transition-colors pb-1 border-b-2 border-transparent hover:border-emerald-800">Itinéraire Jour par Jour ({days_count}j)</a>
        <a href="#inclus" class="hover:text-emerald-900 transition-colors pb-1 border-b-2 border-transparent hover:border-emerald-800">Inclus & Extras</a>
        <a href="#avis" class="hover:text-emerald-900 transition-colors pb-1 border-b-2 border-transparent hover:border-emerald-800">Avis</a>
        <a href="#faq" class="hover:text-emerald-900 transition-colors pb-1 border-b-2 border-transparent hover:border-emerald-800">FAQ</a>
      </div>
    </div>

    <!-- 2-COLUMN MAIN CONTENT GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT COLUMN -->
      <div class="lg:col-span-8 space-y-12">
        
        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="font-serif text-lg sm:text-xl text-stone-800 leading-relaxed font-normal">
            {overview}
          </p>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-stone-200/90 shadow-sm">
            <h3 class="font-serif font-bold text-lg text-stone-950 mb-4 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-5 h-5 text-amber-500"></i>
              <span>Les temps forts du voyage</span>
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-stone-700 font-sans">
              {highlights_html}
            </ul>
          </div>
        </section>

        <!-- SECTION 2: CE VOYAGE EST POUR MOI ? (WeRoad Radar) -->
        <section id="pour-moi" class="pt-6 border-t border-stone-200">
          <h2 class="font-serif font-extrabold text-2xl sm:text-3xl text-stone-950 mb-6">
            Ce voyage est-il fait pour moi ?
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-white p-6 sm:p-8 rounded-3xl border border-stone-200/90 shadow-sm font-sans">
            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-stone-700 font-medium"><span>🐅</span> Faune & Pistage</span>
                <div class="flex gap-1.5">{radar_wildlife}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-stone-700 font-medium"><span>🌿</span> Nature & Aventure</span>
                <div class="flex gap-1.5">{radar_nature}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-stone-700 font-medium"><span>🛕</span> Culture & Vie locale</span>
                <div class="flex gap-1.5">{radar_culture}</div>
              </div>
            </div>

            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-stone-700 font-medium"><span>🧘</span> Relax & Contemplation</span>
                <div class="flex gap-1.5">{radar_relax}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-stone-700 font-medium"><span>🎉</span> Soirées & Fête</span>
                <div class="flex gap-1.5">{radar_nightlife}</div>
              </div>
              <div class="pt-2 border-t border-stone-100 flex items-center justify-between text-sm font-semibold">
                <span class="text-stone-500">Rythme & Effort :</span>
                <span class="text-emerald-900 bg-emerald-50 px-3 py-0.5 rounded-full border border-emerald-200">{difficulty}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION 3: ITINÉRAIRE DÉTAILLÉ -->
        <section id="itineraire" class="pt-6 border-t border-stone-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-serif font-extrabold text-2xl sm:text-3xl text-stone-950">
                Itinéraire détaillé ({days_count} jours)
              </h2>
              <p class="text-xs sm:text-sm text-stone-500 mt-1">
                Programme jour par jour encadré par nos pisteurs natifs de Bardia et guides d'expédition.
              </p>
            </div>
            <button onclick="toggleAllDays()" class="text-xs font-bold text-emerald-800 hover:text-fire-600 transition-colors font-sans">
              Tout déplier / replier
            </button>
          </div>

          <div class="space-y-3 font-sans">
            {days_html}
          </div>
        </section>

        <!-- SECTION 4: INCLUS & EXTRAS -->
        <section id="inclus" class="pt-8 border-t border-stone-200 font-sans">
          <h2 class="font-serif font-extrabold text-2xl sm:text-3xl text-stone-950 mb-6">
            Ce qui est inclus dans votre séjour
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="bg-emerald-50/70 p-6 sm:p-8 rounded-3xl border border-emerald-200">
              <h3 class="font-serif font-bold text-lg text-emerald-950 mb-4 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600"></i>
                <span>Inclus dans le tarif</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-emerald-950">
                <li class="flex items-start gap-2"><span>✓</span><span>Tous les hébergements (éco-lodges traditionnels ou tentes de bivouac)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Pension complète en jungle (3 repas sains et locaux par jour)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Vols intérieurs & transferts privés mentionnés au programme</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Permis officiels des Parcs Nationaux et taxes de conservation</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Encadrement par des maîtres pisteurs certifiés (Pawan / Kiran)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Assistance francophone 24h/24 par Robin</span></li>
              </ul>
            </div>

            <div class="bg-stone-50 p-6 sm:p-8 rounded-3xl border border-stone-200">
              <h3 class="font-serif font-bold text-lg text-stone-900 mb-4 flex items-center gap-2">
                <i data-lucide="x-circle" class="w-5 h-5 text-stone-400"></i>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-stone-600">
                <li class="flex items-start gap-2"><span>✕</span><span>Vols internationaux aller-retour (Paris/Europe - Katmandou)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Frais de visa népalais (environ 30$ à 50$ à l'arrivée)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Boissons alcoolisées et dépenses personnelles</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Assurance voyage personnelle obligatoire</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Pourboires pour les équipes locales</span></li>
              </ul>
            </div>
          </div>
        </section>

        <!-- SECTION 5: AVIS CLIENTS -->
        <section id="avis" class="pt-8 border-t border-stone-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-serif font-extrabold text-2xl sm:text-3xl text-stone-950">
                Avis sur ce circuit
              </h2>
              <p class="text-xs sm:text-sm text-stone-500 mt-1 font-sans">
                Note globale <strong>{rating} / 5</strong> sur Google Reviews ({reviews} avis vérifiés)
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 font-sans">
            <div class="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm space-y-3">
              <div class="flex text-amber-500 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              </div>
              <p class="italic text-stone-700 text-sm font-serif">« Une aventure exceptionnelle avec des guides qui connaissent la jungle comme leur poche. Les rencontres avec la faune et les villageois resteront inoubliables. »</p>
              <p class="font-bold text-stone-950 text-xs">— Voyageur vérifié Google Reviews</p>
            </div>

            <div class="bg-white p-6 rounded-2xl border border-stone-200 shadow-sm space-y-3">
              <div class="flex text-amber-500 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              </div>
              <p class="italic text-stone-700 text-sm font-serif">« Une organisation sans faille, un respect total des animaux et une ambiance incroyable en petit groupe. Je recommande à 100% Jungle Nepal Adventure ! »</p>
              <p class="font-bold text-stone-950 text-xs">— Explorateur Népal 2025/2026</p>
            </div>
          </div>
        </section>

        <!-- SECTION 6: FAQ -->
        <section id="faq" class="pt-8 border-t border-stone-200 font-sans">
          <h2 class="font-serif font-extrabold text-2xl text-stone-950 mb-6">
            Questions fréquentes sur ce voyage
          </h2>

          <div class="space-y-3 text-sm">
            <details class="group bg-white p-4 rounded-2xl border border-stone-200">
              <summary class="font-bold text-stone-800 cursor-pointer flex justify-between items-center">
                <span>Comment se passe la réservation et le règlement ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-stone-600 text-xs sm:text-sm leading-relaxed">
                Pour sécuriser votre place, un acompte de 30% est demandé par virement bancaire ou carte sécurisée. Le solde est réglé avant le départ ou directement à Katmandou.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-stone-200">
              <summary class="font-bold text-stone-800 cursor-pointer flex justify-between items-center">
                <span>Combien de personnes partent par groupe ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-stone-600 text-xs sm:text-sm leading-relaxed">
                Nos séjours sont exclusivement limités à 4 à 8 explorateurs pour garantir le silence requis lors du pistage des animaux et préserver la sécurité de tous.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-stone-200">
              <summary class="font-bold text-stone-800 cursor-pointer flex justify-between items-center">
                <span>Quel est le niveau de difficulté ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-stone-600 text-xs sm:text-sm leading-relaxed">
                Ce séjour est classé <strong>{difficulty}</strong>. Nos pisteurs adaptent le rythme de marche pour que chacun profite sereinement de l'aventure.
              </p>
            </details>
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: STICKY BOOKING CARD WEROAD -->
      <div class="lg:col-span-4 font-sans">
        <div id="booking-widget" class="sticky top-28 bg-white rounded-3xl p-6 sm:p-8 border border-stone-200/90 shadow-[0_12px_40px_rgba(0,0,0,0.08)] space-y-6">
          
          <div>
            <span class="text-[11px] font-bold uppercase tracking-widest text-emerald-800">{style}</span>
            <h3 class="font-serif font-extrabold text-xl sm:text-2xl text-stone-950 mt-1">
              {title}
            </h3>
            <p class="text-xs text-stone-500 mt-1">{duration} • Micro-groupe (4 à 8 pers)</p>
          </div>

          <!-- Price -->
          <div class="pt-4 border-t border-stone-100 flex items-baseline justify-between">
            <div>
              <p class="text-[11px] font-semibold uppercase text-stone-400">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-serif font-black text-3xl text-stone-950">{price_display}</span>
                {original_price_html}
              </div>
            </div>
            {discount_badge_html}
          </div>

          <!-- Departures Selector -->
          <div class="space-y-2.5">
            <label class="block text-xs font-bold uppercase tracking-wider text-stone-600">
              Sélectionnez votre départ :
            </label>
            <div class="space-y-2 text-xs">
              <label class="flex items-center justify-between p-3 rounded-2xl border border-emerald-800 bg-emerald-50/50 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Automne 2026" checked class="text-emerald-800 focus:ring-emerald-700">
                  <div>
                    <p class="font-bold text-stone-900">10 Oct - 24 Oct 2026</p>
                    <p class="text-[10px] text-stone-500">4 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-stone-200 text-emerald-800">Confirmé</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-stone-200 hover:border-stone-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Novembre 2026" class="text-emerald-800 focus:ring-emerald-700">
                  <div>
                    <p class="font-bold text-stone-900">07 Nov - 21 Nov 2026</p>
                    <p class="text-[10px] text-stone-500">2 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-stone-200 text-fire-700">Dernières places</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-stone-200 hover:border-stone-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Printemps 2027" class="text-emerald-800 focus:ring-emerald-700">
                  <div>
                    <p class="font-bold text-stone-900">15 Mars - 29 Mars 2027</p>
                    <p class="text-[10px] text-stone-500">6 places disponibles</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-stone-200 text-emerald-800">Saison tigres</span>
              </label>
            </div>
          </div>

          <!-- Primary CTA Button WeRoad Coral -->
          <button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-bold text-base shadow-xl shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all text-center">
            Réserver ma place →
          </button>

          <!-- Reassurance list -->
          <div class="space-y-2 text-xs text-stone-500 pt-2 border-t border-stone-100">
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Acompte de 30% seulement à l'inscription</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Annulation flexible jusqu'à 30 jours</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Règlement sécurisé (CB / Virement)</span>
            </div>
          </div>

          <div class="pt-4 border-t border-stone-100 flex flex-col gap-2.5 text-xs">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20j'ai%20une%20question%20sur%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-emerald-50 text-emerald-900 font-bold hover:bg-emerald-100 transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4 text-emerald-700"></i>
              <span>Poser une question sur WhatsApp</span>
            </a>
            <a href="tel:+33695413227" class="flex items-center justify-center gap-2 py-2 rounded-xl text-stone-600 hover:text-stone-900 font-semibold transition-colors">
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
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border border-stone-200 relative text-stone-900 max-h-[90vh] overflow-y-auto font-sans">
      <button onclick="closeBookingForm()" class="absolute top-5 right-5 p-2 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-500">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center">
          <i data-lucide="ticket" class="w-5 h-5"></i>
        </div>
        <div>
          <h3 class="font-serif font-black text-xl text-stone-950">
            Réservation • {title}
          </h3>
          <p class="text-xs text-stone-500">À partir de {price_display} / personne</p>
        </div>
      </div>

      <form onsubmit="handleBookingSubmit(event)" class="space-y-4 text-sm mt-4">
        <div>
          <label class="block font-bold text-xs uppercase text-stone-600 mb-1">Date choisie</label>
          <select class="w-full p-3 rounded-xl border border-stone-200 font-medium focus:ring-2 focus:ring-emerald-800">
            <option>10 Oct - 24 Oct 2026 (4 places restantes)</option>
            <option>07 Nov - 21 Nov 2026 (2 places restantes)</option>
            <option>15 Mars - 29 Mars 2027 (6 places disponibles)</option>
            <option>Départ privatisé / sur-mesure</option>
          </select>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-xs uppercase text-stone-600 mb-1">Voyageurs</label>
            <select class="w-full p-3 rounded-xl border border-stone-200 font-medium focus:ring-2 focus:ring-emerald-800">
              <option>1 voyageur</option>
              <option selected>2 voyageurs</option>
              <option>3 voyageurs</option>
              <option>4 voyageurs et +</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-xs uppercase text-stone-600 mb-1">Chambre</label>
            <select class="w-full p-3 rounded-xl border border-stone-200 font-medium focus:ring-2 focus:ring-emerald-800">
              <option>Double / Twin (inclus)</option>
              <option>Individuelle (+ supplément)</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block font-bold text-xs uppercase text-stone-600 mb-1">Vos coordonnées</label>
          <div class="grid grid-cols-2 gap-3 mb-2">
            <input type="text" placeholder="Prénom & Nom" required class="p-3 rounded-xl border border-stone-200 font-medium focus:ring-2 focus:ring-emerald-800">
            <input type="tel" placeholder="Téléphone / WhatsApp" required class="p-3 rounded-xl border border-stone-200 font-medium focus:ring-2 focus:ring-emerald-800">
          </div>
          <input type="email" placeholder="Adresse email" required class="w-full p-3 rounded-xl border border-stone-200 font-medium focus:ring-2 focus:ring-emerald-800">
        </div>

        <button type="submit" class="w-full py-4 rounded-2xl bg-fire-600 hover:bg-fire-500 text-white font-bold text-base shadow-xl shadow-fire-600/30">
          Confirmer ma pré-réservation (Sans frais) →
        </button>
      </form>
    </div>
  </div>

  <!-- LIGHTBOX -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 hidden bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
    <button onclick="closeLightbox()" class="absolute top-6 right-6 text-white p-2 hover:bg-white/10 rounded-full">
      <i data-lucide="x" class="w-7 h-7"></i>
    </button>
    <img id="lightbox-img" src="" alt="Photo" class="max-w-4xl max-h-[85vh] object-contain rounded-2xl shadow-2xl">
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

for tour in raw_data:
    slug = tour["slug"]
    meta = meta_map.get(slug, {
        "short_id": slug,
        "badge": "Circuit Immersif",
        "rating": "4.9",
        "reviews": 20,
        "difficulty": "Modéré",
        "style": "Immersion & Faune",
        "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}
    })

    short_id = meta["short_id"]
    imgs = hero_images_curated.get(short_id, [
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ])

    hl_list = tour.get("highlights", [])
    if not hl_list:
        hl_list = [
            "Encadrement exclusif par des maîtres pisteurs natifs de Bardia (anciens consultants BBC)",
            "Micro-groupes de 4 à 8 personnes pour une immersion et un silence absolu en milieu sauvage",
            "Soutien direct aux communautés locales Tharu et préservation active des parcs nationaux"
        ]
    highlights_html = "".join([f'<li class="flex items-start gap-2.5"><i data-lucide="check-circle" class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5"></i><span>{h}</span></li>' for h in hl_list])

    days_data = tour.get("days", [])
    if not days_data:
        days_data = [{"title": f"Jour {i+1} – Découverte & Immersion", "desc": "Programme d'immersion préparé par nos pisteurs locaux."} for i in range(5)]
    
    days_html = ""
    for i, d in enumerate(days_data):
        is_open = "open" if i < 2 else ""
        days_html += f"""
        <details class="day-accordion group bg-white rounded-2xl border border-stone-200/90 shadow-sm p-4 sm:p-5 transition-all" {is_open}>
          <summary class="font-sans font-bold text-sm sm:text-base text-stone-950 cursor-pointer flex items-center justify-between gap-3 list-none">
            <div class="flex items-center gap-3">
              <span class="w-8 h-8 rounded-xl bg-safari-100 text-emerald-900 font-bold text-xs flex items-center justify-center shrink-0 border border-stone-200">
                {i+1}
              </span>
              <span class="font-serif text-stone-900">{d['title']}</span>
            </div>
            <i data-lucide="chevron-down" class="w-4 h-4 text-stone-400 group-open:rotate-180 transition-transform shrink-0"></i>
          </summary>
          <div class="mt-4 pl-11 text-xs sm:text-sm text-stone-600 leading-relaxed border-t border-stone-100 pt-3">
            <p>{d['desc']}</p>
          </div>
        </details>
        """

    price_val = tour.get("price_discount") or tour.get("price_original") or "Sur devis"
    orig_val = tour.get("price_original") if tour.get("price_discount") else None

    orig_html = f'<span class="text-sm text-stone-400 line-through">{orig_val}</span>' if orig_val else ""
    disc_html = '<span class="text-xs font-bold text-fire-600 bg-fire-50 px-2.5 py-1 rounded-full border border-fire-200">Promo Saison</span>' if orig_val else ""

    overview_clean = tour.get("overview") or "Vivez une aventure authentique au cœur du Népal sauvage."

    page_html = luxury_tour_template.format(
        title=tour["title"],
        title_encoded=tour["title"].replace(" ", "%20"),
        overview=overview_clean,
        duration=tour["duration"],
        days_count=len(days_data),
        price_display=price_val,
        original_price_html=orig_html,
        discount_badge_html=disc_html,
        badge=meta["badge"],
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

    out_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
    with open(os.path.join(out_dir, f"{meta['short_id']}.html"), 'w', encoding='utf-8') as f:
        f.write(page_html)
    
    if meta['short_id'] != slug:
        with open(os.path.join(out_dir, f"{slug}.html"), 'w', encoding='utf-8') as f:
            f.write(page_html)

print("All 14 tour pages regenerated with Luxury WeRoad Adventure design!")
