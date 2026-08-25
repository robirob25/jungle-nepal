import re
import os

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Desktop Navbar for index.html
new_index_nav = """<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-white/90 drop-shadow">
      <a href="#prochains-departs" class="hover:text-amber-300 transition-colors">Départs</a>
      <a href="#prochains-departs" class="hover:text-amber-300 transition-colors">Destinations</a>
      <a href="#concept" class="hover:text-amber-300 transition-colors">L'esprit safari</a>
      <a href="#pisteurs" class="hover:text-amber-300 transition-colors">Maîtres pisteurs</a>
      <a href="a-propos.html" class="hover:text-amber-300 transition-colors font-extrabold">À propos</a>
      <a href="#avis" class="hover:text-amber-300 transition-colors">Avis ★ 5.0</a>
      <a href="contact.html" class="hover:text-amber-300 transition-colors">Contacte-nous</a>
    </nav>"""

html = re.sub(r'<nav class=\"hidden lg:flex[^>]*>.*?</nav>', new_index_nav, html, flags=re.DOTALL)

# Mobile Menu for index.html
new_index_mobile = """<div id="mobile-menu" class="hidden lg:hidden fixed inset-x-4 top-24 z-50 bg-slate-950/95 backdrop-blur-2xl border border-white/15 rounded-3xl p-6 text-white space-y-4 shadow-2xl">
    <nav class="flex flex-col space-y-3 font-bold text-base">
      <a href="#prochains-departs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center justify-between">
        <span><i data-lucide="compass" class="w-4 h-4 inline mr-2"></i>Tous les 14 circuits 2026/2027</span>
        <span class="bg-[#0e8354] text-xs px-2 py-0.5 rounded-full font-black">14</span>
      </a>
      <a href="a-propos.html" class="px-3 py-2 rounded-xl bg-white/10 text-amber-300">
        📖 Notre histoire & équipe
      </a>
      <a href="#concept" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        <i data-lucide="trees" class="w-4 h-4 inline mr-2"></i>L'esprit safari & éthique
      </a>
      <a href="#pisteurs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        <i data-lucide="users" class="w-4 h-4 inline mr-2"></i>Nos maîtres pisteurs (BBC)
      </a>
      <a href="contact.html" class="px-3 py-2 rounded-xl hover:bg-white/10 text-amber-300">
        ✉️ Contactez-nous
      </a>
      <a href="#avis" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        ⭐ Avis Trustpilot (5.0/5)
      </a>
    </nav>
    <div class="pt-4 border-t border-white/10 flex flex-col gap-2">
      <button onclick="toggleMobileMenu(); openCustomTripModal()" class="w-full py-3.5 rounded-2xl bg-[#0e8354] font-black text-sm text-center shadow-lg">
        Créer mon séjour sur-mesure ✨
      </button>
    </div>
  </div>"""

html = re.sub(r'<div id=\"mobile-menu\"[^>]*>.*?</div>\s*</div>', new_index_mobile, html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update a-propos.html navbar & links
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'r', encoding='utf-8') as f:
    about_c = f.read()

new_about_nav = """<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-white/90 drop-shadow">
      <a href="index.html#prochains-departs" class="hover:text-amber-300 transition-colors">Départs</a>
      <a href="index.html#prochains-departs" class="hover:text-amber-300 transition-colors">Destinations</a>
      <a href="index.html#concept" class="hover:text-amber-300 transition-colors">L'esprit safari</a>
      <a href="index.html#pisteurs" class="hover:text-amber-300 transition-colors">Maîtres pisteurs</a>
      <a href="a-propos.html" class="text-amber-300 border-b-2 border-amber-300 pb-0.5 font-black">À propos</a>
      <a href="index.html#avis" class="hover:text-amber-300 transition-colors">Avis ★ 5.0</a>
      <a href="contact.html" class="hover:text-amber-300 transition-colors">Contacte-nous</a>
    </nav>"""

about_c = re.sub(r'<nav class=\"hidden lg:flex[^>]*>.*?</nav>', new_about_nav, about_c, flags=re.DOTALL)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'w', encoding='utf-8') as f:
    f.write(about_c)

# 3. Update contact.html navbar & links
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/contact.html', 'r', encoding='utf-8') as f:
    contact_c = f.read()

new_contact_nav = """<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-slate-700">
        <a href="index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Départs</a>
        <a href="index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Destinations</a>
        <a href="index.html#concept" class="hover:text-[#0e8354] transition-colors">L'esprit safari</a>
        <a href="index.html#pisteurs" class="hover:text-[#0e8354] transition-colors">Maîtres pisteurs</a>
        <a href="a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="index.html#avis" class="hover:text-[#0e8354] transition-colors">Avis ★ 5.0</a>
        <a href="contact.html" class="text-[#0e8354] border-b-2 border-[#0e8354] pb-0.5 font-black">Contacte-nous</a>
      </nav>"""

contact_c = re.sub(r'<nav class=\"hidden lg:flex[^>]*>.*?</nav>', new_contact_nav, contact_c, flags=re.DOTALL)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_c)

# 4. Update all 14 tour pages navbars
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        tc = f.read()
    
    new_tour_nav = """<nav class="hidden md:flex items-center gap-6 text-[13px] font-bold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors">Itinéraire détaillé</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors">Inclus & Extras</a>
        <a href="../a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors">Avis</a>
        <a href="../contact.html" class="hover:text-[#0e8354] transition-colors">Contact</a>
      </nav>"""
    
    tc = re.sub(r'<nav class=\"hidden md:flex[^>]*>.*?</nav>', new_tour_nav, tc, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(tc)

print("All navbars and mobile menus synchronized with 'À propos' and 'Contacte-nous'!")
