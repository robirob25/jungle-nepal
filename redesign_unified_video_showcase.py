import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the unified, stunning Masterpiece Cinema Showcase
unified_cinema_showcase = """  <!-- ========================================================================= -->
  <!-- 7. CINEMA SHOWCASE : L'EXPÉRIENCE EN IMMERSION TOTALE (VIDÉO CENTRALE) -->
  <!-- ========================================================================= -->
  <section id="concept" class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10">
    
    <!-- Ambient emerald lighting glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1000px] h-[600px] bg-[#0e8354]/15 rounded-full blur-[170px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-[#10b981] text-xs font-black uppercase tracking-widest mb-4">
          <i data-lucide="film" class="w-4 h-4 text-[#109363]"></i>
          <span>Documentaire exclusif • 4K</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-[1.1]">
          L'expérience en immersion totale.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 leading-relaxed font-normal">
          Au-delà des mots, découvrez la réalité de nos expéditions au Népal avec Pawan, Robin et les maîtres pisteurs de Bardia.
        </p>
      </div>

      <!-- Masterpiece Cinema Video Player -->
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
        </div>

        <!-- 4 Concrete Quick Fact Badges -->
        <div class="mt-10 grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Territoire</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">Bardia & Babai</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Mode d'approche</p>
            <p class="text-sm sm:text-base font-black text-[#10b981] mt-1">100% à pied</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Grande Faune</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">Tigres & Rhinos</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Micro-Groupes</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">4 à 8 pers. max</p>
          </div>
        </div>

        <!-- Direct Action Bar -->
        <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href="#prochains-departs" class="w-full sm:w-auto px-8 py-4 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white font-extrabold text-sm shadow-xl shadow-[#0e8354]/40 hover:scale-105 active:scale-95 transition-all text-center">
            Explorer les 14 séjours 2026/2027 →
          </a>
          <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20viens%20de%20regarder%20votre%20vidéo%20et%20je%20souhaite%20des%20informations" target="_blank" class="w-full sm:w-auto px-7 py-4 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 text-white font-extrabold text-sm backdrop-blur-md transition-all text-center flex items-center justify-center gap-2">
            <i data-lucide="message-circle" class="w-4 h-4 text-[#10b981]"></i>
            <span>Échanger avec Robin sur WhatsApp</span>
          </a>
        </div>

      </div>

    </div>
  </section>"""

# Replace both section 7 (old cards) and 7.5 (standalone video) with this unified masterpiece
pattern = r'<!-- ========================================================================= -->\s*<!-- 7\. SECTION WILDLIFE & CONCEPT.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS & ÉQUIPE -->'
html = re.sub(pattern, unified_cinema_showcase + "\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE -->", html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Unified Masterpiece Cinema Showcase applied successfully!")
