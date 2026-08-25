import re, glob, os

# 1. Update index.astro top banner:
# Simplify promo text to fit cleanly on mobile screens:
# "✨ -100€ sur votre prochain tour en nov 2027 : code JUNGLE100"
# and ensure it wraps nicely or stays compact.
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace the top-bar in index.astro
top_bar_old = r'<aside aria-label="Bannière d\'information".*?</aside>'
top_bar_new = """<aside aria-label="Bannière d'information" class="bg-gradient-to-r from-[#073021] via-[#0e5c3e] to-[#073021] text-white text-xs sm:text-[13px] py-2 px-3 sm:px-4 font-bold relative z-50 text-center border-b border-emerald-500/20 shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-2">
      <div class="w-4 hidden sm:block"></div>
      <div class="flex-1 flex items-center justify-center gap-1.5 text-center text-[11px] sm:text-xs">
        <span>✨ <strong>-100€</strong> sur votre séjour nov 2027 avec le code <span class="bg-white/15 px-1.5 py-0.5 rounded text-amber-300 font-extrabold border border-amber-300/30 font-mono tracking-wider">JUNGLE100</span></span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/80 hover:text-white text-sm leading-none px-1 cursor-pointer shrink-0" aria-label="Fermer">✕</button>
    </div>
  </aside>"""

idx_content = re.sub(top_bar_old, top_bar_new, idx_content, flags=re.DOTALL)

