import re

mobile_menu_code = """  <!-- MOBILE NAVIGATION DRAWER (FULL-SCREEN, HIGH CONTRAST, 100% LISIBLE) -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-0 z-[9999] bg-slate-950 text-white font-sans overflow-y-auto overscroll-contain">
    <div class="min-h-full flex flex-col justify-between p-5 sm:p-6 max-w-md mx-auto">
      
      <!-- Top Header in Drawer: Logo + Close Button -->
      <div class="flex items-center justify-between pb-4 border-b border-white/15">
        <a href="/index.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5">
          <img src="/assets/logo_nav_white.png" alt="Jungle Nepal Adventure" class="h-8 w-auto" />
          <span class="text-xs font-black uppercase tracking-widest text-emerald-400">Jungle Nepal</span>
        </a>
        <button 
          onclick="toggleMobileMenu()" 
          class="w-10 h-10 rounded-2xl bg-white/10 hover:bg-white/20 active:scale-90 flex items-center justify-center text-white text-base font-bold border border-white/20 transition-all cursor-pointer shadow-lg" 
          aria-label="Fermer le menu"
        >
          ✕
        </button>
      </div>

      <!-- Main Navigation Links -->
      <nav class="py-5 flex flex-col space-y-2 font-bold text-sm">
        
        <!-- 1. Tous les séjours -->
        <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="p-3.5 rounded-2xl bg-white/10 hover:bg-emerald-600/30 border border-white/10 flex items-center justify-between text-white transition-colors active:scale-98">
          <span class="flex items-center gap-3">
            <span class="text-base">🧭</span>
            <span class="font-extrabold text-white text-base">Tous les 15 séjours</span>
          </span>
          <span class="bg-[#0e8354] text-white text-xs px-2.5 py-1 rounded-full font-black">15</span>
        </a>

        <!-- 2. Destinations Accordion -->
        <div class="rounded-2xl bg-white/5 border border-white/10 overflow-hidden">
          <button onclick="document.getElementById('mobile-dest-sub').classList.toggle('hidden'); document.getElementById('mobile-dest-arrow').classList.toggle('rotate-180');" class="w-full p-3.5 flex items-center justify-between text-white hover:bg-white/10 transition-colors text-left cursor-pointer active:bg-white/10">
            <span class="flex items-center gap-3">
              <span class="text-base">🗺️</span>
              <span class="font-extrabold text-white text-base">Destinations</span>
            </span>
            <svg id="mobile-dest-arrow" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-emerald-400 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>

          <div id="mobile-dest-sub" class="hidden px-2 pb-3 space-y-1.5 border-t border-white/10 pt-2 bg-black/40">
            <a href="/destinations/bardia.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 text-white transition-colors">
              <span class="text-base">🐅</span>
              <div>
                <p class="font-bold text-white text-sm">Parc national de Bardia</p>
                <p class="text-xs text-slate-300">Tigres du Bengale & safaris à pied</p>
              </div>
            </a>
            <a href="/destinations/chitwan.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 text-white transition-colors">
              <span class="text-base">🦏</span>
              <div>
                <p class="font-bold text-white text-sm">Parc national de Chitwan</p>
                <p class="text-xs text-slate-300">Rhinocéros & pirogues de la Rapti</p>
              </div>
            </a>
            <a href="/destinations/suklaphanta.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 text-white transition-colors">
              <span class="text-base">🦌</span>
              <div>
                <p class="font-bold text-white text-sm">Parc national de Suklaphanta</p>
                <p class="text-xs text-slate-300">Cerfs des marais & ouest sauvage</p>
              </div>
            </a>
            <a href="/destinations/annapurna.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 text-white transition-colors">
              <span class="text-base">🏔️</span>
              <div>
                <p class="font-bold text-white text-sm">Les Annapurna & Pokhara</p>
                <p class="text-xs text-slate-300">Sommets mythiques & balcons alpins</p>
              </div>
            </a>
            <a href="/destinations/katmandou.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 text-white transition-colors">
              <span class="text-base">🕉️</span>
              <div>
                <p class="font-bold text-white text-sm">Katmandou</p>
                <p class="text-xs text-slate-300">Vallée des rois & temples sacrés</p>
              </div>
            </a>
            <a href="/destinations.html" onclick="toggleMobileMenu()" class="block w-full text-center py-2.5 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow mt-1">
              Voir toutes les destinations →
            </a>
          </div>
        </div>

        <!-- 3. L'esprit safari -->
        <a href="/index.html#concept" onclick="toggleMobileMenu()" class="p-3.5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/5 flex items-center gap-3 text-white transition-colors active:scale-98">
          <span class="text-base">🌿</span>
          <span class="font-bold text-white text-base">L'esprit safari</span>
        </a>

        <!-- 4. Maîtres pisteurs -->
        <a href="/index.html#pisteurs" onclick="toggleMobileMenu()" class="p-3.5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/5 flex items-center gap-3 text-white transition-colors active:scale-98">
          <span class="text-base">🐅</span>
          <span class="font-bold text-white text-base">Maîtres pisteurs</span>
        </a>

        <!-- 5. À propos -->
        <a href="/a-propos.html" onclick="toggleMobileMenu()" class="p-3.5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/5 flex items-center gap-3 text-white transition-colors active:scale-98">
          <span class="text-base">📖</span>
          <span class="font-bold text-white text-base">À propos</span>
        </a>

        <!-- Blog -->
        <a href="https://safarinepal.fr" target="_blank" rel="noopener noreferrer" class="p-3.5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/5 flex items-center gap-3 text-white transition-colors active:scale-98">
          <span class="text-base">📝</span>
          <span class="font-bold text-white text-base">Blog Carnets</span>
          <span class="text-xs bg-white/10 text-emerald-300 px-2 py-0.5 rounded font-mono ml-auto">↗</span>
        </a>

        <!-- 6. Contact -->
        <a href="/contact.html" onclick="toggleMobileMenu()" class="p-3.5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/5 flex items-center gap-3 text-white transition-colors active:scale-98">
          <span class="text-base">✉️</span>
          <span class="font-bold text-white text-base">Contact</span>
        </a>

      </nav>

      <!-- Bottom Drawer Actions -->
      <div class="pt-4 border-t border-white/15 space-y-3">
        <!-- Language Selector -->
        <div>
          <span class="text-[11px] font-bold text-slate-300 uppercase tracking-wider block mb-1.5">Langue / Language</span>
          <div class="grid grid-cols-4 gap-1.5">
            <button onclick="changeLanguage('fr')" data-lang-btn="fr" class="py-2.5 rounded-xl text-xs font-black flex items-center justify-center gap-1 bg-white/15 text-white hover:bg-white/25 active:scale-95 transition-all cursor-pointer border border-white/10">
              <span>🇫🇷</span> <span>FR</span>
            </button>
            <button onclick="changeLanguage('en')" data-lang-btn="en" class="py-2.5 rounded-xl text-xs font-black flex items-center justify-center gap-1 bg-white/15 text-white hover:bg-white/25 active:scale-95 transition-all cursor-pointer border border-white/10">
              <span>🇬🇧</span> <span>EN</span>
            </button>
            <button onclick="changeLanguage('de')" data-lang-btn="de" class="py-2.5 rounded-xl text-xs font-black flex items-center justify-center gap-1 bg-white/15 text-white hover:bg-white/25 active:scale-95 transition-all cursor-pointer border border-white/10">
              <span>🇩🇪</span> <span>DE</span>
            </button>
            <button onclick="changeLanguage('es')" data-lang-btn="es" class="py-2.5 rounded-xl text-xs font-black flex items-center justify-center gap-1 bg-white/15 text-white hover:bg-white/25 active:scale-95 transition-all cursor-pointer border border-white/10">
              <span>🇪🇸</span> <span>ES</span>
            </button>
          </div>
        </div>

        <!-- WhatsApp + Départs Buttons -->
        <div class="flex flex-col gap-2 pt-1">
          <a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="w-full flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-white text-slate-950 font-black text-xs sm:text-sm shadow-lg hover:bg-slate-100 active:scale-98 transition-all">
            <svg class="w-4 h-4 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
            <span>WhatsApp Direct (+33 6 95 41 32 27)</span>
          </a>

          <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="w-full text-center py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs sm:text-sm shadow-lg shadow-emerald-950/40 active:scale-98 transition-all">
            Explorer les 15 séjours & Départs →
          </a>
        </div>
      </div>

    </div>
  </div>"""

for fpath in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'<!-- MOBILE NAVIGATION DRAWER.*?</div>\s*</div>\s*(?=\n\s*<!-- ========================================================================= -->|\n\s*</header>|\n\s*<style>)',
        mobile_menu_code + '\n\n',
        content,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Replaced mobile menu in {fpath}")

