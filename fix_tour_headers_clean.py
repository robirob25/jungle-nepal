import os
import re

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

clean_tour_header = f"""  <!-- HEADER STICKY -->
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
          <a href="../destinations/index.html" class="hover:text-[#0e8354] transition-colors flex items-center gap-1 cursor-pointer">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <!-- Menu Déroulant Sombre Opaque Élite -->
          <div class="absolute top-full left-0 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div class="bg-slate-950/98 backdrop-blur-2xl border border-white/20 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.6)] space-y-1 text-white">
              
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

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header block cleanly
    content = re.sub(r'<header[^>]*>.*?</header>', clean_tour_header, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed header across all 14 tour pages perfectly!")
