import json
import os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

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

# 1. GENERATE HOMEPAGE (100% WeRoad Font Stack: Plus Jakarta Sans / Google Sans / Inter)
cards_html = ""
for t in tours:
    short_id = t["short_id"]
    if short_id in hero_images_curated:
        t["hero_img"] = hero_images_curated[short_id][0]

    orig_price_html = f'<span class="text-xs text-slate-400 line-through font-normal">{t["original_price"]}</span>' if t.get("original_price") else ""
    discount_tag = '<span class="text-[10px] font-extrabold text-amber-900 bg-amber-100 px-2 py-0.5 rounded-full border border-amber-200">Promo</span>' if t.get("original_price") else ""

    cards_html += f"""
        <!-- TRIP CARD: {t['title']} -->
        <article class="trip-card group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,36,25,0.16)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between" data-category="{t['category']}" data-title="{t['title'].lower()}">
          
          <div class="relative">
            <a href="{t['link']}" class="relative h-72 sm:h-80 overflow-hidden block">
              <img 
                src="{t['hero_img']}" 
                alt="{t['title']}" 
                class="w-full h-full object-cover group-hover:scale-108 transition-transform duration-500 ease-out"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent"></div>
              
              <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-10">
                <span class="inline-flex items-center gap-1.5 bg-jungle-950/90 backdrop-blur-md text-amber-300 font-extrabold text-xs px-3 py-1 rounded-full border border-amber-400/30 shadow-md">
                  <span>{t['badge']}</span>
                </span>
                <span class="bg-black/40 backdrop-blur-md text-slate-200 text-xs px-2.5 py-1 rounded-full border border-white/15 font-semibold">
                  4-8 pers.
                </span>
              </div>

              <button onclick="event.preventDefault(); this.classList.toggle('text-rose-500'); this.classList.toggle('fill-rose-500');" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-black/40 backdrop-blur-md border border-white/20 flex items-center justify-center text-white hover:bg-white hover:text-rose-500 transition-all z-10" aria-label="Favoris">
                <i data-lucide="heart" class="w-4 h-4"></i>
              </button>

              <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white text-xs z-10">
                <div class="flex items-center gap-1.5 bg-black/50 backdrop-blur-md px-3 py-1.5 rounded-full border border-white/15">
                  <i data-lucide="calendar" class="w-3.5 h-3.5 text-amber-400"></i>
                  <span class="font-bold text-slate-100">{t['duration']}</span>
                </div>
                <div class="flex items-center gap-1 bg-amber-500 text-jungle-950 font-black px-2.5 py-1 rounded-full shadow">
                  <i data-lucide="star" class="w-3 h-3 fill-jungle-950"></i>
                  <span>{t['rating']} ({t['reviews']})</span>
                </div>
              </div>
            </a>
          </div>

          <div class="p-6 sm:p-7 flex-1 flex flex-col justify-between bg-gradient-to-b from-white to-slate-50/50">
            <div>
              <div class="text-[11px] font-extrabold uppercase tracking-widest text-emerald-800 mb-1.5 flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-600"></span>
                <span>Népal Sauvage • Éco-Safari</span>
              </div>
              <h3 class="font-black text-xl sm:text-[22px] text-slate-900 group-hover:text-emerald-900 transition-colors leading-snug tracking-tight">
                <a href="{t['link']}">{t['title']}</a>
              </h3>
              <p class="mt-3 text-sm text-slate-600 line-clamp-2 leading-relaxed font-normal">
                {t['overview']}
              </p>
            </div>

            <div class="mt-6 pt-5 border-t border-slate-200/70 flex items-end justify-between">
              <div>
                <p class="text-[11px] uppercase tracking-wider font-bold text-slate-400">À partir de</p>
                <div class="flex items-baseline gap-2 mt-0.5">
                  <span class="font-black text-2xl sm:text-3xl text-jungle-950 tracking-tight">{t['price']}</span>
                  {orig_price_html}
                  {discount_tag}
                </div>
                <p class="text-[11px] text-emerald-800 font-bold mt-0.5 flex items-center gap-1">
                  <i data-lucide="check" class="w-3 h-3 text-emerald-600"></i>
                  <span>Départs Confirmés 2026/2027</span>
                </p>
              </div>

              <a href="{t['link']}" class="inline-flex items-center gap-2 px-5 py-3 rounded-full bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-extrabold text-xs sm:text-sm shadow-md shadow-fire-600/20 hover:shadow-lg hover:shadow-fire-600/35 hover:scale-[1.03] active:scale-95 transition-all">
                <span>Voir le voyage</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

        </article>
    """

homepage_html = f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jungle Nepal Adventure – Safaris Sauvages, Tigres du Bengale & Treks au Népal</title>
  <meta name="description" content="Explorez le Népal sauvage et authentique en micro-groupes (4 à 8 pers). 14 séjours d'exception : safaris à pied à Bardia, tracking du tigre du Bengale, bivouacs en jungle et immersion himalayenne.">

  <!-- Open Graph -->
  <meta property="og:title" content="Jungle Nepal Adventure – Safaris & Expéditions Sauvages">
  <meta property="og:description" content="14 séjours immersifs au royaume du tigre du Bengale. Encadrement exclusif par les maîtres pisteurs de Bardia.">
  <meta property="og:image" content="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg">
  <meta property="og:type" content="website">

  <!-- WeRoad Exact Font: Plus Jakarta Sans (Regular, Medium, SemiBold, Bold, ExtraBold, Black) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
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
              600: '#ea580c', // WeRoad coral CTA
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
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .no-scrollbar::-webkit-scrollbar {{ display: none; }}
    .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
  </style>
