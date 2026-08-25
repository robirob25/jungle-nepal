with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Import tours.json in frontmatter
if "import toursData" not in c:
    c = c.replace(
        "import Layout from '../layouts/Layout.astro';",
        "import Layout from '../layouts/Layout.astro';\nimport toursData from '../data/tours.json';"
    )

# The section to add right before <!-- 7. FOOTER CLASSIQUE -->
tours_section = """  <!-- 6. PROPOSITIONS DE SÉJOURS & EXPÉDITIONS PHARES -->
  <section class="py-16 sm:py-24 bg-[#faf8f5] text-slate-900 border-t border-slate-200 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12 sm:mb-14">
        <div>
          <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-100 text-[#0e8354] font-extrabold text-xs uppercase tracking-widest border border-emerald-200 mb-3">
            <span>🐾</span> <span>Expéditions signature</span>
          </span>
          <h2 class="text-2xl sm:text-4xl lg:text-5xl font-black text-slate-950 tracking-tight leading-tight">
            Prêts à explorer le Népal sauvage ?
          </h2>
          <p class="mt-2 text-slate-600 text-sm sm:text-base font-normal max-w-2xl">
            Découvrez une sélection de nos séjours les plus plébiscités, encadrés par Pawan et nos maîtres pisteurs natifs en micro-groupes de 4 à 10 personnes.
          </p>
        </div>
        <div class="shrink-0">
          <a href="/index.html#prochains-departs" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-full bg-slate-900 hover:bg-slate-800 text-white font-extrabold text-xs sm:text-sm shadow-md hover:scale-105 active:scale-95 transition-all">
            <span>Voir les 15 séjours</span>
            <span>→</span>
          </a>
        </div>
      </div>

      <!-- 4 Curated Tour Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
        
        <!-- TOUR 1: Bardia Explorateur (5j) -->
        <article class="bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-lg hover:shadow-2xl hover:border-emerald-500/50 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
          <div class="relative aspect-[4/3] overflow-hidden bg-slate-900">
            <img src="/assets/original_site/tigre_route.webp" alt="Bardia explorateur" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
            <div class="absolute top-3 left-3">
              <span class="px-2.5 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-[11px] font-black text-amber-300 border border-white/20 shadow-md">
                Best-seller
              </span>
            </div>
            <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-white text-xs font-bold">
              <span>📍 Bardia</span>
              <span class="bg-emerald-600/90 px-2 py-0.5 rounded-lg backdrop-blur-md">5 jours</span>
            </div>
          </div>
          <div class="p-5 sm:p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 text-xs font-semibold text-slate-500 mb-1">
                <span>Micro-groupe 4 à 10 pers.</span>
                <span class="text-amber-500 font-bold">⭐ 4.8</span>
              </div>
              <h3 class="font-black text-lg text-slate-900 group-hover:text-[#0e8354] transition-colors leading-snug">
                Bardia explorateur – 5 jours dans la jungle
              </h3>
              <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                Le grand classique du pistage à pied des tigres du Bengale au cœur du parc national le plus préservé.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <div>
                <span class="text-[10px] text-slate-400 font-semibold block uppercase">À partir de</span>
                <span class="text-lg font-black text-slate-900">490€</span>
              </div>
              <a href="/tours/bardia-explorateur.html" class="px-4 py-2 rounded-xl bg-emerald-50 text-[#0e8354] group-hover:bg-[#0e8354] group-hover:text-white font-extrabold text-xs transition-colors">
                Découvrir →
              </a>
            </div>
          </div>
        </article>

        <!-- TOUR 2: Chitwan + Bardia (11j) -->
        <article class="bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-lg hover:shadow-2xl hover:border-emerald-500/50 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
          <div class="relative aspect-[4/3] overflow-hidden bg-slate-900">
            <img src="/assets/original_site/chitwan_rhino.webp" alt="Chitwan + Bardia" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
            <div class="absolute top-3 left-3">
              <span class="px-2.5 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-[11px] font-black text-amber-300 border border-white/20 shadow-md">
                Grand combiné
              </span>
            </div>
            <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-white text-xs font-bold">
              <span>📍 Chitwan & Bardia</span>
              <span class="bg-emerald-600/90 px-2 py-0.5 rounded-lg backdrop-blur-md">11 jours</span>
            </div>
          </div>
          <div class="p-5 sm:p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 text-xs font-semibold text-slate-500 mb-1">
                <span>Micro-groupe 4 à 10 pers.</span>
                <span class="text-amber-500 font-bold">⭐ 4.9</span>
              </div>
              <h3 class="font-black text-lg text-slate-900 group-hover:text-[#0e8354] transition-colors leading-snug">
                Chitwan + Bardia – l’aventure jungle complète
              </h3>
              <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                L'alliance parfaite entre rhinocéros unicornes de Chitwan et tigres royaux de Bardia en un seul voyage.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <div>
                <span class="text-[10px] text-slate-400 font-semibold block uppercase">À partir de</span>
                <span class="text-lg font-black text-slate-900">1,490€</span>
              </div>
              <a href="/tours/chitwan-bardia-complete.html" class="px-4 py-2 rounded-xl bg-emerald-50 text-[#0e8354] group-hover:bg-[#0e8354] group-hover:text-white font-extrabold text-xs transition-colors">
                Découvrir →
              </a>
            </div>
          </div>
        </article>

        <!-- TOUR 3: Babai Spécial Tigres (5j) -->
        <article class="bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-lg hover:shadow-2xl hover:border-emerald-500/50 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
          <div class="relative aspect-[4/3] overflow-hidden bg-slate-900">
            <img src="/assets/drive_photos/julien_safari_a_pied.webp" alt="Babai spécial tigres" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
            <div class="absolute top-3 left-3">
              <span class="px-2.5 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-[11px] font-black text-amber-300 border border-white/20 shadow-md">
                100% Sauvage
              </span>
            </div>
            <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-white text-xs font-bold">
              <span>📍 Vallée de la Babai</span>
              <span class="bg-emerald-600/90 px-2 py-0.5 rounded-lg backdrop-blur-md">5 jours</span>
            </div>
          </div>
          <div class="p-5 sm:p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 text-xs font-semibold text-slate-500 mb-1">
                <span>Micro-groupe 4 à 10 pers.</span>
                <span class="text-amber-500 font-bold">⭐ 4.9</span>
              </div>
              <h3 class="font-black text-lg text-slate-900 group-hover:text-[#0e8354] transition-colors leading-snug">
                Deep into the wild : Babai spécial experience – 5 jours
              </h3>
              <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                Pénétration exclusive dans la vallée secrète de la Babai, zone ultra-protégée aux densités exceptionnelles de félins.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <div>
                <span class="text-[10px] text-slate-400 font-semibold block uppercase">À partir de</span>
                <span class="text-lg font-black text-slate-900">890€</span>
              </div>
              <a href="/tours/babai-special.html" class="px-4 py-2 rounded-xl bg-emerald-50 text-[#0e8354] group-hover:bg-[#0e8354] group-hover:text-white font-extrabold text-xs transition-colors">
                Découvrir →
              </a>
            </div>
          </div>
        </article>

        <!-- TOUR 4: Panthère des Neiges (17j) -->
        <article class="bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-lg hover:shadow-2xl hover:border-emerald-500/50 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group">
          <div class="relative aspect-[4/3] overflow-hidden bg-slate-900">
            <img src="/assets/curated_gallery/panthere_des_neiges_affut_rocher.webp" alt="Panthère des neiges" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
            <div class="absolute top-3 left-3">
              <span class="px-2.5 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-[11px] font-black text-amber-300 border border-white/20 shadow-md">
                Expédition d'élite
              </span>
            </div>
            <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-white text-xs font-bold">
              <span>📍 Haut Manang</span>
              <span class="bg-emerald-600/90 px-2 py-0.5 rounded-lg backdrop-blur-md">17 jours</span>
            </div>
          </div>
          <div class="p-5 sm:p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 text-xs font-semibold text-slate-500 mb-1">
                <span>Micro-groupe 4 à 10 pers.</span>
                <span class="text-amber-500 font-bold">⭐ 5.0</span>
              </div>
              <h3 class="font-black text-lg text-slate-900 group-hover:text-[#0e8354] transition-colors leading-snug">
                Expédition : panthère des neiges exclusive
              </h3>
              <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                9 jours de traque intense à plus de 4 000m d'altitude aux côtés des pisteurs tibétains pour observer le fantôme des montagnes.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <div>
                <span class="text-[10px] text-slate-400 font-semibold block uppercase">À partir de</span>
                <span class="text-lg font-black text-slate-900">3,490€</span>
              </div>
              <a href="/tours/panthere-des-neiges.html" class="px-4 py-2 rounded-xl bg-emerald-50 text-[#0e8354] group-hover:bg-[#0e8354] group-hover:text-white font-extrabold text-xs transition-colors">
                Découvrir →
              </a>
            </div>
          </div>
        </article>

      </div>

      <!-- Bottom Direct CTA -->
      <div class="mt-12 text-center">
        <a href="/index.html#prochains-departs" class="inline-flex items-center gap-3 px-8 py-4 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-extrabold text-sm shadow-xl shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <span>Explorer l'ensemble de nos 15 séjours & départs garantis</span>
          <span>→</span>
        </a>
      </div>

    </div>
  </section>

"""

footer_marker = "  <!-- 7. FOOTER CLASSIQUE -->"
if footer_marker in c:
    c = c.replace(footer_marker, tours_section + "\n  " + footer_marker)
    with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print("✓ Successfully added tours section to a-propos.astro!")
else:
    print("Could not find footer marker in a-propos.astro")
