import re, glob, os

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

svg_hamburger_dark_header = """<button onclick="toggleMobileMenu()" class="lg:hidden w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 text-white border border-white/20 backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Ouvrir le menu / Open menu">
        <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="4" y1="6" x2="20" y2="6"></line>
          <line x1="4" y1="12" x2="20" y2="12"></line>
          <line x1="4" y1="18" x2="20" y2="18"></line>
        </svg>
      </button>"""

svg_hamburger_light_header = """<button onclick="toggleMobileMenu()" class="lg:hidden w-10 h-10 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Ouvrir le menu / Open menu">
        <svg class="w-5 h-5 text-slate-800" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="4" y1="6" x2="20" y2="6"></line>
          <line x1="4" y1="12" x2="20" y2="12"></line>
          <line x1="4" y1="18" x2="20" y2="18"></line>
        </svg>
      </button>"""

# Mobile drawer HTML for tour detail pages if missing
mobile_drawer_tour = """  <!-- Mobile Drawer -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-x-4 top-20 z-50 bg-slate-950/95 backdrop-blur-2xl border border-white/15 rounded-3xl p-6 text-white space-y-4 shadow-2xl">
    <div class="flex items-center justify-between pb-3 border-b border-white/10">
      <span class="font-extrabold text-sm text-emerald-400">Navigation</span>
      <button onclick="toggleMobileMenu()" class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-white text-xs hover:bg-white/20">✕</button>
    </div>
    <nav class="flex flex-col space-y-2.5 font-bold text-sm">
      <a href="/index.html" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center gap-2">
        <span>🏠</span>
        <span>Accueil</span>
      </a>
      <a href="/index.html#prochains-departs" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center justify-between text-amber-300">
        <span class="flex items-center gap-2"><span>🐾</span><span>Tous les 15 séjours</span></span>
        <span class="bg-[#0e8354] text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>
      </a>
      <a href="/destinations/index.html" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center gap-2">
        <span>🗺️</span>
        <span>Destinations</span>
      </a>
      <a href="/a-propos.html" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center gap-2">
        <span>📖</span>
        <span>À propos</span>
      </a>
      <a href="/contact.html" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center gap-2">
        <span>✉️</span>
        <span>Contact</span>
      </a>
    </nav>
    <div class="pt-3 border-t border-white/10">
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin" target="_blank" class="w-full flex items-center justify-center gap-2 py-3 rounded-2xl bg-[#0e8354] text-white font-black text-xs shadow">
        <span>WhatsApp Direct</span>
      </a>
    </div>
  </div>"""

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    is_tour = '/tours/' in fpath
    target_btn = svg_hamburger_light_header if is_tour else svg_hamburger_dark_header

    # Replace any lucide hamburger or old button with pure SVG button
    c = re.sub(
        r'<button\s+onclick=["\'](?:toggleMobileMenu\(\)|document\.getElementById\([\'"]mobile-menu[\'"]\)\.classList\.toggle\([\'"]hidden[\'"]\))["\'][^>]*>.*?</button>',
        target_btn,
        c,
        flags=re.DOTALL
    )

    # In tour pages, ensure mobile drawer is present
    if is_tour and 'id="mobile-menu"' not in c:
        c = c.replace('</header>', '</header>\n\n' + mobile_drawer_tour)

    # In tour pages, ensure toggleMobileMenu function is present
    if is_tour and 'function toggleMobileMenu' not in c:
        c = c.replace('</main>', '</main>\n\n<script is:inline>\nfunction toggleMobileMenu() {\n  const menu = document.getElementById("mobile-menu");\n  if (menu) menu.classList.toggle("hidden");\n}\n</script>')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print(f"Upgraded mobile hamburger menu button with pure inline SVG across all {len(astro_files)} files!")
