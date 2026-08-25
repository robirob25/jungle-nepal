import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

cards_html = ""
for t in tours:
    orig_price_html = f'<span class="text-xs text-slate-400 line-through">{t["original_price"]}</span>' if t.get("original_price") else ""
    price_color = "text-fire-600" if t.get("original_price") else "text-jungle-900"
    
    cards_html += f"""
        <!-- CARD: {t['title']} -->
        <article class="trip-card group bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-weroad hover:shadow-weroad-hover transition-all duration-300 flex flex-col" data-category="{t['category']}" data-title="{t['title'].lower()}">
          <a href="{t['link']}" class="relative h-72 sm:h-80 overflow-hidden block">
            <img 
              src="{t['hero_img']}" 
              alt="{t['title']}" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
            
            <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-10">
              <span class="{t['badge_color']} text-white font-heading font-bold text-xs px-3 py-1 rounded-full shadow-md flex items-center gap-1">
                {t['badge']}
              </span>
              <span class="bg-black/50 backdrop-blur-md text-white font-medium text-xs px-2.5 py-1 rounded-full border border-white/20">
                Max 8 pers.
              </span>
            </div>

            <button onclick="event.preventDefault(); toggleWishlist(this)" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-black/40 backdrop-blur-md border border-white/20 flex items-center justify-center text-white hover:text-fire-500 hover:bg-white transition-all z-10" aria-label="Ajouter aux favoris">
              <i data-lucide="heart" class="w-4 h-4"></i>
            </button>

            <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white text-xs z-10">
              <div class="flex items-center gap-1.5 bg-black/40 backdrop-blur-md px-3 py-1 rounded-full">
                <i data-lucide="clock" class="w-3.5 h-3.5 text-emerald-300"></i>
                <span class="font-bold">{t['duration']}</span>
              </div>
              <div class="flex items-center gap-1 bg-amber-500/90 text-white font-bold px-2.5 py-1 rounded-full shadow">
                <i data-lucide="star" class="w-3 h-3 fill-white"></i>
                <span>{t['rating']} ({t['reviews']} avis)</span>
              </div>
            </div>
          </a>

          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <div class="text-[11px] font-heading font-bold uppercase tracking-wider text-jungle-700 mb-1">
                Népal Sauvage • Écotourisme
              </div>
              <h3 class="font-heading font-extrabold text-xl text-slate-900 group-hover:text-jungle-800 transition-colors leading-tight">
                <a href="{t['link']}">{t['title']}</a>
              </h3>
              <p class="mt-2.5 text-sm text-slate-600 line-clamp-2 leading-relaxed">
                {t['overview']}
              </p>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-end justify-between">
              <div>
                <p class="text-[11px] uppercase tracking-wider font-semibold text-slate-400">À partir de</p>
                <div class="flex items-baseline gap-2">
                  <span class="font-heading font-black text-2xl {price_color}">{t['price']}</span>
                  {orig_price_html}
                </div>
                <p class="text-[11px] text-emerald-700 font-medium">Saison 2026 / 2027</p>
              </div>

              <a href="{t['link']}" class="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-full bg-jungle-800 hover:bg-jungle-900 text-white font-heading font-bold text-xs sm:text-sm shadow-md transition-all group-hover:bg-fire-600">
                <span>Voir le tour</span>
                <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
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
  <title>Jungle Nepal Adventure – Safaris Authentiques, Tigres du Bengale & Treks au Népal</title>
  <meta name="description" content="Explorez le Népal sauvage en petits groupes (4-8 pers) avec Jungle Nepal Adventure. 14 circuits uniques : safaris à pied à Bardia, tigres, Chitwan, rafting et treks himalayens.">

  <!-- Open Graph -->
  <meta property="og:title" content="Jungle Nepal Adventure – Le Népal Sauvage & Authentique">
  <meta property="og:description" content="14 circuits de safaris exclusifs, tracking du tigre du Bengale à Bardia et aventures immersives guidées par des experts locaux.">
  <meta property="og:image" content="https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg">
  <meta property="og:type" content="website">

  <!-- Google Fonts -->
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
  <style>
    .no-scrollbar::-webkit-scrollbar {{ display: none; }}
    .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
  </style>
</head>
<body class="bg-sand-50 text-slate-800 font-sans antialiased selection:bg-jungle-800 selection:text-white">

  <!-- TOP ANNOUNCEMENT BAR -->
  <aside aria-label="Annonce spéciale" class="bg-gradient-to-r from-jungle-950 via-jungle-900 to-jungle-800 text-white text-xs sm:text-sm py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm transition-all duration-300" id="top-announcement">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span class="inline-flex items-center justify-center bg-fire-600 text-white text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full animate-pulse">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-200 hidden sm:inline">
          🇳🇵 <strong>14 circuits disponibles</strong> pour les safaris de saison sèche !
        </span>
        <span class="text-amber-300 font-semibold">
          -100€ sur votre départ avec le code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>

      <div class="flex items-center gap-4 text-xs shrink-0">
        <a href="https://wa.me/33695413227?text=Bonjour%20Jungle%20Nepal%2C%20je%20souhaite%20des%20informations%20sur%20vos%20safaris" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors">
          <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
          <span>WhatsApp Direct : <strong>+33 6 95 41 32 27</strong></span>
        </a>
        <button onclick="document.getElementById('top-announcement').style.display='none'" class="text-white/60 hover:text-white transition-colors p-1" aria-label="Fermer la bannière">
          <i data-lucide="x" class="w-3.5 h-3.5"></i>
        </button>
      </div>
    </div>
  </aside>

  <!-- NAVBAR STICKY -->
  <header id="main-nav" class="fixed top-9 left-0 right-0 z-40 transition-all duration-300 py-4 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto">
      <div id="nav-container" class="flex items-center justify-between px-5 py-3 rounded-2xl transition-all duration-300 bg-black/25 backdrop-blur-md border border-white/15 text-white">
        
        <a href="#" class="flex items-center gap-3 group">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-jungle-700 to-jungle-950 flex items-center justify-center text-emerald-400 border border-emerald-500/30 group-hover:scale-105 transition-transform shadow-md">
            <i data-lucide="footprints" class="w-5 h-5"></i>
          </div>
          <div class="flex flex-col">
            <span class="font-heading font-black text-lg sm:text-xl tracking-tight text-white leading-none">
              JUNGLE NEPAL
            </span>
            <span class="text-[10px] font-bold tracking-widest text-emerald-400 uppercase mt-0.5">
              Adventure • 14 Circuits 100% Intégrés
            </span>
          </div>
        </a>

        <nav class="hidden lg:flex items-center gap-1 font-heading text-sm font-semibold">
          <a href="#prochains-departs" class="px-3.5 py-2 rounded-full hover:bg-white/10 transition-colors flex items-center gap-1.5">
            <span>Tous les 14 Départs</span>
            <span class="bg-fire-600 text-[10px] font-bold px-1.5 py-0.2 rounded-full text-white">14</span>
          </a>
          <a href="#categories" class="px-3.5 py-2 rounded-full hover:bg-white/10 transition-colors">
            Destinations & Parcs
          </a>
          <a href="#concept" class="px-3.5 py-2 rounded-full hover:bg-white/10 transition-colors">
            L'Esprit Jungle
          </a>
          <a href="#equipe" class="px-3.5 py-2 rounded-full hover:bg-white/10 transition-colors">
            Nos Guides (Pawan / Robin)
          </a>
          <a href="#avis" class="px-3.5 py-2 rounded-full hover:bg-white/10 transition-colors flex items-center gap-1">
            <span>Avis</span>
            <span class="text-amber-400 text-xs">★ 4.9</span>
          </a>
        </nav>

        <div class="flex items-center gap-3">
          <button onclick="openCustomTripModal()" class="hidden sm:flex items-center gap-2 px-3.5 py-2 rounded-full text-xs font-semibold bg-white/10 hover:bg-white/20 border border-white/20 transition-all text-white">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-300"></i>
            <span>Sur-mesure</span>
          </button>

          <a href="#prochains-departs" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white text-xs sm:text-sm font-heading font-bold px-5 py-2.5 rounded-full shadow-lg shadow-fire-600/30 hover:shadow-fire-600/50 hover:scale-[1.02] active:scale-95 transition-all">
            <span>Voir les 14 départs</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </a>

          <button onclick="toggleMobileMenu()" class="lg:hidden p-2 rounded-xl bg-white/10 hover:bg-white/20 transition-colors text-white" aria-label="Menu Mobile">
            <i data-lucide="menu" id="menu-icon" class="w-5 h-5"></i>
          </button>
        </div>

      </div>
    </div>

    <div id="mobile-menu" class="hidden lg:hidden mt-2 max-w-7xl mx-auto">
      <div class="bg-jungle-950/95 backdrop-blur-xl border border-white/15 rounded-2xl p-5 text-white space-y-4 shadow-2xl">
        <nav class="flex flex-col space-y-2 font-heading font-semibold text-base">
          <a href="#prochains-departs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10 flex items-center justify-between">
            <span>🐾 Tous les 14 départs 2026/2027</span>
            <span class="bg-fire-600 text-xs px-2 py-0.5 rounded-full">14</span>
          </a>
          <a href="#categories" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            🌿 Safaris Bardia & Chitwan
          </a>
          <a href="#concept" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            🧭 Le Concept & Éthique
          </a>
          <a href="#equipe" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            👥 L'Équipe (Pawan, Kiran, Robin)
          </a>
          <a href="#avis" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-lg hover:bg-white/10">
            ⭐ Avis Voyageurs (4.9/5)
          </a>
        </nav>
        <div class="pt-3 border-t border-white/10 flex flex-col gap-2">
          <a href="tel:+33695413227" class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-white/10 font-semibold text-sm">
            <i data-lucide="phone" class="w-4 h-4 text-emerald-400"></i>
            <span>+33 6 95 41 32 27</span>
          </a>
          <button onclick="toggleMobileMenu(); openCustomTripModal()" class="w-full py-3 rounded-xl bg-fire-600 font-heading font-bold text-sm text-center shadow-lg shadow-fire-600/30">
            Créer mon voyage sur-mesure ✨
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="relative min-h-[92vh] sm:min-h-screen flex items-center justify-center pt-32 pb-20 px-4 sm:px-6 lg:px-8 overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img 
        src="https://junglenepal.com/wp-content/uploads/2017/01/tigre-600x800.jpeg" 
        alt="Tigre du Bengale dans le Parc National de Bardia au Népal" 
        class="w-full h-full object-cover object-center scale-105 animate-pulse duration-[10000ms]"
        style="animation-duration: 20s;"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-jungle-950 via-jungle-950/60 to-black/60"></div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center">
      
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs sm:text-sm font-medium mb-6 shadow-lg">
        <span class="flex h-2 w-2 rounded-full bg-emerald-400 animate-ping"></span>
        <span class="text-emerald-300 font-bold">Agence Locale Népal</span>
        <span class="text-white/40">•</span>
        <span class="text-amber-300 flex items-center gap-1">
          <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-300"></i> 4.9/5 (100% Avis Vérifiés)
        </span>
      </div>

      <h1 class="font-heading font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.1] max-w-4xl drop-shadow-md">
        Explorez le Népal sauvage.<br/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-amber-300 to-fire-400">
          Vivez l'aventure vraie.
        </span>
      </h1>

      <p class="mt-5 text-base sm:text-xl text-slate-200 max-w-2xl font-normal leading-relaxed drop-shadow">
        14 circuits d'exception en petits groupes (4 à 8 pers) & treks secrets. Guidés par les meilleurs pisteurs natifs du Népal.
      </p>

      <!-- Search Box -->
      <div class="w-full max-w-4xl mt-10 p-3 sm:p-4 rounded-3xl bg-white/95 backdrop-blur-xl shadow-2xl border border-white/40 text-left text-slate-900">
        <form id="hero-search-form" onsubmit="handleSearch(event)" class="grid grid-cols-1 md:grid-cols-12 gap-3 items-center">
          
          <div class="md:col-span-4 p-3 rounded-2xl hover:bg-slate-100/80 transition-colors cursor-pointer border border-slate-200/60 md:border-transparent">
            <label class="block text-[11px] font-heading font-bold uppercase tracking-wider text-slate-400">
              Où veux-tu aller ?
            </label>
            <div class="flex items-center gap-2 mt-1">
              <i data-lucide="map-pin" class="w-4 h-4 text-jungle-700 shrink-0"></i>
              <select id="search-dest" class="w-full bg-transparent font-heading font-bold text-sm sm:text-base text-slate-800 focus:outline-none cursor-pointer">
                <option value="all">Tous les 14 circuits</option>
                <option value="safari">Bardia National Park (Tigres & Bivouac)</option>
                <option value="chitwan">Chitwan (Rhinocéros & Rivières)</option>
                <option value="bivouac">Vallée de Babai (Camping sauvage)</option>
                <option value="trek">Haut-Mustang & Lac Rara</option>
                <option value="rafting">Rivières Karnali (Rafting)</option>
                <option value="culture">Culture, Yoga & Carnet de voyage</option>
              </select>
            </div>
          </div>

          <div class="hidden md:block w-[1px] h-10 bg-slate-200"></div>

          <div class="md:col-span-4 p-3 rounded-2xl hover:bg-slate-100/80 transition-colors cursor-pointer border border-slate-200/60 md:border-transparent">
            <label class="block text-[11px] font-heading font-bold uppercase tracking-wider text-slate-400">
              Quand partir ?
            </label>
            <div class="flex items-center gap-2 mt-1">
              <i data-lucide="calendar" class="w-4 h-4 text-jungle-700 shrink-0"></i>
              <select id="search-date" class="w-full bg-transparent font-heading font-bold text-sm sm:text-base text-slate-800 focus:outline-none cursor-pointer">
                <option value="all">Toute l'année (Oct - Juin recommandé)</option>
                <option value="autumn">Automne 2026 (Oct - Déc) 🍂</option>
                <option value="winter">Hiver 2026/2027 (Jan - Fév) ❄️</option>
                <option value="spring">Printemps 2027 (Mars - Mai • Meilleur pour les tigres) 🐅</option>
              </select>
            </div>
          </div>

          <div class="md:col-span-3 flex items-center">
            <button type="submit" class="w-full h-14 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-heading font-black text-base rounded-2xl flex items-center justify-center gap-2 shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
              <i data-lucide="search" class="w-5 h-5"></i>
              <span>Rechercher</span>
            </button>
          </div>

        </form>
      </div>

      <div class="mt-6 flex flex-wrap items-center justify-center gap-2 text-xs sm:text-sm text-slate-300">
        <span>Tu ne sais pas quel circuit choisir parmi nos 14 offres ?</span>
        <button onclick="openCustomTripModal()" class="inline-flex items-center gap-1 font-bold text-amber-300 hover:text-white underline underline-offset-4 decoration-amber-300/50 hover:decoration-white transition-all">
          <span>Demande conseil à Robin & Pawan en direct</span>
          <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
        </button>
      </div>

    </div>
  </section>

  <!-- CATEGORIES FILTER CAROUSEL -->
  <section id="categories" class="py-10 bg-white border-b border-slate-200/80 sticky top-[72px] z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-3 overflow-x-auto no-scrollbar py-2 -mx-4 px-4 sm:mx-0 sm:px-0">
        
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-jungle-800 text-white font-heading font-bold text-xs sm:text-sm whitespace-nowrap shadow-sm hover:scale-105 transition-all" data-filter="all">
          <i data-lucide="compass" class="w-4 h-4 text-emerald-300"></i>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-[11px] px-2 py-0.5 rounded-full">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-heading font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="safari">
          <span class="text-base">🐅</span>
          <span>Safaris & Tigres (Bardia)</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-heading font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="bivouac">
          <span class="text-base">⛺</span>
          <span>Bivouac & Camping Sauvage</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-heading font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="chitwan">
          <span class="text-base">🦏</span>
          <span>Chitwan & Rhinocéros</span>
        </button>

        <button onclick="filterTrips('trek')" class="category-pill flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-heading font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="trek">
          <span class="text-base">🏔️</span>
          <span>Treks & Lac Rara</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-heading font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="culture">
          <span class="text-base">🕉️</span>
          <span>Culture & Spiritualité</span>
        </button>

        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-heading font-bold text-xs sm:text-sm whitespace-nowrap transition-all" data-filter="rafting">
          <span class="text-base">🚣</span>
          <span>Rafting Karnali</span>
        </button>

      </div>
    </div>
  </section>

  <!-- PROCHAINS DEPARTS - 14 TOURS GRID -->
  <section id="prochains-departs" class="py-16 sm:py-24 bg-sand-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
        <div>
          <div class="inline-flex items-center gap-2 text-xs font-heading font-bold uppercase tracking-wider text-fire-600 bg-fire-50 px-3 py-1 rounded-full mb-3">
            <i data-lucide="flame" class="w-3.5 h-3.5"></i>
            <span>Dernières places disponibles • Saison 2026 - 2027</span>
          </div>
          <h2 class="font-heading font-extrabold text-3xl sm:text-4xl md:text-5xl text-jungle-950 tracking-tight">
            Nos 14 circuits immersifs au Népal
          </h2>
          <p class="mt-3 text-base text-slate-600 max-w-2xl">
            Cliquez sur un voyage pour consulter la page WeRoad détaillée (itinéraire jour par jour, photos, radar et réservation).
          </p>
        </div>

        <div class="flex items-center gap-3">
          <span id="trip-count-badge" class="text-sm font-semibold text-slate-500 bg-white px-4 py-2 rounded-full border border-slate-200 shadow-sm">
            Affichage de <strong>14 circuits</strong>
          </span>
        </div>
      </div>

      <!-- GRID OF 14 CARDS -->
      <div id="trips-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {cards_html}
      </div>

    </div>
  </section>

  <!-- L'ESPRIT JUNGLE -->
  <section id="concept" class="py-20 sm:py-28 bg-white border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="inline-block text-xs font-heading font-bold uppercase tracking-wider text-jungle-800 bg-jungle-50 px-3.5 py-1 rounded-full mb-3 border border-jungle-200">
          L'Esprit Jungle Nepal
        </span>
        <h2 class="font-heading font-extrabold text-3xl sm:text-5xl text-jungle-950 tracking-tight">
          Pourquoi explorer le Népal avec nous ?
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-600 leading-relaxed">
          Oubliez les bus de 40 personnes et les circuits standardisés. Nous offrons une expérience humaine et sauvage, au plus près des animaux et des habitants.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 sm:gap-8">
        <div class="md:col-span-7 rounded-3xl p-8 sm:p-10 bg-gradient-to-br from-jungle-950 to-jungle-900 text-white flex flex-col justify-between relative overflow-hidden shadow-xl border border-jungle-800">
          <div class="relative z-10">
            <div class="w-14 h-14 rounded-2xl bg-emerald-500/20 border border-emerald-400/30 flex items-center justify-center text-emerald-400 mb-6">
              <i data-lucide="shield-check" class="w-7 h-7"></i>
            </div>
            <span class="text-xs font-heading font-bold uppercase tracking-wider text-amber-300">Pisteurs Légendaires</span>
            <h3 class="font-heading font-black text-2xl sm:text-3xl text-white tracking-tight mt-1">
              Les meilleurs pisteurs de tigres du pays
            </h3>
            <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
              Fondée par d'anciens présidents de l'Association des Guides de Bardia et consultants faune pour la BBC Wildlife. Nos pisteurs lisent les empreintes fraîches et vous garantissent une sécurité absolue.
            </p>
          </div>
          <div class="relative z-10 mt-8 pt-6 border-t border-white/10 flex flex-wrap items-center gap-4 text-xs text-slate-300">
            <span>✓ 20+ ans de terrain</span>
            <span>✓ Certifiés Parcs Nationaux</span>
            <span>✓ Bilingues Français & Anglais</span>
          </div>
        </div>

        <div class="md:col-span-5 rounded-3xl p-8 sm:p-10 bg-sand-100 text-slate-900 flex flex-col justify-between border border-sand-200 shadow-sm hover:shadow-md transition-shadow">
          <div>
            <div class="w-14 h-14 rounded-2xl bg-fire-100 border border-fire-200 flex items-center justify-center text-fire-600 mb-6">
              <i data-lucide="users" class="w-7 h-7"></i>
            </div>
            <span class="text-xs font-heading font-bold uppercase tracking-wider text-fire-600">Micro-Groupes</span>
            <h3 class="font-heading font-black text-2xl text-slate-900 tracking-tight mt-1">
              4 à 8 explorateurs par séjour
            </h3>
            <p class="mt-3 text-slate-600 text-sm leading-relaxed">
              Pour observer un tigre ou un rhinocéros en silence absolu, la discrétion est la clé. Vous voyagez entre passionnés du même esprit.
            </p>
          </div>
          <div class="mt-6 flex items-center gap-2 text-xs font-bold text-jungle-800">
            <i data-lucide="sparkles" class="w-4 h-4"></i>
            <span>Ambiance conviviale & respectueuse</span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- L'ÉQUIPE -->
  <section id="equipe" class="py-20 bg-sand-50 border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="inline-block text-xs font-heading font-bold uppercase tracking-wider text-fire-600 bg-fire-50 px-3.5 py-1 rounded-full mb-3">
        L'Équipe Fondatrice
      </span>
      <h2 class="font-heading font-extrabold text-3xl sm:text-5xl text-jungle-950 tracking-tight">
        Les coulisses de vos aventures
      </h2>

      <div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-10">
        <div class="flex flex-col items-center text-center group">
          <div class="relative w-36 h-36 sm:w-44 sm:h-44 rounded-full overflow-hidden p-1.5 bg-gradient-to-tr from-jungle-800 via-amber-400 to-fire-600 shadow-xl group-hover:scale-105 transition-all">
            <img src="https://junglenepal.com/wp-content/uploads/2025/12/1.png" alt="Pawan - Chef Pisteur" class="w-full h-full object-cover rounded-full bg-slate-200"/>
          </div>
          <h3 class="mt-6 font-heading font-bold text-xl text-jungle-950">Pawan</h3>
          <p class="text-xs font-heading font-semibold text-fire-600 uppercase tracking-wider">Chef Pisteur & Expert BBC Wildlife</p>
        </div>

        <div class="flex flex-col items-center text-center group">
          <div class="relative w-36 h-36 sm:w-44 sm:h-44 rounded-full overflow-hidden p-1.5 bg-gradient-to-tr from-jungle-800 via-emerald-400 to-jungle-950 shadow-xl group-hover:scale-105 transition-all">
            <img src="https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-1720-x-1080-px-1024x643.png" alt="Kiran" class="w-full h-full object-cover rounded-full bg-slate-200"/>
          </div>
          <h3 class="mt-6 font-heading font-bold text-xl text-jungle-950">Kiran</h3>
          <p class="text-xs font-heading font-semibold text-emerald-700 uppercase tracking-wider">Pionnier de l'Écotourisme</p>
        </div>

        <div class="flex flex-col items-center text-center group">
          <div class="relative w-36 h-36 sm:w-44 sm:h-44 rounded-full overflow-hidden p-1.5 bg-gradient-to-tr from-amber-400 via-fire-500 to-jungle-800 shadow-xl group-hover:scale-105 transition-all">
            <img src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png" alt="Robin" class="w-full h-full object-cover rounded-full bg-slate-200"/>
          </div>
          <h3 class="mt-6 font-heading font-bold text-xl text-jungle-950">Robin</h3>
          <p class="text-xs font-heading font-semibold text-fire-600 uppercase tracking-wider">Coordinateur France-Népal</p>
        </div>
      </div>
    </div>
  </section>

  <!-- AVIS CLIENTS -->
  <section id="avis" class="py-20 sm:py-28 bg-white border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="font-heading font-extrabold text-3xl sm:text-5xl text-jungle-950 tracking-tight">
          Ce que disent nos explorateurs
        </h2>
        <p class="mt-3 text-base text-slate-600">
          Note globale <strong>4.9 / 5</strong> sur Google Reviews • Avis 100% Vérifiés
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="rounded-3xl p-8 bg-sand-50 border border-slate-200 shadow-sm">
          <p class="italic text-slate-700">« Choisir Jungle Nepal Adventure pour découvrir ce pays sous l'angle de sa vie sauvage, c'est la meilleure option. Des moments uniques ! »</p>
          <p class="mt-4 font-bold text-jungle-950 text-sm">— Samantha G. (Voyageuse vérifiée)</p>
        </div>
        <div class="rounded-3xl p-8 bg-sand-50 border border-slate-200 shadow-sm">
          <p class="italic text-slate-700">« Je reviens de 15 jours au Népal... ce que je retiens avant tout, c'est l'humain. Une équipe sincère et dévouée. Une expérience rare ! »</p>
          <p class="mt-4 font-bold text-jungle-950 text-sm">— Adrien N. (Voyageur vérifié)</p>
        </div>
        <div class="rounded-3xl p-8 bg-sand-50 border border-slate-200 shadow-sm">
          <p class="italic text-slate-700">« Un voyage gravé à vie. Séjourner chez l'habitant au milieu de la jungle de Bardia est une expérience hors du commun. »</p>
          <p class="mt-4 font-bold text-jungle-950 text-sm">— Alice P. (Voyageuse vérifiée)</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-jungle-950 text-white pt-20 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-white/10 text-sm text-slate-400">
        <div>
          <h4 class="font-heading font-bold text-white text-base mb-3">Jungle Nepal Adventure</h4>
          <p class="text-xs leading-relaxed">Agence locale d'écotourisme et de safaris immersifs au Népal. Katmandou & Parc National de Bardia.</p>
        </div>
        <div>
          <h4 class="font-heading font-bold text-white text-sm mb-3">Contact Direct</h4>
          <p class="text-xs">WhatsApp : +33 6 95 41 32 27</p>
          <p class="text-xs mt-1">Email : contact@junglenepal.com</p>
        </div>
        <div>
          <h4 class="font-heading font-bold text-white text-sm mb-3">14 Circuits Proposés</h4>
          <p class="text-xs">Bardia, Chitwan, Babai, Mustang, Lac Rara, Karnali Rafting, Yoga & Carnet de dessin.</p>
        </div>
        <div>
          <h4 class="font-heading font-bold text-white text-sm mb-3">Garanties</h4>
          <p class="text-xs">Acompte 30% • Annulation flexible • Retombées 100% locales.</p>
        </div>
      </div>
      <p class="pt-8 text-xs text-slate-500 text-center">© 2026 Jungle Nepal Adventure. Tous droits réservés.</p>
    </div>
  </footer>

  <!-- MODAL SUR-MESURE -->
  <div id="custom-trip-modal" class="fixed inset-0 z-50 hidden bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-xl w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative text-slate-900 max-h-[90vh] overflow-y-auto">
      <button onclick="closeCustomTripModal()" class="absolute top-5 right-5 p-2 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-2xl bg-fire-100 text-fire-600 flex items-center justify-center">
          <i data-lucide="sparkles" class="w-5 h-5"></i>
        </div>
        <div>
          <h3 class="font-heading font-black text-2xl text-jungle-950">Voyage sur-mesure au Népal</h3>
          <p class="text-xs text-slate-500">Réponse sous 24h avec Robin & Pawan.</p>
        </div>
      </div>

      <form onsubmit="handleCustomTripSubmit(event)" class="space-y-4 text-sm mt-4">
        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Nombre de voyageurs</label>
          <select class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <option>1 personne (Solo)</option>
            <option selected>2 personnes (Couple / Duo)</option>
            <option>3 à 5 personnes (Famille / Amis)</option>
            <option>6 personnes et plus</option>
          </select>
        </div>

        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Vos coordonnées</label>
          <div class="grid grid-cols-2 gap-3 mb-2">
            <input type="text" placeholder="Nom complet" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
            <input type="tel" placeholder="Téléphone / WhatsApp" required class="p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
          </div>
          <input type="email" placeholder="Adresse email" required class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800">
        </div>

        <div>
          <label class="block font-heading font-bold text-xs uppercase text-slate-600 mb-1">Vos envies particulières</label>
          <textarea rows="3" placeholder="Parcs souhaités, dates idéales, durée..." class="w-full p-3 rounded-xl border border-slate-200 font-medium focus:ring-2 focus:ring-jungle-800 text-xs"></textarea>
        </div>

        <button type="submit" class="w-full py-4 rounded-2xl bg-fire-600 hover:bg-fire-500 text-white font-heading font-black text-base shadow-xl shadow-fire-600/30">
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
      if (window.scrollY > 50) {{
        nav.classList.add('top-0');
        nav.classList.remove('top-9');
        navContainer.classList.remove('bg-black/25');
        navContainer.classList.add('bg-jungle-950/90', 'shadow-xl', 'border-white/10');
      }} else {{
        nav.classList.remove('top-0');
        nav.classList.add('top-9');
        navContainer.classList.add('bg-black/25');
        navContainer.classList.remove('bg-jungle-950/90', 'shadow-xl', 'border-white/10');
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
          pill.classList.add('bg-jungle-800', 'text-white');
          pill.classList.remove('bg-slate-100', 'text-slate-700');
        }} else {{
          pill.classList.remove('bg-jungle-800', 'text-white');
          pill.classList.add('bg-slate-100', 'text-slate-700');
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

    function toggleWishlist(btn) {{
      btn.classList.toggle('text-fire-500');
      btn.classList.toggle('fill-fire-500');
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

print("Updated index.html with all 14 tours successfully!")
