import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the stunning, visual National Geographic / Luxury Safari Wildlife Concept Section
new_concept_section = """  <!-- ========================================================================= -->
  <!-- 7. SECTION WILDLIFE & CONCEPT (Visual Storytelling Haute Couture) -->
  <!-- ========================================================================= -->
  <section id="concept" class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden">
    
    <!-- Ambient jungle glow background -->
    <div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-[#0e8354]/15 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4">
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-[#109363]"></i>
          <span>La Différence Jungle Nepal</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          L'anti-tourisme de masse.
        </h2>
        <p class="mt-5 text-base sm:text-lg text-slate-300 leading-relaxed font-medium">
          Nous refusons les jeeps bondées et les circuits aseptisés. Nous offrons une immersion brute et respectueuse au cœur des sanctuaires inviolés du Terai.
        </p>
      </div>

      <!-- 3 Visual Wildlife Cards Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- CARD 1: PISTAGE TIGRE -->
        <article class="group relative rounded-3xl overflow-hidden min-h-[460px] sm:min-h-[520px] flex flex-col justify-between p-7 sm:p-9 border border-white/15 shadow-2xl hover:border-emerald-400/50 transition-all duration-500">
          
          <!-- Background Wildlife Image -->
          <div class="absolute inset-0 z-0 overflow-hidden">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png" 
              alt="Tigre du Bengale dans la jungle de Bardia" 
              class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 ease-out filter brightness-90"
              loading="lazy"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/30"></div>
          </div>

          <!-- Top Badge -->
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-black/60 backdrop-blur-md border border-white/20 text-amber-300 text-xs font-black">
              <span>🐅</span>
              <span>Pistage du Tigre à Pied</span>
            </span>
            <span class="w-8 h-8 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center text-white/80 group-hover:bg-[#0e8354] group-hover:text-white transition-colors">
              <i data-lucide="compass" class="w-4 h-4"></i>
            </span>
          </div>

          <!-- Bottom Content -->
          <div class="relative z-10 space-y-3">
            <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
              Le Silence du Traqueur
            </h3>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-normal">
              Apprenez à déchiffrer les empreintes fraîches dans la rosée matinale, à écouter le cri d'alarme du cerf chital et à pister le tigre en liberté sans clôture ni artifice.
            </p>
            <div class="pt-3 border-t border-white/15 flex items-center gap-2 text-xs font-extrabold text-amber-300">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-[#109363]"></i>
              <span>Encadrement double pisteur natif d'élite</span>
            </div>
          </div>

        </article>

        <!-- CARD 2: RHINOS & FAUNE SAUVAGE -->
        <article class="group relative rounded-3xl overflow-hidden min-h-[460px] sm:min-h-[520px] flex flex-col justify-between p-7 sm:p-9 border border-white/15 shadow-2xl hover:border-emerald-400/50 transition-all duration-500">
          
          <!-- Background Wildlife Image -->
          <div class="absolute inset-0 z-0 overflow-hidden">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png" 
              alt="Grand Rhinocéros unicorne au Népal" 
              class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 ease-out filter brightness-90"
              loading="lazy"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/30"></div>
          </div>

          <!-- Top Badge -->
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-black/60 backdrop-blur-md border border-white/20 text-emerald-300 text-xs font-black">
              <span>🦏</span>
              <span>Sanctuaires Inviolés</span>
            </span>
            <span class="w-8 h-8 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center text-white/80 group-hover:bg-[#0e8354] group-hover:text-white transition-colors">
              <i data-lucide="eye" class="w-4 h-4"></i>
            </span>
          </div>

          <!-- Bottom Content -->
          <div class="relative z-10 space-y-3">
            <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
              Les Géants du Népal
            </h3>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-normal">
              Observez les rhinocéros unicornes, les troupeaux d'éléphants sauvages et les gavials le long des rivières Karnali et Rapti, dans le strict respect de leur tranquillité.
            </p>
            <div class="pt-3 border-t border-white/15 flex items-center gap-2 text-xs font-extrabold text-emerald-300">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-[#109363]"></i>
              <span>Observation éthique & distances de sécurité</span>
            </div>
          </div>

        </article>

        <!-- CARD 3: BIVOUAC & MICRO-GROUPES -->
        <article class="group relative rounded-3xl overflow-hidden min-h-[460px] sm:min-h-[520px] flex flex-col justify-between p-7 sm:p-9 border border-white/15 shadow-2xl hover:border-emerald-400/50 transition-all duration-500">
          
          <!-- Background Wildlife Image -->
          <div class="absolute inset-0 z-0 overflow-hidden">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg" 
              alt="Bivouac sauvage sous la canopée au Népal" 
              class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 ease-out filter brightness-90"
              loading="lazy"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/30"></div>
          </div>

          <!-- Top Badge -->
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-black/60 backdrop-blur-md border border-white/20 text-amber-300 text-xs font-black">
              <span>⛺</span>
              <span>Micro-groupes 4 à 8</span>
            </span>
            <span class="w-8 h-8 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center text-white/80 group-hover:bg-[#0e8354] group-hover:text-white transition-colors">
              <i data-lucide="users" class="w-4 h-4"></i>
            </span>
          </div>

          <!-- Bottom Content -->
          <div class="relative z-10 space-y-3">
            <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
              Bivouacs & Retombées Locales
            </h3>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-normal">
              Dormez sous tente au son de la jungle dans la vallée secrète de Babai. 100% de votre voyage rémunère directement les guides Tharu et soutient la protection des parcs.
            </p>
            <div class="pt-3 border-t border-white/15 flex items-center gap-2 text-xs font-extrabold text-amber-300">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-[#109363]"></i>
              <span>100% Écotourisme direct sans intermédiaire</span>
            </div>
          </div>

        </article>

      </div>

    </div>
  </section>"""

# Replace in html
pattern = r'<!-- ========================================================================= -->\s*<!-- 7\. SECTION L\'ESPRIT SAFARI -->.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS & ÉQUIPE -->'
html = re.sub(pattern, new_concept_section + "\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE -->", html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Redesigned wildlife concept section with real tiger & rhino photos applied successfully!")
