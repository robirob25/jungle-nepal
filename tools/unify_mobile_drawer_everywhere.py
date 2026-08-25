import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

unified_mobile_drawer = """  <!-- MOBILE NAVIGATION DRAWER (EXACT REPLICA OF DESKTOP) -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-x-3 top-20 z-50 max-h-[85vh] overflow-y-auto bg-slate-950/98 backdrop-blur-2xl border border-white/15 rounded-3xl p-5 text-white shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-4 font-sans">
    
    <!-- Top Bar with Close Button -->
    <div class="flex items-center justify-between pb-3 border-b border-white/10">
      <span class="text-xs font-black uppercase tracking-widest text-emerald-400">Navigation</span>
      <button onclick="toggleMobileMenu()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white text-sm font-bold transition-colors cursor-pointer" aria-label="Fermer le menu">
        ✕
      </button>
    </div>

    <!-- Main Navigation Links (Exact Desktop Structure) -->
    <nav class="flex flex-col space-y-1.5 font-bold text-sm">
      
      <!-- 1. Tous les séjours -->
      <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl bg-white/5 hover:bg-white/10 flex items-center justify-between text-white transition-colors">
        <span class="flex items-center gap-2.5">
          <span>🐾</span>
          <span>Tous les 15 séjours</span>
        </span>
        <span class="bg-[#0e8354] text-white text-[11px] px-2.5 py-0.5 rounded-full font-black">15</span>
      </a>

      <!-- 2. Destinations Dropdown Accordion -->
      <div class="rounded-2xl bg-white/5 overflow-hidden">
        <button onclick="document.getElementById('mobile-dest-sub').classList.toggle('hidden'); document.getElementById('mobile-dest-arrow').classList.toggle('rotate-180');" class="w-full px-3.5 py-2.5 flex items-center justify-between text-white hover:bg-white/10 transition-colors text-left cursor-pointer">
          <span class="flex items-center gap-2.5">
            <span>🗺️</span>
            <span>Destinations</span>
          </span>
          <svg id="mobile-dest-arrow" xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-400 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        <div id="mobile-dest-sub" class="hidden px-2 pb-2.5 space-y-1 border-t border-white/5 pt-2">
          <a href="/destinations/bardia.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <span>🐅</span>
            <div>
              <p class="font-bold text-white">Parc national de Bardia</p>
              <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
            </div>
          </a>
          <a href="/destinations/chitwan.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <span>🦏</span>
            <div>
              <p class="font-bold text-white">Parc national de Chitwan</p>
              <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
            </div>
          </a>
          <a href="/destinations/suklaphanta.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <span>🦌</span>
            <div>
              <p class="font-bold text-white">Parc national de Suklaphanta</p>
              <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
            </div>
          </a>
          <a href="/destinations/annapurna.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <span>🏔️</span>
            <div>
              <p class="font-bold text-white">Les Annapurna & Pokhara</p>
              <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
            </div>
          </a>
          <a href="/destinations/katmandou.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <span>🕉️</span>
            <div>
              <p class="font-bold text-white">Katmandou</p>
              <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
            </div>
          </a>
          <a href="/destinations/index.html" onclick="toggleMobileMenu()" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow mt-1">
            Voir toutes les destinations →
          </a>
        </div>
      </div>

      <!-- 3. L'esprit safari -->
      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        <span>🌿</span>
        <span>L'esprit safari</span>
      </a>

      <!-- 4. Maîtres pisteurs -->
      <a href="/index.html#pisteurs" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        <span>🐅</span>
        <span>Maîtres pisteurs</span>
      </a>

      <!-- 5. À propos -->
      <a href="/a-propos.html" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        <span>📖</span>
        <span>À propos</span>
      </a>

      <!-- 6. Contact -->
      <a href="/contact.html" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        <span>✉️</span>
        <span>Contact</span>
      </a>

    </nav>

    <!-- Language Selector Buttons (4 Languages in 1 tap) -->
    <div class="pt-3 border-t border-white/10 space-y-2">
      <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider block">Langue / Language</span>
      <div class="grid grid-cols-4 gap-1.5">
        <button onclick="changeLanguage('fr')" data-lang-btn="fr" class="py-2 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1 bg-white/10 text-white hover:bg-white/20 transition-all cursor-pointer">
          <span>🇫🇷</span> <span>FR</span>
        </button>
        <button onclick="changeLanguage('en')" data-lang-btn="en" class="py-2 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1 bg-white/10 text-white hover:bg-white/20 transition-all cursor-pointer">
          <span>🇬🇧</span> <span>EN</span>
        </button>
        <button onclick="changeLanguage('de')" data-lang-btn="de" class="py-2 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1 bg-white/10 text-white hover:bg-white/20 transition-all cursor-pointer">
          <span>🇩🇪</span> <span>DE</span>
        </button>
        <button onclick="changeLanguage('es')" data-lang-btn="es" class="py-2 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1 bg-white/10 text-white hover:bg-white/20 transition-all cursor-pointer">
          <span>🇪🇸</span> <span>ES</span>
        </button>
      </div>
    </div>

    <!-- CTA Buttons (WhatsApp + Départs & Prix) -->
    <div class="pt-3 border-t border-white/10 flex flex-col gap-2">
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20vos%20séjours%20au%20Népal" target="_blank" class="w-full flex items-center justify-center gap-2 py-3 rounded-2xl bg-white text-slate-950 font-black text-xs shadow hover:bg-slate-100 transition-all">
        <svg class="w-4 h-4 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>WhatsApp Direct (+33 6 95 41 32 27)</span>
      </a>

      <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="w-full text-center py-3 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs shadow transition-all">
        Explorer les 15 séjours & Départs →
      </a>
    </div>

  </div>"""

updated_files = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    
    # Replace existing mobile-menu drawer block
    if 'id="mobile-menu"' in c:
        c = re.sub(
            r'<!--\s*(?:Mobile Drawer|MOBILE NAVIGATION DRAWER).*?id="mobile-menu".*?</div>\s*</div>',
            unified_mobile_drawer,
            c,
            flags=re.DOTALL
        )
    else:
        # Append mobile drawer right after header
        if '</header>' in c:
            c = c.replace('</header>', '</header>\n\n' + unified_mobile_drawer)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1

print(f"Applied unified mobile navigation drawer across {updated_files} files!")
