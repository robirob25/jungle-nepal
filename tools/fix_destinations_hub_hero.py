with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Darken the tiger background image + add real dark gradient overlay
# 2. Remove the "Sanctuaires Sauvages du Népal" pill button

old_hero_block = """  <!-- HERO HUB -->
  <section class="relative min-h-[50vh] sm:min-h-[60vh] flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950 text-white">
    <div class="absolute inset-0 z-0">
      <img src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" alt="Tigre de Bardia" class="w-full h-full object-cover filter brightness-70 contrast-105"/>
      
    </div>
    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/25 text-amber-100 text-xs font-black uppercase tracking-wider mb-6">
        <span>Sanctuaires Sauvages du Népal</span>
      </div>
      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-2xl">
        Nos Destinations
      </h1>
      <p class="mt-6 text-base sm:text-xl text-slate-200 max-w-2xl font-medium leading-relaxed drop-shadow">
        Des sanctuaires inviolés du Terai aux sommets himalayens, découvrez les 5 grands territoires explorés avec nos maîtres pisteurs.
      </p>
    </div>
  </section>"""

new_hero_block = """  <!-- HERO HUB (ASSOMBRI POUR CONTRASTE OPTIMAL + SANS BADGE) -->
  <section class="relative min-h-[50vh] sm:min-h-[60vh] flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950 text-white">
    <div class="absolute inset-0 z-0">
      <img src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" alt="Tigre de Bardia" class="w-full h-full object-cover opacity-45 filter brightness-50 contrast-110"/>
      <div class="absolute inset-0 bg-slate-950/40"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/75 to-black/85"></div>
    </div>
    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-[0_4px_20px_rgba(0,0,0,0.9)]">
        Nos destinations
      </h1>
      <p class="mt-6 text-base sm:text-xl text-slate-200 max-w-2xl font-medium leading-relaxed drop-shadow-[0_2px_10px_rgba(0,0,0,0.8)]">
        Des sanctuaires inviolés du Terai aux sommets himalayens, découvrez les 5 grands territoires explorés avec nos maîtres pisteurs.
      </p>
    </div>
  </section>"""

c = c.replace(old_hero_block, new_hero_block)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Darkened destinations hub hero photo and removed the pill button!")
