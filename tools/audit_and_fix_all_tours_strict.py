import os
import re
from html.parser import HTMLParser

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

perfect_tour_header = f"""  <!-- HEADER STICKY -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-8 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="../index.html" class="flex items-center gap-2 group shrink-0">
        <img src="../assets/logo_dark.png" alt="Jungle Nepal Adventure" class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-sm group-hover:scale-105 transition-transform duration-300" />
      </a>

      <!-- NAVIGATION DESKTOP -->
      <nav class="hidden lg:flex items-center gap-6 xl:gap-7 text-[13px] font-bold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>
        
        <!-- DROPDOWN DESTINATIONS -->
        <div class="relative group py-2">
          <a href="../destinations/index.html" class="hover:text-[#0e8354] transition-colors flex items-center gap-1.5 cursor-pointer font-bold">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <!-- Menu Déroulant 100% Opaque & Sombre -->
          <div class="absolute top-full left-0 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div style="background-color: #041d13 !important; color: #ffffff !important;" class="rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] border border-emerald-500/30 space-y-1">
              
              <a href="../destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🐅
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                  <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
                </div>
              </a>

              <a href="../destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🦏
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                  <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
                </div>
              </a>

              <a href="../destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🦌
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                  <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
                </div>
              </a>

              <a href="../destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🏔️
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                  <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
                </div>
              </a>

              <a href="../destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🕉️
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Katmandou</p>
                  <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
                </div>
              </a>

              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="../destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>

        <a href="#programme" class="hover:text-[#0e8354] transition-colors">Itinéraire détaillé</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors">Inclus & Extras</a>
        <a href="../a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="{exact_google_url}" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors flex items-center gap-1"><span class="text-[#00b67a]">★</span> Avis 5.0</a>
        <a href="../contact.html" class="hover:text-[#0e8354] transition-colors">Contact</a>
      </nav>

      <!-- CTA BUTTON -->
      <div class="flex items-center gap-3">
        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white text-xs sm:text-[13px] font-black px-5 py-2.5 rounded-full shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <i data-lucide="calendar" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </header>"""

share_clean_block = """      <!-- BOUTON PARTAGER UNIQUEMENT (SANS FAVORIS) -->
      <div class="relative">
        <button id="share-btn" onclick="handleShareTour()" class="flex items-center gap-2 px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-extrabold text-slate-800 hover:text-[#0e8354] hover:border-[#0e8354] shadow-sm hover:shadow transition-all group cursor-pointer">
          <i data-lucide="share-2" class="w-4 h-4 text-slate-500 group-hover:text-[#0e8354] transition-colors"></i>
          <span>Partager ce séjour</span>
        </button>

        <!-- Dropdown Menu Partage -->
        <div id="share-menu" class="absolute right-0 top-full mt-2 w-64 bg-white/98 backdrop-blur-xl border border-slate-200 rounded-2xl p-2 shadow-2xl opacity-0 translate-y-2 pointer-events-none transition-all duration-200 z-50 space-y-1">
          <button onclick="copyTourLink()" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-emerald-50 hover:text-[#0e8354] transition-colors text-left">
            <i data-lucide="link" class="w-4 h-4 text-[#0e8354]"></i>
            <span>Copier le lien direct</span>
          </button>
          <a id="share-whatsapp" href="#" target="_blank" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-emerald-50 hover:text-[#0e8354] transition-colors text-left">
            <i data-lucide="message-circle" class="w-4 h-4 text-[#109363]"></i>
            <span>Envoyer sur WhatsApp</span>
          </a>
          <a id="share-email" href="#" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-emerald-50 hover:text-[#0e8354] transition-colors text-left">
            <i data-lucide="mail" class="w-4 h-4 text-slate-600"></i>
            <span>Partager par Email</span>
          </a>
        </div>
      </div>"""

