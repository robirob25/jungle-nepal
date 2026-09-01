import glob, re

# The gold-standard navigation links from index.astro:
# 1. Tous les 15 séjours (/ ou /#prochains-departs)
# 2. Destinations (Dropdown)
# 3. Nos guides (/#concept)
# 4. Galerie (/#galerie-faune)
# 5. À propos (/a-propos.html)
# 6. Contact (/contact.html)

dest_index_path = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro'

with open(dest_index_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace desktop nav in destinations/index.astro
desktop_nav_old = """      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-semibold text-white/90">
        <a href="/#prochains-departs" class="hover:text-amber-100 transition-colors">Tous les 15 séjours</a>

        <!-- Destinations Dropdown (Mega-menu style) -->
        <div class="relative group py-2">
          <a href="/destinations.html" class="hover:text-amber-100 transition-colors flex items-center gap-1.5 cursor-pointer">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div style="background-color: #041d13 !important;" class="border border-white/10 rounded-2xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white">
              <a href="/destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Parc national de Bardia</p>
                  <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
                </div>
              </a>
              <a href="/destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Parc national de Chitwan</p>
                  <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
                </div>
              </a>
              <a href="/destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Parc national de Suklaphanta</p>
                  <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
                </div>
              </a>
              <a href="/destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Les Annapurna & Pokhara</p>
                  <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
                </div>
              </a>
              <a href="/destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Katmandou</p>
                  <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
                </div>
              </a>

              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="/destinations.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
        <a href="/a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="/contact.html" class="hover:text-[#0e8354] transition-colors">Contact</a>
      </nav>"""

desktop_nav_new = """      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-semibold text-white/90 whitespace-nowrap">
        <a href="/#prochains-departs" class="hover:text-amber-100 transition-colors">Tous les 15 séjours</a>

        <!-- Destinations Dropdown (Mega-menu style) -->
        <div class="relative group py-2">
          <a href="/destinations.html" class="hover:text-amber-100 transition-colors flex items-center gap-1.5 cursor-pointer">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div style="background-color: #041d13 !important;" class="border border-white/10 rounded-2xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white">
              <a href="/destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Parc national de Bardia</p>
                  <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
                </div>
              </a>
              <a href="/destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Parc national de Chitwan</p>
                  <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
                </div>
              </a>
              <a href="/destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Parc national de Suklaphanta</p>
                  <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
                </div>
              </a>
              <a href="/destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Les Annapurna & Pokhara</p>
                  <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
                </div>
              </a>
              <a href="/destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Katmandou</p>
                  <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
                </div>
              </a>

              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="/destinations.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>

        <a href="/#concept" class="hover:text-amber-100 transition-colors">Nos guides</a>
        <a href="/#galerie-faune" class="hover:text-amber-100 transition-colors">Galerie</a>
        <a href="/a-propos.html" class="hover:text-amber-100 transition-colors font-extrabold">À propos</a>
        <a href="/contact.html" class="hover:text-amber-100 transition-colors">Contact</a>
      </nav>"""

if desktop_nav_old in c:
    c = c.replace(desktop_nav_old, desktop_nav_new)
    with open(dest_index_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("✓ Synced header in destinations/index.astro exactly to match homepage!")
else:
    print("Could not find exact snippet in destinations/index.astro")
