import os, re, glob

def update_homepage(file_path, is_en=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Ensure Mobile Menu is modern, complete, and contains all links + destinations accordion
    if is_en:
        mobile_menu_html = """  <!-- Mobile Navigation Drawer -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-2xl p-6 text-white overflow-y-auto transition-all duration-300">
    <div class="flex items-center justify-between pb-6 border-b border-white/10">
      <a href="/en/index.html" class="flex items-center gap-2">
        <img src="/assets/logo.png" alt="Jungle Nepal Adventure" class="h-12 w-auto object-contain filter drop-shadow">
      </a>
      <button onclick="toggleMobileMenu()" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white hover:bg-white/20 active:scale-95 transition-all" aria-label="Close menu">
        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>

    <nav class="py-6 space-y-4 font-bold text-base">
      <a href="/en/index.html#prochains-departs" onclick="toggleMobileMenu()" class="flex items-center justify-between p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-white">
        <span class="flex items-center gap-3"><span>🧭</span><span>All 15 Expeditions</span></span>
        <span class="bg-[#0e8354] text-xs px-2.5 py-0.5 rounded-full font-black">15</span>
      </a>

      <!-- Destinations Collapsible in Mobile -->
      <div class="p-3 rounded-2xl bg-white/5 space-y-2">
        <div class="text-xs font-black uppercase tracking-widest text-emerald-400 px-1 pt-1">Destinations</div>
        <div class="grid grid-cols-1 gap-1 text-sm font-semibold">
          <a href="/en/destinations/bardia.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🐅</span><span>Bardia National Park</span></a>
          <a href="/en/destinations/chitwan.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🦏</span><span>Chitwan National Park</span></a>
          <a href="/en/destinations/suklaphanta.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🦌</span><span>Suklaphanta Reserve</span></a>
          <a href="/en/destinations/annapurna.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🏔️</span><span>Annapurna & Pokhara</span></a>
          <a href="/en/destinations/katmandou.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🕉️</span><span>Kathmandu Valley</span></a>
        </div>
      </div>

      <a href="/en/a-propos.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-amber-300">
        <span>📖</span><span>About Us & Team</span>
      </a>
      <a href="/en/index.html#concept" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10">
        <span>🌿</span><span>Safari Spirit & Ethics</span>
      </a>
      <a href="/en/index.html#pisteurs" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10">
        <span>🐾</span><span>Master Trackers (BBC)</span>
      </a>
      <a href="/en/contact.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-white">
        <span>✉️</span><span>Contact Us</span>
      </a>
    </nav>

    <div class="pt-4 border-t border-white/10 space-y-3">
      <a href="https://wa.me/33695413227?text=Hello%20Robin%2C%20I%20would%20like%20information%20on%20expeditions" target="_blank" class="w-full flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-sm shadow-lg">
        <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>Direct WhatsApp (Robin)</span>
      </a>
      <div class="flex items-center justify-center gap-4 text-xs text-slate-400 font-bold pt-2">
        <a href="/index.html" class="hover:text-white">🇫🇷 Français</a>
        <span>•</span>
        <a href="/en/index.html" class="text-amber-300">🇬🇧 English</a>
      </div>
    </div>
  </div>"""
    else:
        mobile_menu_html = """  <!-- Mobile Navigation Drawer -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-2xl p-6 text-white overflow-y-auto transition-all duration-300">
    <div class="flex items-center justify-between pb-6 border-b border-white/10">
      <a href="/index.html" class="flex items-center gap-2">
        <img src="/assets/logo.png" alt="Jungle Nepal Adventure" class="h-12 w-auto object-contain filter drop-shadow">
      </a>
      <button onclick="toggleMobileMenu()" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white hover:bg-white/20 active:scale-95 transition-all" aria-label="Fermer le menu">
        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>

    <nav class="py-6 space-y-4 font-bold text-base">
      <a href="/index.html#prochains-departs" onclick="toggleMobileMenu()" class="flex items-center justify-between p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-white">
        <span class="flex items-center gap-3"><span>🧭</span><span>Tous les 15 séjours</span></span>
        <span class="bg-[#0e8354] text-xs px-2.5 py-0.5 rounded-full font-black">15</span>
      </a>

      <!-- Destinations Collapsible in Mobile -->
      <div class="p-3 rounded-2xl bg-white/5 space-y-2">
        <div class="text-xs font-black uppercase tracking-widest text-emerald-400 px-1 pt-1">Destinations</div>
        <div class="grid grid-cols-1 gap-1 text-sm font-semibold">
          <a href="/destinations/bardia.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🐅</span><span>Parc national de Bardia</span></a>
          <a href="/destinations/chitwan.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🦏</span><span>Parc national de Chitwan</span></a>
          <a href="/destinations/suklaphanta.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🦌</span><span>Parc national de Suklaphanta</span></a>
          <a href="/destinations/annapurna.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🏔️</span><span>Les Annapurna & Pokhara</span></a>
          <a href="/destinations/katmandou.html" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10"><span>🕉️</span><span>Katmandou & Vallée</span></a>
        </div>
      </div>

      <a href="/a-propos.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-amber-300">
        <span>📖</span><span>Notre histoire & équipe</span>
      </a>
      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10">
        <span>🌿</span><span>L'esprit safari & éthique</span>
      </a>
      <a href="/index.html#pisteurs" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10">
        <span>🐾</span><span>Maîtres pisteurs (BBC)</span>
      </a>
      <a href="/contact.html" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl bg-white/5 hover:bg-white/10 text-white">
        <span>✉️</span><span>Contactez-nous</span>
      </a>
    </nav>

    <div class="pt-4 border-t border-white/10 space-y-3">
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20vos%20séjours%20au%20Népal" target="_blank" class="w-full flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-sm shadow-lg">
        <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>WhatsApp Direct (Robin)</span>
      </a>
      <div class="flex items-center justify-center gap-4 text-xs text-slate-400 font-bold pt-2">
        <a href="/index.html" class="text-amber-300">🇫🇷 Français</a>
        <span>•</span>
        <a href="/en/index.html" class="hover:text-white">🇬🇧 English</a>
      </div>
    </div>
  </div>"""

    # Replace mobile drawer
    c = re.sub(r'<!-- Mobile Drawer -->.*?</div>\s*<!-- Hero', mobile_menu_html + '\n\n  <!-- Hero', c, flags=re.DOTALL)
    c = re.sub(r'<div id="mobile-menu".*?</div>\s*<!-- Hero', mobile_menu_html + '\n\n  <!-- Hero', c, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"✓ Upgraded mobile menu on {file_path}")

update_homepage('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', is_en=False)
update_homepage('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', is_en=True)
