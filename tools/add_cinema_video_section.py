import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the luxurious Cinema Video Section
video_section_html = """  <!-- ========================================================================= -->
  <!-- 7.5 SECTION CINÉMA DOCUMENTAIRE (Immersion Vidéo Officielle) -->
  <!-- ========================================================================= -->
  <section id="immersion-video" class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10">
    
    <!-- Ambient emerald lighting -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[900px] h-[550px] bg-[#0e8354]/15 rounded-full blur-[150px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4">
          <i data-lucide="play-circle" class="w-4 h-4 text-[#109363]"></i>
          <span>Immersion Documentaire • 4K</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          Au cœur du sanctuaire sauvage.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 leading-relaxed font-normal">
          Découvrez en images les sensations réelles d'un safari à pied à Bardia, l'approche silencieuse du tigre du Bengale et l'atmosphère unique de nos bivouacs.
        </p>
      </div>

      <!-- Video Player Frame -->
      <div class="max-w-5xl mx-auto">
        <div class="relative rounded-3xl overflow-hidden border border-white/20 shadow-[0_25px_60px_rgba(0,0,0,0.7)] bg-slate-900 aspect-video group" id="video-wrapper">
          
          <!-- Poster Thumbnail with Play Button -->
          <div id="video-cover" class="absolute inset-0 z-10 cursor-pointer overflow-hidden" onclick="playYouTubeVideo()">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" 
              alt="Immersion Jungle Nepal Adventure Vidéo" 
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-85"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/30 to-black/40"></div>

            <!-- Pulsing Play Button -->
            <div class="absolute inset-0 flex flex-col items-center justify-center gap-4">
              <div class="relative">
                <div class="absolute -inset-4 rounded-full bg-[#0e8354]/40 animate-ping"></div>
                <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-gradient-to-tr from-[#0e8354] via-[#109363] to-[#0e8354] text-white flex items-center justify-center shadow-2xl group-hover:scale-110 active:scale-95 transition-all duration-300 border-2 border-white/40">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-9 h-9 fill-white translate-x-1" viewBox="0 0 24 24">
                    <polygon points="5 3 19 12 5 21 5 3"/>
                  </svg>
                </div>
              </div>
              <p class="text-xs sm:text-sm font-extrabold text-white uppercase tracking-widest drop-shadow">
                Lancer le documentaire (4K)
              </p>
            </div>
          </div>

          <!-- YouTube Embed Container (activé au clic) -->
          <div id="video-container" class="w-full h-full"></div>

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
  </section>

  <script>
    function playYouTubeVideo() {
      const container = document.getElementById('video-container');
      const cover = document.getElementById('video-cover');
      if (cover) cover.style.display = 'none';
      if (container) {
        container.innerHTML = `<iframe 
          class="w-full h-full" 
          src="https://www.youtube-nocookie.com/embed/nApJul2Wgxo?autoplay=1&rel=0&modestbranding=1&showinfo=0" 
          title="Jungle Nepal Adventure Documentaire" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen>
        </iframe>`;
      }
    }
  </script>
"""

# Insert right after concept section and before pisteurs section
pattern = r'<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS & ÉQUIPE -->'
html = re.sub(pattern, video_section_html + "\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE -->", html)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Cinematic YouTube video section successfully integrated into index.html!")
