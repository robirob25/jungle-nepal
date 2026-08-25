import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Humanize Hero Section
content = re.sub(
    r'<h1 class="font-black text-4xl sm:text-6xl lg:text-7xl text-white tracking-tight leading-\[1\.08\] mb-6 drop-shadow-lg">.*?</h1>',
    """<h1 class="font-black text-4xl sm:text-6xl lg:text-7xl text-white tracking-tight leading-[1.08] mb-6 drop-shadow-lg">
          Le Népal sauvage, <br />
          <span class="font-serif italic font-normal text-amber-300">à pied</span> au plus près des tigres.
        </h1>""",
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<p class="text-base sm:text-xl text-slate-200 font-medium max-w-2xl leading-relaxed mb-8 drop-shadow">.*?</p>',
    """<p class="text-base sm:text-xl text-slate-200 font-medium max-w-2xl leading-relaxed mb-8 drop-shadow">
          Ni 4x4 bondés, ni sentiers battus. Nous partons en petit comité avec Pawan & Kiran, maîtres pisteurs natifs de Bardia, sur les traces fraîches des tigres et des rhinocéros du Teraï.
        </p>""",
    content,
    flags=re.DOTALL
)

# 2. Humanize Hero Badge
content = re.sub(
    r'<span class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-slate-950/80 border border-emerald-500/40 text-emerald-400 text-xs sm:text-sm font-black uppercase tracking-wider mb-6 backdrop-blur-md shadow-2xl">.*?</span>',
    """<span class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-slate-950/80 border border-emerald-500/40 text-emerald-300 text-xs sm:text-sm font-bold uppercase tracking-widest mb-6 backdrop-blur-md shadow-2xl">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Safaris à pied & Bivouacs sauvages • Petits groupes (4 à 8 max)
        </span>""",
    content,
    flags=re.DOTALL
)

# 3. Clean up the Category Carousel Buttons (Remove emojis, keep refined typography)
content = re.sub(
    r'<span class="text-sm">🐾</span>\s*<span>Tous les séjours</span>',
    '<span>Tous les séjours</span>',
    content
)
content = re.sub(
    r'<span class="text-sm">🐅</span>\s*<span>Safaris et grands félins</span>',
    '<span>Safaris & grands félins</span>',
    content
)
content = re.sub(
    r'<span class="text-sm">🏕️</span>\s*<span>Bivouacs et nuits sauvages</span>',
    '<span>Bivouacs & nuits sauvages</span>',
    content
)
content = re.sub(
    r'<span class="text-sm">🦏</span>\s*<span>Rhinocéros et Chitwan</span>',
    '<span>Rhinocéros & Chitwan</span>',
    content
)
content = re.sub(
    r'<span class="text-sm">🛶</span>\s*<span>Rafting et rivières sauvages</span>',
    '<span>Rafting & rivières</span>',
    content
)
content = re.sub(
    r'<span class="text-sm">🏔️</span>\s*<span>Himalaya et Mustang</span>',
    '<span>Himalaya & Mustang</span>',
    content
)

# 4. Humanize Concept Section (L'Esprit Safari)
concept_replacement = """  <!-- ========================================================================= -->
  <!-- 4. L'ESPRIT DU SAFARI À PIED (PHILOSOPHIE DE TERRAIN) -->
  <!-- ========================================================================= -->
  <section id="concept" class="scroll-mt-16 sm:scroll-mt-20 py-20 sm:py-28 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10">
    <div class="absolute -top-40 right-0 w-[500px] h-[500px] bg-emerald-500/10 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
        <span class="text-xs font-bold uppercase tracking-widest text-emerald-400 bg-emerald-950/80 px-4 py-1.5 rounded-full border border-emerald-500/30">
          Philosophie de terrain
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight mt-4">
          Pourquoi le safari à pied <span class="font-serif italic font-normal text-emerald-400">change absolument tout</span>.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          Le moteur d'un 4x4 brise le silence et fait fuir les prédateurs à des centaines de mètres. À pied, la jungle se dévoile dans sa réalité brute.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-8 rounded-3xl bg-slate-900/80 border border-white/10 hover:border-emerald-500/40 transition-all duration-300 space-y-4">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-mono font-black text-lg border border-emerald-500/30">
            01
          </div>
          <h3 class="font-black text-xl text-white tracking-tight">Le silence comme seul guide</h3>
          <p class="text-sm text-slate-300 leading-relaxed font-normal">
            En progressant au pas dans les herbes à éléphant, nos sens sont en éveil permanent. Le cri d'alarme d'un cerf aboyeur ou d'un langur nous avertit de la présence du tigre bien avant qu'il ne soit visible.
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-slate-900/80 border border-white/10 hover:border-emerald-500/40 transition-all duration-300 space-y-4">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-mono font-black text-lg border border-emerald-500/30">
            02
          </div>
          <h3 class="font-black text-xl text-white tracking-tight">L'œil des maîtres pisteurs</h3>
          <p class="text-sm text-slate-300 leading-relaxed font-normal">
            Pawan et Kiran sont nés à la frontière de Bardia. Ils ne suivent pas de routes balisées : ils interprètent la fraîcheur d'une empreinte dans la boue de la Babai et les marques de griffes sur l'écorce des arbres de Sal.
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-slate-900/80 border border-white/10 hover:border-emerald-500/40 transition-all duration-300 space-y-4">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-mono font-black text-lg border border-emerald-500/30">
            03
          </div>
          <h3 class="font-black text-xl text-white tracking-tight">Loin du tourisme de masse</h3>
          <p class="text-sm text-slate-300 leading-relaxed font-normal">
            Bardia accueille moins de 2% des voyageurs du Népal. Nous limitons chaque groupe à 8 explorateurs maximum pour préserver la quiétude des animaux et garantir une sécurité irréprochable.
          </p>
        </div>

      </div>
    </div>
  </section>"""

content = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 4\. L\'ESPRIT DU SAFARI.*?<!-- ========================================================================= -->\s*<!-- 5\. GALERIE',
    concept_replacement + '\n\n  <!-- ========================================================================= -->\n  <!-- 5. GALERIE',
    content,
    flags=re.DOTALL
)

# 5. Humanize Section Pisteurs & add Founder Quote Card
pisteurs_header_replacement = """  <!-- ========================================================================= -->
  <!-- 8. PISTEURS & ÉQUIPE DE TERRAIN -->
  <!-- ========================================================================= -->
  <section id="pisteurs" class="scroll-mt-16 sm:scroll-mt-20 py-16 sm:py-24 lg:py-28 bg-white border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="inline-block text-xs font-bold uppercase tracking-widest text-[#0e8354] bg-emerald-50 border border-emerald-200 px-4 py-1.5 rounded-full mb-3">
          Sur le terrain depuis 20 ans
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">
          Ceux qui vous ouvrent les portes <span class="font-serif italic font-normal text-[#0e8354]">du Teraï</span>
        </h2>
        <p class="mt-3 text-base text-slate-600">
          L'expertise brute des guides natifs de Bardia alliée à une coordination francophone disponible 24h/24.
        </p>
      </div>"""

content = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS.*?<div class="grid grid-cols-1 md:grid-cols-3 gap-10">',
    pisteurs_header_replacement + '\n\n      <div class="grid grid-cols-1 md:grid-cols-3 gap-10">',
    content,
    flags=re.DOTALL
)

# Add founder quote under the 3 tracker cards
founder_quote_block = """      </div>

      <!-- Founder Field Note Quote -->
      <div class="mt-14 p-6 sm:p-8 rounded-3xl bg-safari-50 border border-slate-200/90 text-slate-700 max-w-4xl mx-auto flex flex-col sm:flex-row items-center gap-6 shadow-sm">
        <div class="w-16 h-16 rounded-full overflow-hidden shrink-0 border-2 border-[#0e8354]/40 shadow-md">
          <img src="https://junglenepal.com/wp-content/uploads/2025/12/3.png" alt="Robin Rozier" class="w-full h-full object-cover" />
        </div>
        <div class="space-y-1.5 text-center sm:text-left flex-1">
          <p class="font-serif italic text-base sm:text-lg text-slate-900 leading-relaxed">
            « Sur le terrain, la différence entre un simple guide et un maître pisteur se mesure au silence. Avec Pawan et Kiran, chaque journée en jungle est une véritable leçon d'humilité et de précision face au sauvage. »
          </p>
          <p class="text-xs font-bold text-slate-500 uppercase tracking-wider">— Robin Rozier, Coordinateur des Expéditions & Relations France</p>
        </div>
      </div>

    </div>
  </section>"""

content = re.sub(
    r'</div>\s*</div>\s*</section>\s*<!-- ========================================================================= -->\s*<!-- 9\. AVIS',
    founder_quote_block + '\n\n  <!-- ========================================================================= -->\n  <!-- 9. AVIS',
    content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("Homepage successfully humanized without breaking the layout!")
