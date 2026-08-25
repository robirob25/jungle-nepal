import re, glob

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

clean_tour_header = """  <!-- 1. TOP HEADER (SLIM & BALANCED - NO OVERFLOW) -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 py-2.5 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between gap-4 h-14 sm:h-16">
      
        <!-- LEFT: LOGO -->
        <div class="flex items-center shrink-0">
          <a href="/index.html" class="flex items-center gap-2 group">
            <img 
              src="/assets/logo_nav_dark.webp" 
              alt="Jungle Nepal Adventure" 
              class="h-9 sm:h-10 w-auto object-contain group-hover:scale-105 transition-transform" 
            />
          </a>
        </div>

        <!-- CENTER: STREAMLINED NAVIGATION -->
        <nav class="hidden lg:flex items-center justify-center gap-5 xl:gap-7 text-[13px] xl:text-[14px] font-semibold text-slate-700">
          <a href="/index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Tous les 15 séjours</a>

          <!-- Destinations Dropdown -->
          <div class="relative group py-2">
            <a href="/destinations/index.html" class="hover:text-[#0e8354] transition-colors flex items-center gap-1 cursor-pointer whitespace-nowrap">
              <span>Destinations</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 transition-transform duration-200 group-hover:rotate-180 opacity-70" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </a>

            <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-200 z-50">
              <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white">
                <a href="/destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                  <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-xs shrink-0">🐅</div>
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                    <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
                  </div>
                </a>
                <a href="/destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                  <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-xs shrink-0">🦏</div>
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                    <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
                  </div>
                </a>
                <a href="/destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                  <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-xs shrink-0">🦌</div>
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                    <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
                  </div>
                </a>
                <a href="/destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                  <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-xs shrink-0">🏔️</div>
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                    <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
                  </div>
                </a>
                <a href="/destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                  <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-xs shrink-0">🕉️</div>
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
          </div>

          <a href="#programme" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Itinéraire</a>
          <a href="#inclusions" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Inclus</a>
          <a href="https://safarinepal.com" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Blog</a>
          <a href="/a-propos.html" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">À propos</a>
          <a href="/contact.html" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Contact</a>
        </nav>

        <!-- RIGHT: ACTIONS -->
        <div class="flex items-center gap-2.5 sm:gap-3 shrink-0">
          <!-- LANGUAGE SWITCHER (GLOBE) -->
          <div class="relative group/lang py-1">
            <button onclick="toggleLangMenu(this)" class="w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-slate-100 hover:bg-slate-200 border-slate-200 text-slate-700 border backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-700" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
              </svg>
            </button>
            <div class="lang-dropdown-box absolute right-0 top-full mt-1.5 w-48 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
              <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
                <button onclick="changeLanguage('fr')" data-lang-btn="fr" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
                  <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
                </button>
                <button onclick="changeLanguage('en')" data-lang-btn="en" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
                  <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
                </button>
                <button onclick="changeLanguage('de')" data-lang-btn="de" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
                  <span class="flex items-center gap-2"><span>🇩🇪</span><span>Deutsch</span></span>
                </button>
                <button onclick="changeLanguage('es')" data-lang-btn="es" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
                  <span class="flex items-center gap-2"><span>🇪🇸</span><span>Español</span></span>
                </button>
              </div>
            </div>
          </div>

          <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white text-xs sm:text-[13px] font-black px-4 py-2 sm:px-5 sm:py-2.5 rounded-full shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all whitespace-nowrap cursor-pointer">
            <span>Départs & Prix</span>
          </button>

          <!-- Mobile Hamburger Button -->
          <button onclick="toggleMobileMenu()" class="lg:hidden w-9 h-9 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-900 border border-slate-300 backdrop-blur-md flex flex-col items-center justify-center gap-1 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer shadow-sm p-1.5" aria-label="Menu">
            <span class="w-4 h-[2px] bg-slate-900 rounded-full block"></span>
            <span class="w-4 h-[2px] bg-slate-900 rounded-full block"></span>
            <span class="w-4 h-[2px] bg-slate-900 rounded-full block"></span>
          </button>
        </div>

      </div>
    </div>
  </header>"""

# Also clean top banner on tour pages
clean_tour_top_bar = """  <!-- TOP BAR PROMO -->
  <aside class="bg-[#05281a] text-white text-[11px] sm:text-xs py-1.5 px-4 relative z-50 text-center border-b border-emerald-500/20" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="w-4 hidden sm:block"></div>
      <div class="flex-1 flex items-center justify-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span>✨ <strong>Exceptionnellement -100€</strong> sur votre prochain tour en novembre 2027 avec le code <span class="bg-white/15 px-1.5 py-0.5 rounded text-amber-300 font-extrabold border border-amber-300/30 font-mono tracking-wider ml-1">JUNGLE100</span></span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/70 hover:text-white text-xs px-1 cursor-pointer">✕</button>
    </div>
  </aside>"""

for tp in tour_files:
    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace header
    c = re.sub(r'<header.*?</header>', clean_tour_header, c, flags=re.DOTALL)

    # Replace top bar
    c = re.sub(r'<aside id="top-bar".*?</aside>|<aside class="bg-\[#05281a\].*?</aside>|<!-- TOP BAR.*?</aside>', clean_tour_top_bar, c, flags=re.DOTALL)

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Fixed header overflow and streamlined navigation across all {len(tour_files)} tour pages!")
