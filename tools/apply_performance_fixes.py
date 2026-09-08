# 1. Update Layout.astro CSP
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

old_csp = '<meta http-equiv="Content-Security-Policy" content="default-src \'self\' https: data: \'unsafe-inline\' \'unsafe-eval\'; script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://translate.google.com https://translate.googleapis.com https://unpkg.com; style-src \'self\' \'unsafe-inline\' https://fonts.googleapis.com https://translate.googleapis.com; font-src \'self\' https://fonts.gstatic.com data:; img-src \'self\' data: https: blob:; frame-src \'self\' https://www.youtube.com https://translate.google.com; object-src \'none\'; base-uri \'self\';">'

new_csp = '<meta http-equiv="Content-Security-Policy" content="default-src \'self\' https: data: \'unsafe-inline\' \'unsafe-eval\'; script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://*.googleapis.com https://translate.google.com https://translate-pa.googleapis.com https://unpkg.com; style-src \'self\' \'unsafe-inline\' https://*.googleapis.com https://translate.googleapis.com; font-src \'self\' https://fonts.gstatic.com data:; img-src \'self\' data: https: blob:; frame-src \'self\' https://www.youtube.com https://translate.google.com; object-src \'none\'; base-uri \'self\';">'

layout = layout.replace(old_csp, new_csp)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

# 2. Update YouTube Video to lightweight Façade in index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

old_yt = """      <!-- Masterpiece Cinema Video Player -->
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

new_yt = """      <!-- Masterpiece Cinema Video Player (Ultra-Fast Façade - Zero Long Tasks) -->
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

idx = idx.replace(old_yt, new_yt)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Applied YouTube Façade & CSP updates!")
