import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero Section with the spacious, airy, exact text requested
new_hero = """  <!-- 3. HERO SECTION AÉRÉE & ÉPURÉE (WeRoad Luxe Vibe) -->
  <section class="relative min-h-[92vh] flex items-center justify-center pt-40 pb-32 px-4 sm:px-6 lg:px-8 overflow-hidden bg-jungle-950">
    
    <!-- Background Cinema Image with clean cinematic contrast -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" 
        alt="Tigre du Bengale dans le Parc National de Bardia au Népal" 
        class="w-full h-full object-cover object-center scale-100 filter brightness-75 contrast-105"
      />
      <!-- Subtle Atmospheric Overlay -->
      <div class="absolute inset-0 bg-gradient-to-t from-jungle-950/90 via-black/40 to-black/60"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
      
      <!-- Subtle Clean Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-slate-100 text-xs sm:text-sm font-semibold mb-8 shadow-sm">
        <span class="flex h-2 w-2 rounded-full bg-amber-400"></span>
        <span class="text-amber-300 font-bold uppercase tracking-wider text-[11px]">Écotourisme d'exception au Népal</span>
        <span class="text-white/40">•</span>
        <span class="text-slate-200 flex items-center gap-1 font-bold">
          <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i> 4.9/5 (Avis Vérifiés)
        </span>
      </div>

      <!-- EXACT H1 REQUESTED BY USER -->
      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl lg:text-8xl text-white tracking-tight leading-[1.08] drop-shadow-2xl">
        L'autre côté du Népal
      </h1>

      <!-- EXACT SUBTITLE POETRY REQUESTED BY USER -->
      <div class="mt-8 text-base sm:text-xl md:text-2xl text-slate-100 max-w-2xl font-medium leading-relaxed drop-shadow space-y-1.5">
        <p>Là où les routes s’arrêtent.</p>
        <p>Là où les territoires sauvages recommencent.</p>
        <p class="text-amber-200 font-semibold">Guidé par ceux qui y vivent.</p>
        <p class="pt-2 text-white font-bold">Offrez-vous votre voyage nature au Népal.</p>
      </div>

      <!-- WeRoad Airy Floating Search Bar -->
      <div class="w-full max-w-3xl mt-12 p-3 sm:p-4 rounded-3xl bg-white/95 backdrop-blur-2xl shadow-[0_25px_60px_rgba(0,0,0,0.4)] border border-white/60 text-left text-slate-900">
        <form onsubmit="handleSearch(event)" class="grid grid-cols-1 md:grid-cols-12 gap-3 items-center">
          
          <div class="md:col-span-5 p-3 rounded-2xl hover:bg-slate-100/80 transition-colors cursor-pointer">
            <label class="block text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
              Type de séjour
            </label>
            <div class="flex items-center gap-2 mt-1">
              <i data-lucide="compass" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <select id="search-dest" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer">
                <option value="all">Tous les 14 circuits</option>
                <option value="safari">Tigres & Jungle de Bardia (Pistage à pied)</option>
                <option value="bivouac">Bivouac & Camping Sauvage (Babai)</option>
                <option value="chitwan">Chitwan (Rhinocéros & Pirogue)</option>
                <option value="trek">Haut-Mustang & Lac Rara (Himalaya)</option>
                <option value="rafting">Rivières Sauvages Karnali (Rafting)</option>
                <option value="culture">Culture Tharu, Yoga & Carnet de Dessin</option>
              </select>
            </div>
          </div>

          <div class="hidden md:block w-[1px] h-10 bg-slate-200"></div>

          <div class="md:col-span-4 p-3 rounded-2xl hover:bg-slate-100/80 transition-colors cursor-pointer">
            <label class="block text-[11px] font-extrabold uppercase tracking-wider text-slate-500">
              Période idéale
            </label>
            <div class="flex items-center gap-2 mt-1">
              <i data-lucide="calendar" class="w-4 h-4 text-emerald-800 shrink-0"></i>
              <select id="search-date" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer">
                <option value="all">Saison 2026 - 2027</option>
                <option value="autumn">Automne (Oct - Déc)</option>
                <option value="winter">Hiver (Janv - Fév)</option>
                <option value="spring">Printemps (Mars - Mai)</option>
              </select>
            </div>
          </div>

          <div class="md:col-span-3 flex items-center">
            <button type="submit" class="w-full h-14 bg-gradient-to-r from-fire-600 to-fire-500 hover:from-fire-500 hover:to-fire-600 text-white font-black text-base rounded-2xl flex items-center justify-center gap-2 shadow-lg shadow-fire-600/30 hover:scale-[1.02] active:scale-95 transition-all">
              <i data-lucide="search" class="w-5 h-5"></i>
              <span>Explorer</span>
            </button>
          </div>

        </form>
      </div>

    </div>
  </section>

  <!-- REASSURANCE BAR (AÉRÉE, HORS DU HERO) -->
  <section class="bg-white border-y border-slate-200/90 py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div class="flex flex-col items-center">
          <p class="font-black text-2xl text-slate-900 tracking-tight">4 à 8 Max</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Silence & immersion totale</p>
        </div>
        <div class="flex flex-col items-center border-l border-slate-200/80">
          <p class="font-black text-2xl text-emerald-800 tracking-tight">BBC Wildlife</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Pisteurs certifiés faune sauvage</p>
        </div>
        <div class="flex flex-col items-center border-l border-slate-200/80">
          <p class="font-black text-2xl text-amber-700 tracking-tight">100% Local</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Retombées directes pour les villages</p>
        </div>
        <div class="flex flex-col items-center border-l border-slate-200/80">
          <p class="font-black text-2xl text-fire-600 tracking-tight">Sur-mesure</p>
          <p class="text-xs text-slate-500 font-medium mt-1">Coordinateur francophone (Robin)</p>
        </div>
      </div>
    </div>
  </section>"""

# Replace in html
# Find section 3 in html
pattern = r'<!-- 3\. HERO SECTION.*?</section>'
html = re.sub(pattern, new_hero, html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero successfully updated with spacious airy layout and requested copy!")
