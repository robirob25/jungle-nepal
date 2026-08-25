home_astro = """---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import toursData from '../data/tours.json';
import destinationsData from '../data/destinations.json';
import reviewsData from '../data/reviews.json';
---

<Layout 
  title="Jungle Nepal Adventure – Safaris Sauvages, Tigres du Bengale & Treks au Népal"
  description="Découvrez le Népal sauvage en micro-groupes (4 à 8 pers). 14 séjours d'exception : safaris à pied à Bardia, tracking du tigre du Bengale, bivouacs en jungle et immersion himalayenne."
  image="/assets/logo.png"
  lang="fr"
>
  <Header isTransparent={true} lang="fr" currentPath="/" />

  <!-- 1. HERO SECTION WEROAD -->
  <section class="relative min-h-[92vh] flex items-center justify-center pt-44 pb-28 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">
    <div class="absolute inset-0 z-0">
      <img 
        src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" 
        alt="Tigre du Bengale au Népal" 
        class="w-full h-full object-cover opacity-60 scale-105"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-black/60"></div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto text-center space-y-6 text-white">
      
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-xs sm:text-sm font-black tracking-wide text-amber-300">
        <span>🇳🇵</span> L'AUTRE CÔTÉ DU NÉPAL • SAISON 2026-2027
      </div>

      <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight leading-[1.08] text-white">
        Là où les routes s'arrêtent.<br class="hidden sm:inline" />
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-300 via-amber-200 to-emerald-400">
          Là où commence le Népal sauvage.
        </span>
      </h1>

      <p class="text-base sm:text-xl text-slate-200 max-w-2xl mx-auto font-medium leading-relaxed drop-shadow">
        Safaris immersifs à pied, pistage éthique du tigre du Bengale et bivouacs sauvages encadrés par les maîtres pisteurs de Bardia.
      </p>

      <!-- BARRE DE RECHERCHE RAPIDE WEROAD -->
      <div class="pt-4 max-w-3xl mx-auto">
        <div class="bg-white/95 backdrop-blur-xl p-3 sm:p-4 rounded-3xl sm:rounded-full shadow-2xl border border-white/30 text-slate-800 flex flex-col sm:flex-row items-center gap-3">
          
          <div class="w-full sm:flex-1 px-4 text-left border-b sm:border-b-0 sm:border-r border-slate-200 pb-2 sm:pb-0">
            <label class="block text-[10px] font-black uppercase tracking-wider text-slate-400">Où explorer ?</label>
            <select id="hero-dest-select" onchange="filterFromHero()" class="w-full bg-transparent font-bold text-sm text-slate-900 focus:outline-none cursor-pointer">
              <option value="all">Tous les 14 séjours</option>
              <option value="safari">Bardia & Tigres du Bengale</option>
              <option value="bivouac">Bivouacs & Vallée de Babai</option>
              <option value="chitwan">Chitwan & Rhinocéros</option>
              <option value="trek">Treks & Lac Rara</option>
              <option value="culture">Culture, Carnet & Yoga</option>
              <option value="rafting">Rafting Karnali</option>
            </select>
          </div>

          <div class="w-full sm:flex-1 px-4 text-left border-b sm:border-b-0 sm:border-r border-slate-200 pb-2 sm:pb-0">
            <label class="block text-[10px] font-black uppercase tracking-wider text-slate-400">Quand ?</label>
            <select class="w-full bg-transparent font-bold text-sm text-slate-900 focus:outline-none cursor-pointer">
              <option>Toute l'année (Saison 2026-2027)</option>
              <option>Automne 2026 (Oct - Déc)</option>
              <option>Hiver 2026-2027 (Jan - Fév)</option>
              <option>Printemps 2027 (Mars - Mai • Saison Tigres)</option>
            </select>
          </div>

          <a href="#prochains-departs" class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-sm transition-all hover:scale-105 active:scale-95 shadow-lg flex items-center justify-center gap-2 shrink-0">
            <span>Trouver mon séjour</span>
            <span>→</span>
          </a>

        </div>

        <div class="mt-4 flex flex-wrap items-center justify-center gap-2 text-xs text-slate-300">
          <span class="text-slate-400">Idées rapides :</span>
          <a href="/tours/nepal-sauvage" class="bg-white/10 hover:bg-white/20 px-3 py-1 rounded-full border border-white/15 transition-colors">🐅 Népal Sauvage 15j</a>
          <a href="/tours/babai-special" class="bg-white/10 hover:bg-white/20 px-3 py-1 rounded-full border border-white/15 transition-colors">⛺ Babai Bivouac 5j</a>
          <a href="/tours/chitwan-culture" class="bg-white/10 hover:bg-white/20 px-3 py-1 rounded-full border border-white/15 transition-colors">🦏 Chitwan Culture 4j</a>
        </div>

      </div>

    </div>
  </section>

  <!-- 2. REASSURANCE TRUST BANNER -->
  <section class="bg-white border-y border-slate-200/90 py-8 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        
        <div class="space-y-1">
          <div class="text-xl sm:text-2xl font-black text-slate-950 tracking-tight">4 à 8 Max</div>
          <p class="text-xs text-slate-500 font-semibold">Silence & immersion totale</p>
        </div>

        <div class="space-y-1">
          <div class="text-xl sm:text-2xl font-black text-[#0e8354] tracking-tight">BBC Wildlife</div>
          <p class="text-xs text-slate-500 font-semibold">Pisteurs certifiés faune sauvage</p>
        </div>

        <div class="space-y-1">
          <div class="text-xl sm:text-2xl font-black text-amber-500 tracking-tight">★ 5.0 / 5</div>
          <p class="text-xs text-slate-500 font-semibold">Avis 100% vérifiés sur Google</p>
        </div>

        <div class="space-y-1">
          <div class="text-xl sm:text-2xl font-black text-slate-950 tracking-tight">Sur-mesure</div>
          <p class="text-xs text-slate-500 font-semibold">Coordinateur francophone (Robin)</p>
        </div>

      </div>
    </div>
  </section>

  <!-- 3. CATEGORIES FILTER CAROUSEL (AVEC FLÈCHES VISIBLES < ET >) -->
  <section id="categories" class="py-4 bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
      
      <!-- Flèche Gauche < -->
      <button onclick="scrollCategories(-280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 mr-3 cursor-pointer z-10" aria-label="Faire défiler vers la gauche">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
      </button>

      <!-- Conteneur des Catégories Scrollable -->
      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Safaris et pistage Bardia</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Bivouacs et nuits sauvages</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Chitwan et rhinocéros</span>
        </button>

        <button onclick="filterTrips('trek')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="trek">
          <span>🏔️</span>
          <span>Treks et lac Rara</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="culture">
          <span>🎨</span>
          <span>Culture, yoga et carnet</span>
        </button>

        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting Karnali</span>
        </button>
      </div>

      <!-- Flèche Droite > -->
      <button onclick="scrollCategories(280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 ml-3 cursor-pointer z-10" aria-label="Faire défiler vers la droite">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
      </button>

    </div>
  </section>

  <!-- 4. LES 14 CIRCUITS (GRILLE COMPLÈTE) -->
  <section id="prochains-departs" class="py-16 sm:py-24 bg-safari-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-[#0e8354] font-black text-xs uppercase tracking-wider mb-2">
            ✨ Départs garantis • Petits groupes de 4 à 8 explorateurs
          </span>
          <h2 class="text-3xl sm:text-4xl font-black text-slate-950 tracking-tight">
            Les 14 séjours immersifs au Népal
          </h2>
          <p class="text-slate-500 text-sm mt-1">
            Sélectionnez votre aventure pour explorer le détail jour par jour, la fiche d'inclusions et réserver votre place.
          </p>
        </div>

        <div class="text-xs text-slate-500 font-bold bg-white px-4 py-2 rounded-2xl border border-slate-200 shadow-sm shrink-0">
          Affichage de <span id="trip-count" class="font-black text-slate-900">{toursData.length}</span> séjours
        </div>
      </div>

      <!-- CARDS GRID -->
      <div id="trips-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {toursData.map((tour) => (
          <div 
            class="trip-card bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col group cursor-pointer"
            data-category={tour.category}
            onclick={`window.location.href='/tours/${tour.slug}'`}
          >
            <!-- Photo Hero -->
            <div class="relative h-64 overflow-hidden bg-slate-900">
              <img 
                src={tour.images[0]} 
                alt={tour.title} 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-black/20"></div>

              <div class="absolute top-4 left-4 right-4 flex items-center justify-between">
                <span class="px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-300 border border-amber-300/30 text-xs font-black">
                  {tour.badge}
                </span>
                <span class="px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white text-xs font-bold">
                  4–8 pers.
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 text-white">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-200">
                  <span>🕒 {tour.duration}</span>
                  <span>•</span>
                  <span class="text-amber-300">★ {tour.rating} ({tour.reviews} avis)</span>
                </div>
              </div>
            </div>

            <!-- Card Body -->
            <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">{tour.style}</span>
                <h3 class="font-black text-xl text-slate-950 mt-1 leading-snug group-hover:text-[#0e8354] transition-colors">
                  {tour.title}
                </h3>
                <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                  {tour.overview}
                </p>
              </div>

              <!-- Price & CTA -->
              <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <span class="text-[10px] font-extrabold uppercase text-slate-400 block">À partir de</span>
                  <div class="flex items-baseline gap-2">
                    <span class="font-black text-2xl text-slate-950 tracking-tight">{tour.price}</span>
                    {tour.originalPrice && (
                      <span class="text-xs text-slate-400 line-through font-bold">{tour.originalPrice}</span>
                    )}
                  </div>
                </div>

                <a 
                  href={`/tours/${tour.slug}`}
                  class="px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/30 group-hover:shadow-lg hover:scale-105 transition-all"
                >
                  Voir le séjour →
                </a>
              </div>

            </div>
          </div>
        ))}
      </div>

    </div>
  </section>

  <!-- 5. CINEMA DOCUMENTARY VIDEO SHOWCASE -->
  <section id="concept" class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/20 text-[#10b981] border border-emerald-500/30 text-xs font-black uppercase tracking-widest">
          🎬 DOCUMENTAIRE EXCLUSIF AU NÉPAL
        </span>
        <h2 class="text-3xl sm:text-5xl font-black tracking-tight text-white">
          Vivez l'expérience comme si vous y étiez
        </h2>
        <p class="text-slate-400 text-base sm:text-lg">
          L'immersion totale au cœur du parc national de Bardia. Silence absolu, pistage et rencontre avec le tigre du Bengale.
        </p>
      </div>

      <!-- VIDEO PLAYER -->
      <div class="relative rounded-3xl overflow-hidden shadow-2xl border border-white/20 max-w-4xl mx-auto bg-black">
        <video 
          controls 
          playsinline 
          preload="metadata"
          poster="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
          class="w-full aspect-video object-cover"
        >
          <source src="https://junglenepal.com/wp-content/uploads/2025/12/bande-annonce-jungle-nepal-adventure-site.mp4" type="video/mp4" />
          Votre navigateur ne supporte pas la lecture de vidéo.
        </video>
      </div>

      <!-- 3 EXACT BADGES (As requested) -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 max-w-3xl mx-auto text-center pt-4">
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl">
          <p class="text-[10px] font-black uppercase tracking-widest text-slate-400">Territoire</p>
          <p class="text-base font-bold text-white mt-1">Bardia National Park</p>
        </div>
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl">
          <p class="text-[10px] font-black uppercase tracking-widest text-slate-400">Approche</p>
          <p class="text-base font-bold text-[#10b981] mt-1">À pied et en jeep</p>
        </div>
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl">
          <p class="text-[10px] font-black uppercase tracking-widest text-slate-400">Saison</p>
          <p class="text-base font-bold text-amber-300 mt-1">Mai</p>
        </div>
      </div>

    </div>
  </section>

  <!-- 6. PISTEURS & ÉQUIPE -->
  <section id="pisteurs" class="py-20 sm:py-28 bg-white border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
      
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">NOS GUIDES NATIFS</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-950 tracking-tight">
          Pawan & Kiran : Les maîtres pisteurs de Bardia
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Nés à la lisière de la jungle, ils ont guidé les équipes documentaires de la BBC et du National Geographic. Une connaissance inégalée de la faune.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="bg-safari-50 rounded-3xl p-6 sm:p-8 border border-slate-200 text-center space-y-4">
          <div class="w-24 h-24 mx-auto rounded-full overflow-hidden border-4 border-[#0e8354] shadow-lg">
            <img src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png" alt="Pawan" class="w-full h-full object-cover" />
          </div>
          <div>
            <h3 class="font-black text-xl text-slate-950">Pawan</h3>
            <p class="text-xs font-bold text-[#0e8354] uppercase tracking-wider">Maître Pisteur en Chef</p>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Plus de 15 ans d'expérience dans le tracking des grands prédateurs. Capable de repérer un tigre au simple frémissement des branches.
          </p>
        </div>

        <div class="bg-safari-50 rounded-3xl p-6 sm:p-8 border border-slate-200 text-center space-y-4">
          <div class="w-24 h-24 mx-auto rounded-full overflow-hidden border-4 border-[#0e8354] shadow-lg">
            <img src="https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg" alt="Kiran" class="w-full h-full object-cover" />
          </div>
          <div>
            <h3 class="font-black text-xl text-slate-950">Kiran</h3>
            <p class="text-xs font-bold text-[#0e8354] uppercase tracking-wider">Guide Naturaliste & Bivouac</p>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Expert des expéditions reculées dans la vallée de Babai et de la survie douce en jungle. Passionné d'ornithologie.
          </p>
        </div>

        <div class="bg-safari-50 rounded-3xl p-6 sm:p-8 border border-slate-200 text-center space-y-4">
          <div class="w-24 h-24 mx-auto rounded-full overflow-hidden border-4 border-[#0e8354] shadow-lg">
            <img src="https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-27-at-13.17.14.jpeg" alt="Robin" class="w-full h-full object-cover" />
          </div>
          <div>
            <h3 class="font-black text-xl text-slate-950">Robin</h3>
            <p class="text-xs font-bold text-[#0e8354] uppercase tracking-wider">Coordinateur Francophone</p>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Votre interlocuteur dédié avant, pendant et après votre voyage. Assistance personnalisée et organisation millimétrée.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- 7. AVIS GOOGLE REVIEWS VÉRIFIÉS -->
  <section id="avis" class="py-20 sm:py-28 bg-safari-50 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">RETOURS D'EXPÉRIENCE</span>
          <h2 class="text-3xl sm:text-4xl font-black text-slate-950 tracking-tight mt-1">
            Ce que disent nos voyageurs
          </h2>
          <p class="text-slate-500 text-sm mt-1">
            100% des avis sont authentiques et vérifiables sur notre fiche Google.
          </p>
        </div>

        <a href="https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-white px-5 py-3 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-all self-start sm:self-auto">
          <span class="text-[#00b67a] font-black text-lg">★ 5.0</span>
          <span class="text-xs font-bold text-slate-700">Lire les avis Google →</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {reviewsData.slice(0, 6).map((rev: any) => (
          <div class="bg-white p-6 sm:p-7 rounded-3xl border border-slate-200/90 shadow-sm space-y-4 flex flex-col justify-between">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-800 font-black text-sm flex items-center justify-center">
                    {rev.name.slice(0, 2).toUpperCase()}
                  </div>
                  <div>
                    <h4 class="font-bold text-sm text-slate-900">{rev.name}</h4>
                    <p class="text-[11px] text-slate-400">{rev.date}</p>
                  </div>
                </div>
                <span class="text-amber-400 text-sm">★★★★★</span>
              </div>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed italic">
                « {rev.text} »
              </p>
            </div>
            <span class="text-[10px] text-slate-400 font-bold">Avis vérifié Google Maps</span>
          </div>
        ))}
      </div>

    </div>
  </section>

  <!-- 8. FAQ ACCORDION -->
  <section id="faq" class="py-20 sm:py-28 bg-white border-t border-slate-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      
      <div class="text-center space-y-3">
        <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">QUESTIONS FRÉQUENTES</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-950 tracking-tight">
          Tout ce que vous devez savoir avant de partir
        </h2>
      </div>

      <div class="space-y-4">
        <details class="group bg-safari-50 p-5 rounded-2xl border border-slate-200">
          <summary class="font-bold text-slate-900 cursor-pointer flex justify-between items-center text-sm sm:text-base">
            <span>Combien de personnes partent par groupe ?</span>
            <svg class="w-4 h-4 transition-transform group-open:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
          </summary>
          <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
            Nos séjours sont strictement limités à 4 à 8 explorateurs. Cette taille de groupe garantit le silence nécessaire lors du pistage des tigres et préserve la sécurité de chacun.
          </p>
        </details>

        <details class="group bg-safari-50 p-5 rounded-2xl border border-slate-200">
          <summary class="font-bold text-slate-900 cursor-pointer flex justify-between items-center text-sm sm:text-base">
            <span>Quel est le montant de l'acompte à la réservation ?</span>
            <svg class="w-4 h-4 transition-transform group-open:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
          </summary>
          <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
            Pour bloquer votre place, un acompte de 30% est demandé par carte ou virement bancaire sécurisé. Le solde est réglé avant le départ ou directement à Katmandou.
          </p>
        </details>

        <details class="group bg-safari-50 p-5 rounded-2xl border border-slate-200">
          <summary class="font-bold text-slate-900 cursor-pointer flex justify-between items-center text-sm sm:text-base">
            <span>Quelle est la meilleure saison pour voir les tigres ?</span>
            <svg class="w-4 h-4 transition-transform group-open:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
          </summary>
          <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed">
            La période de mars à mai (printemps) est la plus propice car la végétation est basse et les animaux se rassemblent autour des points d'eau. L'automne (octobre à décembre) offre un climat très doux et une nature resplendissante.
          </p>
        </details>
      </div>

    </div>
  </section>

  <Footer lang="fr" />

  <script is:inline>
    window.scrollCategories = function(amount) {
      const el = document.getElementById('categories-scroll-container');
      if (el) el.scrollBy({ left: amount, behavior: 'smooth' });
    };

    window.filterTrips = function(category) {
      const pills = document.querySelectorAll('.category-pill');
      pills.forEach(p => {
        if (p.getAttribute('data-filter') === category) {
          p.classList.add('bg-slate-950', 'text-white', 'border-slate-900');
          p.classList.remove('bg-white', 'text-slate-900');
        } else {
          p.classList.remove('bg-slate-950', 'text-white', 'border-slate-900');
          p.classList.add('bg-white', 'text-slate-900');
        }
      });

      const cards = document.querySelectorAll('.trip-card');
      let visible = 0;
      cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-category') === category) {
          card.style.display = 'flex';
          visible++;
        } else {
          card.style.display = 'none';
        }
      });

      const countEl = document.getElementById('trip-count');
      if (countEl) countEl.textContent = visible;
    };

    window.filterFromHero = function() {
      const select = document.getElementById('hero-dest-select');
      if (select) {
        filterTrips(select.value);
        document.getElementById('prochains-departs').scrollIntoView({ behavior: 'smooth' });
      }
    };
  </script>
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(home_astro)

# English home page
en_home = home_astro.replace('lang="fr"', 'lang="en"').replace('currentPath="/"', 'currentPath="/en"')
en_home = en_home.replace("L'AUTRE CÔTÉ DU NÉPAL", "THE OTHER SIDE OF NEPAL")
en_home = en_home.replace("Là où les routes s'arrêtent.", "Where roads end.")
en_home = en_home.replace("Là où commence le Népal sauvage.", "Where wild territories begin.")
en_home = en_home.replace("Safaris immersifs à pied, pistage éthique du tigre du Bengale et bivouacs sauvages encadrés par les maîtres pisteurs de Bardia.", "Immersive walking safaris, ethical tiger tracking, and wild bivouacs guided by Bardia's master trackers.")
en_home = en_home.replace("Où explorer ?", "Where to explore?")
en_home = en_home.replace("Quand ?", "When?")
en_home = en_home.replace("Trouver mon séjour", "Find My Expedition")
en_home = en_home.replace("Tous les séjours", "All Expeditions")
en_home = en_home.replace("Safaris et pistage Bardia", "Bardia Safari & Tracking")
en_home = en_home.replace("Bivouacs et nuits sauvages", "Wild Bivouacs & Camping")
en_home = en_home.replace("Chitwan et rhinocéros", "Chitwan & Rhinos")
en_home = en_home.replace("Treks et lac Rara", "Treks & Rara Lake")
en_home = en_home.replace("Culture, yoga et carnet", "Culture, Yoga & Art")
en_home = en_home.replace("Rafting Karnali", "Karnali Rafting")
en_home = en_home.replace("Les 14 séjours immersifs au Népal", "All 14 Immersive Expeditions in Nepal")
en_home = en_home.replace("Voir le séjour →", "Explore Trip →")
en_home = en_home.replace("À partir de", "Starting from")
en_home = en_home.replace("DOCUMENTAIRE EXCLUSIF AU NÉPAL", "EXCLUSIVE NEPAL DOCUMENTARY")
en_home = en_home.replace("Vivez l'expérience comme si vous y étiez", "Experience the Wild as if you were there")
en_home = en_home.replace("Pawan & Kiran : Les maîtres pisteurs de Bardia", "Pawan & Kiran: Bardia Master Trackers")
en_home = en_home.replace("Ce que disent nos voyageurs", "What Our Travelers Say")
en_home = en_home.replace("Tout ce que vous devez savoir avant de partir", "Everything You Need to Know Before Departure")
en_home = en_home.replace("<Footer lang=\"fr\" />", "<Footer lang=\"en\" />")
en_home = en_home.replace("href={`/tours/${tour.slug}`}", "href={`/en/tours/${tour.slug}`}")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'w', encoding='utf-8') as f:
    f.write(en_home)

print("Created src/pages/index.astro and English mirror src/pages/en/index.astro!")
