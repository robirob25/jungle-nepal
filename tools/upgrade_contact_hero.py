with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the gradient hero with an authentic, high-impact horizontal photography from Drive (River crossing / Sunset in Bardia)
# Remove the "Conseils & Échanges directs" pill button

old_hero = """  <!-- 3. HERO EN-TÊTE DE LA PAGE CONTACT -->
  <section class="bg-gradient-to-b from-slate-900 via-[#05281a] to-slate-950 text-white py-14 sm:py-20 relative overflow-hidden border-b border-white/10">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-emerald-600/20 via-transparent to-transparent pointer-events-none"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Breadcrumb -->
      <nav class="flex items-center gap-2 text-xs font-semibold text-emerald-400 mb-4" aria-label="Fil d'Ariane">
        <a href="/index.html" class="hover:underline opacity-80">Accueil</a>
        <span class="opacity-50">/</span>
        <span class="text-white">Contact</span>
      </nav>

      <div class="max-w-3xl">
        <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/20 text-[#10b981] font-extrabold text-xs uppercase tracking-widest border border-emerald-500/30 mb-4">
          <span>🌿</span> <span>Conseils & Échanges directs</span>
        </span>
        <h1 class="font-black text-3xl sm:text-4xl md:text-5xl text-white tracking-tight leading-tight">
          Parlons de votre prochaine aventure au Népal
        </h1>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mt-4 font-medium">
          Que vous ayez une question précise sur un circuit, un projet sur-mesure ou besoin de conseils pour caler votre itinéraire, notre équipe locale et Robin vous répondent sous 24h.
        </p>
      </div>
    </div>
  </section>"""

new_hero = """  <!-- 3. HERO EN-TÊTE DE LA PAGE CONTACT (PHOTO DRIVE HORIZONTALE EFFET WAHOU) -->
  <section class="relative min-h-[380px] sm:min-h-[440px] flex items-center bg-slate-950 text-white overflow-hidden py-16 sm:py-24 border-b border-white/10">
    <!-- Photo Drive Horizontale Authentique (Bardia Sunset River Horizon) -->
    <div class="absolute inset-0 z-0">
      <img 
        src="/assets/drive_photos/adrien_bardia_sunset.webp" 
        alt="Coucher de soleil sauvage sur la rivière Karnali à Bardia Népal" 
        class="w-full h-full object-cover opacity-60 scale-105 filter brightness-90"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/75 to-slate-950/40"></div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
      <!-- Breadcrumb -->
      <nav class="flex items-center gap-2 text-xs font-semibold text-emerald-400 mb-4" aria-label="Fil d'Ariane">
        <a href="/index.html" class="hover:underline opacity-80">Accueil</a>
        <span class="opacity-50">/</span>
        <span class="text-white">Contact</span>
      </nav>

      <div class="max-w-2xl space-y-3">
        <h1 class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-white tracking-tight leading-tight drop-shadow-[0_4px_20px_rgba(0,0,0,0.9)]">
          Parlons de votre prochaine aventure au Népal.
        </h1>
        <p class="text-slate-200 text-sm sm:text-base md:text-lg leading-relaxed font-normal drop-shadow-[0_2px_10px_rgba(0,0,0,0.8)] pt-2">
          Que vous ayez une question sur un itinéraire, une demande de voyage privatisé ou besoin de conseils directs, Robin et nos maîtres pisteurs vous répondent sous 24h.
        </p>
      </div>
    </div>
  </section>"""

c = c.replace(old_hero, new_hero)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced contact gradient with stunning horizontal drive photo and removed badge!")
