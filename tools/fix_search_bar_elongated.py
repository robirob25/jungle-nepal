import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the elongated, luxurious, single-line horizontal search bar & perfect hero spacing
new_hero = """  <!-- 3. HERO SECTION AÉRÉE & ÉPURÉE (WeRoad Luxe Vibe) -->
  <section class="relative min-h-[95vh] flex items-center justify-center pt-48 pb-36 px-4 sm:px-6 lg:px-8 overflow-hidden bg-jungle-950">
    
    <!-- Background Cinema Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" 
        alt="Tigre du Bengale dans le Parc National de Bardia au Népal" 
        class="w-full h-full object-cover object-center filter brightness-75 contrast-105"
      />
      <!-- Atmospheric Gradient -->
      <div class="absolute inset-0 bg-gradient-to-t from-jungle-950/90 via-black/40 to-black/60"></div>
    </div>

    <div class="relative z-10 max-w-6xl mx-auto text-center flex flex-col items-center w-full">
      
      <!-- Subtle Trust Pill -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-slate-100 text-xs sm:text-sm font-semibold mb-6 shadow-sm">
        <span class="flex h-2 w-2 rounded-full bg-amber-400"></span>
        <span class="text-amber-300 font-bold uppercase tracking-wider text-[11px]">Écotourisme d'exception au Népal</span>
        <span class="text-white/40">•</span>
        <span class="text-slate-200 flex items-center gap-1 font-bold">
          <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i> 4.9/5 (Avis Vérifiés)
        </span>
      </div>

      <!-- EXACT H1 REQUESTED -->
      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl lg:text-[80px] text-white tracking-tight leading-[1.1] drop-shadow-2xl">
        L'autre côté du Népal
      </h1>

      <!-- EXACT SUBTITLE POETRY REQUESTED -->
      <div class="mt-6 text-base sm:text-xl md:text-2xl text-slate-100 max-w-3xl font-medium leading-relaxed drop-shadow space-y-1">
        <p>Là où les routes s’arrêtent.</p>
        <p>Là où les territoires sauvages recommencent.</p>
        <p class="text-amber-200 font-bold">Guidé par ceux qui y vivent.</p>
        <p class="pt-2 text-white font-extrabold">Offrez-vous votre voyage nature au Népal.</p>
      </div>

      <!-- ELONGATED & LUXURIOUS WEROAD SEARCH BAR (Single line, spacious, no ugly breaks) -->
      <div class="w-full max-w-5xl mt-12 p-3 sm:p-3.5 rounded-full bg-white/95 backdrop-blur-2xl shadow-[0_25px_60px_rgba(0,0,0,0.45)] border border-white/80 text-left text-slate-900">
        <form onsubmit="handleSearch(event)" class="flex flex-col lg:flex-row items-center justify-between gap-2 lg:gap-0">
          
          <!-- Field 1: Type de séjour -->
          <div class="w-full lg:flex-1 px-5 py-2.5 rounded-full hover:bg-slate-100/70 transition-colors cursor-pointer">
            <label class="block text-[10px] font-extrabold uppercase tracking-wider text-slate-400">
              Type de séjour
            </label>
            <div class="flex items-center gap-2.5 mt-0.5">
              <i data-lucide="compass" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <select id="search-dest" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer truncate">
                <option value="all">Tous les 14 circuits</option>
                <option value="safari">Tigres & Jungle de Bardia</option>
                <option value="bivouac">Bivouac & Camping Sauvage (Babai)</option>
                <option value="chitwan">Chitwan (Rhinocéros & Pirogue)</option>
                <option value="trek">Haut-Mustang & Lac Rara</option>
                <option value="rafting">Rivières Sauvages Karnali (Rafting)</option>
                <option value="culture">Culture Tharu, Yoga & Carnet</option>
              </select>
            </div>
          </div>

          <!-- Divider -->
          <div class="hidden lg:block w-px h-10 bg-slate-200/90 mx-1"></div>

          <!-- Field 2: Période idéale -->
          <div class="w-full lg:flex-1 px-5 py-2.5 rounded-full hover:bg-slate-100/70 transition-colors cursor-pointer">
            <label class="block text-[10px] font-extrabold uppercase tracking-wider text-slate-400">
              Période idéale
            </label>
            <div class="flex items-center gap-2.5 mt-0.5">
              <i data-lucide="calendar" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <select id="search-date" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer truncate">
                <option value="all">Saison 2026 - 2027 (Octobre à Mai)</option>
                <option value="autumn">Automne 2026 (Octobre - Décembre)</option>
                <option value="winter">Hiver 2026/2027 (Janvier - Février)</option>
                <option value="spring">Printemps 2027 (Mars - Mai • Pic Tigres)</option>
              </select>
            </div>
          </div>

          <!-- Divider -->
          <div class="hidden lg:block w-px h-10 bg-slate-200/90 mx-1"></div>

          <!-- Field 3: Groupe -->
          <div class="w-full lg:w-48 px-5 py-2.5 rounded-full hover:bg-slate-100/70 transition-colors cursor-pointer">
            <label class="block text-[10px] font-extrabold uppercase tracking-wider text-slate-400">
              Format
            </label>
            <div class="flex items-center gap-2.5 mt-0.5">
              <i data-lucide="users" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <span class="font-extrabold text-sm sm:text-base text-slate-900 whitespace-nowrap">
                Micro-groupe 4-8
              </span>
            </div>
          </div>

          <!-- Search Button -->
          <div class="w-full lg:w-auto p-1">
            <button type="submit" class="w-full lg:w-auto px-8 h-13 py-3.5 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-black text-sm sm:text-base rounded-full flex items-center justify-center gap-2.5 shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all whitespace-nowrap">
              <i data-lucide="search" class="w-4 h-4"></i>
              <span>Explorer les séjours</span>
            </button>
          </div>

        </form>
      </div>

    </div>
  </section>"""

pattern = r'<!-- 3\. HERO SECTION.*?</section>'
html = re.sub(pattern, new_hero, html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Elongated luxury search bar applied successfully!")
