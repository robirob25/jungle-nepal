with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the plain Charte section with a stunning, high-end section styled exactly like the second screenshot:
# - Rich panoramic background image (Bardia river sunset or green misty jungle)
# - Subtitle and title with great contrast
# - 4 cards with individual authentic photos, clean 01-04 numbered badges, and elegant typography

old_charte_section = """  <!-- 6. NOS 4 PILIERS D'ENGAGEMENT -->
  <section class="py-20 sm:py-28 bg-slate-950 text-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="inline-block text-xs font-black uppercase tracking-widest text-slate-200 bg-white/10 px-3.5 py-1 rounded-full mb-3 border border-white/10">
          Éthique & Respect Absolu
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight">
          Notre charte d'immersion sauvage
        </h2>
        <p class="mt-3 text-base text-slate-300 font-medium">
          Pourquoi nos safaris à pied sont reconnus comme les plus respectueux du Népal.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        
        <div class="p-6 rounded-3xl bg-white/5 border border-white/10 space-y-4 hover:border-emerald-800/50 transition-colors">
          <div class="w-12 h-12 rounded-2xl bg-white/10 text-slate-200 flex items-center justify-center text-2xl">
            
          </div>
          <h3 class="font-black text-lg text-white">Zéro exploitation animale</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Nous refusons catégoriquement les balades à dos d'éléphant. Tous nos safaris se font à pied, en jeep ou en pirogue traditionnelle silencieuse.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-white/5 border border-white/10 space-y-4 hover:border-emerald-800/50 transition-colors">
          <div class="w-12 h-12 rounded-2xl bg-white/10 text-slate-200 flex items-center justify-center text-2xl">
            
          </div>
          <h3 class="font-black text-lg text-white">Pistage silencieux à pied</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Nous n'encerclons jamais les animaux. Nos maîtres pisteurs lisent les traces et attendent patiemment aux points d'eau sans perturber le biotope.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-white/5 border border-white/10 space-y-4 hover:border-emerald-800/50 transition-colors">
          <div class="w-12 h-12 rounded-2xl bg-white/10 text-slate-200 flex items-center justify-center text-2xl">
            
          </div>
          <h3 class="font-black text-lg text-white">Micro-groupes stricts</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Maximum 4 à 10 explorateurs par groupe. Cela garantit une discrétion absolue en forêt et des interactions privilégiées avec nos guides.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-white/5 border border-white/10 space-y-4 hover:border-emerald-800/50 transition-colors">
          <div class="w-12 h-12 rounded-2xl bg-white/10 text-slate-200 flex items-center justify-center text-2xl">
            
          </div>
          <h3 class="font-black text-lg text-white">Retombées 100% locales</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Rémunération juste des porteurs et pisteurs, soutien aux écoles villageoises et circuits conçus en partenariat direct avec les communautés locales.
          </p>
        </div>

      </div>

    </div>
  </section>"""

new_charte_section = """  <!-- 6. NOTRE CHARTE D'IMMERSION SAUVAGE (DESIGN IMMERSIF AVEC PHOTO BACKGROUND & 4 CARTES PHOTOS) -->
  <section class="relative py-24 sm:py-32 bg-slate-950 text-white overflow-hidden border-y border-white/10">
    <!-- Photo Panoramique Horizontale en Background -->
    <div class="absolute inset-0 z-0">
      <img 
        src="/assets/drive_photos/adrien_bardia_sunset.webp" 
        alt="Immersion sauvage et respect de la nature au Népal" 
        class="w-full h-full object-cover opacity-55 scale-105 filter brightness-90 contrast-105"
        loading="lazy"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/50 to-slate-950/70"></div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- En-tête de section -->
      <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
        <p class="text-xs font-black tracking-widest uppercase text-slate-300 mb-3">
          Éthique et respect absolu
        </p>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          Notre charte d'immersion sauvage
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-200 font-normal leading-relaxed max-w-2xl mx-auto">
          Pourquoi nos safaris et expéditions sont reconnus comme les plus respectueux du Népal.
        </p>
      </div>

      <!-- Grille 4 Cartes Immersives avec Photos Dédiées -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
        
        <!-- 1. Zéro exploitation animale -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/curated_gallery/troupeau_elephants_asie_lisiere.webp" 
              alt="Éléphants sauvages libres en jungle" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-75 filter brightness-95 contrast-105"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/50 to-slate-950/20"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              01
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Zéro exploitation animale
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Nous refusons catégoriquement les balades à dos d'éléphant. Tous nos safaris se font à pied, en jeep ou en pirogue traditionnelle silencieuse.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15 text-xs text-slate-300 font-bold">
            Protection animale intégrale
          </div>
        </div>

        <!-- 2. Pistage silencieux à pied -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/original_site/safari_pied.webp" 
              alt="Pistage silencieux à pied dans la jungle" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-75 filter brightness-95 contrast-105"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/50 to-slate-950/20"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              02
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Pistage silencieux à pied
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Nous n'encerclons jamais les animaux. Nos maîtres pisteurs lisent les traces et attendent patiemment aux points d'eau sans perturber le biotope.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15 text-xs text-slate-300 font-bold">
            Discrétion & écoute de la forêt
          </div>
        </div>

        <!-- 3. Micro-groupes stricts -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/original_site/bivouac_camp.webp" 
              alt="Micro groupe en campement sauvage" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-75 filter brightness-95 contrast-105"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/50 to-slate-950/20"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              03
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Micro-groupes stricts
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Maximum 4 à 10 explorateurs par groupe. Cela garantit une discrétion absolue en forêt et des interactions privilégiées avec nos guides.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15 text-xs text-slate-300 font-bold">
            Maximum 4 à 10 personnes
          </div>
        </div>

        <!-- 4. Retombées 100% locales -->
        <div class="group relative rounded-3xl overflow-hidden min-h-[380px] sm:min-h-[420px] p-7 flex flex-col justify-between shadow-2xl border border-white/15 bg-slate-950 transition-all duration-300 hover:border-white/30 hover:-translate-y-1">
          <div class="absolute inset-0 z-0">
            <img 
              src="/assets/drive_photos/adrien_enfants_ecole.webp" 
              alt="Retombées directes pour les communautés et villages" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-75 filter brightness-95 contrast-105"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/50 to-slate-950/20"></div>
          </div>

          <div class="relative z-10 space-y-3">
            <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur-md border border-white/15 text-white flex items-center justify-center font-mono font-extrabold text-xs">
              04
            </div>
            <h3 class="font-black text-xl text-white group-hover:text-amber-100 transition-colors leading-snug">
              Retombées 100% locales
            </h3>
            <p class="text-xs sm:text-[13px] text-slate-200 leading-relaxed font-normal">
              Rémunération juste des porteurs et pisteurs, soutien aux écoles villageoises et circuits conçus en partenariat direct avec les communautés.
            </p>
          </div>

          <div class="relative z-10 pt-4 border-t border-white/15 text-xs text-slate-300 font-bold">
            Économie solidaire et Tharu
          </div>
        </div>

      </div>

    </div>
  </section>"""

c = c.replace(old_charte_section, new_charte_section)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Upgraded 'Notre charte d'immersion sauvage' to match the 4-cards photo design with panoramic background!")
