import re, glob

# 1. Update index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_code = f.read()

balanced_header_index = """  <!-- 2. MAIN NAVIGATION (BALANCED 3-ZONE CENTERING) -->
  <header class="absolute top-[42px] left-0 right-0 z-40 py-3 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 sm:h-20">
      
        <!-- LEFT: LOGO (Symmetric Left Column) -->
        <div class="flex items-center justify-start w-1/4 shrink-0">
          <a href="/index.html" class="flex items-center gap-3 group">
            <img 
              src="/assets/logo_nav_white.png" 
              alt="Jungle Nepal Adventure Logo" 
              class="h-10 sm:h-12 w-auto object-contain filter drop-shadow-[0_2px_8px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform"
            />
          </a>
        </div>

        <!-- CENTER: NAVIGATION LINKS (Strictly Centered) -->
        <nav class="hidden lg:flex items-center justify-center flex-1 gap-7 xl:gap-8 text-[14px] font-semibold text-white/95 drop-shadow">
          <a href="#prochains-departs" class="hover:text-amber-300 transition-colors whitespace-nowrap">Tous les séjours</a>
          
          <!-- Destinations Dropdown -->
          <div class="relative group py-2">
            <a href="/destinations/index.html" class="hover:text-amber-300 transition-colors flex items-center gap-1.5 cursor-pointer whitespace-nowrap">
              <span>Destinations</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </a>

            <!-- Dropdown Menu 100% OPAQUE & LISIBLE -->
            <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
              <div style="background-color: #041d13 !important; color: #ffffff !important;" class="rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] border border-emerald-500/30 space-y-1">
                
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
          </div>

          <a href="#concept" class="hover:text-amber-300 transition-colors whitespace-nowrap">L'esprit safari</a>
          <a href="#pisteurs" class="hover:text-amber-300 transition-colors whitespace-nowrap">Maîtres pisteurs</a>
          <a href="/a-propos.html" class="hover:text-amber-300 transition-colors whitespace-nowrap">À propos</a>
          <a href="/contact.html" class="hover:text-amber-300 transition-colors whitespace-nowrap">Contact</a>
        </nav>

        <!-- RIGHT: ACTIONS (Symmetric Right Column) -->
        <div class="flex items-center justify-end w-1/4 gap-3 sm:gap-3.5 shrink-0">
          
          <!-- LANGUAGE SWITCHER (GLOBE) -->
          <div class="relative group/lang py-1">
            <button onclick="toggleLangMenu(this)" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 hover:bg-white/20 border-white/20 text-white border backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
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

          <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20vos%20séjours%20au%20Népal" target="_blank" class="hidden sm:flex items-center gap-2 px-5 py-2.5 rounded-full bg-white text-slate-950 font-extrabold text-xs sm:text-[13px] shadow-lg hover:bg-slate-100 hover:scale-105 active:scale-95 transition-all whitespace-nowrap">
            <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
            <span>WhatsApp Direct</span>
          </a>

          <button onclick="toggleMobileMenu()" class="lg:hidden w-10 h-10 rounded-2xl bg-white/15 hover:bg-white/25 text-white border border-white/30 backdrop-blur-md flex flex-col items-center justify-center gap-1.5 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer shadow-lg p-2" aria-label="Menu principal">
            <span class="w-5 h-[2.5px] bg-white rounded-full block"></span>
            <span class="w-5 h-[2.5px] bg-white rounded-full block"></span>
            <span class="w-5 h-[2.5px] bg-white rounded-full block"></span>
          </button>
        </div>

      </div>
    </div>
  </header>"""

idx_code = re.sub(r'<!-- 2\. MAIN NAVIGATION.*?<!-- Mobile Drawer -->', balanced_header_index + '\n\n  <!-- Mobile Drawer -->', idx_code, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_code)