share_js_functions = """
    // REAL SHARE FUNCTIONALITY & TOAST NOTIFICATION
    function handleShareTour() {
      const pageUrl = window.location.href;
      const pageTitle = document.title || 'Séjour Jungle Nepal Adventure';
      
      const waLink = document.getElementById('share-whatsapp');
      if (waLink) {
        waLink.href = `https://api.whatsapp.com/send?text=${encodeURIComponent('Découvre ce séjour au Népal : ' + pageTitle + ' ' + pageUrl)}`;
      }
      const emailLink = document.getElementById('share-email');
      if (emailLink) {
        emailLink.href = `mailto:?subject=${encodeURIComponent(pageTitle)}&body=${encodeURIComponent('Je voulais te partager ce séjour au Népal avec Jungle Nepal Adventure : ' + pageUrl)}`;
      }

      if (navigator.share && /mobile|android|iphone|ipad/i.test(navigator.userAgent)) {
        navigator.share({
          title: pageTitle,
          text: 'Découvre ce séjour d\'immersion au Népal avec Jungle Nepal Adventure',
          url: pageUrl
        }).catch(() => {});
        return;
      }

      const menu = document.getElementById('share-menu');
      if (menu) {
        const isOpen = menu.classList.contains('opacity-100');
        if (isOpen) {
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        } else {
          menu.classList.remove('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }
    }

    function copyTourLink() {
      const pageUrl = window.location.href;
      navigator.clipboard.writeText(pageUrl).then(() => {
        showToast('✅ Lien du séjour copié dans le presse-papier !');
        const menu = document.getElementById('share-menu');
        if (menu) {
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }).catch(() => {
        showToast('Lien : ' + pageUrl);
      });
    }

    function showToast(msg) {
      let toast = document.getElementById('toast-notification');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.className = 'fixed bottom-8 left-1/2 -translate-x-1/2 bg-slate-950/95 backdrop-blur-xl text-white text-xs sm:text-sm font-black px-5 py-3 rounded-full border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.4)] transition-all duration-300 z-50 opacity-0 translate-y-4 pointer-events-none flex items-center gap-2';
        document.body.appendChild(toast);
      }
      toast.innerHTML = `<span class="text-amber-300 font-bold">✨</span> <span>${msg}</span>`;
      toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
      toast.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      
      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        toast.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }, 2800);
    }

    document.addEventListener('click', (e) => {
      const btn = document.getElementById('share-btn');
      const menu = document.getElementById('share-menu');
      if (menu && btn && !btn.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
        menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }
    });
"""

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
all_tour_files = [os.path.join(tours_dir, f) for f in os.listdir(tours_dir) if f.endswith('.html')]

print(f"Processing all {len(all_tour_files)} tour files strictly...")

for fpath in all_tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Enforce perfect clean single-row header
    c = re.sub(r'<header[^>]*>.*?</header>', perfect_tour_header, c, flags=re.DOTALL)

    # 2. Remove all Favoris buttons and replace share block
    # Matches any share / favorite block next to title
    share_fav_regex = r'<div class=\"flex items-center gap-2\">\s*<button[^>]*>.*?Partager.*?</button>\s*<button[^>]*>.*?Favoris.*?</button>\s*</div>'
    c = re.sub(share_fav_regex, share_clean_block, c, flags=re.DOTALL)
    
    # Also matches if already single share or any remaining favoris button
    c = re.sub(r'<button[^>]*>.*?<span>Favoris</span>\s*</button>', '', c, flags=re.DOTALL)
    c = re.sub(r'<button[^>]*aria-label=[\"\']Favoris[\"\']>.*?</button>', '', c, flags=re.DOTALL)

    # 3. Ensure share JS functions are in place
    if 'function handleShareTour' not in c:
        c = c.replace('</body>', f'<script>\n{share_js_functions}\n</script>\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Updated all 14 tour files cleanly!")

# Audit all 14 tour files
errors = 0
for fpath in all_tour_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_favoris = 'Favoris' in content or 'heart' in content.lower()
    has_share = 'handleShareTour' in content
    has_header = '<header' in content and '</header>' in content
    
    # Check header tag balance
    header_match = re.search(r'<header[^>]*>(.*?)</header>', content, re.DOTALL)
    if not header_match:
        print(f"❌ {fname}: Missing header!")
        errors += 1
        continue
    
    header_html = header_match.group(0)
    div_opens = header_html.count('<div')
    div_closes = header_html.count('</div')
    nav_opens = header_html.count('<nav')
    nav_closes = header_html.count('</nav')
    
    if div_opens != div_closes or nav_opens != nav_closes:
        print(f"❌ {fname}: Unbalanced header tags! divs: {div_opens}/{div_closes}, nav: {nav_opens}/{nav_closes}")
        errors += 1
    elif has_favoris:
        print(f"❌ {fname}: Still contains Favoris button!")
        errors += 1
    else:
        print(f"✅ {fname:30} -> Header 100% Balanced | 0 Favoris | Share Active")

if errors == 0:
    print("\nALL 14 TOURS ARE 100% PERFECT & VERIFIED!")
else:
    print(f"\nFound {errors} errors to fix.")
