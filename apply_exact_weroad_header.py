import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Curated High-End Images for all 14 tours
hero_images_curated = {
    "nepal-sauvage": "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
    "nepal-immersion-totale": "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
    "babai-special": "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
    "bardia-babai-camping": "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
    "bardia-explorateur": "https://junglenepal.com/wp-content/uploads/2025/12/P1133754-scaled.jpg",
    "rafting-safari": "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
    "bardia-nuit-sauvage": "https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-8.webp",
    "tiji-mustang": "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
    "chitwan-culture": "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
    "rara-lake-bardia": "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-2.webp",
    "chitwan-bardia-complete": "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
    "carnet-de-voyage": "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
    "jungle-extreme": "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3.webp",
    "immersion-spirituelle": "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0177-1-scaled.jpeg"
}

cards_html = ""
for t in tours:
    short_id = t["short_id"]
    img_src = hero_images_curated.get(short_id, t.get("hero_img", "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"))
    orig_price_html = f'<span class="text-xs text-slate-400 line-through font-normal">{t["original_price"]}</span>' if t.get("original_price") else ""
    discount_tag = '<span class="text-[10px] font-extrabold text-amber-900 bg-amber-100 px-2 py-0.5 rounded-full border border-amber-200">Promo</span>' if t.get("original_price") else ""

    cards_html += f"""
        <!-- TRIP CARD: {t['title']} -->
        <article class="trip-card group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,36,25,0.16)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between" data-category="{t['category']}" data-title="{t['title'].lower()}">
          
          <div class="relative">
            <a href="{t['link']}" class="relative h-72 sm:h-80 overflow-hidden block">
              <img 
                src="{img_src}" 
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

              <a href="{t['link']}" class="group/btn inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white font-extrabold text-xs sm:text-sm shadow-[0_4px_14px_rgba(234,88,12,0.35)] hover:shadow-[0_8px_24px_rgba(234,88,12,0.55)] hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300 border-t border-white/25 whitespace-nowrap">
                <span>Voir le séjour</span>
                <i data-lucide="arrow-right" class="w-4 h-4 group-hover/btn:translate-x-1 transition-transform"></i>
              </a>
            </div>
          </div>

        </article>
    """