# 2. Update Header.astro component
header_comp_code = """---
interface Props {
  lang?: string;
  currentPath?: string;
  isTransparent?: boolean;
}

const { lang = 'fr', currentPath = '', isTransparent = false } = Astro.props;
---

<header class={`sticky top-0 z-40 transition-all duration-300 ${isTransparent ? 'bg-slate-950/80 backdrop-blur-md text-white border-b border-white/10' : 'bg-white/95 backdrop-blur-md text-slate-900 border-b border-slate-200 shadow-sm'}`}>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16 sm:h-20">
    
      <!-- LEFT: LOGO (1/4 Width) -->
      <div class="flex items-center justify-start w-1/4 shrink-0">
        <a href="/index.html" class="flex items-center gap-3 group">
          <img 
            src={isTransparent ? "/assets/logo_nav_white.png" : "/assets/logo_nav_dark.png"} 
            alt="Jungle Nepal Adventure" 
            class="h-10 sm:h-12 w-auto object-contain group-hover:scale-105 transition-transform" 
          />
        </a>
      </div>

      <!-- CENTER: NAVIGATION LINKS (Strictly Centered 2/4 Width) -->
      <nav class={`hidden lg:flex items-center justify-center flex-1 gap-7 xl:gap-8 text-[14px] font-semibold ${isTransparent ? 'text-white/90' : 'text-slate-700'}`}>
        <a href="/index.html#prochains-departs" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          Tous les 15 séjours
        </a>

        <!-- Destinations Dropdown -->
        <div class="relative group py-2">
          <a href="/destinations/index.html" class={`flex items-center gap-1.5 cursor-pointer whitespace-nowrap transition-colors ${isTransparent ? 'hover:text-amber-300' : 'hover:text-[#0e8354]'}`}>
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white">
              <a href="/destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">🐅</div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                  <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
                </div>
              </a>
              <a href="/destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">🦏</div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                  <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
                </div>
              </a>
              <a href="/destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">🦌</div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                  <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
                </div>
              </a>
              <a href="/destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">🏔️</div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                  <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
                </div>
              </a>
              <a href="/destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">🕉️</div>
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

        <a href="/index.html#concept" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          L'esprit safari
        </a>
        <a href="/index.html#pisteurs" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          Maîtres pisteurs
        </a>
        <a href="/a-propos.html" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          À propos
        </a>
        <a href="/contact.html" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          Contact
        </a>
      </nav>

      <!-- RIGHT: ACTIONS (1/4 Width) -->
      <div class="flex items-center justify-end w-1/4 gap-3 sm:gap-3.5 shrink-0">
        <!-- GLOBE SWITCHER -->
        <div class="relative group/lang py-1">
          <button onclick="toggleLangMenu(this)" class={`w-9 h-9 sm:w-10 sm:h-10 rounded-full ${isTransparent ? 'bg-white/10 hover:bg-white/20 border-white/20 text-white' : 'bg-slate-100 hover:bg-slate-200 border-slate-200 text-slate-700'} border backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer`} aria-label="Changer de langue / Change language">
            <svg xmlns="http://www.w3.org/2000/svg" class={`w-4 h-4 ${isTransparent ? 'text-white' : 'text-slate-700'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
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

        <a href="/index.html#prochains-departs" class="inline-flex items-center gap-2 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white text-xs sm:text-[13px] font-black px-5 py-2.5 rounded-full shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all whitespace-nowrap">
          <span>Départs & Prix</span>
        </a>

        <!-- Mobile Hamburger Button -->
        <button onclick="toggleMobileMenu()" class={`lg:hidden w-10 h-10 rounded-2xl ${isTransparent ? 'bg-white/15 hover:bg-white/25 text-white border-white/30' : 'bg-slate-100 hover:bg-slate-200 text-slate-900 border-slate-300'} border backdrop-blur-md flex flex-col items-center justify-center gap-1.5 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer shadow-sm p-2`} aria-label="Menu">
          <span class={`w-5 h-[2.5px] ${isTransparent ? 'bg-white' : 'bg-slate-900'} rounded-full block`}></span>
          <span class={`w-5 h-[2.5px] ${isTransparent ? 'bg-white' : 'bg-slate-900'} rounded-full block`}></span>
          <span class={`w-5 h-[2.5px] ${isTransparent ? 'bg-white' : 'bg-slate-900'} rounded-full block`}></span>
        </button>
      </div>

    </div>
  </div>
</header>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(header_comp_code)

print("Balanced header applied to index.astro and Header.astro!")
