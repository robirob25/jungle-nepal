import re

# Complete Bento Grid for French a-propos.astro
bento_section_fr = """  <!-- ========================================================================= -->
  <!-- 6. BENTO GRID : POURQUOI VOYAGER AVEC JUNGLE NEPAL ? (NOS 4 PILIERS) -->
  <!-- ========================================================================= -->
  <section class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden">
    <!-- Ambient Radial Light Layers -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-gradient-to-b from-emerald-500/10 via-emerald-500/5 to-transparent blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 right-0 w-96 h-96 bg-[#0e8354]/10 rounded-full blur-3xl pointer-events-none"></div>

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

      <!-- BENTO GRID -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- CARD 1 (HERO BENTO - 7 Cols): Micro-Groupes 4 à 8 pers -->
        <div class="lg:col-span-7 rounded-3xl bg-gradient-to-br from-white/[0.08] to-white/[0.02] border border-white/15 p-8 sm:p-10 flex flex-col justify-between relative overflow-hidden group hover:border-emerald-500/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(14,131,84,0.15)]">
          <div class="absolute top-0 right-0 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-emerald-500/20 transition-colors"></div>
          
          <div class="space-y-4 relative z-10">
            <div class="flex items-center justify-between">
              <span class="w-12 h-12 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-[#10b981]">
                <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
              </span>
              <span class="px-3.5 py-1 rounded-full bg-slate-900/80 border border-white/10 text-amber-300 text-xs font-black">
                Max 8 voyageurs
              </span>
            </div>

            <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight mt-4">
              Micro-groupes exclusifs (4 à 8 personnes)
            </h3>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-normal">
              Le seul format permettant d'approcher la faune sauvage en silence absolu. Zéro bus de touristes, zéro convoi : vous progressez en symbiose avec la nature, guidés par le rythme de la forêt et l'émulation chaleureuse du groupe autour du feu de camp le soir.
            </p>
          </div>

          <div class="mt-8 pt-6 border-t border-white/10 flex flex-wrap items-center justify-between gap-4 text-xs font-bold text-slate-300 relative z-10">
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

        <!-- CARD 2 (BENTO - 5 Cols): Pisteurs Natifs -->
        <div class="lg:col-span-5 rounded-3xl bg-gradient-to-br from-white/[0.08] to-white/[0.02] border border-white/15 p-8 sm:p-10 flex flex-col justify-between relative overflow-hidden group hover:border-emerald-500/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(14,131,84,0.15)]">
          <div class="space-y-4 relative z-10">
            <div class="flex items-center justify-between">
              <span class="w-12 h-12 rounded-2xl bg-amber-400/20 border border-amber-400/30 flex items-center justify-center text-amber-300">
                <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
              </span>
              <span class="px-3.5 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-black">
                2 pisteurs / groupe
              </span>
            </div>

            <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight mt-4">
              Maîtres pisteurs natifs certifiés
            </h3>
            <p class="text-slate-300 text-sm leading-relaxed font-normal">
              Chaque safari à pied est encadré par deux pisteurs expérimentés (dont Pawan, ex-consultant BBC Wildlife). Nés en lisière du parc, ils lisent les empreintes fraîches, décodent les cris d'alarme des cerfs axis et garantissent une sécurité irréprochable.
            </p>
          </div>

          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-amber-300 font-bold">
            🐅 Taux de rencontre exceptionnel sur nos séjours
          </div>
        </div>

        <!-- CARD 3 (BENTO - 5 Cols): 100% Impact Local & Éthique -->
        <div class="lg:col-span-5 rounded-3xl bg-gradient-to-br from-white/[0.08] to-white/[0.02] border border-white/15 p-8 sm:p-10 flex flex-col justify-between relative overflow-hidden group hover:border-emerald-500/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(14,131,84,0.15)]">
          <div class="space-y-4 relative z-10">
            <div class="flex items-center justify-between">
              <span class="w-12 h-12 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-[#10b981]">
                <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg>
              </span>
              <span class="px-3.5 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-black">
                100% Éthique
              </span>
            </div>

            <h3 class="font-black text-2xl text-white tracking-tight mt-4">
              Zéro safari à dos d'éléphant & Impact direct
            </h3>
            <p class="text-slate-300 text-sm leading-relaxed font-normal">
              Aucun intermédiaire financier en Europe : chaque euro versé rémunère directement et dignement les pisteurs, porteurs, cuisiniers et familles Tharu locales. Nous respectons strictement la liberté et la quiétude de la faune sauvage.
            </p>
          </div>

          <div class="mt-6 pt-4 border-t border-white/10 text-xs text-emerald-400 font-bold">
            🌿 Protection active des écosystèmes du Terai
          </div>
        </div>

        <!-- CARD 4 (HERO BENTO - 7 Cols avec Avis Client & Photo d'ambiance): Note 5.0/5 -->
        <div class="lg:col-span-7 rounded-3xl bg-gradient-to-br from-white/[0.08] to-white/[0.02] border border-white/15 p-8 sm:p-10 flex flex-col justify-between relative overflow-hidden group hover:border-amber-400/40 transition-all duration-500 hover:shadow-[0_20px_50px_rgba(245,158,11,0.1)]">
          <div class="space-y-5 relative z-10">
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

            <h3 class="font-black text-2xl sm:text-3xl text-white tracking-tight">
              Une expérience humaine gravée à jamais
            </h3>

            <!-- Testimonial Quote -->
            <blockquote class="p-4 sm:p-5 rounded-2xl bg-white/5 border border-white/10 text-slate-200 text-sm italic font-normal leading-relaxed">
              « Suivre les traces fraîches d'un tigre du Bengale à pied avec Pawan dans le silence de Bardia, puis partager le Dal Bhat le soir au campement... C'est sans doute le voyage le plus authentique et marquant de notre vie. »
              <span class="block not-italic font-bold text-xs text-amber-300 mt-2">— Sophie & Marc D. (Séjour Bardia Explorateur)</span>
            </blockquote>
          </div>

          <div class="mt-6 pt-4 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs text-slate-400 font-medium">Assistance & conciergerie 24/7 avec Robin</span>
            <a href="/index.html#avis" class="text-xs font-bold text-amber-300 hover:underline flex items-center gap-1">
              <span>Lire les 56 avis Google & Trustpilot</span>
              <span>→</span>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>
"""

