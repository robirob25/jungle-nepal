import os

fr_page = """---
import Layout from '../../layouts/Layout.astro';
---

<Layout title="Expédition : Panthère des Neiges Exclusive (17 jours) | Jungle Nepal Adventure" lang="fr">

  <!-- TOP BAR -->
  <aside aria-label="Bannière d'information" class="bg-slate-950 text-slate-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4 font-bold">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span class="inline-flex items-center justify-center bg-[#0e8354] text-white text-[10px] font-black uppercase tracking-widest px-2 py-0.5 rounded-full">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-200 hidden sm:inline">
          🇳🇵 <strong>Micro-groupe 4 à 8 explorateurs</strong> ou départ privatisé.
        </span>
        <span class="text-amber-300 font-bold">
          -100€ code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20l'expédition%20Panthère%20des%20Neiges" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs font-semibold">
        <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>WhatsApp direct : <strong>+33 6 95 41 32 27</strong> (Robin)</span>
      </a>
    </div>
  </aside>

  <!-- HEADER STICKY -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-8 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="/index.html" class="flex items-center gap-2 group shrink-0">
        <img src="/assets/logo_dark.png" alt="Jungle Nepal Adventure" class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-sm group-hover:scale-105 transition-transform duration-300" />
      </a>

      <!-- NAVIGATION DESKTOP -->
      <nav class="hidden lg:flex items-center gap-6 xl:gap-7 text-[13px] font-bold text-slate-700">
        <a href="/index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les séjours</a>
        
        <!-- DROPDOWN DESTINATIONS -->
        <div class="relative group py-2">
          <a href="/destinations/index.html" class="hover:text-[#0e8354] transition-colors flex items-center gap-1.5 cursor-pointer font-bold">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <!-- DROPDOWN MENU LUXE SOMBRE OPAQUE (#041d13) -->
          <div style="background-color: #041d13 !important;" class="absolute left-0 top-full hidden group-hover:block w-80 rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.8)] border border-emerald-500/30 p-3 space-y-1.5 transition-all duration-300 z-50">
            <div class="px-3 py-2 border-b border-white/10 mb-1">
              <p class="text-[10px] font-black uppercase tracking-widest text-emerald-400">Territoires sauvages du Népal</p>
            </div>

            <a href="/destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🐅
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
              </div>
            </a>

            <a href="/destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🦏
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
              </div>
            </a>

            <a href="/destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🦌
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
              </div>
            </a>

            <a href="/destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🏔️
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
              </div>
            </a>

            <a href="/destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🕉️
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Katmandou</p>
                <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
              </div>
            </a>

            <div class="pt-2 border-t border-white/10 mt-1">
              <a href="/destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                Voir toutes les destinations →
              </a>
            </div>
          </div>
        </div>

        <a href="/index.html#esprit-safari" class="hover:text-[#0e8354] transition-colors">L'esprit safari</a>
        <a href="/index.html#maitres-pisteurs" class="hover:text-[#0e8354] transition-colors">Maîtres pisteurs</a>
        <a href="/a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="/contact.html" class="hover:text-[#0e8354] transition-colors">Contact</a>
      </nav>

      <!-- LANGUE & CTA DÉPARTS -->
      <div class="flex items-center gap-3 sm:gap-4">
        <!-- Sélecteur de langue -->
        <div class="relative group py-2">
          <button class="flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-slate-200 hover:border-slate-400 text-xs font-black text-slate-700 bg-white shadow-sm transition-all">
            <span>🇫🇷</span>
            <span>FR</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          
          <div style="background-color: #041d13 !important;" class="absolute right-0 top-full hidden group-hover:block w-36 rounded-2xl shadow-[0_15px_35px_rgba(0,0,0,0.6)] border border-emerald-500/30 p-1.5 space-y-1 z-50">
            <a href="/tours/panthere-des-neiges.html" class="flex items-center gap-2 px-3 py-2 rounded-xl bg-white/15 text-amber-300 font-bold text-xs">
              <span>🇫🇷</span>
              <span>Français</span>
            </a>
            <a href="/en/tours/panthere-des-neiges.html" class="flex items-center gap-2 px-3 py-2 rounded-xl hover:bg-white/10 text-white font-bold text-xs transition-colors">
              <span>🇬🇧</span>
              <span>English</span>
            </a>
          </div>
        </div>

        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white text-xs sm:text-[13px] font-black px-5 py-2.5 rounded-full shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <svg class="w-4 h-4 text-emerald-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN TOUR CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24 font-sans">

    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-slate-500 font-semibold mb-3 overflow-x-auto whitespace-nowrap">
      <a href="/index.html" class="hover:text-slate-900 flex items-center gap-1">
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="/index.html#prochains-departs" class="hover:text-slate-900">Nos 15 Séjours</a>
      <span>›</span>
      <span class="text-slate-900 font-bold truncate">Expédition : Panthère des Neiges Exclusive</span>
    </nav>

    <!-- Header Title & Badges Row -->
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6">
      <div>
        <h1 class="font-black text-2xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">
          Expédition : Panthère des Neiges Exclusive
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-slate-700 bg-amber-50 border border-amber-200 px-3 py-1 rounded-full">
            <svg class="w-4 h-4 text-amber-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2"></path><path d="M12 20v2"></path><path d="m4.93 4.93 1.41 1.41"></path><path d="m17.66 17.66 1.41 1.41"></path><path d="M2 12h2"></path><path d="M20 12h2"></path><path d="m6.34 17.66-1.41 1.41"></path><path d="m19.07 4.93-1.41 1.41"></path></svg>
            <span>17 jours</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-900 font-bold px-3 py-1 rounded-full border border-emerald-200">
            <svg class="w-4 h-4 text-amber-400 fill-amber-400 shrink-0" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            <span>5.0 (10 avis vérifiés)</span>
          </div>
          <span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">
            🏔️ Himalaya, Mustang & Spiritualité
          </span>
        </div>
      </div>

      <!-- BOUTON PARTAGER -->
      <div class="relative shrink-0">
        <button id="share-btn" onclick="handleShareTour()" class="flex items-center gap-2 px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-extrabold text-slate-800 hover:text-[#0e8354] hover:border-[#0e8354] shadow-sm hover:shadow transition-all cursor-pointer">
          <svg class="w-4 h-4 text-slate-500 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"></line><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"></line></svg>
          <span>Partager ce séjour</span>
        </button>
      </div>
    </div>

    <!-- PHOTO MOSAIC GALLERY WEROAD -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[460px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="/assets/snow-leopard/snow_leopard_portrait.jpg" alt="Panthère des Neiges - Portrait" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)" />
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="/assets/snow-leopard/snow_leopard_2.jpg" alt="Panthère des Neiges sur falaise" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)" />
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="/assets/snow-leopard/manang_gangapurna.jpg" alt="Vallée de Manang et Lac Gangapurna" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)" />
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="/assets/snow-leopard/annapurna_himalayas.jpg" alt="Chaîne des Annapurnas" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)" />
        </div>
      </div>
      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105">
        <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[69px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-bold text-slate-600">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Aperçu</a>
        <a href="#points-forts" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Points Forts</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Itinéraire (17j)</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Inclus & Extras</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">FAQ</a>
      </div>
    </div>

    <!-- 2-COLUMN MAIN CONTENT GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT COLUMN -->
      <div class="lg:col-span-8 space-y-12">
        
        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
            Partez sur les traces du félin le plus insaisissable et mythique de la planète : la <strong>Panthère des Neiges</strong> (<em>Panthera uncia</em>, le Fantôme des Montagnes). Au cœur de la haute vallée sauvage de Manang (3 600 m – 4 500 m) et des contreforts sacrés des Annapurnas, cette expédition exclusive de 17 jours allie acclimatation progressive, <strong>9 jours complets de pistage intensif</strong> avec nos maîtres pisteurs himalayens, et immersion culturelle bouddhiste au monastère séculaire de Braka Gompa.
          </p>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Durée</span>
              <span class="text-base sm:text-lg font-black text-slate-900">17 Jours</span>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Altitude Max</span>
              <span class="text-base sm:text-lg font-black text-[#0e8354]">4 200 m</span>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Groupe</span>
              <span class="text-base sm:text-lg font-black text-slate-900">4 à 8 pers.</span>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Pistage terrain</span>
              <span class="text-base sm:text-lg font-black text-amber-600">9 Jours non-stop</span>
            </div>
          </div>
        </section>

        <!-- SECTION 2: POINTS FORTS -->
        <section id="points-forts" class="space-y-4">
          <h2 class="font-black text-2xl text-slate-950 tracking-tight">Les temps forts de cette expédition</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="flex items-start gap-3 p-4 rounded-2xl bg-white border border-slate-200 shadow-sm">
              <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold shrink-0">🐾</span>
              <p class="text-sm font-medium text-slate-700"><strong>9 jours complets d'affûts</strong> et de pistage dédié au léopard des neiges avec matériel d'observation HD.</p>
            </div>
            <div class="flex items-start gap-3 p-4 rounded-2xl bg-white border border-slate-200 shadow-sm">
              <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold shrink-0">🏔️</span>
              <p class="text-sm font-medium text-slate-700"><strong>Acclimatation sécurisée</strong> en paliers successifs (Chame 2 700 m, Manang 3 600 m et lac glaciaire de Gangapurna).</p>
            </div>
            <div class="flex items-start gap-3 p-4 rounded-2xl bg-white border border-slate-200 shadow-sm">
              <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold shrink-0">🕉️</span>
              <p class="text-sm font-medium text-slate-700"><strong>Journée de césure culturelle</strong> au monastère historique de Braka Gompa vieux de 600 ans.</p>
            </div>
            <div class="flex items-start gap-3 p-4 rounded-2xl bg-white border border-slate-200 shadow-sm">
              <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold shrink-0">✈️</span>
              <p class="text-sm font-medium text-slate-700"><strong>Vol panoramique</strong> face aux Annapurnas et détente aux sources chaudes naturelles.</p>
            </div>
          </div>
        </section>

        <!-- SECTION 3: PROGRAMME JOUR PAR JOUR -->
        <section id="programme" class="space-y-6">
          <div class="flex items-center justify-between">
            <h2 class="font-black text-2xl text-slate-950 tracking-tight">Itinéraire détaillé jour par jour</h2>
            <span class="text-xs font-bold text-slate-500">17 jours d'aventure</span>
          </div>

          <div class="space-y-4 relative before:absolute before:inset-0 before:left-4 before:w-0.5 before:bg-emerald-200">
            
            <!-- J1 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 1</span>
              <h3 class="font-extrabold text-base text-slate-900">Arrivée à Katmandou – Transfert direct à la cité royale de Bhaktapur</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Accueil à l'aéroport international et transfert direct vers la cité historique de Bhaktapur. Installation à l'hôtel et présentation de l'expédition. Ce choix permet une première immersion culturelle immédiate, à l'écart de l'agitation du centre de la capitale.
              </p>
            </div>

            <!-- J2 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 2</span>
              <h3 class="font-extrabold text-base text-slate-900">Vol Katmandou – Pokhara face aux Annapurnas & Temps libre</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Vol domestique de 30 minutes vers Pokhara offrant un panorama unique sur la chaîne des Annapurnas. Temps libre l’après-midi pour explorer les abords du lac, les temples, organiser les derniers préparatifs et profiter de la vue sur les montagnes. Nuit à l'hôtel.
              </p>
            </div>

            <!-- J3 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 3</span>
              <h3 class="font-extrabold text-base text-slate-900">Pokhara – Chame (2 700 m) : Remontée de la vallée & Sources chaudes</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Départ en véhicule privatif 4x4 pour Chame (environ 6h de piste). Ce trajet marque le début de la remontée de la vallée et constitue le premier palier d'acclimatation à l'altitude. En fin de journée, accès aux sources d'eau chaude naturelles en bord de rivière. Nuit à l'hôtel.
              </p>
            </div>

            <!-- J4 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 4</span>
              <h3 class="font-extrabold text-base text-slate-900">Chame – Manang (3 600 m) & Marche d'acclimatation au Lac Gangapurna</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Trajet de 2 heures pour rejoindre Manang. Pour valider ce deuxième palier de contrôle d'acclimatation, une marche est programmée vers le lac glaciaire turquoise de Gangapurna. Nuit à l'hôtel à Manang.
              </p>
            </div>

            <!-- J5-13 -->
            <div class="relative pl-10 space-y-1.5 p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200">
              <div class="absolute left-2.5 top-5 w-3 h-3 rounded-full bg-amber-500 border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-amber-700">Jours 5 à 13 (9 Jours)</span>
              <h3 class="font-extrabold text-base text-slate-950">Expédition Léopard des Neiges – 9 Jours de suivi et de pistage intensif</h3>
              <p class="text-sm text-slate-700 leading-relaxed font-normal">
                Neuf jours complets sur le terrain dédiés au suivi et à l'observation du Léopard des neiges aux côtés de nos pisteurs himalayens spécialisés. L'itinéraire intègre une flexibilité permettant d'effectuer une journée de césure et de transition culturelle au monastère de Braka Gompa, un site historique majeur vieux de 600 ans.
              </p>
            </div>

            <!-- J14 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 14</span>
              <h3 class="font-extrabold text-base text-slate-900">Manang – Bandipur : Descente vers la cité Newar préservée</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Amorce de la descente des hautes altitudes. Trajet de 6 à 7 heures de route pour rejoindre Bandipur, un village traditionnel Newar reconnu pour son architecture préservée et son panorama sur les sommets environnants. Nuit sur place.
              </p>
            </div>

            <!-- J15 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 15</span>
              <h3 class="font-extrabold text-base text-slate-900">Bandipur – Katmandou & Soirée libre à Thamel</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Route de retour vers Katmandou (environ 4h de trajet). Installation à l'hôtel et fin de journée libre pour se reposer et explorer le quartier de Thamel.
              </p>
            </div>

            <!-- J16 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 16</span>
              <h3 class="font-extrabold text-base text-slate-900">Visite culturelle de Katmandou et quartier de Thamel</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Journée consacrée à la découverte des grands sites culturels de la vallée de Katmandou et derniers moments d'échange avec l'équipe locale.
              </p>
            </div>

            <!-- J17 -->
            <div class="relative pl-10 space-y-1.5">
              <div class="absolute left-2.5 top-1.5 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 17</span>
              <h3 class="font-extrabold text-base text-slate-900">Transfert aéroport & Vol retour</h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                Transfert à l'aéroport international pour votre vol de retour.
              </p>
            </div>

          </div>
        </section>

        <!-- SECTION 4: INCLUSIONS -->
        <section id="inclusions" class="space-y-6 pt-4">
          <h2 class="font-black text-2xl text-slate-950 tracking-tight">Ce qui est inclus dans votre séjour</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-6 rounded-3xl bg-emerald-50/80 border border-emerald-200 space-y-3">
              <h3 class="font-extrabold text-base text-emerald-950 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-[#0e8354] text-white flex items-center justify-center text-xs">✓</span>
                <span>Inclus dans le tarif</span>
              </h3>
              <ul class="space-y-2 text-xs sm:text-sm text-slate-700">
                <li class="flex items-start gap-2"><span>•</span><span>Vol intérieur régulier Katmandou – Pokhara</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Tous les transports privatifs 4x4 tout-terrain</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>9 jours de pistage terrain avec maîtres pisteurs</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Tous les permis de trek et zones protégées (ACAP)</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Hébergements en lodges de montagne & hôtels de charme</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Pension complète durant l'expédition en montagne</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Matériel d'observation optique longue-vue HD partagé</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Assistance francophone 24/7 avec Robin</span></li>
              </ul>
            </div>

            <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200 space-y-3">
              <h3 class="font-extrabold text-base text-slate-900 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-slate-300 text-slate-700 flex items-center justify-center text-xs">✕</span>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2 text-xs sm:text-sm text-slate-600">
                <li class="flex items-start gap-2"><span>•</span><span>Vols internationaux jusqu'à Katmandou</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Visa népalais (obtenu à l'arrivée)</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Assurance rapatriement et secours en montagne (obligatoire)</span></li>
                <li class="flex items-start gap-2"><span>•</span><span>Boissons personnelles et pourboires aux guides</span></li>
              </ul>
            </div>
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: STICKY BOOKING CARD -->
      <div class="lg:col-span-4">
        <div id="booking-card" class="sticky top-28 bg-slate-950 text-white rounded-3xl p-6 sm:p-7 border border-emerald-500/30 shadow-[0_20px_50px_rgba(0,0,0,0.5)] space-y-6">
          
          <div class="flex items-baseline justify-between border-b border-white/10 pb-4">
            <div>
              <span class="text-xs font-bold text-slate-400">Tarif par personne</span>
              <p class="text-3xl sm:text-4xl font-black text-amber-300 tracking-tight">4 300 €</p>
            </div>
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
              17 jours tout compris
            </span>
          </div>

          <div class="space-y-3 text-xs text-slate-300">
            <div class="flex items-center justify-between">
              <span>👥 Taille du groupe :</span>
              <strong class="text-white">4 à 8 explorateurs max</strong>
            </div>
            <div class="flex items-center justify-between">
              <span>📅 Meilleure saison :</span>
              <strong class="text-amber-300">Nov – Mars (hiver himalayen)</strong>
            </div>
            <div class="flex items-center justify-between">
              <span>🏔️ Zone :</span>
              <strong class="text-white">Haute Vallée de Manang</strong>
            </div>
          </div>

          <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20réserver%20ou%20avoir%20des%20infos%20sur%20l'expédition%20Panthère%20des%20Neiges%20(4300€)" target="_blank" rel="noopener noreferrer" class="w-full flex items-center justify-center gap-2 py-3.5 px-6 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:brightness-110 text-white font-black text-sm shadow-lg shadow-[#0e8354]/40 hover:scale-105 active:scale-95 transition-all text-center">
            <svg class="w-5 h-5 text-white shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
            <span>Réserver via WhatsApp (Robin)</span>
          </a>

          <p class="text-[11px] text-center text-slate-400 font-medium">
            Réponse garantie en moins de 2 heures. Conseil personnalisé pour l'équipement thermique et l'acclimatation.
          </p>

        </div>
      </div>

    </div>

  </main>

  <!-- LIGHTBOX MODAL SCRIPT -->
  <script is:inline>
    function scrollToBooking() {
      const el = document.getElementById('booking-card');
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }
    function handleShareTour() {
      if (navigator.share) {
        navigator.share({
          title: 'Expédition Panthère des Neiges Exclusive | Jungle Nepal Adventure',
          url: window.location.href
        });
      } else {
        navigator.clipboard.writeText(window.location.href);
        alert('Lien copié dans le presse-papier !');
      }
    }
  </script>

</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/panthere-des-neiges.astro', 'w', encoding='utf-8') as f:
    f.write(fr_page)

# Generate English version
en_page = fr_page.replace('lang="fr"', 'lang="en"')
en_page = en_page.replace('title="Expédition : Panthère des Neiges Exclusive (17 jours) | Jungle Nepal Adventure"', 'title="Exclusive Snow Leopard Expedition (17 Days) | Jungle Nepal Adventure"')
en_page = en_page.replace('Accueil', 'Home')
en_page = en_page.replace('Nos 15 Séjours', 'Our 15 Expeditions')
en_page = en_page.replace('Expédition : Panthère des Neiges Exclusive', 'Exclusive Snow Leopard Expedition')
en_page = en_page.replace('17 jours tout compris', '17 days all-inclusive')
en_page = en_page.replace('Tarif par personne', 'Price per person')
en_page = en_page.replace('Taille du groupe :', 'Group Size:')
en_page = en_page.replace('4 à 8 explorateurs max', '4 to 8 explorers max')
en_page = en_page.replace('Meilleure saison :', 'Best Season:')
en_page = en_page.replace('Nov – Mars (hiver himalayen)', 'Nov – March (Himalayan winter)')
en_page = en_page.replace('Réserver via WhatsApp (Robin)', 'Book via WhatsApp (Robin)')
en_page = en_page.replace('/tours/panthere-des-neiges.html', '/en/tours/panthere-des-neiges.html')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/panthere-des-neiges.astro', 'w', encoding='utf-8') as f:
    f.write(en_page)

print("Created src/pages/tours/panthere-des-neiges.astro and src/pages/en/tours/panthere-des-neiges.astro!")
