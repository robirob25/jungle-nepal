with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the 4 cards with authentic horizontal background photos for each of the 4 worlds,
# with strict sentence case (une seule majuscule au début, pas de majuscules à chaque mot)
# and clean white/slate numbering (zero vert fluo!).

old_section_block = """      <!-- Grille 4 Cartes Glassmorphism avec Reflet et Profondeur -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
        
        <!-- 1. Jungle & Faune Sauvage -->
        <div class="group relative rounded-3xl p-7 bg-white/[0.04] backdrop-blur-xl border border-white/10 hover:border-emerald-700/60 hover:bg-white/[0.07] transition-all duration-300 flex flex-col justify-between shadow-2xl">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-800/40 text-emerald-300 flex items-center justify-center font-mono font-black text-sm">
              01
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-emerald-300 transition-colors leading-snug">
              Safaris & Grands Félins
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-300 leading-relaxed font-normal">
              Pistage silencieux à pied des tigres du Bengale, rhinocéros unicornes et éléphants dans les sanctuaires de Bardia, Chitwan et Suklaphanta.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10">
            <a href="/destinations/bardia.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-200 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Explorer la jungle</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- 2. Montagnes & Hauts Sommets -->
        <div class="group relative rounded-3xl p-7 bg-white/[0.04] backdrop-blur-xl border border-white/10 hover:border-emerald-700/60 hover:bg-white/[0.07] transition-all duration-300 flex flex-col justify-between shadow-2xl">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-800/40 text-emerald-300 flex items-center justify-center font-mono font-black text-sm">
              02
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-emerald-300 transition-colors leading-snug">
              Hautes Montagnes & Treks
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-300 leading-relaxed font-normal">
              Balcons alpins des Annapurna, expéditions panthère des neiges à Manang (3 600 m) et traversées de cols secrets loin de la foule.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10">
            <a href="/destinations/annapurna.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-200 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Découvrir les treks</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- 3. Culture & Vie de Village -->
        <div class="group relative rounded-3xl p-7 bg-white/[0.04] backdrop-blur-xl border border-white/10 hover:border-emerald-700/60 hover:bg-white/[0.07] transition-all duration-300 flex flex-col justify-between shadow-2xl">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-800/40 text-emerald-300 flex items-center justify-center font-mono font-black text-sm">
              03
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-emerald-300 transition-colors leading-snug">
              Culture, Temples & Retraites
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-300 leading-relaxed font-normal">
              Immersion chez l'habitant, découverte des cités sacrées de Katmandou et Bhaktapur, festivals tibétains au Mustang (Tiji) et méditation.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10">
            <a href="/destinations/katmandou.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-200 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Vivre la culture</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- 4. Rivières & Bivouacs Sauvages -->
        <div class="group relative rounded-3xl p-7 bg-white/[0.04] backdrop-blur-xl border border-white/10 hover:border-emerald-700/60 hover:bg-white/[0.07] transition-all duration-300 flex flex-col justify-between shadow-2xl">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-800/40 text-emerald-300 flex items-center justify-center font-mono font-black text-sm">
              04
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-emerald-300 transition-colors leading-snug">
              Expéditions Rivières & Bivouacs
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-300 leading-relaxed font-normal">
              Descentes de rivières sauvages en rafting (Karnali), nuits sous tente sur les bancs de sable et feux de camp sous les étoiles de l'Himalaya.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10">
            <a href="/tours/rafting-safari.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-200 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Voir les expéditions</span>
              <span>→</span>
            </a>
          </div>
        </div>

      </div>"""

new_section_block = """      <!-- Grille 4 Cartes avec Photos Immersives en Arrière-Plan & Typographie Sobre -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
        
        <!-- 1. Jungle & Faune Sauvage -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/drive_photos/julien_tigre_bengale3.webp" 
              alt="Safari tigre en jungle" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-45 filter brightness-75"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/70 to-slate-950/40"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              01
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Safaris et grands félins
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Pistage silencieux à pied des tigres du Bengale, rhinocéros unicornes et éléphants dans les sanctuaires de Bardia, Chitwan et Suklaphanta.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15">
            <a href="/destinations/bardia.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-100 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Explorer la jungle</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- 2. Montagnes & Hauts Sommets -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/original_site/machapuchare.webp" 
              alt="Sommets sacrés des Annapurna" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-45 filter brightness-75"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/70 to-slate-950/40"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              02
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Hautes montagnes et treks
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Balcons alpins des Annapurna, expéditions panthère des neiges à Manang (3 600 m) et traversées de cols secrets loin de la foule.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15">
            <a href="/destinations/annapurna.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-100 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Découvrir les treks</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- 3. Culture & Vie de Village -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/drive_photos/adrien_bhaktapur1.webp" 
              alt="Temples sacrés et vie locale" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-45 filter brightness-75"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/70 to-slate-950/40"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              03
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Culture, temples et retraites
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Immersion chez l'habitant, découverte des cités royales de Katmandou et Bhaktapur, festivals tibétains au Mustang (Tiji) et méditation.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15">
            <a href="/destinations/katmandou.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-100 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Vivre la culture</span>
              <span>→</span>
            </a>
          </div>
        </div>

        <!-- 4. Rivières & Bivouacs Sauvages -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/drive_photos/adrien_bardia_river.webp" 
              alt="Expédition rivière et rafting" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-45 filter brightness-75"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/70 to-slate-950/40"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              04
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Expéditions rivières et bivouacs
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Descentes de rivières sauvages en rafting (Karnali), nuits sous tente sur les bancs de sable et feux de camp sous les étoiles de l'Himalaya.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15">
            <a href="/tours/rafting-safari.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-slate-100 group-hover:text-white group-hover:translate-x-1 transition-all">
              <span>Voir les expéditions</span>
              <span>→</span>
            </a>
          </div>
        </div>

      </div>"""

c = c.replace(old_section_block, new_section_block)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced cards with photo backgrounds, removed fluorescent colors, and enforced strict sentence-case titles!")