# Read and update French file
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    fr_code = f.read()

fr_code = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 6\. NOS 4 PILIERS D\'ENGAGEMENT -->.*?(?=<!-- ========================================================================= -->\s*<!-- 7\.)',
    bento_section_fr + '\n',
    fr_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(fr_code)

print("Updated a-propos.astro with elite Bento Grid!")

# English translation of Bento Grid
bento_section_en = bento_section_fr.replace("Nos 4 Piliers Fondamentaux", "Our 4 Core Commitments")
bento_section_en = bento_section_en.replace("Pourquoi explorer le Népal avec nous ?", "Why Explore Nepal With Us?")
bento_section_en = bento_section_en.replace("Nous avons banni les voyages standardisés pour créer une expérience de safari immersif, éthique et intime, guidée par ceux qui connaissent chaque recoin de la jungle.", "We banned mass tourism to craft an intimate, highly ethical, and deeply immersive safari experience led by those who know every heartbeat of the jungle.")
bento_section_en = bento_section_en.replace("Micro-groupes exclusifs (4 à 8 personnes)", "Exclusive Small Groups (4 to 8 Guests)")
bento_section_en = bento_section_en.replace("Max 8 voyageurs", "Max 8 Guests")
bento_section_en = bento_section_en.replace("Le seul format permettant d'approcher la faune sauvage en silence absolu. Zéro bus de touristes, zéro convoi : vous progressez en symbiose avec la nature, guidés par le rythme de la forêt et l'émulation chaleureuse du groupe autour du feu de camp le soir.", "The only way to approach wildlife in total silence. No tourist buses, no convoys: you move in complete harmony with nature, guided by the forest's pulse and the warm camaraderie around the evening campfire.")
bento_section_en = bento_section_en.replace("Silence & discrétion maximale", "Maximum silence & stealth")
bento_section_en = bento_section_en.replace("Départs garantis dès 4 inscrits", "Guaranteed departures from 4 guests")
bento_section_en = bento_section_en.replace("2 pisteurs / groupe", "2 Trackers / Group")
bento_section_en = bento_section_en.replace("Maîtres pisteurs natifs certifiés", "Certified Native Master Trackers")
bento_section_en = bento_section_en.replace("Chaque safari à pied est encadré par deux pisteurs expérimentés (dont Pawan, ex-consultant BBC Wildlife). Nés en lisière du parc, ils lisent les empreintes fraîches, décodent les cris d'alarme des cerfs axis et garantissent une sécurité irréprochable.", "Every walking safari is led by two veteran trackers (including Pawan, former BBC Wildlife consultant). Born on the edge of the park, they read fresh tracks, decode alarm calls, and ensure complete safety.")
bento_section_en = bento_section_en.replace("🐅 Taux de rencontre exceptionnel sur nos séjours", "🐅 Outstanding wildlife sighting success rate")
bento_section_en = bento_section_en.replace("100% Éthique", "100% Ethical")
bento_section_en = bento_section_en.replace("Zéro safari à dos d'éléphant & Impact direct", "Zero Elephant Rides & Direct Local Impact")
bento_section_en = bento_section_en.replace("Aucun intermédiaire financier en Europe : chaque euro versé rémunère directement et dignement les pisteurs, porteurs, cuisiniers et familles Tharu locales. Nous respectons strictement la liberté et la quiétude de la faune sauvage.", "Zero middleman in Europe: every payment directly and fairly supports our native trackers, porters, cooks, and local Tharu families. We strictly respect animal welfare and habitat preservation.")
bento_section_en = bento_section_en.replace("🌿 Protection active des écosystèmes du Terai", "🌿 Active conservation of the Terai wilderness")
bento_section_en = bento_section_en.replace("100% Avis Vérifiés", "100% Verified Reviews")
bento_section_en = bento_section_en.replace("Une expérience humaine gravée à jamais", "An Unforgettable Human & Wild Adventure")
bento_section_en = bento_section_en.replace("« Suivre les traces fraîches d'un tigre du Bengale à pied avec Pawan dans le silence de Bardia, puis partager le Dal Bhat le soir au campement... C'est sans doute le voyage le plus authentique et marquant de notre vie. »", "“Tracking fresh Bengal tiger pugmarks on foot with Pawan in the silence of Bardia, then sharing a warm Dal Bhat around the campfire... This is truly the most authentic and memorable journey of our lives.”")
bento_section_en = bento_section_en.replace("— Sophie & Marc D. (Séjour Bardia Explorateur)", "— Sophie & Marc D. (Bardia Explorer Trip)")
bento_section_en = bento_section_en.replace("Assistance & conciergerie 24/7 avec Robin", "24/7 dedicated support with Robin")
bento_section_en = bento_section_en.replace("Lire les 56 avis Google & Trustpilot", "Read all 56 Google & Trustpilot reviews")
bento_section_en = bento_section_en.replace("/index.html#avis", "/en/index.html#avis")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'r', encoding='utf-8') as f:
    en_code = f.read()

en_code = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 6\. NOS 4 PILIERS D\'ENGAGEMENT -->.*?(?=<!-- ========================================================================= -->\s*<!-- 7\.)',
    bento_section_en + '\n',
    en_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(en_code)

print("Updated en/a-propos.astro with elite Bento Grid!")
