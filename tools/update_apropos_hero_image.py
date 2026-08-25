with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

import re

new_hero_html = """  <!-- 3. HERO IMMERSIF (PHOTO AUTHENTIQUE DRIVE : SAFARI À PIED EN JUNGLE) -->
  <section class="relative min-h-[580px] sm:min-h-[640px] flex items-center justify-center bg-slate-950 text-white overflow-hidden pt-36 pb-20 sm:pt-44 sm:pb-28">
    <!-- Image de fond authentique du Drive -->
    <div class="absolute inset-0 z-0">
      <img 
        src="/assets/drive_photos/julien_safari_a_pied.webp" 
        alt="Pistage à pied dans la jungle de Bardia Népal" 
        class="w-full h-full object-cover opacity-65 scale-105 transform filter brightness-95"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/45 to-slate-950/70"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center px-4 sm:px-6">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-950/70 backdrop-blur-md border border-emerald-400/40 text-amber-300 text-xs font-black uppercase tracking-widest mb-6 shadow-xl">
        <span>🇳🇵 L'histoire d'une alliance franco-népalaise</span>
      </div>

      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-[0_4px_20px_rgba(0,0,0,0.9)]">
        Ceux qui écoutent la jungle.
      </h1>

      <p class="mt-6 text-base sm:text-xl text-slate-100 max-w-2xl font-medium leading-relaxed drop-shadow-[0_2px_10px_rgba(0,0,0,0.8)]">
        Née de la rencontre entre des maîtres pisteurs indigènes de Bardia et des passionnés de faune sauvage, Jungle Nepal Adventure réinvente l'immersion éco-responsable au Népal.
      </p>
    </div>
  </section>"""

c = re.sub(r'<!-- 3\. HERO IMMERSIF.*?<\/section>', new_hero_html, c, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated À propos hero with authentic Drive photo (julien_safari_a_pied.webp)!")
