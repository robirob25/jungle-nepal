import re

search_bar_fr = """<!-- SEARCH CARD WEROAD LUXE (AVEC ICÔNES INLINE GARANTIES & BOUTON RECHERCHE) -->
      <div class="w-full max-w-3xl mt-10 bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.35)] p-2 sm:p-2.5 border border-slate-100 text-left text-slate-900">
        <form onsubmit="handleSearch(event)" class="flex flex-col sm:flex-row items-center justify-between gap-1.5 sm:gap-2">
          
          <!-- Column 1: Où ? -->
          <div class="w-full sm:flex-1 px-4 sm:px-5 py-2.5 rounded-2xl hover:bg-slate-50 transition-colors cursor-pointer group/field">
            <div class="flex items-center gap-1.5 text-[11px] font-extrabold text-[#0e8354] uppercase tracking-wider">
              <svg class="w-3.5 h-3.5 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>OÙ ?</span>
            </div>
            <div class="relative mt-0.5">
              <select id="search-dest" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer pr-6 appearance-none">
                <option value="all">Tous les 14 circuits</option>
                <option value="safari">🐅 Bardia (Tigres & Safaris à pied)</option>
                <option value="bivouac">⛺ Vallée de Babai (Bivouacs)</option>
                <option value="chitwan">🦏 Chitwan (Rhinocéros & Pirogues)</option>
                <option value="grand-tour">🇳🇵 Grands Tours 360° (Jungle + Sommets)</option>
                <option value="aventure">🚣 Aventure (Rafting Karnali & 4x4)</option>
                <option value="culture">🕉️ Culture, Mustang & Spiritualité</option>
              </select>
              <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center text-slate-400">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </div>
          </div>

          <!-- Divider -->
          <div class="hidden sm:block w-px h-10 bg-slate-200"></div>

          <!-- Column 2: Quand ? -->
          <div class="w-full sm:flex-1 px-4 sm:px-5 py-2.5 rounded-2xl hover:bg-slate-50 transition-colors cursor-pointer group/field">
            <div class="flex items-center gap-1.5 text-[11px] font-extrabold text-[#0e8354] uppercase tracking-wider">
              <svg class="w-3.5 h-3.5 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
              <span>QUAND ?</span>
            </div>
            <div class="relative mt-0.5">
              <select id="search-date" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer pr-6 appearance-none">
                <option value="all">Toute l'année (Saison 2026-2027)</option>
                <option value="autumn">Automne 2026 (Octobre - Décembre)</option>
                <option value="winter">Hiver 2026/2027 (Janvier - Février)</option>
                <option value="spring">Printemps 2027 (Mars - Mai • Pic Tigres)</option>
              </select>
              <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center text-slate-400">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </div>
          </div>

          <!-- Square Emerald Action Button with Search Icon & Text -->
          <div class="w-full sm:w-auto p-1">
            <button type="submit" class="w-full sm:w-auto px-6 py-3.5 sm:py-3.5 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-black text-sm rounded-2xl flex items-center justify-center gap-2.5 shadow-lg shadow-[#0e8354]/40 hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer" aria-label="Rechercher">
              <svg class="w-5 h-5 text-white stroke-[2.5]" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <span class="font-extrabold tracking-tight">Rechercher</span>
            </button>
          </div>

        </form>
      </div>"""

search_bar_en = """<!-- SEARCH CARD WEROAD LUXE EN -->
      <div class="w-full max-w-3xl mt-10 bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.35)] p-2 sm:p-2.5 border border-slate-100 text-left text-slate-900">
        <form onsubmit="handleSearch(event)" class="flex flex-col sm:flex-row items-center justify-between gap-1.5 sm:gap-2">
          
          <!-- Column 1: WHERE ? -->
          <div class="w-full sm:flex-1 px-4 sm:px-5 py-2.5 rounded-2xl hover:bg-slate-50 transition-colors cursor-pointer group/field">
            <div class="flex items-center gap-1.5 text-[11px] font-extrabold text-[#0e8354] uppercase tracking-wider">
              <svg class="w-3.5 h-3.5 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>WHERE ?</span>
            </div>
            <div class="relative mt-0.5">
              <select id="search-dest" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer pr-6 appearance-none">
                <option value="all">All 14 Expeditions</option>
                <option value="safari">🐅 Bardia (Tigers & Walking Safaris)</option>
                <option value="bivouac">⛺ Babai Valley (Wild Bivouacs)</option>
                <option value="chitwan">🦏 Chitwan (Rhinos & River Canoes)</option>
                <option value="grand-tour">🇳🇵 360° Grand Tours (Jungle + Peaks)</option>
                <option value="aventure">🚣 Adventure (Karnali Rafting & 4x4)</option>
                <option value="culture">🕉️ Culture, Mustang & Spirituality</option>
              </select>
              <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center text-slate-400">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </div>
          </div>

          <!-- Divider -->
          <div class="hidden sm:block w-px h-10 bg-slate-200"></div>

          <!-- Column 2: WHEN ? -->
          <div class="w-full sm:flex-1 px-4 sm:px-5 py-2.5 rounded-2xl hover:bg-slate-50 transition-colors cursor-pointer group/field">
            <div class="flex items-center gap-1.5 text-[11px] font-extrabold text-[#0e8354] uppercase tracking-wider">
              <svg class="w-3.5 h-3.5 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
              <span>WHEN ?</span>
            </div>
            <div class="relative mt-0.5">
              <select id="search-date" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer pr-6 appearance-none">
                <option value="all">All Year (Season 2026-2027)</option>
                <option value="autumn">Autumn 2026 (October - December)</option>
                <option value="winter">Winter 2026/2027 (January - February)</option>
                <option value="spring">Spring 2027 (March - May • Peak Tigers)</option>
              </select>
              <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center text-slate-400">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </div>
          </div>

          <!-- Square Emerald Action Button with Search Icon & Text -->
          <div class="w-full sm:w-auto p-1">
            <button type="submit" class="w-full sm:w-auto px-6 py-3.5 sm:py-3.5 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-black text-sm rounded-2xl flex items-center justify-center gap-2.5 shadow-lg shadow-[#0e8354]/40 hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer" aria-label="Search">
              <svg class="w-5 h-5 text-white stroke-[2.5]" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <span class="font-extrabold tracking-tight">Search</span>
            </button>
          </div>

        </form>
      </div>"""

# Search handler JS
search_js = """
  function handleSearch(e) {
    if (e) e.preventDefault();
    const dest = document.getElementById('search-dest')?.value || 'all';
    if (typeof filterTrips === 'function') {
      filterTrips(dest);
    }
    const target = document.getElementById('prochains-departs');
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  }
"""

for fpath, bar in [
    ('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', search_bar_fr),
    ('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', search_bar_fr),
    ('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', search_bar_en),
    ('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', search_bar_en)
]:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the search card
    c = re.sub(r'<!-- SEARCH CARD WEROAD.*?</div>\s*</div>\s*</div>', bar, c, flags=re.DOTALL)
    
    # Ensure handleSearch is present
    if 'function handleSearch' not in c:
        c = c.replace('</script>', search_js + '\n</script>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Upgraded search bar with guaranteed inline SVGs, labels, and beautiful CTA across all pages!")
