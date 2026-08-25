import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

direct_video_section = """  <!-- ========================================================================= -->
  <!-- 7.5 SECTION CINÉMA DOCUMENTAIRE (Immersion Vidéo Officielle) -->
  <!-- ========================================================================= -->
  <section id="immersion-video" class="py-20 sm:py-28 bg-slate-950 text-white relative overflow-hidden border-y border-white/10">
    
    <!-- Ambient emerald lighting glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[900px] h-[550px] bg-[#0e8354]/15 rounded-full blur-[160px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4">
          <i data-lucide="play-circle" class="w-4 h-4 text-[#109363]"></i>
          <span>Immersion Documentaire • 4K</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight leading-tight">
          Au cœur du sanctuaire sauvage.
        </h2>
        <p class="mt-3 text-base sm:text-lg text-slate-300 leading-relaxed font-normal">
          Découvrez en images les sensations réelles d'un safari à pied à Bardia, l'approche silencieuse du tigre du Bengale et l'atmosphère de nos bivouacs.
        </p>
      </div>

      <!-- Direct Cinema YouTube Video Player -->
      <div class="max-w-4xl mx-auto">
        <div class="relative rounded-3xl overflow-hidden border-2 border-white/20 shadow-[0_25px_60px_rgba(0,0,0,0.8)] bg-black aspect-video">
          <iframe 
            class="w-full h-full" 
            src="https://www.youtube.com/embed/nApJul2Wgxo?rel=0&modestbranding=1" 
            title="Jungle Nepal Adventure – Immersion Vidéo" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        </div>

        <!-- 3 Feature Bullets under Video -->
        <div class="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs font-bold text-slate-300">
          <div class="flex items-center gap-3 p-4 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">🐾</span>
            <span>Pistage réel à pied sans grille ni clôture</span>
          </div>
          <div class="flex items-center gap-3 p-4 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">⛺</span>
            <span>Bivouacs sauvages sous la canopée de Babai</span>
          </div>
          <div class="flex items-center gap-3 p-4 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">🐅</span>
            <span>Maîtres pisteurs natifs certifiés BBC Wildlife</span>
          </div>
        </div>

      </div>

    </div>
  </section>"""

pattern = r'<!-- ========================================================================= -->\s*<!-- 7\.5 SECTION CINÉMA DOCUMENTAIRE.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS & ÉQUIPE -->'
html = re.sub(pattern, direct_video_section + "\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE -->", html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with directly loaded YouTube video!")
