with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the plain four-worlds section with a high-end, atmospheric dark container
# with a panoramic horizontal photograph of Nepal (Himalayas sunrise + misty jungle)
# with subtle glassmorphism cards and elegant typography.

old_section = """  <!-- 4.1. NOS 4 UNIVERS D'EXPLORATION -->
  <section class="py-16 sm:py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
          Diversité des expériences
        </p>
        <h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight">
          Quatre façons d'éprouver le Népal
        </h2>
        <p class="mt-3 text-base text-slate-600 font-medium">
          Chaque voyageur a son propre rythme. Nos séjours s'articulent autour de quatre grands piliers d'exploration.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- 1. Jungle & Faune Sauvage -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            01
          </div>
          <h3 class="font-black text-xl text-slate-900">Safaris & Grands Félins</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Pistage silencieux à pied des tigres du Bengale, rhinocéros unicornes et éléphants dans les sanctuaires de Bardia, Chitwan et Suklaphanta.
          </p>
          <a href="/destinations/bardia.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Explorer la jungle →</a>
        </div>

        <!-- 2. Montagnes & Hauts Sommets -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            02
          </div>
          <h3 class="font-black text-xl text-slate-900">Hautes Montagnes & Treks</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Balcons alpins des Annapurna, expéditions panthère des neiges à Manang (3 600 m) et traversées de cols secrets loin de la foule.
          </p>
          <a href="/destinations/annapurna.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Découvrir les treks →</a>
        </div>

        <!-- 3. Culture & Vie de Village -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            03
          </div>
          <h3 class="font-black text-xl text-slate-900">Culture, Temples & Retraites</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Immersion chez l'habitant, découverte des cités sacrées de la vallée de Katmandou, festivals tibétains au Mustang (Tiji) et méditation.
          </p>
          <a href="/destinations/katmandou.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Vivre la culture →</a>
        </div>

        <!-- 4. Rivières & Bivouacs Sauvages -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            04
          </div>
          <h3 class="font-black text-xl text-slate-900">Expéditions Rivières & Bivouacs</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Descentes de rivières sauvages en rafting (Karnali), nuits sous tente sur les bancs de sable et feux de camp sous les étoiles de l'Himalaya.
          </p>
          <a href="/tours/rafting-safari.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Voir les expéditions →</a>
        </div>

      </div>

    </div>
  </section>"""

new_section = """  <!-- 4.1. NOS 4 UNIVERS D'EXPLORATION (DESIGN LUXE AVEC PHOTO PANORAMIQUE EN BACKGROUND & GLASSMORPHISM) -->
  <section class="relative py-24 sm:py-32 bg-slate-950 text-white overflow-hidden border-y border-white/10">
    <!-- Photo Panoramique Horizontale de l'Himalaya & du Népal Sauvage -->
    <div class="absolute inset-0 z-0">
      <img 
        src="/assets/original_site/himalayas_sunrise_peaks.webp" 
        alt="Chaîne himalayenne et sommets sacrés au lever du soleil" 
        class="w-full h-full object-cover opacity-30 scale-105 filter brightness-75 contrast-110"
        loading="lazy"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/80 to-slate-950/90"></div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- En-tête de section -->
      <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
        <p class="text-xs font-black tracking-widest uppercase text-slate-400 mb-3">
          Diversité des expériences
        </p>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          Quatre façons d'éprouver le Népal
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-normal leading-relaxed max-w-2xl mx-auto">
          Chaque voyageur a son propre rythme. Nos séjours s'articulent autour de quatre grands piliers d'exploration.
        </p>
      </div>

      <!-- Grille 4 Cartes Glassmorphism avec Reflet et Profondeur -->
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

      </div>

    </div>
  </section>"""

c = c.replace(old_section, new_section)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Upgraded 'Quatre façons d'éprouver le Népal' with stunning horizontal mountain background & glassmorphic cards!")
