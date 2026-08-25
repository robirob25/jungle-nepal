import re

# Update French a-propos.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    fr_code = f.read()

# 1. Hero background photo -> Epic Nepal wild landscape
fr_code = re.sub(
    r'<img\s+src=[\'\"]https://junglenepal\.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430\.png[\'\"]\s+alt=[\'\"][^\'\"]*[\'\"]\s+class=[\'\"]w-full h-full object-cover[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg" alt="Immersion sauvage et paysages grandioses du Népal" class="w-full h-full object-cover object-center filter brightness-75 contrast-105" />',
    fr_code,
    count=1
)

# 2. Section 4 Notre Histoire photo -> Majestic Bengal tiger on trail
fr_code = fr_code.replace(
    'src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"',
    'src="https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png"'
)

# 3. Bento Card 1 photo (Micro-groupes) -> Wild elephant herd crossing river at sunrise
fr_code = fr_code.replace(
    'src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png"',
    'src="https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg"'
)
fr_code = fr_code.replace(
    'alt="Safari à pied immersif en micro-groupe à Bardia"',
    'alt="Éléphants sauvages traversant la rivière en liberté au Népal"'
)
fr_code = fr_code.replace(
    '👣 Safari à pied silencieux • Bardia',
    '🐘 Faune sauvage en liberté • Immersion pure'
)

# 4. Bento Card 2 photo (Pisteurs) -> Action tracking in deep grassland
fr_code = fr_code.replace(
    'src="https://junglenepal.com/wp-content/uploads/2025/12/2.png"',
    'src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"'
)
# (Keep team Pawan avatar in team section by restoring first occurrence of 2.png)
# Let's do targeted replacements for Bento Grid cards specifically:

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(fr_code)

print("Applied diversified photo set to French about page!")

