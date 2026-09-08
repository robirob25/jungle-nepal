import re

# 1. Update index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Update Slide 0 to have explicit dimensions and high priority
old_s0 = """      <!-- Slide 0: Tigre royal au bord de l'eau -->
      <div class="hero-slide absolute inset-0 transition-opacity duration-400 ease-out opacity-100 scale-100" data-slide="0">
        <img 
          src="/assets/hero/hero_1_tiger_water.webp" 
          alt="Tigre du Bengale au point d'eau" 
          class="w-full h-full object-cover object-[75%_30%] filter brightness-90 contrast-105"
          loading="eager"
        />
      </div>"""

new_s0 = """      <!-- Slide 0: Tigre royal au bord de l'eau (LCP Hero) -->
      <div class="hero-slide absolute inset-0 transition-opacity duration-400 ease-out opacity-100 scale-100" data-slide="0">
        <img 
          src="/assets/hero/hero_1_tiger_water.webp" 
          alt="Tigre du Bengale au point d'eau à Bardia" 
          width="1920"
          height="1080"
          fetchpriority="high"
          loading="eager"
          decoding="sync"
          class="w-full h-full object-cover object-[75%_30%] filter brightness-90 contrast-105"
        />
      </div>"""

if old_s0 in idx:
    idx = idx.replace(old_s0, new_s0)

# Update YouTube Section
old_yt_section = """      <!-- Masterpiece Cinema Video Player -->
      <div class="max-w-5xl mx-auto">
        <div class="relative rounded-3xl sm:rounded-[32px] overflow-hidden border-2 border-white/20 shadow-[0_30px_90px_rgba(0,0,0,0.85)] bg-black aspect-video">
          <iframe 
            class="w-full h-full" 
            src="https://www.youtube.com/embed/nApJul2Wgxo?rel=0&modestbranding=1" 
            title="Jungle Nepal Adventure – Documentaire immersif" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        </div>"""

new_yt_section = """      <!-- Masterpiece Cinema Video Player (Façade Ultra-Rapide - Zero Tâche Longue) -->
      <div class="max-w-5xl mx-auto">
        <div id="video-facade" class="relative rounded-3xl sm:rounded-[32px] overflow-hidden border-2 border-white/20 shadow-[0_30px_90px_rgba(0,0,0,0.85)] bg-black aspect-video cursor-pointer group" onclick="this.innerHTML='<iframe class=\\'w-full h-full\\' src=\\'https://www.youtube.com/embed/nApJul2Wgxo?autoplay=1&rel=0&modestbranding=1\\' title=\\'Jungle Nepal Adventure – Documentaire immersif\\' frameborder=\\'0\\' allow=\\'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\' allowfullscreen></iframe>'">
          <img 
            src="https://img.youtube.com/vi/nApJul2Wgxo/maxresdefault.jpg" 
            alt="Aperçu vidéo Documentaire immersif Jungle Nepal" 
            width="1280"
            height="720"
            loading="lazy"
            decoding="async"
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-90 group-hover:opacity-100"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-center justify-center">
            <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-[#0e8354]/90 hover:bg-[#0e8354] text-white flex items-center justify-center shadow-[0_0_50px_rgba(14,131,84,0.6)] group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 sm:w-10 sm:h-10 text-white translate-x-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </div>
          </div>
          <div class="absolute bottom-6 left-6 right-6 flex items-center justify-between text-white pointer-events-none">
            <span class="font-bold text-sm sm:text-base drop-shadow-md">Documentaire terrain • Guide Pawan à Bardia</span>
            <span class="text-xs bg-black/60 backdrop-blur-md px-3 py-1 rounded-full border border-white/20 font-mono">Lecture 4K</span>
          </div>
        </div>"""

if old_yt_section in idx:
    idx = idx.replace(old_yt_section, new_yt_section)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. Update Layout.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Replace CSP
layout = re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>', '<meta http-equiv="Content-Security-Policy" content="default-src \'self\' https: data: \'unsafe-inline\' \'unsafe-eval\'; script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://*.googleapis.com https://translate.google.com https://translate-pa.googleapis.com https://unpkg.com; style-src \'self\' \'unsafe-inline\' https://*.googleapis.com https://translate.googleapis.com https://fonts.googleapis.com; font-src \'self\' https://fonts.gstatic.com data:; img-src \'self\' data: https: blob:; frame-src \'self\' https://www.youtube.com https://translate.google.com; object-src \'none\'; base-uri \'self\';">', layout)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

print("✓ Full refactor applied to src files!")
