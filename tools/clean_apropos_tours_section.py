with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the top-right button "Voir les 15 séjours →"
old_header = """      <!-- Section Header -->
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
      </div>"""

new_header = """      <!-- Section Header -->
      <div class="max-w-3xl mb-10 sm:mb-12">
        <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-100 text-[#0e8354] font-extrabold text-xs uppercase tracking-widest border border-emerald-200 mb-3">
          <span>🐾</span> <span>Expéditions signature</span>
        </span>
        <h2 class="text-2xl sm:text-4xl lg:text-5xl font-black text-slate-950 tracking-tight leading-tight">
          Prêts à explorer le Népal sauvage ?
        </h2>
        <p class="mt-2 text-slate-600 text-sm sm:text-base font-normal max-w-2xl leading-relaxed">
          Découvrez une sélection de nos séjours les plus plébiscités, encadrés par Pawan et nos maîtres pisteurs natifs en micro-groupes de 4 à 10 personnes.
        </p>
      </div>"""

content = content.replace(old_header, new_header)

# 2. Fix the missing snow leopard image path:
content = content.replace(
    '/assets/curated_gallery/panthere_des_neiges_affut_rocher.webp',
    '/assets/snow-leopard/snow_leopard_portrait.webp'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Cleaned header and fixed snow leopard photo in a-propos.astro!")