</head>
<body class="bg-safari-50 text-slate-800 font-sans antialiased selection:bg-jungle-900 selection:text-amber-200">

  <!-- 1. TOP ANNOUNCEMENT BAR -->
  <aside aria-label="Bannière d'information" class="bg-jungle-950 text-slate-200 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis font-bold">
        <span class="inline-flex items-center justify-center bg-fire-600 text-white text-[10px] font-black uppercase tracking-widest px-2 py-0.5 rounded-full">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-300 hidden sm:inline">
          🇳🇵 <strong>14 séjours en micro-groupes (4 à 8 pers.)</strong> et privatisations sur-mesure.
        </span>
        <span class="text-amber-300 font-bold">
          • Réduction -100€ code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>

      <div class="flex items-center gap-4 shrink-0 font-medium">
        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20vos%20safaris%20au%20Népal" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs">
          <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
          <span>WhatsApp : <strong>+33 6 95 41 32 27</strong> (Robin)</span>
        </a>
      </div>
    </div>
  </aside>

  <!-- 2. NAVBAR LUXE IMMERSIVE -->
  <header id="main-nav" class="fixed top-8 left-0 right-0 z-40 transition-all duration-300 py-3.5 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto">
      <div id="nav-container" class="flex items-center justify-between px-6 py-3 rounded-2xl transition-all duration-300 bg-jungle-950/80 backdrop-blur-xl border border-white/15 text-white shadow-2xl">
        
        <!-- Logo -->
        <a href="#" class="flex items-center gap-3.5 group">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-600 to-jungle-950 flex items-center justify-center text-amber-300 border border-amber-400/30 group-hover:scale-105 transition-transform shadow-md">
            <i data-lucide="footprints" class="w-5 h-5"></i>
          </div>
          <div class="flex flex-col">
            <span class="font-black text-lg sm:text-xl tracking-tight text-white leading-none">
              JUNGLE NEPAL
            </span>
            <span class="text-[9px] font-extrabold tracking-widest text-amber-300 uppercase mt-0.5">
              Adventure • 14 Circuits
            </span>
          </div>
        </a>

        <!-- Links -->
        <nav class="hidden lg:flex items-center gap-1 text-sm font-bold text-slate-200">
          <a href="#prochains-departs" class="px-4 py-2 rounded-full hover:bg-white/10 transition-colors flex items-center gap-1.5">
            <span>Les 14 Séjours</span>
            <span class="bg-fire-600 text-white text-[10px] font-black px-2 py-0.2 rounded-full">14</span>
          </a>
          <a href="#concept" class="px-4 py-2 rounded-full hover:bg-white/10 transition-colors">
            L'Esprit Safari Sauvage
          </a>
          <a href="#pisteurs" class="px-4 py-2 rounded-full hover:bg-white/10 transition-colors">
            Maîtres Pisteurs (BBC)
          </a>
          <a href="#avis" class="px-4 py-2 rounded-full hover:bg-white/10 transition-colors flex items-center gap-1">
            <span>Avis</span>
            <span class="text-amber-400 text-xs">★ 4.9/5</span>
          </a>
        </nav>

        <!-- Right Action Buttons -->
        <div class="flex items-center gap-3">
          <button onclick="openCustomTripModal()" class="hidden sm:flex items-center gap-1.5 px-4 py-2 rounded-full text-xs font-bold bg-white/10 hover:bg-white/20 border border-white/20 transition-all text-slate-200 hover:text-white">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-300"></i>
            <span>Privatisation & Sur-mesure</span>
          </button>

          <a href="#prochains-departs" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white text-xs sm:text-sm font-black px-5 py-2.5 rounded-full shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
            <span>Explorer les départs</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </a>

          <button onclick="toggleMobileMenu()" class="lg:hidden p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white" aria-label="Menu">
            <i data-lucide="menu" class="w-5 h-5"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Mobile Drawer -->
    <div id="mobile-menu" class="hidden lg:hidden mt-2 max-w-7xl mx-auto">
      <div class="bg-jungle-950/95 backdrop-blur-2xl border border-white/15 rounded-2xl p-5 text-white space-y-4 shadow-2xl">
        <nav class="flex flex-col space-y-2 font-bold text-base">
          <a href="#prochains-departs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10 flex items-center justify-between">
            <span>🐾 Tous les 14 circuits 2026/2027</span>
            <span class="bg-fire-600 text-xs px-2 py-0.5 rounded-full font-black">14</span>
          </a>
          <a href="#concept" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            🧭 L'Esprit Jungle & Éthique
          </a>
          <a href="#pisteurs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            🐅 Nos Maîtres Pisteurs (BBC)
          </a>
          <a href="#avis" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            ⭐ Avis Voyageurs Vérifiés (4.9/5)
          </a>
        </nav>
        <div class="pt-3 border-t border-white/10 flex flex-col gap-2">
          <button onclick="toggleMobileMenu(); openCustomTripModal()" class="w-full py-3 rounded-xl bg-fire-600 font-black text-sm text-center shadow-lg shadow-fire-600/30">
            Créer mon séjour sur-mesure ✨
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- 3. HERO SECTION HAUTE COUTURE (WeRoad Vibe) -->
  <section class="relative min-h-screen flex items-center justify-center pt-32 pb-24 px-4 sm:px-6 lg:px-8 overflow-hidden bg-jungle-950">
    <div class="absolute inset-0 z-0">
      <img 
        src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" 
        alt="Tigre du Bengale dans le Parc National de Bardia au Népal" 
        class="w-full h-full object-cover object-center scale-105 filter brightness-90 contrast-105"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-jungle-950 via-jungle-950/65 to-black/60"></div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center">
      
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-amber-400/30 text-slate-100 text-xs sm:text-sm font-semibold mb-6 shadow-xl">
        <span class="flex h-2 w-2 rounded-full bg-amber-400 animate-ping"></span>
        <span class="text-amber-300 font-extrabold tracking-wider uppercase text-[11px]">Expéditions & Safaris Éco-Responsables</span>
        <span class="text-white/40">•</span>
        <span class="text-slate-200 flex items-center gap-1 font-bold">
          <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i> 4.9/5 (100% Avis Vérifiés)
        </span>
      </div>

      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl lg:text-8xl text-white tracking-tight leading-[1.05] max-w-4xl drop-shadow-2xl">
        L'Appel Sauvage <br/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-amber-300 to-amber-100">
          du Népal Secret.
        </span>
      </h1>

      <p class="mt-6 text-base sm:text-xl text-slate-200 max-w-2xl font-medium leading-relaxed drop-shadow">
        Safaris à pied dans les territoires inviolés de Bardia, tracking du tigre du Bengale et bivouacs sous la canopée. En micro-groupes de <strong>4 à 8 explorateurs</strong>.
      </p>

      <!-- WeRoad Floating Booking Search Bar -->
      <div class="w-full max-w-4xl mt-10 p-3 sm:p-4 rounded-3xl bg-white/95 backdrop-blur-2xl shadow-[0_20px_60px_rgba(0,0,0,0.35)] border border-white/50 text-left text-slate-900">
        <form onsubmit="handleSearch(event)" class="grid grid-cols-1 md:grid-cols-12 gap-3 items-center">
          
          <div class="md:col-span-4 p-3 rounded-2xl hover:bg-slate-100/80 transition-colors cursor-pointer border border-slate-200/60 md:border-transparent">
            <label class="block text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
              Expérience recherchée
            </label>
            <div class="flex items-center gap-2 mt-1">
              <i data-lucide="compass" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <select id="search-dest" class="w-full bg-transparent font-black text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer">
                <option value="all">Tous les 14 circuits</option>
                <option value="safari">Tigres & Jungle de Bardia (Pistage à pied)</option>
                <option value="bivouac">Bivouac & Camping Sauvage (Babai)</option>
                <option value="chitwan">Chitwan (Rhinocéros & Pirogue)</option>
                <option value="trek">Haut-Mustang & Lac Rara (Himalaya)</option>
                <option value="rafting">Rivières Sauvages Karnali (Rafting)</option>
                <option value="culture">Culture Tharu, Yoga & Carnet de Dessin</option>
              </select>
            </div>
          </div>

          <div class="hidden md:block w-[1px] h-10 bg-slate-200"></div>

          <div class="md:col-span-4 p-3 rounded-2xl hover:bg-slate-100/80 transition-colors cursor-pointer border border-slate-200/60 md:border-transparent">
            <label class="block text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
              Période de départ
            </label>
            <div class="flex items-center gap-2 mt-1">
              <i data-lucide="calendar" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <select id="search-date" class="w-full bg-transparent font-black text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer">
                <option value="all">Saison 2026 - 2027 (Oct - Juin)</option>
                <option value="autumn">Automne 2026 (Octobre - Décembre)</option>
                <option value="winter">Hiver 2026/2027 (Janvier - Février)</option>
                <option value="spring">Printemps 2027 (Mars - Mai • Pic d'observation)</option>
              </select>
            </div>
          </div>

          <div class="md:col-span-3 flex items-center">
            <button type="submit" class="w-full h-14 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-black text-base rounded-2xl flex items-center justify-center gap-2 shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
              <i data-lucide="search" class="w-5 h-5"></i>
              <span>Rechercher</span>
            </button>
          </div>

        </form>
      </div>

      <div class="mt-12 pt-8 border-t border-white/15 w-full grid grid-cols-2 md:grid-cols-4 gap-4 text-slate-200 text-left sm:text-center">
        <div class="p-3.5 rounded-2xl bg-white/5 backdrop-blur-md border border-white/10">
          <p class="font-black text-xl sm:text-2xl text-amber-300 tracking-tight">4 à 8 Max</p>
          <p class="text-xs text-slate-300 font-medium mt-0.5">Silence & discrétion totale</p>
        </div>
        <div class="p-3.5 rounded-2xl bg-white/5 backdrop-blur-md border border-white/10">
          <p class="font-black text-xl sm:text-2xl text-emerald-400 tracking-tight">BBC Wildlife</p>
          <p class="text-xs text-slate-300 font-medium mt-0.5">Consultants documentaires faune</p>
        </div>
        <div class="p-3.5 rounded-2xl bg-white/5 backdrop-blur-md border border-white/10">
          <p class="font-black text-xl sm:text-2xl text-amber-300 tracking-tight">100% Local</p>
          <p class="text-xs text-slate-300 font-medium mt-0.5">Retombées directes villages</p>
        </div>
        <div class="p-3.5 rounded-2xl bg-white/5 backdrop-blur-md border border-white/10">
          <p class="font-black text-xl sm:text-2xl text-emerald-400 tracking-tight">Sur-mesure</p>
          <p class="text-xs text-slate-300 font-medium mt-0.5">Coordinateur français (Robin)</p>
        </div>
      </div>

    </div>
  </section>

  <!-- 4. CATEGORIES FILTER CAROUSEL -->
  <section id="categories" class="py-6 bg-white border-b border-slate-200/80 sticky top-[70px] z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1">
        
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-jungle-950 text-amber-300 font-bold text-xs sm:text-sm whitespace-nowrap shadow-sm hover:scale-105 transition-all" data-filter="all">
          <i data-lucide="compass" class="w-4 h-4"></i>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="safari">
          <span>🐅</span>
          <span>Safaris & Pistage Bardia</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="bivouac">
          <span>⛺</span>
          <span>Bivouacs & Nuits Sauvages</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="chitwan">
          <span>🦏</span>
          <span>Chitwan & Rhinocéros</span>
        </button>

        <button onclick="filterTrips('trek')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="trek">
          <span>🏔️</span>
          <span>Treks & Lac Rara</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="culture">
          <span>🕉️</span>
          <span>Culture, Yoga & Carnet de Voyage</span>
        </button>

        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting Karnali</span>
        </button>

      </div>
    </div>
  </section>

  <!-- 5. LES 14 CIRCUITS WEROAD -->
  <section id="prochains-departs" class="py-16 sm:py-24 bg-safari-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
        <div>
          <div class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wider text-emerald-900 bg-emerald-100 px-3 py-1 rounded-full mb-3">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-emerald-700"></i>
            <span>Départs Garantis • Petits Groupes 4-8 Explorateurs</span>
          </div>
          <h2 class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight">
            Les 14 Séjours Immersifs au Népal
          </h2>
          <p class="mt-3 text-base text-slate-600 max-w-2xl font-normal">
            Sélectionnez votre aventure pour explorer le détail jour par jour, la fiche d'inclusions et réserver votre place.
          </p>
        </div>

        <div>
          <span id="trip-count-badge" class="text-xs sm:text-sm font-extrabold text-slate-700 bg-white px-4 py-2.5 rounded-full border border-slate-200 shadow-sm">
            Affichage de <strong>14 séjours</strong>
          </span>
        </div>
      </div>

      <div id="trips-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {cards_html}
      </div>

    </div>
  </section>

  <!-- 6. SECTION L'ESPRIT SAFARI -->
  <section id="concept" class="py-20 sm:py-28 bg-jungle-950 text-white relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="inline-block text-xs font-black uppercase tracking-widest text-amber-300 bg-white/10 px-3.5 py-1 rounded-full mb-3 border border-amber-300/30">
          La Différence Jungle Nepal
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight">
          L'anti-tourisme de masse.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 leading-relaxed font-normal">
          Nous refusons les jeeps bondées et les itinéraires aseptisés. Nous proposons une connexion brute avec le monde sauvage, dans le respect sacré des animaux et des peuples du Terai.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="rounded-3xl p-8 bg-white/5 backdrop-blur-md border border-white/10 flex flex-col justify-between hover:bg-white/10 transition-all duration-300">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-amber-400/20 border border-amber-400/40 flex items-center justify-center text-amber-300 mb-6">
              <i data-lucide="eye" class="w-7 h-7"></i>
            </div>
            <h3 class="font-black text-2xl text-white tracking-tight">Le Pistage Silencieux</h3>
            <p class="mt-3 text-slate-300 text-sm leading-relaxed font-normal">
              Apprenez à déchiffrer les empreintes dans la rosée du matin, à écouter le cri d'alarme du cerf chital et à pister le tigre à pied en toute humilité.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-amber-300 font-bold flex items-center gap-1.5">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>Encadrement double pisteur d'élite</span>
          </div>
        </div>

        <div class="rounded-3xl p-8 bg-white/5 backdrop-blur-md border border-white/10 flex flex-col justify-between hover:bg-white/10 transition-all duration-300">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-emerald-400/20 border border-emerald-400/40 flex items-center justify-center text-emerald-300 mb-6">
              <i data-lucide="users" class="w-7 h-7"></i>
            </div>
            <h3 class="font-black text-2xl text-white tracking-tight">4 à 8 Voyageurs</h3>
            <p class="mt-3 text-slate-300 text-sm leading-relaxed font-normal">
              La taille idéale pour voyager entre passionnés du même état d'esprit. Une atmosphère chaleureuse au coin du feu et des souvenirs gravés à vie.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-emerald-300 font-bold flex items-center gap-1.5">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>Ambiance intime & cohésion</span>
          </div>
        </div>

        <div class="rounded-3xl p-8 bg-white/5 backdrop-blur-md border border-white/10 flex flex-col justify-between hover:bg-white/10 transition-all duration-300">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-fire-500/20 border border-fire-500/40 flex items-center justify-center text-fire-400 mb-6">
              <i data-lucide="heart-handshake" class="w-7 h-7"></i>
            </div>
            <h3 class="font-black text-2xl text-white tracking-tight">100% Impact Local</h3>
            <p class="mt-3 text-slate-300 text-sm leading-relaxed font-normal">
              Sans intermédiaire financier en Europe. Votre séjour finance directement les pisteurs indigènes Tharu, l'éducation locale et la protection des parcs.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-fire-400 font-bold flex items-center gap-1.5">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>Écotourisme certifié et éthique</span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 7. PISTEURS & ÉQUIPE -->
  <section id="pisteurs" class="py-20 sm:py-28 bg-white border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="inline-block text-xs font-black uppercase tracking-widest text-emerald-900 bg-emerald-100 px-3.5 py-1 rounded-full mb-3">
          Une Alliance Unique Népal - France
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">
          Nos Maîtres Pisteurs & Organisateurs
        </h2>
        <p class="mt-3 text-base text-slate-600">
          Plus de 20 ans d'expérience du terrain combinés à une conciergerie francophone 24h/24.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
        <div class="flex flex-col items-center text-center p-6 rounded-3xl bg-safari-50 border border-slate-200/80">
          <div class="w-36 h-36 rounded-full overflow-hidden p-1 bg-gradient-to-tr from-jungle-900 via-amber-400 to-fire-600 shadow-xl mb-6">
            <img src="https://junglenepal.com/wp-content/uploads/2025/12/1.png" alt="Pawan - Chef Pisteur" class="w-full h-full object-cover rounded-full"/>
          </div>
          <h3 class="font-black text-2xl text-slate-900 tracking-tight">Pawan</h3>
          <p class="text-xs font-extrabold text-fire-600 uppercase tracking-wider mt-1">Chef Pisteur & Expert Faune (BBC Wildlife)</p>
          <p class="mt-3 text-sm text-slate-600 leading-relaxed font-normal">
            Natif de Bardia, ancien Président de l'Association des Guides. Il a guidé les équipes documentaires de la BBC et connaît chaque recoin du sanctuaire.
          </p>
        </div>

        <div class="flex flex-col items-center text-center p-6 rounded-3xl bg-safari-50 border border-slate-200/80">
          <div class="w-36 h-36 rounded-full overflow-hidden p-1 bg-gradient-to-tr from-emerald-600 via-slate-400 to-jungle-950 shadow-xl mb-6">
            <img src="https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-1720-x-1080-px-1024x643.png" alt="Kiran" class="w-full h-full object-cover rounded-full"/>
          </div>
          <h3 class="font-black text-2xl text-slate-900 tracking-tight">Kiran</h3>
          <p class="text-xs font-extrabold text-emerald-800 uppercase tracking-wider mt-1">Co-Fondateur & Pionnier Écotourisme</p>
          <p class="mt-3 text-sm text-slate-600 leading-relaxed font-normal">
            Pionnier du tourisme d'aventure responsable au Népal depuis plus de 20 ans. Il orchestre la logistique des camps et les relations avec les villages.
          </p>
        </div>

        <div class="flex flex-col items-center text-center p-6 rounded-3xl bg-safari-50 border border-slate-200/80">
          <div class="w-36 h-36 rounded-full overflow-hidden p-1 bg-gradient-to-tr from-amber-400 via-fire-500 to-jungle-950 shadow-xl mb-6">
            <img src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png" alt="Robin" class="w-full h-full object-cover rounded-full"/>
          </div>
          <h3 class="font-black text-2xl text-slate-900 tracking-tight">Robin</h3>
          <p class="text-xs font-extrabold text-fire-600 uppercase tracking-wider mt-1">Coordinateur Voyageurs & Relations France</p>
          <p class="mt-3 text-sm text-slate-600 leading-relaxed font-normal">
            Passionné de faune sauvage. Votre contact privilégié en français avant et pendant votre voyage pour concevoir le séjour parfait.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- 8. AVIS CLIENTS -->
  <section id="avis" class="py-20 sm:py-28 bg-safari-100 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <div class="flex items-center justify-center gap-1 text-amber-500 mb-2">
          <i data-lucide="star" class="w-5 h-5 fill-amber-500"></i>
          <i data-lucide="star" class="w-5 h-5 fill-amber-500"></i>
          <i data-lucide="star" class="w-5 h-5 fill-amber-500"></i>
          <i data-lucide="star" class="w-5 h-5 fill-amber-500"></i>
          <i data-lucide="star" class="w-5 h-5 fill-amber-500"></i>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">
          Ce que disent nos explorateurs
        </h2>
        <p class="mt-3 text-base text-slate-600">
          Note globale <strong>4.9 / 5</strong> sur Google Reviews • Avis 100% Vérifiés
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="rounded-3xl p-8 bg-white border border-slate-200/90 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex text-amber-500 gap-1 mb-4">
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
            </div>
            <p class="text-slate-700 text-sm sm:text-base leading-relaxed italic font-medium">
              « Choisir Jungle Nepal Adventure pour découvrir ce pays sous l'angle de sa vie sauvage, c'est la meilleure décision. Voir des tigres et rhinos en liberté avec Pawan est magique ! »
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-jungle-900 text-amber-300 font-bold flex items-center justify-center text-sm shadow">SG</div>
            <div>
              <p class="font-bold text-sm text-slate-900">Samantha Gonthier</p>
              <p class="text-xs text-slate-500">Voyage en micro-groupe • Bardia</p>
            </div>
          </div>
        </div>

        <div class="rounded-3xl p-8 bg-white border border-slate-200/90 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex text-amber-500 gap-1 mb-4">
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
            </div>
            <p class="text-slate-700 text-sm sm:text-base leading-relaxed italic font-medium">
              « Je reviens de 15 jours au Népal... ce que je retiens avant tout, c'est l'humain. Une équipe sincère et dévouée. On ne se sent jamais comme un simple client. Une expérience rare ! »
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-fire-600 text-white font-bold flex items-center justify-center text-sm shadow">AN</div>
            <div>
              <p class="font-bold text-sm text-slate-900">Adrien Noat</p>
              <p class="text-xs text-slate-500">Circuit Népal Sauvage 15 jours</p>
            </div>
          </div>
        </div>

        <div class="rounded-3xl p-8 bg-white border border-slate-200/90 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex text-amber-500 gap-1 mb-4">
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
            </div>
            <p class="text-slate-700 text-sm sm:text-base leading-relaxed italic font-medium">
              « Un voyage gravé à vie. Séjourner chez l'habitant au milieu de la jungle de Bardia est une expérience hors du commun. Merci à toute l'équipe pour ces précieux souvenirs ! »
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-emerald-800 text-white font-bold flex items-center justify-center text-sm shadow">AP</div>
            <div>
              <p class="font-bold text-sm text-slate-900">Alice Palasti</p>
              <p class="text-xs text-slate-500">Immersion chez l'habitant & Jungle</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 9. FOOTER -->
  <footer class="bg-jungle-950 text-slate-300 pt-20 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 pb-16 border-b border-white/10 text-sm">
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-600 flex items-center justify-center text-white shadow">
              <i data-lucide="footprints" class="w-5 h-5"></i>
            </div>
            <span class="font-black text-xl text-white tracking-tight">Jungle Nepal Adventure</span>
          </div>
          <p class="text-slate-400 text-xs leading-relaxed">
            Agence locale d'écotourisme d'exception et de safaris immersifs au Népal. Katmandou & Parc National de Bardia.
          </p>
        </div>

        <div>
          <h4 class="font-black text-white text-xs uppercase tracking-widest mb-4">Contact Direct</h4>
          <p class="text-xs text-slate-300">WhatsApp / Tél : <strong>+33 6 95 41 32 27</strong></p>
          <p class="text-xs text-slate-300 mt-1">Email : <strong>contact@junglenepal.com</strong></p>
          <p class="text-xs text-slate-400 mt-2">Bardia National Park, Népal</p>
        </div>

        <div>
          <h4 class="font-black text-white text-xs uppercase tracking-widest mb-4">14 Circuits Disponibles</h4>
          <p class="text-xs text-slate-400 leading-relaxed">
            Bardia, Chitwan, Babai, Mustang, Lac Rara, Karnali Rafting, Yoga & Carnet de dessin.
          </p>
        </div>

        <div>
          <h4 class="font-black text-white text-xs uppercase tracking-widest mb-4">Garanties & Confiance</h4>
          <p class="text-xs text-slate-400 leading-relaxed">
            Acompte de 30% • Annulation flexible • Retombées 100% locales • Pisteurs certifiés BBC Wildlife.
          </p>
        </div>
      </div>

      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <p>© 2026 Jungle Nepal Adventure. Tous droits réservés.</p>
        <p class="text-amber-300 font-bold">Créé avec passion pour le Népal sauvage 🇳🇵</p>
      </div>

    </div>
  </footer>

  <!-- MODAL SUR-MESURE -->
  <div id="custom-trip-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-xl w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative text-slate-900 max-h-[90vh] overflow-y-auto">
      <button onclick="closeCustomTripModal()" class="absolute top-5 right-5 p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center">
          <i data-lucide="sparkles" class="w-5 h-5"></i>
        </div>
        <div>
          <h3 class="font-black text-2xl text-slate-950 tracking-tight">Séjour Privatisé & Sur-Mesure</h3>
          <p class="text-xs text-slate-500">Étude personnalisée sous 24h avec Robin & Pawan.</p>
        </div>
      </div>

      <form onsubmit="handleCustomTripSubmit(event)" class="space-y-4 text-sm mt-4">
        <div>
          <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Nombre de voyageurs</label>
          <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <option>1 personne (Solo)</option>
            <option selected>2 personnes (Couple / Duo)</option>
            <option>3 à 5 personnes (Famille / Amis)</option>
            <option>6 personnes et plus</option>
          </select>
        </div>

        <div>
          <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Vos coordonnées</label>
          <div class="grid grid-cols-2 gap-3 mb-2">
            <input type="text" placeholder="Nom complet" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <input type="tel" placeholder="Téléphone / WhatsApp" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
          </div>
          <input type="email" placeholder="Adresse email" required class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
        </div>

        <div>
          <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Vos envies particulières</label>
          <textarea rows="3" placeholder="Parcs souhaités, dates idéales, durée..." class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800 text-xs"></textarea>
        </div>

        <button type="submit" class="w-full py-4 rounded-2xl bg-fire-600 hover:bg-fire-500 text-white font-black text-base shadow-xl shadow-fire-600/30">
          Envoyer ma demande à l'équipe locale →
        </button>
      </form>
    </div>
  </div>

  <script>
    lucide.createIcons();

    const nav = document.getElementById('main-nav');
    const navContainer = document.getElementById('nav-container');

    window.addEventListener('scroll', () => {{
      if (window.scrollY > 40) {{
        nav.classList.add('top-0');
        nav.classList.remove('top-8');
      }} else {{
        nav.classList.remove('top-0');
        nav.classList.add('top-8');
      }}
    }});

    function toggleMobileMenu() {{
      document.getElementById('mobile-menu').classList.toggle('hidden');
    }}

    function filterTrips(category) {{
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      pills.forEach(pill => {{
        if (pill.dataset.filter === category) {{
          pill.classList.add('bg-jungle-950', 'text-amber-300');
          pill.classList.remove('bg-slate-100', 'text-slate-800');
        }} else {{
          pill.classList.remove('bg-jungle-950', 'text-amber-300');
          pill.classList.add('bg-slate-100', 'text-slate-800');
        }}
      }});

      cards.forEach(card => {{
        const cardCategories = card.dataset.category || '';
        if (category === 'all' || cardCategories.includes(category)) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      document.getElementById('trip-count-badge').innerHTML = `Affichage de <strong>${{visibleCount}} circuit${{visibleCount > 1 ? 's' : ''}}</strong>`;
    }}

    function handleSearch(e) {{
      e.preventDefault();
      const dest = document.getElementById('search-dest').value;
      filterTrips(dest);
      document.getElementById('prochains-departs').scrollIntoView({{ behavior: 'smooth' }});
    }}

    function openCustomTripModal() {{
      document.getElementById('custom-trip-modal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeCustomTripModal() {{
      document.getElementById('custom-trip-modal').classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function handleCustomTripSubmit(e) {{
      e.preventDefault();
      alert('🙏 Namasté ! Votre demande a été transmise directement à Robin et Pawan.');
      closeCustomTripModal();
    }}
  </script>
</body>
</html>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(homepage_html)

print("Homepage rewritten with Plus Jakarta Sans (WeRoad Font Stack)!")

# 2. GENERATE ALL 14 TOUR PAGES WITH WEROAD FONT
tour_page_template = """<!DOCTYPE html>
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

  <!-- WeRoad Font: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
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
  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
  </style>
</head>
<body class="bg-safari-50 text-slate-800 font-sans antialiased selection:bg-jungle-900 selection:text-amber-200">

  <!-- TOP BAR -->
  <aside aria-label="Bannière d'information" class="bg-jungle-950 text-slate-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4 font-bold">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span class="inline-flex items-center justify-center bg-fire-600 text-white text-[10px] font-black uppercase tracking-widest px-2 py-0.5 rounded-full">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-200 hidden sm:inline">
          🇳🇵 <strong>Micro-groupe 4 à 8 explorateurs</strong> ou départ privatisé.
        </span>
        <span class="text-amber-300 font-bold">
          -100€ code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs font-semibold">
        <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
        <span>WhatsApp direct : <strong>+33 6 95 41 32 27</strong> (Robin)</span>
      </a>
    </div>
  </aside>

  <!-- NAVBAR -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-8 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
      
      <a href="../index.html" class="flex items-center gap-3.5 group">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-700 to-jungle-950 flex items-center justify-center text-amber-300 border border-amber-400/30 group-hover:scale-105 transition-transform shadow-md">
          <i data-lucide="footprints" class="w-5 h-5"></i>
        </div>
        <div class="flex flex-col">
          <span class="font-black text-base sm:text-lg tracking-tight text-slate-900 leading-none">
            JUNGLE NEPAL
          </span>
          <span class="text-[9px] font-extrabold tracking-widest text-emerald-800 uppercase mt-0.5">
            Adventure • 14 Circuits
          </span>
        </div>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-xs sm:text-sm font-bold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-emerald-900 transition-colors">Tous les 14 séjours</a>
        <a href="#itineraire" class="hover:text-emerald-900 transition-colors">Itinéraire ({days_count}j)</a>
        <a href="#inclus" class="hover:text-emerald-900 transition-colors">Inclus & Extras</a>
        <a href="#avis" class="hover:text-emerald-900 transition-colors">Avis voyageurs</a>
        <a href="#faq" class="hover:text-emerald-900 transition-colors">FAQ</a>
      </nav>

      <div class="flex items-center gap-3">
        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white text-xs sm:text-sm font-black px-4 sm:px-5 py-2.5 rounded-full shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <i data-lucide="calendar" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN TOUR CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-slate-500 font-semibold mb-4 overflow-x-auto whitespace-nowrap">
      <a href="../index.html" class="hover:text-slate-900 flex items-center gap-1">
        <i data-lucide="home" class="w-3.5 h-3.5"></i>
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="../index.html#prochains-departs" class="hover:text-slate-900">Nos 14 Séjours</a>
      <span>›</span>
      <span class="text-slate-900 font-black truncate">{title}</span>
    </nav>

    <!-- Header Title & Badges Row -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6">
      <div>
        <h1 class="font-black text-2xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">
          {title}
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-slate-700 bg-slate-200/70 px-3 py-1 rounded-full">
            <i data-lucide="sun" class="w-4 h-4 text-amber-600"></i>
            <span>{duration}</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-900 font-extrabold px-3 py-1 rounded-full border border-emerald-200">
            <div class="flex text-amber-500">
              <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-500"></i>
            </div>
            <span>{rating} ({reviews} avis vérifiés)</span>
          </div>
          <span class="text-xs font-black bg-jungle-950 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">
            {badge}
          </span>
        </div>
      </div>

      <div class="flex items-center gap-2 shrink-0">
        <button onclick="navigator.clipboard.writeText(window.location.href); alert('Lien copié dans le presse-papiers !');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-slate-200 bg-white text-xs font-bold text-slate-700 hover:bg-slate-50 transition-colors">
          <i data-lucide="share-2" class="w-4 h-4 text-slate-500"></i>
          <span>Partager</span>
        </button>
        <button onclick="this.classList.toggle('text-rose-500'); this.classList.toggle('bg-rose-50');" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl border border-slate-200 bg-white text-xs font-bold text-slate-700 hover:bg-slate-50 transition-colors">
          <i data-lucide="heart" class="w-4 h-4 text-slate-500"></i>
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

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-black text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105">
        <i data-lucide="images" class="w-4 h-4 text-emerald-800"></i>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[73px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-extrabold text-slate-600">
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
          <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
            {overview}
          </p>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm">
            <h3 class="font-black text-lg text-slate-950 mb-4 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-5 h-5 text-amber-500"></i>
              <span>Les temps forts du voyage</span>
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-slate-700">
              {highlights_html}
            </ul>
          </div>
        </section>

        <!-- SECTION 2: CE VOYAGE EST POUR MOI ? (WeRoad Radar) -->
        <section id="pour-moi" class="pt-6 border-t border-slate-200">
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 mb-6 tracking-tight">
            Ce voyage est-il fait pour moi ?
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/90 shadow-sm">
            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-semibold"><span>🐅</span> Faune & Pistage</span>
                <div class="flex gap-1.5">{radar_wildlife}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-semibold"><span>🌿</span> Nature & Aventure</span>
                <div class="flex gap-1.5">{radar_nature}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-semibold"><span>🛕</span> Culture & Vie locale</span>
                <div class="flex gap-1.5">{radar_culture}</div>
              </div>
            </div>

            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-semibold"><span>🧘</span> Relax & Contemplation</span>
                <div class="flex gap-1.5">{radar_relax}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-semibold"><span>🎉</span> Soirées & Fête</span>
                <div class="flex gap-1.5">{radar_nightlife}</div>
              </div>
              <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-sm font-bold">
                <span class="text-slate-500">Rythme & Effort :</span>
                <span class="text-emerald-900 bg-emerald-50 px-3 py-0.5 rounded-full border border-emerald-200">{difficulty}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION 3: ITINÉRAIRE DÉTAILLÉ -->
        <section id="itineraire" class="pt-6 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">
                Itinéraire détaillé ({days_count} jours)
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Programme jour par jour encadré par nos pisteurs natifs de Bardia et guides d'expédition.
              </p>
            </div>
            <button onclick="toggleAllDays()" class="text-xs font-bold text-emerald-800 hover:text-fire-600 transition-colors">
              Tout déplier / replier
            </button>
          </div>

          <div class="space-y-3">
            {days_html}
          </div>
        </section>

        <!-- SECTION 4: INCLUS & EXTRAS -->
        <section id="inclus" class="pt-8 border-t border-slate-200">
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 mb-6 tracking-tight">
            Ce qui est inclus dans votre séjour
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="bg-emerald-50/70 p-6 sm:p-8 rounded-3xl border border-emerald-200">
              <h3 class="font-black text-lg text-emerald-950 mb-4 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600"></i>
                <span>Inclus dans le tarif</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-emerald-950 font-medium">
                <li class="flex items-start gap-2"><span>✓</span><span>Tous les hébergements (éco-lodges traditionnels ou tentes de bivouac)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Pension complète en jungle (3 repas sains et locaux par jour)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Vols intérieurs & transferts privés mentionnés au programme</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Permis officiels des Parcs Nationaux et taxes de conservation</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Encadrement par des maîtres pisteurs certifiés (Pawan / Kiran)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Assistance francophone 24h/24 par Robin</span></li>
              </ul>
            </div>

            <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200">
              <h3 class="font-black text-lg text-slate-900 mb-4 flex items-center gap-2">
                <i data-lucide="x-circle" class="w-5 h-5 text-slate-400"></i>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-600 font-medium">
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
        <section id="avis" class="pt-8 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">
                Avis sur ce circuit
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Note globale <strong>{rating} / 5</strong> sur Google Reviews ({reviews} avis vérifiés)
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex text-amber-500 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              </div>
              <p class="italic text-slate-700 text-sm font-medium">« Une aventure exceptionnelle avec des guides qui connaissent la jungle comme leur poche. Les rencontres avec la faune et les villageois resteront inoubliables. »</p>
              <p class="font-black text-slate-950 text-xs">— Voyageur vérifié Google Reviews</p>
            </div>

            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <div class="flex text-amber-500 gap-1">
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
                <i data-lucide="star" class="w-4 h-4 fill-amber-500"></i>
              </div>
              <p class="italic text-slate-700 text-sm font-medium">« Une organisation sans faille, un respect total des animaux et une ambiance incroyable en petit groupe. Je recommande à 100% Jungle Nepal Adventure ! »</p>
              <p class="font-black text-slate-950 text-xs">— Explorateur Népal 2025/2026</p>
            </div>
          </div>
        </section>

        <!-- SECTION 6: FAQ -->
        <section id="faq" class="pt-8 border-t border-slate-200">
          <h2 class="font-black text-2xl text-slate-950 mb-6 tracking-tight">
            Questions fréquentes sur ce voyage
          </h2>

          <div class="space-y-3 text-sm">
            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment se passe la réservation et le règlement ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Pour sécuriser votre place, un acompte de 30% est demandé par virement bancaire ou carte sécurisée. Le solde est réglé avant le départ ou directement à Katmandou.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Combien de personnes partent par groupe ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Nos séjours sont exclusivement limités à 4 à 8 explorateurs pour garantir le silence requis lors du pistage des animaux et préserver la sécurité de tous.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Quel est le niveau de difficulté ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Ce séjour est classé <strong>{difficulty}</strong>. Nos pisteurs adaptent le rythme de marche pour que chacun profite sereinement de l'aventure.
              </p>
            </details>
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: STICKY BOOKING CARD WEROAD -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-28 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-[0_12px_40px_rgba(0,0,0,0.08)] space-y-6">
          
          <div>
            <span class="text-[11px] font-extrabold uppercase tracking-widest text-emerald-800">{style}</span>
            <h3 class="font-black text-xl sm:text-2xl text-slate-950 mt-1 tracking-tight">
              {title}
            </h3>
            <p class="text-xs text-slate-500 mt-1 font-semibold">{duration} • Micro-groupe (4 à 8 pers)</p>
          </div>

          <!-- Price -->
          <div class="pt-4 border-t border-slate-100 flex items-baseline justify-between">
            <div>
              <p class="text-[11px] font-extrabold uppercase text-slate-400">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-black text-3xl text-slate-950 tracking-tight">{price_display}</span>
                {original_price_html}
              </div>
            </div>
            {discount_badge_html}
          </div>

          <!-- Departures Selector -->
          <div class="space-y-2.5">
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-600">
              Sélectionnez votre départ :
            </label>
            <div class="space-y-2 text-xs">
              <label class="flex items-center justify-between p-3 rounded-2xl border border-emerald-800 bg-emerald-50/50 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Automne 2026" checked class="text-emerald-800 focus:ring-emerald-700">
                  <div>
                    <p class="font-bold text-slate-900">10 Oct - 24 Oct 2026</p>
                    <p class="text-[10px] text-slate-500">4 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-emerald-800">Confirmé</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Novembre 2026" class="text-emerald-800 focus:ring-emerald-700">
                  <div>
                    <p class="font-bold text-slate-900">07 Nov - 21 Nov 2026</p>
                    <p class="text-[10px] text-slate-500">2 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-fire-700">Dernières places</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Printemps 2027" class="text-emerald-800 focus:ring-emerald-700">
                  <div>
                    <p class="font-bold text-slate-900">15 Mars - 29 Mars 2027</p>
                    <p class="text-[10px] text-slate-500">6 places disponibles</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-emerald-800">Saison tigres</span>
              </label>
            </div>
          </div>

          <!-- Primary CTA Button WeRoad Coral -->
          <button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-black text-base shadow-xl shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all text-center">
            Réserver ma place →
          </button>

          <!-- Reassurance list -->
          <div class="space-y-2 text-xs text-slate-500 pt-2 border-t border-slate-100 font-medium">
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

          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2.5 text-xs">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20j'ai%20une%20question%20sur%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-emerald-50 text-emerald-900 font-bold hover:bg-emerald-100 transition-colors">
              <i data-lucide="message-circle" class="w-4 h-4 text-emerald-700"></i>
              <span>Poser une question sur WhatsApp</span>
            </a>
            <a href="tel:+33695413227" class="flex items-center justify-center gap-2 py-2 rounded-xl text-slate-600 hover:text-slate-900 font-bold transition-colors">
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
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative text-slate-900 max-h-[90vh] overflow-y-auto">
      <button onclick="closeBookingForm()" class="absolute top-5 right-5 p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center">
          <i data-lucide="ticket" class="w-5 h-5"></i>
        </div>
        <div>
          <h3 class="font-black text-xl text-slate-950">
            Réservation • {title}
          </h3>
          <p class="text-xs text-slate-500 font-medium">À partir de {price_display} / personne</p>
        </div>
      </div>

      <form onsubmit="handleBookingSubmit(event)" class="space-y-4 text-sm mt-4">
        <div>
          <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Date choisie</label>
          <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-emerald-800">
            <option>10 Oct - 24 Oct 2026 (4 places restantes)</option>
            <option>07 Nov - 21 Nov 2026 (2 places restantes)</option>
            <option>15 Mars - 29 Mars 2027 (6 places disponibles)</option>
            <option>Départ privatisé / sur-mesure</option>
          </select>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Voyageurs</label>
            <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-emerald-800">
              <option>1 voyageur</option>
              <option selected>2 voyageurs</option>
              <option>3 voyageurs</option>
              <option>4 voyageurs et +</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Chambre</label>
            <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-emerald-800">
              <option>Double / Twin (inclus)</option>
              <option>Individuelle (+ supplément)</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block font-bold text-xs uppercase text-slate-600 mb-1">Vos coordonnées</label>
          <div class="grid grid-cols-2 gap-3 mb-2">
            <input type="text" placeholder="Prénom & Nom" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-emerald-800">
            <input type="tel" placeholder="Téléphone / WhatsApp" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-emerald-800">
          </div>
          <input type="email" placeholder="Adresse email" required class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-emerald-800">
        </div>

        <button type="submit" class="w-full py-4 rounded-2xl bg-fire-600 hover:bg-fire-500 text-white font-black text-base shadow-xl shadow-fire-600/30">
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

# Helper for dots
def generate_dots(val):
    dots = ""
    for i in range(5):
        if i < val:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-emerald-800"></span>'
        else:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-slate-300"></span>'
    return dots

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

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/all_tours_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

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
        <details class="day-accordion group bg-white rounded-2xl border border-slate-200/90 shadow-sm p-4 sm:p-5 transition-all" {is_open}>
          <summary class="font-extrabold text-sm sm:text-base text-slate-950 cursor-pointer flex items-center justify-between gap-3 list-none">
            <div class="flex items-center gap-3">
              <span class="w-8 h-8 rounded-xl bg-safari-100 text-emerald-900 font-black text-xs flex items-center justify-center shrink-0 border border-slate-200">
                {i+1}
              </span>
              <span class="font-extrabold text-slate-900">{d['title']}</span>
            </div>
            <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 group-open:rotate-180 transition-transform shrink-0"></i>
          </summary>
          <div class="mt-4 pl-11 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3 font-normal">
            <p>{d['desc']}</p>
          </div>
        </details>
        """

    price_val = tour.get("price_discount") or tour.get("price_original") or "Sur devis"
    orig_val = tour.get("price_original") if tour.get("price_discount") else None

    orig_html = f'<span class="text-sm text-slate-400 line-through font-normal">{orig_val}</span>' if orig_val else ""
    disc_html = '<span class="text-xs font-black text-fire-600 bg-fire-50 px-2.5 py-1 rounded-full border border-fire-200">Promo Saison</span>' if orig_val else ""

    overview_clean = tour.get("overview") or "Vivez une aventure authentique au cœur du Népal sauvage."

    page_html = tour_page_template.format(
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

print("All 14 tour pages regenerated with WeRoad Font (Plus Jakarta Sans)!")
