with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Enrich the Hero Title & Subtitle to cover Jungle, Mountain, Culture & Immersion:
c = c.replace(
    """      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-[0_4px_20px_rgba(0,0,0,0.9)]">
        Ceux qui écoutent la jungle.
      </h1>

      <p class="mt-6 text-base sm:text-xl text-slate-100 max-w-2xl font-medium leading-relaxed drop-shadow-[0_2px_10px_rgba(0,0,0,0.8)]">
        Née de la rencontre entre des maîtres pisteurs indigènes de Bardia et des passionnés de faune sauvage, Jungle Nepal Adventure réinvente l'immersion éco-responsable au Népal.
      </p>""",
    """      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-[0_4px_20px_rgba(0,0,0,0.9)]">
        L'exploration authentique du Népal.
      </h1>

      <p class="mt-6 text-base sm:text-xl text-slate-100 max-w-3xl font-medium leading-relaxed drop-shadow-[0_2px_10px_rgba(0,0,0,0.8)]">
        Des sanctuaires sauvages du Terai aux balcons sacrés de l'Himalaya, en passant par les villages millénaires et les fêtes traditionnelles : nous concevons des voyages d'immersion humaine, culturelle et naturaliste en micro-groupes.
      </p>"""
)

# 2. Enrich the Manifesto section to embrace Mountains, Culture, Spirit & Wilderness:
c = c.replace(
    """          <h2 class="font-black text-3xl sm:text-4xl text-slate-950 tracking-tight leading-tight">
            Le Népal authentique n'est pas dans les bus de touristes.
          </h2>
          
          <p class="text-slate-600 text-base leading-relaxed font-normal">
            Le Népal est universellement célèbre pour ses sommets himalayens. Pourtant, au sud du pays, au pied des montagnes, s’étend un royaume méconnu, secret et palpitant : les plaines sauvages du Terai.
          </p>
          
          <p class="text-slate-600 text-base leading-relaxed font-normal">
            C’est ici que vivent les derniers grands tigres du Bengale, les rhinocéros unicornes, les troupeaux d’éléphants sauvages et le peuple Tharu. Face au développement d'un tourisme de masse bruyant, nous avons fondé <strong>Jungle Nepal Adventure</strong> avec une promesse simple : <strong>redonner au voyage sa dimension d'exploration noble et silencieuse</strong>.
          </p>""",
    """          <h2 class="font-black text-3xl sm:text-4xl text-slate-950 tracking-tight leading-tight">
            Le Népal authentique n'est pas dans les bus de touristes.
          </h2>
          
          <p class="text-slate-600 text-base leading-relaxed font-normal">
            Le Népal ne se résume pas à une carte postale de haute montagne ni aux circuits touristiques standardisés. C'est une terre de contrastes absolus : des jungles denses du Terai où rodent tigres et rhinocéros, aux cités royales préservées de Katmandou et Bhaktapur, jusqu'aux vallées secrètes du Mustang et aux sentiers himalayens immaculés.
          </p>
          
          <p class="text-slate-600 text-base leading-relaxed font-normal">
            Nous avons fondé <strong>Jungle Nepal Adventure</strong> pour offrir une alternative intime et respectueuse : des safaris animaliers à pied, des immersions culturelles chez l'habitant, des retraites spirituelles au pied des géants de neige et des treks d'altitude exclusifs (comme la quête de la panthère des neiges), encadrés par des guides natifs et des maîtres pisteurs.
          </p>"""
)

# 3. Add a dedicated Section for "Nos 4 Mondes d'Exploration" (Jungle, Montagne, Culture, Fleuves & Bivouacs)
four_worlds_section = """  <!-- 4.1. NOS 4 UNIVERS D'EXPLORATION -->
  <section class="py-16 sm:py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
          Diversité des expériences
        </p>
        <h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight">
          Quatre façons d'éprouver le Népal
        </h2>
        <p class="mt-3 text-base text-slate-600 font-medium">
          Chaque voyageur a son propre rythme. Nos séjours s'articulent autour de quatre grands piliers d'exploration.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- 1. Jungle & Faune Sauvage -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            01
          </div>
          <h3 class="font-black text-xl text-slate-900">Safaris & Grands Félins</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Pistage silencieux à pied des tigres du Bengale, rhinocéros unicornes et éléphants dans les sanctuaires de Bardia, Chitwan et Suklaphanta.
          </p>
          <a href="/destinations/bardia.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Explorer la jungle →</a>
        </div>

        <!-- 2. Montagnes & Hauts Sommets -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            02
          </div>
          <h3 class="font-black text-xl text-slate-900">Hautes Montagnes & Treks</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Balcons alpins des Annapurna, expéditions panthère des neiges à Manang (3 600 m) et traversées de cols secrets loin de la foule.
          </p>
          <a href="/destinations/annapurna.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Découvrir les treks →</a>
        </div>

        <!-- 3. Culture & Vie de Village -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            03
          </div>
          <h3 class="font-black text-xl text-slate-900">Culture, Temples & Retraites</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Immersion chez l'habitant, découverte des cités sacrées de la vallée de Katmandou, festivals tibétains au Mustang (Tiji) et méditation.
          </p>
          <a href="/destinations/katmandou.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Vivre la culture →</a>
        </div>

        <!-- 4. Rivières & Bivouacs Sauvages -->
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm hover:shadow-lg transition-all space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm">
            04
          </div>
          <h3 class="font-black text-xl text-slate-900">Expéditions Rivières & Bivouacs</h3>
          <p class="text-xs text-slate-600 leading-relaxed font-normal">
            Descentes de rivières sauvages en rafting (Karnali), nuits sous tente sur les bancs de sable et feux de camp sous les étoiles de l'Himalaya.
          </p>
          <a href="/tours/rafting-safari.html" class="inline-block text-xs font-bold text-[#0e8354] hover:underline pt-2">Voir les expéditions →</a>
        </div>

      </div>

    </div>
  </section>
"""

# Insert the 4 worlds section right before section 5
c = c.replace('<!-- 5. LES FONDATEURS & MAÎTRES PISTEURS -->', four_worlds_section + '\n  <!-- 5. LES FONDATEURS & MAÎTRES PISTEURS -->')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Enriched a-propos.astro with Mountains, Treks, Cultural Immersion, and 4 Exploration Worlds!")