# Update Mobile Navigation Drawer in index.astro and Header.astro:
# - No "Navigation" title (just close button aligned or minimal header)
# - "Explorer les 15 séjours et départs →" (lowercase d on départs)
# - No smileys
mobile_menu_template = """  <!-- MOBILE NAVIGATION DRAWER (OPAQUE, NO EMOJIS, CLEAN) -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-x-3 top-20 z-50 max-h-[85vh] overflow-y-auto bg-slate-950 border border-white/15 rounded-3xl p-5 text-white shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-4 font-sans">
    
    <!-- Top Bar with Close Button -->
    <div class="flex items-center justify-end pb-2 border-b border-white/10">
      <button onclick="toggleMobileMenu()" class="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white text-sm font-bold transition-colors cursor-pointer" aria-label="Fermer le menu">
        ✕
      </button>
    </div>

    <!-- Main Navigation Links -->
    <nav class="flex flex-col space-y-1.5 font-bold text-sm">
      
      <!-- 1. Tous les séjours -->
      <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl bg-white/5 hover:bg-white/10 flex items-center justify-between text-white transition-colors">
        <span>Tous les 15 séjours</span>
        <span class="bg-[#0e8354] text-white text-[11px] px-2.5 py-0.5 rounded-full font-black">15</span>
      </a>

      <!-- 2. Destinations Dropdown Accordion -->
      <div class="rounded-2xl bg-white/5 overflow-hidden">
        <button onclick="document.getElementById('mobile-dest-sub').classList.toggle('hidden'); document.getElementById('mobile-dest-arrow').classList.toggle('rotate-180');" class="w-full px-3.5 py-2.5 flex items-center justify-between text-white hover:bg-white/10 transition-colors text-left cursor-pointer">
          <span>Destinations</span>
          <svg id="mobile-dest-arrow" xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-400 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        <div id="mobile-dest-sub" class="hidden px-2 pb-2.5 space-y-1 border-t border-white/5 pt-2">
          <a href="/destinations/bardia.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div>
              <p class="font-bold text-white">Parc national de Bardia</p>
              <p class="text-[10px] text-slate-400">Tigres du Bengale &amp; safaris à pied</p>
            </div>
          </a>
          <a href="/destinations/chitwan.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div>
              <p class="font-bold text-white">Parc national de Chitwan</p>
              <p class="text-[10px] text-slate-400">Rhinocéros &amp; pirogues de la Rapti</p>
            </div>
          </a>
          <a href="/destinations/suklaphanta.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div>
              <p class="font-bold text-white">Parc national de Suklaphanta</p>
              <p class="text-[10px] text-slate-400">Cerfs des marais &amp; ouest sauvage</p>
            </div>
          </a>
          <a href="/destinations/annapurna.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div>
              <p class="font-bold text-white">Les Annapurna &amp; Pokhara</p>
              <p class="text-[10px] text-slate-400">Sommets mythiques &amp; balcons alpins</p>
            </div>
          </a>
          <a href="/destinations/katmandou.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div>
              <p class="font-bold text-white">Katmandou</p>
              <p class="text-[10px] text-slate-400">Vallée des rois &amp; temples sacrés</p>
            </div>
          </a>
          <a href="/destinations.html" onclick="toggleMobileMenu()" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow mt-1">
            Voir toutes les destinations →
          </a>
        </div>
      </div>

      <!-- 3. L'esprit safari -->
      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center text-slate-200 hover:text-white transition-colors">
        <span>L'esprit safari</span>
      </a>

      <!-- 4. Maîtres pisteurs -->
      <a href="/index.html#pisteurs" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center text-slate-200 hover:text-white transition-colors">
        <span>Maîtres pisteurs</span>
      </a>

      <!-- 5. À propos -->
      <a href="/a-propos.html" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center text-slate-200 hover:text-white transition-colors">
        <span>À propos</span>
      </a>

      <!-- Blog -->
      <a href="https://safarinepal.fr" target="_blank" rel="noopener noreferrer" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center justify-between text-slate-200 hover:text-white transition-colors">
        <span>Blog</span>
        <span class="text-[10px] bg-white/10 text-slate-300 px-1.5 py-0.5 rounded font-mono">↗</span>
      </a>

      <!-- 6. Contact -->
      <a href="/contact.html" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center text-slate-200 hover:text-white transition-colors">
        <span>Contact</span>
      </a>

    </nav>

    <!-- Language Selector Buttons -->
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

    <!-- CTA Buttons -->
    <div class="pt-3 border-t border-white/10 flex flex-col gap-2">
      <a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="w-full flex items-center justify-center gap-2 py-3 rounded-2xl bg-white text-slate-950 font-black text-xs shadow hover:bg-slate-100 transition-all">
        <svg class="w-4 h-4 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>WhatsApp Direct (+33 6 95 41 32 27)</span>
      </a>

      <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="w-full text-center py-3 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs shadow transition-all">
        Explorer les 15 séjours et départs →
      </a>
    </div>

  </div>"""

# Update index.astro mobile menu
idx_content = re.sub(
    r'<!-- MOBILE NAVIGATION DRAWER.*?</div>\s*</div>\s*(?=\n\s*<!-- ========================================================================= -->)',
    mobile_menu_template + '\n\n',
    idx_content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("✓ index.astro updated successfully")

# Update Header.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'r', encoding='utf-8') as f:
    hdr_content = f.read()

hdr_content = re.sub(
    r'<!-- MOBILE NAVIGATION DRAWER.*?</div>\s*</div>\s*</div>(\s*\n\s*</header>|\s*\n\s*<style>|\s*$)',
    mobile_menu_template + r'\1',
    hdr_content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(hdr_content)
print("✓ Header.astro updated successfully")

# Also check any occurrences of "Explorer les 15 séjours & Départs" or "Explorer les 15 séjours et Départs" across all files and replace with "Explorer les 15 séjours et départs"
all_astro = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)
for fpath in all_astro:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    orig_c = c
    c = c.replace("Explorer les 15 séjours & Départs", "Explorer les 15 séjours et départs")
    c = c.replace("Explorer les 15 séjours & départs", "Explorer les 15 séjours et départs")
    c = c.replace("Explorer les 15 séjours et Départs", "Explorer les 15 séjours et départs")
    if c != orig_c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Fixed casing in {os.path.basename(fpath)}")

