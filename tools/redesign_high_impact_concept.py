import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the compelling, high-impact storytelling concept section
new_concept_section = """  <!-- ========================================================================= -->
  <!-- 7. SECTION WILDLIFE & CONCEPT (Storytelling Haute Émotion) -->
  <!-- ========================================================================= -->
  <section id="concept" class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden">
    
    <!-- Ambient jungle glow background -->
    <div class="absolute top-1/3 left-1/2 -translate-x-1/2 w-[850px] h-[550px] bg-[#0e8354]/15 rounded-full blur-[160px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-[#10b981] text-xs font-black uppercase tracking-widest mb-4">
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-[#109363]"></i>
          <span>L'anti-tourisme de masse</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          Ce que vous ne vivrez nulle part ailleurs.
        </h2>
        <p class="mt-5 text-base sm:text-lg text-slate-300 leading-relaxed font-normal">
          Nous refusons les convois de jeeps bruyantes et les circuits standardisés. Nous vous ouvrons les portes des derniers sanctuaires secrets du Népal en micro-groupes de 4 à 8 explorateurs.
        </p>
      </div>

      <!-- 3 High-Impact Storytelling Cards -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- CARD 1: PISTAGE TIGRE -->
        <article class="group relative rounded-3xl overflow-hidden min-h-[500px] sm:min-h-[560px] flex flex-col justify-between p-7 sm:p-9 border border-white/15 shadow-2xl hover:border-emerald-400/60 transition-all duration-500">
          
          <!-- Background Wildlife Image -->
          <div class="absolute inset-0 z-0 overflow-hidden">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png" 
              alt="Tigre du Bengale dans la jungle de Bardia" 
              class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 ease-out filter brightness-85"
              loading="lazy"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/65 to-black/35"></div>
          </div>

          <!-- Top Badge -->
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[#10b981] text-xs font-black">
              <span>🐅</span>
              <span>Pistage à pied exclusif</span>
            </span>
            <span class="w-8 h-8 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center text-white/80 group-hover:bg-[#0e8354] group-hover:text-white transition-colors">
              <i data-lucide="footprints" class="w-4 h-4"></i>
            </span>
          </div>

          <!-- Bottom Content -->
          <div class="relative z-10 space-y-4">
            <div>
              <p class="text-[11px] font-extrabold uppercase tracking-widest text-[#10b981] mb-1">Immersion & Frissons</p>
              <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
                Regarder le tigre dans les yeux.
              </h3>
            </div>
            <p class="text-slate-300 text-sm leading-relaxed font-normal">
              Ici, pas de vitre teintée ni de moteur qui vrombit. Vous avancez à pas feutrés dans les hautes herbes de Bardia, guidé par les sens aiguisés de Pawan. L'émotion brute d'un face-à-face à hauteur d'homme, où chaque bruissement de feuille prend tout son sens.
            </p>
            <div class="pt-4 border-t border-white/15 flex items-center justify-between">
              <span class="text-xs font-extrabold text-[#10b981] flex items-center gap-1.5">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                <span>Double pisteur d'élite certifié</span>
              </span>
              <a href="tours/nepal-sauvage.html" class="inline-flex items-center gap-1 text-xs font-black text-white hover:text-amber-300 transition-colors">
                <span>Voir le circuit</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

        </article>

        <!-- CARD 2: RHINOS & PIROGUE -->
        <article class="group relative rounded-3xl overflow-hidden min-h-[500px] sm:min-h-[560px] flex flex-col justify-between p-7 sm:p-9 border border-white/15 shadow-2xl hover:border-emerald-400/60 transition-all duration-500">
          
          <!-- Background Wildlife Image -->
          <div class="absolute inset-0 z-0 overflow-hidden">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png" 
              alt="Grand Rhinocéros unicorne au Népal" 
              class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 ease-out filter brightness-85"
              loading="lazy"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/65 to-black/35"></div>
          </div>

          <!-- Top Badge -->
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[#10b981] text-xs font-black">
              <span>🦏</span>
              <span>Chitwan & Rivières sauvages</span>
            </span>
            <span class="w-8 h-8 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center text-white/80 group-hover:bg-[#0e8354] group-hover:text-white transition-colors">
              <i data-lucide="eye" class="w-4 h-4"></i>
            </span>
          </div>

          <!-- Bottom Content -->
          <div class="relative z-10 space-y-4">
            <div>
              <p class="text-[11px] font-extrabold uppercase tracking-widest text-[#10b981] mb-1">Silence & Contemplation</p>
              <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
                Glisser en pirogue au ras des géants.
              </h3>
            </div>
            <p class="text-slate-300 text-sm leading-relaxed font-normal">
              Au lever du jour sur la rivière Rapti, la brume se dissipe pour dévoiler la silhouette préhistorique d'un rhinocéros unicorne venu s'abreuver. En canoë de bois silencieux, vous approchez les géants et les gavials sans jamais troubler la paix du sanctuaire.
            </p>
            <div class="pt-4 border-t border-white/15 flex items-center justify-between">
              <span class="text-xs font-extrabold text-[#10b981] flex items-center gap-1.5">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                <span>Observation éthique & douce</span>
              </span>
              <a href="tours/chitwan-culture.html" class="inline-flex items-center gap-1 text-xs font-black text-white hover:text-amber-300 transition-colors">
                <span>Voir le circuit</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

        </article>

        <!-- CARD 3: BIVOUAC BABAI -->
        <article class="group relative rounded-3xl overflow-hidden min-h-[500px] sm:min-h-[560px] flex flex-col justify-between p-7 sm:p-9 border border-white/15 shadow-2xl hover:border-emerald-400/60 transition-all duration-500">
          
          <!-- Background Wildlife Image -->
          <div class="absolute inset-0 z-0 overflow-hidden">
            <img 
              src="https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg" 
              alt="Bivouac sauvage sous la canopée au Népal" 
              class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 ease-out filter brightness-85"
              loading="lazy"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/65 to-black/35"></div>
          </div>

          <!-- Top Badge -->
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[#10b981] text-xs font-black">
              <span>⛺</span>
              <span>Vallée interdite de Babai</span>
            </span>
            <span class="w-8 h-8 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center text-white/80 group-hover:bg-[#0e8354] group-hover:text-white transition-colors">
              <i data-lucide="tent" class="w-4 h-4"></i>
            </span>
          </div>

          <!-- Bottom Content -->
          <div class="relative z-10 space-y-4">
            <div>
              <p class="text-[11px] font-extrabold uppercase tracking-widest text-[#10b981] mb-1">Aventure Pure & Étoiles</p>
              <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight leading-snug">
                Dormir au cœur du territoire des fauves.
              </h3>
            </div>
            <p class="text-slate-300 text-sm leading-relaxed font-normal">
              La vallée secrète de Babai est inaccessible au tourisme ordinaire. Nous y dressons un campement éphémère sous la voûte céleste. Le soir, autour du feu avec les pisteurs Tharus, vous écoutez le feulement lointain du tigre résonner dans la nuit noire.
            </p>
            <div class="pt-4 border-t border-white/15 flex items-center justify-between">
              <span class="text-xs font-extrabold text-[#10b981] flex items-center gap-1.5">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                <span>Bivouac exclusif 100% sauvage</span>
              </span>
              <a href="tours/babai-special.html" class="inline-flex items-center gap-1 text-xs font-black text-white hover:text-amber-300 transition-colors">
                <span>Voir le circuit</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

        </article>

      </div>

    </div>
  </section>"""

# Replace in html
pattern = r'<!-- ========================================================================= -->\s*<!-- 7\. SECTION WILDLIFE & CONCEPT.*?<!-- ========================================================================= -->\s*<!-- 7\.5 SECTION CINÉMA DOCUMENTAIRE'
html = re.sub(pattern, new_concept_section + "\n\n  <!-- ========================================================================= -->\n  <!-- 7.5 SECTION CINÉMA DOCUMENTAIRE", html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Redesigned concept section with high-impact emotional storytelling successfully!")