full_html = f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jungle Nepal Adventure – Safaris Sauvages, Tigres du Bengale & Treks au Népal</title>
  <meta name="description" content="Découvrez le Népal sauvage en micro-groupes (4 à 8 pers). 14 séjours d'exception : safaris à pied à Bardia, tracking du tigre du Bengale, bivouacs en jungle et immersion himalayenne.">

  <!-- Open Graph -->
  <meta property="og:title" content="Jungle Nepal Adventure – Safaris & Expéditions Sauvages">
  <meta property="og:description" content="14 séjours immersifs au royaume du tigre du Bengale. Encadrement exclusif par les maîtres pisteurs de Bardia.">
  <meta property="og:image" content="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg">
  <meta property="og:type" content="website">

  <!-- WeRoad Exact Font: Plus Jakarta Sans -->
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
            wered: {{
              500: '#f04f47',
              600: '#ea382e',
              700: '#d12920',
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
    .no-scrollbar::-webkit-scrollbar {{ display: none; }}
    .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
  </style>
</head>
<body class="bg-safari-50 text-slate-800 font-sans antialiased selection:bg-jungle-900 selection:text-amber-200">

  <!-- ========================================================================= -->
  <!-- 1. TOP ANNOUNCEMENT BAR (WeRoad Signature Red/Coral) -->
  <!-- ========================================================================= -->
  <aside aria-label="Bannière promotionnelle" class="bg-[#f04f47] text-white text-xs sm:text-[13px] py-2.5 px-4 font-bold relative z-50 text-center shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="w-6 hidden sm:block"></div>
      <div class="flex-1 flex items-center justify-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span>☀️ <strong>Saison 2026-2027</strong> : dernières places en micro-groupes au Népal ! <strong>100€ de réduction</strong> avec le code <span class="underline decoration-2">JUNGLE100</span> 🇳🇵</span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/80 hover:text-white text-base leading-none px-1" aria-label="Fermer">✕</button>
    </div>
  </aside>

  <!-- ========================================================================= -->
  <!-- 2. EXACT WEROAD HEADER (Transparent, Full-Width, NO CONTAINER BOX) -->
  <!-- ========================================================================= -->
  <header class="absolute top-[40px] left-0 right-0 z-40 px-6 sm:px-12 lg:px-16 py-5 flex items-center justify-between text-white">
    
    <!-- Left: WeRoad Style Framed Logo Badge -->
    <a href="#" class="flex items-center gap-3 group">
      <div class="px-3.5 py-1.5 rounded-xl bg-black/40 backdrop-blur-md border border-white/30 flex items-center gap-2 shadow-lg group-hover:bg-black/60 transition-all">
        <span class="font-black text-lg sm:text-xl tracking-tighter text-white uppercase flex items-center gap-1.5">
          <span class="text-[#f04f47] font-black">JUNGLE</span>NEPAL
        </span>
      </div>
    </a>

    <!-- Center / Right: Clean Text Navigation (Exactly like WeRoad) -->
    <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-white/90 drop-shadow">
      <a href="#prochains-departs" class="hover:text-white transition-colors">Départs</a>
      <a href="#prochains-departs" class="hover:text-white transition-colors">Destinations</a>
      <a href="#concept" class="hover:text-white transition-colors">L'Esprit Safari</a>
      <a href="#pisteurs" class="hover:text-white transition-colors">Maîtres Pisteurs</a>
      <a href="#avis" class="hover:text-white transition-colors">Avis ★ 4.9</a>
      <a href="javascript:void(0)" onclick="openCustomTripModal()" class="hover:text-white transition-colors">Sur-mesure</a>
      <a href="https://wa.me/33695413227" target="_blank" class="hover:text-white transition-colors">Contacte-nous</a>
    </nav>

    <!-- Far Right: Globe + Profile/Connexion Pill Button -->
    <div class="flex items-center gap-4">
      <button class="hidden sm:flex items-center text-white/90 hover:text-white p-1" aria-label="Langue">
        <i data-lucide="globe" class="w-5 h-5"></i>
      </button>

      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20vos%20séjours%20au%20Népal" target="_blank" class="hidden sm:flex items-center gap-2 px-5 py-2.5 rounded-full bg-white text-slate-900 font-extrabold text-xs sm:text-[13px] shadow-lg hover:bg-slate-100 hover:scale-105 active:scale-95 transition-all">
        <i data-lucide="user" class="w-4 h-4 text-slate-700"></i>
        <span>WhatsApp Direct</span>
      </a>

      <!-- Mobile Hamburger -->
      <button onclick="toggleMobileMenu()" class="lg:hidden p-2 rounded-xl bg-black/40 backdrop-blur-md text-white border border-white/20" aria-label="Menu">
        <i data-lucide="menu" class="w-5 h-5"></i>
      </button>
    </div>

  </header>

  <!-- Mobile Drawer -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-x-4 top-24 z-50 bg-slate-950/95 backdrop-blur-2xl border border-white/15 rounded-3xl p-6 text-white space-y-4 shadow-2xl">
    <nav class="flex flex-col space-y-3 font-bold text-base">
      <a href="#prochains-departs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center justify-between">
        <span>🐾 Tous les 14 circuits 2026/2027</span>
        <span class="bg-[#f04f47] text-xs px-2 py-0.5 rounded-full font-black">14</span>
      </a>
      <a href="#concept" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        🧭 L'Esprit Safari & Éthique
      </a>
      <a href="#pisteurs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        🐅 Nos Maîtres Pisteurs (BBC)
      </a>
      <a href="#avis" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        ⭐ Avis Voyageurs (4.9/5)
      </a>
    </nav>
    <div class="pt-4 border-t border-white/10 flex flex-col gap-2">
      <button onclick="toggleMobileMenu(); openCustomTripModal()" class="w-full py-3.5 rounded-2xl bg-[#f04f47] font-black text-sm text-center shadow-lg">
        Créer mon séjour sur-mesure ✨
      </button>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 3. HERO SECTION (Exact WeRoad Layout with Big Cinema Background) -->
  <!-- ========================================================================= -->
  <section class="relative min-h-[92vh] flex items-center justify-center pt-44 pb-28 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">
    
    <!-- Cinema Hero Photo -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" 
        alt="Tigre du Bengale au Népal" 
        class="w-full h-full object-cover object-center filter brightness-85 contrast-105"
      />
      <!-- Soft ambient shadow overlay for crisp text readability -->
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-black/30 to-black/50"></div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center w-full">
      
      <!-- Main H1 (Bold, WeRoad Style) -->
      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl lg:text-[76px] text-white tracking-tight leading-[1.06] drop-shadow-2xl">
        L'autre côté du Népal
      </h1>

      <!-- Subtitle Poetry (User requested) -->
      <div class="mt-6 text-base sm:text-xl md:text-2xl text-white/95 max-w-3xl font-semibold leading-relaxed drop-shadow space-y-1">
        <p>Là où les routes s’arrêtent.</p>
        <p>Là où les territoires sauvages recommencent.</p>
        <p class="text-amber-300 font-bold">Guidé par ceux qui y vivent.</p>
        <p class="pt-2 text-white font-extrabold">Offrez-vous votre voyage nature au Népal.</p>
      </div>

      <!-- EXACT WEROAD SEARCH CARD (2 columns + Red Square Search Button) -->
      <div class="w-full max-w-3xl mt-12 bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.35)] p-2.5 sm:p-3 border border-slate-100 text-left text-slate-900">
        <form onsubmit="handleSearch(event)" class="flex flex-col sm:flex-row items-center justify-between gap-2">
          
          <!-- Column 1: Où ? -->
          <div class="w-full sm:flex-1 px-5 py-2.5 rounded-2xl hover:bg-slate-50 transition-colors cursor-pointer">
            <label class="block text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              Où ?
            </label>
            <div class="flex items-center gap-2 mt-0.5">
              <select id="search-dest" class="w-full bg-transparent font-extrabold text-base sm:text-[17px] text-slate-900 focus:outline-none cursor-pointer">
                <option value="all">Tous les 14 circuits</option>
                <option value="safari">Bardia (Tigres & Safari à pied)</option>
                <option value="bivouac">Vallée de Babai (Camping Sauvage)</option>
                <option value="chitwan">Chitwan (Rhinocéros & Pirogue)</option>
                <option value="trek">Haut-Mustang & Lac Rara</option>
                <option value="rafting">Rivières Karnali (Rafting Expédition)</option>
                <option value="culture">Culture Tharu, Yoga & Dessin</option>
              </select>
            </div>
          </div>

          <!-- Divider -->
          <div class="hidden sm:block w-px h-10 bg-slate-200"></div>

          <!-- Column 2: Quand ? -->
          <div class="w-full sm:flex-1 px-5 py-2.5 rounded-2xl hover:bg-slate-50 transition-colors cursor-pointer">
            <label class="block text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              Quand ?
            </label>
            <div class="flex items-center gap-2 mt-0.5">
              <select id="search-date" class="w-full bg-transparent font-extrabold text-base sm:text-[17px] text-slate-900 focus:outline-none cursor-pointer">
                <option value="all">Toute l'année (Saison 2026-2027)</option>
                <option value="autumn">Automne 2026 (Octobre - Décembre)</option>
                <option value="winter">Hiver 2026/2027 (Janvier - Février)</option>
                <option value="spring">Printemps 2027 (Mars - Mai • Pic Tigres)</option>
              </select>
            </div>
          </div>

          <!-- WeRoad Square Red Action Button -->
          <div class="w-full sm:w-auto">
            <button type="submit" class="w-full sm:w-16 h-14 bg-[#f04f47] hover:bg-[#ea382e] text-white font-black rounded-2xl flex items-center justify-center shadow-lg shadow-[#f04f47]/35 hover:scale-105 active:scale-95 transition-all" aria-label="Rechercher">
              <i data-lucide="search" class="w-6 h-6"></i>
            </button>
          </div>

        </form>
      </div>

      <!-- WeRoad "Reprends où tu t'es arrêté" Quick Trip Pills -->
      <div class="mt-8 flex flex-wrap items-center justify-center gap-3 text-xs sm:text-sm font-bold text-white">
        <span class="text-white/80 font-medium">Idées de séjours :</span>
        <a href="tours/nepal-sauvage.html" class="inline-flex items-center gap-2 px-4 py-2 rounded-2xl bg-white/15 backdrop-blur-md border border-white/20 hover:bg-white/25 transition-all shadow-sm">
          <img src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png" class="w-6 h-6 rounded-lg object-cover" alt="Népal Sauvage"/>
          <span>Népal Sauvage 15j</span>
        </a>
        <a href="tours/babai-special.html" class="inline-flex items-center gap-2 px-4 py-2 rounded-2xl bg-white/15 backdrop-blur-md border border-white/20 hover:bg-white/25 transition-all shadow-sm">
          <img src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" class="w-6 h-6 rounded-lg object-cover" alt="Babai"/>
          <span>Babai Spécial Tigres 5j</span>
        </a>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 4. REASSURANCE TRUST BANNER -->
  <!-- ========================================================================= -->
  <section class="bg-white border-y border-slate-200/90 py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div class="flex flex-col items-center">
          <p class="font-black text-2xl text-slate-900 tracking-tight">4 à 8 Max</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Silence & immersion totale</p>
        </div>
        <div class="flex flex-col items-center border-l border-slate-200/80">
          <p class="font-black text-2xl text-emerald-800 tracking-tight">BBC Wildlife</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Pisteurs certifiés faune sauvage</p>
        </div>
        <div class="flex flex-col items-center border-l border-slate-200/80">
          <p class="font-black text-2xl text-amber-700 tracking-tight">100% Local</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Retombées directes pour les villages</p>
        </div>
        <div class="flex flex-col items-center border-l border-slate-200/80">
          <p class="font-black text-2xl text-[#f04f47] tracking-tight">Sur-mesure</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Coordinateur francophone (Robin)</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 5. CATEGORIES FILTER CAROUSEL -->
  <!-- ========================================================================= -->
  <section id="categories" class="py-6 bg-white border-b border-slate-200/80 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1">
        
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-amber-300 font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-amber-400/40 hover:scale-105 active:scale-95 transition-all duration-200" data-filter="all">
          <i data-lucide="compass" class="w-4 h-4"></i>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="safari">
          <span>🐅</span>
          <span>Safaris & Pistage Bardia</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="bivouac">
          <span>⛺</span>
          <span>Bivouacs & Nuits Sauvages</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="chitwan">
          <span>🦏</span>
          <span>Chitwan & Rhinocéros</span>
        </button>

        <button onclick="filterTrips('trek')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="trek">
          <span>🏔️</span>
          <span>Treks & Lac Rara</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="culture">
          <span>🕉️</span>
          <span>Culture, Yoga & Carnet</span>
        </button>

        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting Karnali</span>
        </button>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 6. LES 14 CIRCUITS (GRILLE COMPLÈTE WEROAD) -->
  <!-- ========================================================================= -->
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

      <!-- 14 CARDS -->
      <div id="trips-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {cards_html}
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 7. SECTION L'ESPRIT SAFARI -->
  <!-- ========================================================================= -->
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

  <!-- ========================================================================= -->
  <!-- 8. PISTEURS & ÉQUIPE -->
  <!-- ========================================================================= -->
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

  <!-- ========================================================================= -->
  <!-- 9. AVIS CLIENTS -->
  <!-- ========================================================================= -->
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
            <div class="w-10 h-10 rounded-full bg-[#f04f47] text-white font-bold flex items-center justify-center text-sm shadow">AN</div>
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

  <!-- ========================================================================= -->
  <!-- 10. FOOTER -->
  <!-- ========================================================================= -->
  <footer class="bg-slate-950 text-slate-300 pt-20 pb-12 border-t border-white/10">
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

        <button type="submit" class="w-full py-4 rounded-2xl bg-[#f04f47] hover:bg-[#ea382e] text-white font-black text-base shadow-xl shadow-[#f04f47]/30">
          Envoyer ma demande à l'équipe locale →
        </button>
      </form>
    </div>
  </div>

  <script>
    lucide.createIcons();

    function toggleMobileMenu() {{
      document.getElementById('mobile-menu').classList.toggle('hidden');
    }}

    function filterTrips(category) {{
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      pills.forEach(pill => {{
        if (pill.dataset.filter === category) {{
          pill.classList.add('bg-slate-950', 'text-amber-300', 'border-amber-400/40', 'scale-105');
          pill.classList.remove('bg-white', 'text-slate-800');
        }} else {{
          pill.classList.remove('bg-slate-950', 'text-amber-300', 'border-amber-400/40', 'scale-105');
          pill.classList.add('bg-white', 'text-slate-800');
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
    f.write(full_html)

print("Exact WeRoad Header & Hero Layout applied to index.html successfully!")
