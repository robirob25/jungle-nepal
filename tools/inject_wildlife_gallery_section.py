import json, re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Build the Bento Grid HTML
bento_cards_html = []

card_layouts = [
    # Card 0: Tiger water (Wide / Prominent)
    ("md:col-span-2 md:row-span-2 h-[340px] sm:h-[460px] md:h-[500px]", "felins"),
    # Card 1: Rhino mist (Square/Standard)
    ("md:col-span-1 h-[260px] sm:h-[300px] md:h-[240px]", "geants"),
    # Card 2: Tiger stalk (Tall/Square)
    ("md:col-span-1 h-[260px] sm:h-[300px] md:h-[240px]", "felins"),
    # Card 3: Elephant jungle (Wide)
    ("md:col-span-2 h-[260px] sm:h-[300px] md:h-[245px]", "geants"),
    # Card 4: Peacock wheel (Wide/Highlight)
    ("md:col-span-2 md:row-span-2 h-[340px] sm:h-[440px] md:h-[500px]", "oiseaux"),
    # Card 5: Croco water (Standard)
    ("md:col-span-1 h-[260px] sm:h-[300px] md:h-[240px]", "reptiles"),
    # Card 6: Hornbill Calao (Standard)
    ("md:col-span-1 h-[260px] sm:h-[300px] md:h-[240px]", "oiseaux"),
    # Card 7: Tiger jungle (Wide)
    ("md:col-span-2 h-[260px] sm:h-[300px] md:h-[245px]", "felins"),
    # Card 8: Deer plain (Standard)
    ("md:col-span-1 h-[260px] sm:h-[300px] md:h-[240px]", "herbivores"),
    # Card 9: Nilgai forest (Standard)
    ("md:col-span-1 h-[260px] sm:h-[300px] md:h-[240px]", "herbivores"),
    # Card 10: Marabout flight (Wide)
    ("md:col-span-2 h-[260px] sm:h-[300px] md:h-[240px]", "oiseaux"),
]

for idx, item in enumerate(items):
    layout_cls, cat = card_layouts[idx]
    card = f"""        <!-- Wildlife Card {idx+1}: {item['title']} -->
        <div class="wildlife-card {layout_cls} relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-500/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.3)] transition-all duration-500" data-category="{cat}" onclick="openWildlifeLightbox({idx})">
          <img 
            src="{item['file']}" 
            alt="{item['title']} - {item['location']}" 
            class="w-full h-full object-cover group-hover:scale-108 transition-transform duration-700 ease-out filter brightness-95 group-hover:brightness-105"
            loading="lazy"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-transparent opacity-80 group-hover:opacity-60 transition-opacity duration-300"></div>
          
          <!-- Top Badge: Location -->
          <div class="absolute top-4 left-4 z-10">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/75 backdrop-blur-md border border-white/15 text-[11px] font-extrabold text-amber-300 shadow">
              <span>📍</span>
              <span>{item['location']}</span>
            </span>
          </div>

          <!-- Bottom Caption on Glassmorphism -->
          <div class="absolute bottom-4 left-4 right-4 z-10 p-4 rounded-2xl bg-slate-950/80 backdrop-blur-md border border-white/15 text-white transition-all duration-300 group-hover:-translate-y-1">
            <div class="flex items-center justify-between gap-2">
              <div>
                <h3 class="font-black text-base sm:text-lg text-white group-hover:text-amber-300 transition-colors leading-tight">
                  {item['title']}
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium line-clamp-1">
                  {item['desc']}
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0 border border-emerald-500/30 group-hover:scale-110 transition-transform">
                <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>
        </div>"""
    bento_cards_html.append(card)

cards_joined = "\n\n".join(bento_cards_html)