# Now do precise Bento Grid replacements for both FR and EN
bento_photos_fr = """  <!-- ========================================================================= -->
  <!-- 6. BENTO GRID AVEC PHOTOS VARIÉES DU NÉPAL SAUVAGE -->
  <!-- ========================================================================= -->
  <section class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden">
    <!-- Ambient Radial Light Layers -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-gradient-to-b from-emerald-500/15 via-emerald-500/5 to-transparent blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 right-0 w-96 h-96 bg-[#0e8354]/15 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 space-y-16">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-[#10b981] bg-emerald-500/10 border border-emerald-500/20 px-4 py-1.5 rounded-full shadow-inner">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Nos 4 Piliers Fondamentaux</span>
        </span>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          Pourquoi explorer le Népal avec nous ?
        </h2>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-medium max-w-2xl mx-auto">
          Nous avons banni les voyages standardisés pour créer une expérience de safari immersif, éthique et intime, guidée par ceux qui connaissent chaque recoin de la jungle.
        </p>
      </div>

      <!-- BENTO GRID AVEC PHOTOS HD VARIÉES -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- CARD 1 (HERO BENTO - 7 Cols): Micro-Groupes avec Photo Éléphants Sauvages -->
        <div class="lg:col-span-7 rounded-3xl bg-white/[0.04] border border-white/15 p-7 sm:p-9 flex flex-col justify-between relative overflow-hidden group hover:border-emerald-500/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(14,131,84,0.2)]">
          <div class="space-y-6">
            
            <div class="flex items-center justify-between">
              <span class="w-12 h-12 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-[#10b981]">
                <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
              </span>
              <span class="px-3.5 py-1 rounded-full bg-slate-900/90 border border-amber-300/30 text-amber-300 text-xs font-black">
                Max 8 voyageurs
              </span>
            </div>

            <div>
              <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight">
                Micro-groupes exclusifs (4 à 8 personnes)
              </h3>
              <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-normal mt-2">
                Le seul format permettant d'approcher la faune en silence absolu. Zéro bus de touristes, zéro convoi : vous progressez en symbiose avec la nature, au plus près des animaux sauvages.
              </p>
            </div>

            <!-- Photo HD 1 : Éléphants Sauvages dans la brume -->
            <div class="relative h-56 sm:h-64 rounded-2xl overflow-hidden border border-white/10 shadow-lg group">
              <img 
                src="https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg" 
                alt="Hardes d'éléphants sauvages traversant la rivière en liberté au Népal" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-90"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <span class="absolute bottom-3 left-3 px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white text-[11px] font-bold border border-white/20">
                🐘 Faune en liberté totale • Teraï Sauvage
              </span>
            </div>

          </div>

          <div class="mt-6 pt-4 border-t border-white/10 flex flex-wrap items-center justify-between gap-4 text-xs font-bold text-slate-300">
            <span class="flex items-center gap-1.5 text-emerald-400">
              <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              Silence & discrétion maximale
            </span>
            <span class="flex items-center gap-1.5 text-emerald-400">
              <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              Départs garantis dès 4 inscrits
            </span>
          </div>
        </div>

        <!-- CARD 2 (BENTO - 5 Cols): Maîtres Pisteurs avec Photo Tracking Terrain -->
        <div class="lg:col-span-5 rounded-3xl bg-white/[0.04] border border-white/15 p-7 sm:p-9 flex flex-col justify-between relative overflow-hidden group hover:border-emerald-500/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(14,131,84,0.2)]">
          <div class="space-y-6">
            
            <div class="flex items-center justify-between">
              <span class="w-12 h-12 rounded-2xl bg-amber-400/20 border border-amber-400/30 flex items-center justify-center text-amber-300">
                <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
              </span>
              <span class="px-3.5 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-black">
                2 pisteurs / groupe
              </span>
            </div>

            <div>
              <h3 class="font-black text-2xl text-white tracking-tight">
                Maîtres pisteurs natifs certifiés
              </h3>
              <p class="text-slate-300 text-sm leading-relaxed font-normal mt-2">
                Chaque safari à pied est guidé par deux pisteurs chevronnés (dont Pawan, ex-consultant BBC Wildlife). Nés en lisière du parc, ils décodent chaque empreinte et son de la jungle.
              </p>
            </div>

            <!-- Photo HD 2 : Safari à pied dans les hautes herbes -->
            <div class="relative h-56 sm:h-64 rounded-2xl overflow-hidden border border-white/10 shadow-lg group">
              <img 
                src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png" 
                alt="Tracking silencieux du tigre du Bengale avec maîtres pisteurs" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-95"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <span class="absolute bottom-3 left-3 px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-amber-300 text-[11px] font-bold border border-amber-300/30">
                🐅 Tracking silencieux • Savoir Tharu
              </span>
            </div>

          </div>

          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-amber-300 font-bold">
            🐅 Taux de rencontre exceptionnel sur nos séjours
          </div>
        </div>

        <!-- CARD 3 (BENTO - 5 Cols): 100% Éthique avec Photo Village Tharu -->
        <div class="lg:col-span-5 rounded-3xl bg-white/[0.04] border border-white/15 p-7 sm:p-9 flex flex-col justify-between relative overflow-hidden group hover:border-emerald-500/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(14,131,84,0.2)]">
          <div class="space-y-6">
            
            <div class="flex items-center justify-between">
              <span class="w-12 h-12 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-[#10b981]">
                <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg>
              </span>
              <span class="px-3.5 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-black">
                100% Éthique
              </span>
            </div>

            <div>
              <h3 class="font-black text-2xl text-white tracking-tight">
                Zéro exploitation & Impact local direct
              </h3>
              <p class="text-slate-300 text-sm leading-relaxed font-normal mt-2">
                Zéro safari à dos d'éléphant. Aucun intermédiaire européen : chaque euro bénéficie directement aux pisteurs, porteurs, et familles des villages Tharu.
              </p>
            </div>

            <!-- Photo HD 3 : Vie et accueil dans les villages du Teraï -->
            <div class="relative h-52 rounded-2xl overflow-hidden border border-white/10 shadow-lg group">
              <img 
                src="https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg" 
                alt="Rencontre chaleureuse dans les villages traditionnels du Népal" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-90"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
              <span class="absolute bottom-3 left-3 px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white text-[11px] font-bold border border-white/20">
                🌿 Accueil & partage avec les communautés locales
              </span>
            </div>

          </div>

          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-emerald-400 font-bold">
            🌿 Protection active des écosystèmes du Terai
          </div>
        </div>

        <!-- CARD 4 (HERO BENTO - 7 Cols): Campement Sauvage & Bivouac sous les étoiles (PHOTO CONSERVÉE !) -->
        <div class="lg:col-span-7 rounded-3xl bg-white/[0.04] border border-white/15 p-7 sm:p-9 flex flex-col justify-between relative overflow-hidden group hover:border-amber-400/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(245,158,11,0.15)]">
          <div class="space-y-6">
            
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-1.5 text-amber-400">
                <svg class="w-5 h-5 fill-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                <svg class="w-5 h-5 fill-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                <svg class="w-5 h-5 fill-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                <svg class="w-5 h-5 fill-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                <svg class="w-5 h-5 fill-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                <span class="ml-2 font-black text-white text-lg">5.0 / 5</span>
              </div>
              <span class="px-3.5 py-1 rounded-full bg-amber-400/20 border border-amber-400/30 text-amber-300 text-xs font-black">
                100% Avis Vérifiés
              </span>
            </div>

            <div>
              <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight">
                Nuits sauvages en jungle & bivouacs sous les étoiles
              </h3>
              <p class="text-slate-300 text-sm leading-relaxed font-normal mt-2">
                Dormir en tente dans la vallée secrète de Babai ou séjourner dans nos éco-lodges de charme Tharu au son magique des bruits de la nuit.
              </p>
            </div>

            <!-- Photo HD 4 (CAMPING DU DRIVE / REPO CONSERVÉ !) -->
            <div class="relative h-52 rounded-2xl overflow-hidden border border-white/10 shadow-lg group">
              <img 
                src="https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg" 
                alt="Campement sauvage sous tente dans la jungle de Bardia" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-90"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
              <span class="absolute bottom-3 left-3 px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-amber-300 text-[11px] font-bold border border-amber-300/30">
                ⛺ Bivouac sous les étoiles • Vallée de Babai
              </span>
            </div>

          </div>

          <div class="mt-6 pt-4 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs text-slate-400 font-medium">Assistance 24/7 francophone avec Robin</span>
            <a href="/index.html#avis" class="text-xs font-bold text-amber-300 hover:underline flex items-center gap-1">
              <span>Lire les avis voyageurs</span>
              <span>→</span>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    fr_code = f.read()

fr_code = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 6\. (?:BENTO GRID|NOS 4 PILIERS).*?(?=<!-- ========================================================================= -->\s*<!-- 7\.)',
    bento_photos_fr + '\n',
    fr_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(fr_code)

print("Updated French a-propos.astro with completely diversified photos!")

# English translation
bento_photos_en = bento_photos_fr.replace("Nos 4 Piliers Fondamentaux", "Our 4 Core Pillars")
bento_photos_en = bento_photos_en.replace("Pourquoi explorer le Népal avec nous ?", "Why Explore Nepal With Us?")
bento_photos_en = bento_photos_en.replace("Nous avons banni les voyages standardisés pour créer une expérience de safari immersif, éthique et intime, guidée par ceux qui connaissent chaque recoin de la jungle.", "We banned mass tourism to craft an intimate, highly ethical, and deeply immersive safari experience led by those who know every heartbeat of the jungle.")
bento_photos_en = bento_photos_en.replace("Micro-groupes exclusifs (4 à 8 personnes)", "Exclusive Small Groups (4 to 8 Guests)")
bento_photos_en = bento_photos_en.replace("Max 8 voyageurs", "Max 8 Guests")
bento_photos_en = bento_photos_en.replace("Le seul format permettant d'approcher la faune en silence absolu. Zéro bus de touristes, zéro convoi : vous progressez en symbiose avec la nature, au plus près des animaux sauvages.", "The only format allowing quiet wildlife observation in pure silence. Zero tourist buses, zero convoys: move in harmony with nature.")
bento_photos_en = bento_photos_en.replace("🐘 Faune en liberté totale • Teraï Sauvage", "🐘 Wildlife in Total Freedom • Wild Terai")
bento_photos_en = bento_photos_en.replace("Silence & discrétion maximale", "Maximum silence & stealth")
bento_photos_en = bento_photos_en.replace("Départs garantis dès 4 inscrits", "Guaranteed departures from 4 guests")
bento_photos_en = bento_photos_en.replace("2 pisteurs / groupe", "2 Trackers / Group")
bento_photos_en = bento_photos_en.replace("Maîtres pisteurs natifs certifiés", "Certified Native Master Trackers")
bento_photos_en = bento_photos_en.replace("Chaque safari à pied est guidé par deux pisteurs chevronnés (dont Pawan, ex-consultant BBC Wildlife). Nés en lisière du parc, ils décodent chaque empreinte et son de la jungle.", "Every walking safari is guided by two veteran trackers (including Pawan, ex-BBC Wildlife consultant). Born on the edge of the jungle, they decode every track and call.")
bento_photos_en = bento_photos_en.replace("🐅 Tracking silencieux • Savoir Tharu", "🐅 Silent Tracking • Tharu Expertise")
bento_photos_en = bento_photos_en.replace("🐅 Taux de rencontre exceptionnel sur nos séjours", "🐅 Outstanding wildlife sighting success rate")
bento_photos_en = bento_photos_en.replace("100% Éthique", "100% Ethical")
bento_photos_en = bento_photos_en.replace("Zéro exploitation & Impact local direct", "Zero Animal Exploitation & Direct Local Impact")
bento_photos_en = bento_photos_en.replace("Zéro safari à dos d'éléphant. Aucun intermédiaire européen : chaque euro bénéficie directement aux pisteurs, porteurs, et familles des villages Tharu.", "Zero elephant rides. Zero European middleman: every payment directly benefits our native trackers, porters, and local Tharu village families.")
bento_photos_en = bento_photos_en.replace("🌿 Accueil & partage avec les communautés locales", "🌿 Authentic Connection with Local Communities")
bento_photos_en = bento_photos_en.replace("🌿 Protection active des écosystèmes du Terai", "🌿 Active conservation of the Terai wilderness")
bento_photos_en = bento_photos_en.replace("100% Avis Vérifiés", "100% Verified Reviews")
bento_photos_en = bento_photos_en.replace("Nuits sauvages en jungle & bivouacs sous les étoiles", "Wild Nights in the Jungle & Starry Campfires")
bento_photos_en = bento_photos_en.replace("Dormir en tente dans la vallée secrète de Babai ou séjourner dans nos éco-lodges de charme Tharu au son magique des bruits de la nuit.", "Sleep in private tents inside the secret Babai Valley or relax in charming Tharu eco-lodges surrounded by the sounds of the night.")
bento_photos_en = bento_photos_en.replace("⛺ Bivouac sous les étoiles • Vallée de Babai", "⛺ Campfire under the Stars • Babai Valley")
bento_photos_en = bento_photos_en.replace("Assistance 24/7 francophone avec Robin", "24/7 dedicated assistance with Robin")
bento_photos_en = bento_photos_en.replace("Lire les avis voyageurs", "Read traveler reviews")
bento_photos_en = bento_photos_en.replace("/index.html#avis", "/en/index.html#avis")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'r', encoding='utf-8') as f:
    en_code = f.read()

en_code = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 6\. (?:BENTO GRID|NOS 4 PILIERS).*?(?=<!-- ========================================================================= -->\s*<!-- 7\.)',
    bento_photos_en + '\n',
    en_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(en_code)

print("Updated English a-propos.astro with completely diversified photos!")