gallery_section_html = f"""  <!-- ========================================================================= -->
  <!-- 7. GALERIE ÉLITE DE FAUNE SAUVAGE (BENTO GRID 2026) -->
  <!-- ========================================================================= -->
  <section id="galerie-faune" class="py-24 sm:py-32 bg-slate-950 text-white relative overflow-hidden border-b border-white/10">
    
    <!-- Ambient Lighting Layers -->
    <div class="absolute top-0 left-1/4 w-96 h-96 bg-emerald-600/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4">
          <span>🌿 Instants Sauvages du Népal</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          La faune du Terai dans son intimité brute.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          Toutes ces photographies ont été capturées lors de nos expéditions réelles par nos voyageurs et maîtres pisteurs. Aucun appât, aucun artifice : la pureté de la rencontre à pied.
        </p>
      </div>

      <!-- Filter Tabs -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12" id="wildlife-tabs">
        <button onclick="filterWildlife('all')" class="wildlife-tab-btn active px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-emerald-600 text-white shadow-lg shadow-emerald-900/30 border border-emerald-400/40 cursor-pointer">
          🐾 Tous les clichés (11)
        </button>
        <button onclick="filterWildlife('felins')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐅 Tigres du Bengale
        </button>
        <button onclick="filterWildlife('geants')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦏 Rhinos & Éléphants
        </button>
        <button onclick="filterWildlife('oiseaux')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦚 Oiseaux & Calaos
        </button>
        <button onclick="filterWildlife('herbivores')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦌 Cerfs & Nilgauts
        </button>
        <button onclick="filterWildlife('reptiles')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐊 Crocodiles & Rivières
        </button>
      </div>

      <!-- Bento Grid (Responsive 1, 2, 4 columns) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6 auto-rows-auto" id="wildlife-grid">
{cards_joined}
      </div>

      <!-- Bottom Banner CTA -->
      <div class="mt-14 p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-[#041d13] via-[#0b4830] to-[#041d13] border border-emerald-500/30 flex flex-col sm:flex-row items-center justify-between gap-6 shadow-2xl">
        <div class="text-center sm:text-left space-y-1">
          <p class="font-black text-lg sm:text-xl text-white">Envie de vivre ces observations de vos propres yeux ?</p>
          <p class="text-xs sm:text-sm text-slate-300">Nos pisteurs Pawan & Kiran vous guident en micro-groupe de 4 à 8 explorateurs.</p>
        </div>
        <div class="flex items-center gap-3 shrink-0">
          <a href="#prochains-departs" class="px-6 py-3 rounded-full bg-white text-slate-950 font-black text-xs sm:text-sm hover:bg-slate-100 hover:scale-105 active:scale-95 transition-all shadow-lg">
            Explorer les 15 circuits faune →
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- WILDLIFE FULLSCREEN LIGHTBOX MODAL -->
  <div id="wildlife-lightbox-modal" class="fixed inset-0 bg-slate-950/95 backdrop-blur-2xl z-50 hidden opacity-0 transition-opacity duration-300 flex items-center justify-center p-4" onclick="if(event.target===this)closeWildlifeLightbox()">
    
    <!-- Top Bar with Counter, Title & Close -->
    <div class="absolute top-6 left-6 right-6 flex items-center justify-between text-white z-30">
      <div class="flex items-center gap-3">
        <div id="wildlife-counter" class="bg-white/10 backdrop-blur-md px-4 py-1.5 rounded-full text-xs font-black border border-white/20">
          1 / 11
        </div>
        <div id="wildlife-modal-title" class="hidden sm:block text-xs font-bold text-slate-200"></div>
      </div>
      <button onclick="closeWildlifeLightbox()" class="w-11 h-11 rounded-full bg-white/10 hover:bg-white/25 border border-white/20 flex items-center justify-center text-white transition-all hover:scale-105 active:scale-95 cursor-pointer shadow-xl" aria-label="Fermer la galerie">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>

    <!-- Navigation Arrows -->
    <button onclick="prevWildlifeImage(event)" class="absolute left-3 sm:left-6 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-900/80 hover:bg-slate-900 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-30 shadow-2xl cursor-pointer" aria-label="Photo précédente">
      <svg class="w-6 h-6 sm:w-7 sm:h-7" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path></svg>
    </button>
    <button onclick="nextWildlifeImage(event)" class="absolute right-3 sm:right-6 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-900/80 hover:bg-slate-900 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-30 shadow-2xl cursor-pointer" aria-label="Photo suivante">
      <svg class="w-6 h-6 sm:w-7 sm:h-7" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
    </button>

    <!-- Main Image & Caption Container -->
    <div class="relative max-w-5xl max-h-[88vh] flex flex-col items-center justify-center z-20">
      <img id="wildlife-lightbox-img" src="" alt="Faune sauvage du Népal" class="max-w-full max-h-[76vh] object-contain rounded-2xl shadow-2xl transition-all duration-300">
      <div id="wildlife-lightbox-caption" class="mt-3 px-4 py-2 rounded-xl bg-slate-900/80 backdrop-blur-md border border-white/10 text-center text-xs text-slate-200"></div>
    </div>
  </div>"""

wildlife_script_js = """  // WILDLIFE GALLERY CONTROLLER
  window.wildlifeData = """ + json.dumps(items, ensure_ascii=False) + """;
  window.currentWildlifeIndex = 0;

  window.filterWildlife = function(category) {
    var cards = document.querySelectorAll('.wildlife-card');
    var buttons = document.querySelectorAll('.wildlife-tab-btn');
    
    buttons.forEach(function(btn) {
      btn.classList.remove('bg-emerald-600', 'text-white', 'shadow-lg', 'shadow-emerald-900/30', 'border-emerald-400/40');
      btn.classList.add('bg-white/10', 'text-slate-300', 'border-white/10');
    });
    
    if (window.event && window.event.target) {
      var target = window.event.target.closest('button');
      if (target) {
        target.classList.remove('bg-white/10', 'text-slate-300', 'border-white/10');
        target.classList.add('bg-emerald-600', 'text-white', 'shadow-lg', 'shadow-emerald-900/30', 'border-emerald-400/40');
      }
    }

    cards.forEach(function(card) {
      if (category === 'all' || card.getAttribute('data-category') === category) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  };

  window.openWildlifeLightbox = function(index) {
    window.currentWildlifeIndex = index;
    window.updateWildlifeModalContent();
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal) {
      modal.classList.remove('hidden');
      setTimeout(function() {
        modal.classList.remove('opacity-0');
        modal.classList.add('opacity-100');
      }, 10);
    }
    document.body.style.overflow = 'hidden';
  };

  window.closeWildlifeLightbox = function() {
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal) {
      modal.classList.remove('opacity-100');
      modal.classList.add('opacity-0');
      setTimeout(function() {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }, 300);
    }
  };

  window.updateWildlifeModalContent = function() {
    var img = document.getElementById('wildlife-lightbox-img');
    var counter = document.getElementById('wildlife-counter');
    var caption = document.getElementById('wildlife-lightbox-caption');
    var topTitle = document.getElementById('wildlife-modal-title');
    var data = window.wildlifeData[window.currentWildlifeIndex];

    if (data) {
      if (img) img.src = data.file;
      if (counter) counter.textContent = (window.currentWildlifeIndex + 1) + ' / ' + window.wildlifeData.length;
      if (caption) caption.innerHTML = '<strong class="text-amber-300 text-sm">' + data.title + '</strong> • ' + data.desc + ' <span class="text-emerald-400">(' + data.location + ')</span>';
      if (topTitle) topTitle.textContent = data.title + ' • ' + data.location;
    }
  };

  window.prevWildlifeImage = function(e) {
    if (e && e.stopPropagation) e.stopPropagation();
    window.currentWildlifeIndex = (window.currentWildlifeIndex - 1 + window.wildlifeData.length) % window.wildlifeData.length;
    window.updateWildlifeModalContent();
  };

  window.nextWildlifeImage = function(e) {
    if (e && e.stopPropagation) e.stopPropagation();
    window.currentWildlifeIndex = (window.currentWildlifeIndex + 1) % window.wildlifeData.length;
    window.updateWildlifeModalContent();
  };

  document.addEventListener('keydown', function(e) {
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal && !modal.classList.contains('hidden')) {
      if (e.key === 'Escape') window.closeWildlifeLightbox();
      if (e.key === 'ArrowLeft') window.prevWildlifeImage();
      if (e.key === 'ArrowRight') window.nextWildlifeImage();
    }
  });"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace or insert the Wildlife Gallery section before Reviews / Avis
if 'id="galerie-faune"' in c:
    c = re.sub(r'<!-- ===+ -->\s*<!-- 7\. GALERIE ÉLITE.*?<\/div>\s*<\/div>\s*<\/section>', gallery_section_html, c, flags=re.DOTALL)
else:
    c = c.replace('<!-- 5. AVIS & TÉMOIGNAGES', f'{gallery_section_html}\n\n  <!-- 5. AVIS & TÉMOIGNAGES')

# Insert the script
if 'WILDLIFE GALLERY CONTROLLER' not in c:
    c = c.replace('</Layout>', f'<script is:inline>\n{wildlife_script_js}\n</script>\n</Layout>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully injected elite Bento Wildlife Gallery and modal into index.astro!")
