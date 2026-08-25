import json, re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

cards_html = []
for idx, item in enumerate(items):
    card = f"""        <!-- Photo {idx+1}: {item['title']} -->
        <div class="wildlife-card break-inside-avoid mb-6 relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-500/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.25)] transition-all duration-300 bg-slate-900" data-category="{item['category']}" data-idx="{idx}" onclick="openWildlifeLightbox({idx})">
          
          <img 
            src="{item['file']}" 
            alt="{item['title']} - {item['location']}" 
            class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300"
            loading="lazy"
          />
          
          <!-- Subtle Gradient Overlay (Revealed on Hover) -->
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>

          <!-- Top Location Badge -->
          <div class="absolute top-3.5 left-3.5 z-10 pointer-events-none">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[11px] font-black text-amber-300 shadow-md">
              <span>📍</span>
              <span>{item['location']}</span>
            </span>
          </div>

          <!-- Bottom Floating Glass Caption -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-10 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-white/15 text-white opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 shadow-2xl pointer-events-none">
            <div class="flex items-center justify-between gap-3">
              <div class="min-w-0 flex-1">
                <h3 class="font-black text-sm sm:text-base text-white group-hover:text-amber-300 transition-colors leading-tight truncate">
                  {item['title']}
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium truncate">
                  {item['desc']}
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0 border border-emerald-500/30">
                <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>

        </div>"""
    cards_html.append(card)

cards_joined = "\n\n".join(cards_html)

counts = {
    "all": len(items),
    "felins": sum(1 for i in items if i['category'] == 'felins'),
    "mammiferes": sum(1 for i in items if i['category'] == 'mammiferes'),
    "oiseaux": sum(1 for i in items if i['category'] == 'oiseaux'),
    "reptiles": sum(1 for i in items if i['category'] == 'reptiles'),
}

new_gallery_section = f"""  <!-- ========================================================================= -->
  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL (SÉLECTION PRÉCISE ET CURATÉE) -->
  <!-- ========================================================================= -->
  <section id="galerie-faune" class="py-20 sm:py-28 lg:py-32 bg-[#020617] text-white relative overflow-hidden">
    <!-- Ambient jungle glow -->
    <div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-emerald-600/10 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-14">
        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-emerald-400 bg-emerald-950/80 border border-emerald-500/30 px-4 py-1.5 rounded-full mb-4 shadow-inner">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          Observations 100% Sauvages
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight leading-tight">
          La faune du Terai dans son intimité brute.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          Photographies authentiques capturées par nos voyageurs lors de nos safaris à pied et en jeep au Népal. Faune sauvage dans son habitat naturel préservé.
        </p>
      </div>

      <!-- Category Filter Tabs -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12">
        <button 
          onclick="filterWildlife('all')" 
          class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-black transition-all duration-300 border bg-emerald-600 text-white shadow-lg shadow-emerald-900/30 border-emerald-400/40 cursor-pointer"
          data-filter="all"
        >
          🧭 Tous les clichés ({counts['all']})
        </button>
        <button 
          onclick="filterWildlife('felins')" 
          class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-black transition-all duration-300 border bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
          data-filter="felins"
        >
          🐅 Grands Félins ({counts['felins']})
        </button>
        <button 
          onclick="filterWildlife('mammiferes')" 
          class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-black transition-all duration-300 border bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
          data-filter="mammiferes"
        >
          🦏 Grands Mammifères ({counts['mammiferes']})
        </button>
        <button 
          onclick="filterWildlife('oiseaux')" 
          class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-black transition-all duration-300 border bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
          data-filter="oiseaux"
        >
          🦜 Oiseaux Rares ({counts['oiseaux']})
        </button>
        <button 
          onclick="filterWildlife('reptiles')" 
          class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-black transition-all duration-300 border bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
          data-filter="reptiles"
        >
          🐊 Reptiles & Rivières ({counts['reptiles']})
        </button>
      </div>

      <!-- Fluid Multi-Column Masonry Collage -->
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 max-w-7xl mx-auto" id="wildlife-grid">
{cards_joined}
      </div>

      <!-- Load More Button (Voir +) -->
      <div class="mt-12 text-center" id="wildlife-load-more-container">
        <button 
          id="wildlife-load-more-btn"
          onclick="loadMoreWildlife()" 
          class="inline-flex items-center gap-3 px-8 py-4 rounded-full bg-slate-900/90 hover:bg-emerald-600 text-white font-extrabold text-sm sm:text-base border border-emerald-500/40 hover:border-emerald-400 shadow-xl shadow-emerald-950/40 transition-all duration-300 hover:scale-105 active:scale-95 cursor-pointer group"
        >
          <span class="w-6 h-6 rounded-full bg-emerald-500/20 group-hover:bg-white/20 flex items-center justify-center text-emerald-400 group-hover:text-white transition-colors">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12h14"></path></svg>
          </span>
          <span id="wildlife-load-more-text">Voir + de photos</span>
          <span class="text-xs px-2.5 py-0.5 rounded-full bg-white/10 text-amber-300 font-mono" id="wildlife-count-badge">21 / {counts['all']}</span>
        </button>
      </div>

      <!-- Bottom Banner CTA -->
      <div class="mt-14 p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-[#041d13] via-[#0b4830] to-[#041d13] border border-emerald-500/30 flex flex-col sm:flex-row items-center justify-between gap-6 shadow-2xl">
        <div class="text-center sm:text-left space-y-1">
          <p class="font-black text-lg sm:text-xl text-white">Envie de vivre ces observations de vos propres yeux ?</p>
          <p class="text-xs sm:text-sm text-slate-300">Nos pisteurs <a href="/a-propos" class="text-emerald-400 hover:text-emerald-300 font-semibold underline decoration-emerald-500/30 underline-offset-2 transition-colors">Pawan & Kiran</a> vous guident en micro-groupe de 4 à 8 explorateurs.</p>
        </div>
        <div class="flex items-center gap-3 shrink-0">
          <a href="#prochains-departs" class="px-6 py-3 rounded-full bg-white text-slate-950 font-black text-xs sm:text-sm hover:bg-slate-100 hover:scale-100 active:scale-95 transition-all shadow-lg">
            Explorer les 15 circuits faune →
          </a>
        </div>
      </div>

    </div>

    <!-- ========================================================================= -->
    <!-- WILDLIFE LIGHTBOX MODAL (PLEIN ÉCRAN FLUIDE) -->
    <!-- ========================================================================= -->
    <div 
      id="wildlife-lightbox-modal" 
      class="fixed inset-0 z-[9999] bg-black/95 backdrop-blur-2xl hidden opacity-0 transition-opacity duration-300 flex items-center justify-center p-4 sm:p-6 select-none"
      onclick="if(event.target === this) closeWildlifeLightbox()"
    >
      <!-- Close Button Top Right -->
      <button 
        onclick="closeWildlifeLightbox()" 
        class="absolute top-4 right-4 sm:top-6 sm:right-6 w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center border border-white/20 transition-all duration-200 hover:scale-110 z-50 cursor-pointer shadow-2xl"
        aria-label="Fermer"
      >
        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6L6 18M6 6l12 12"></path></svg>
      </button>

      <!-- Top Badge Info -->
      <div class="absolute top-4 left-4 sm:top-6 sm:left-6 z-50 flex items-center gap-3">
        <span class="px-4 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-500/30 text-emerald-400 font-mono text-xs sm:text-sm font-bold shadow-lg" id="wildlife-counter">
          1 / {counts['all']}
        </span>
        <span class="hidden sm:inline-block px-4 py-1.5 rounded-full bg-white/10 border border-white/15 text-slate-200 text-xs sm:text-sm font-semibold backdrop-blur-md" id="wildlife-modal-location">
          Népal Sauvage
        </span>
      </div>

      <!-- Navigation Arrow Left -->
      <button 
        onclick="prevWildlifePhoto(event)" 
        class="absolute left-2 sm:left-6 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-900/80 hover:bg-emerald-600 text-white flex items-center justify-center border border-white/20 hover:border-emerald-400 transition-all duration-200 hover:scale-110 z-50 cursor-pointer shadow-2xl group"
        aria-label="Photo précédente"
      >
        <svg class="w-6 h-6 sm:w-7 sm:h-7 group-hover:-translate-x-0.5 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 19l-7-7 7-7"></path></svg>
      </button>

      <!-- Navigation Arrow Right -->
      <button 
        onclick="nextWildlifePhoto(event)" 
        class="absolute right-2 sm:right-6 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-900/80 hover:bg-emerald-600 text-white flex items-center justify-center border border-white/20 hover:border-emerald-400 transition-all duration-200 hover:scale-110 z-50 cursor-pointer shadow-2xl group"
        aria-label="Photo suivante"
      >
        <svg class="w-6 h-6 sm:w-7 sm:h-7 group-hover:translate-x-0.5 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 5l7 7-7 7"></path></svg>
      </button>

      <!-- Main Content Container -->
      <div class="relative max-w-6xl max-h-[92vh] flex flex-col items-center justify-center z-40 mx-auto" onclick="event.stopPropagation()">
        <!-- Image Display -->
        <div class="relative rounded-2xl overflow-hidden shadow-[0_25px_60px_rgba(0,0,0,0.8)] border border-white/15 bg-slate-950 flex items-center justify-center">
          <img 
            id="wildlife-lightbox-img" 
            src="" 
            alt="Photographie faune sauvage du Népal" 
            class="max-h-[75vh] max-w-[90vw] md:max-w-[80vw] w-auto h-auto object-contain block transition-all duration-200"
          />
        </div>

        <!-- Caption & Details -->
        <div class="mt-4 px-6 py-3 rounded-2xl bg-slate-900/90 backdrop-blur-xl border border-white/15 text-center max-w-2xl shadow-xl">
          <h3 id="wildlife-modal-title" class="text-base sm:text-lg font-black text-white"></h3>
          <p id="wildlife-lightbox-caption" class="text-xs sm:text-sm text-slate-300 mt-0.5 font-medium"></p>
        </div>
      </div>
    </div>

  </section>"""

wildlife_script_js = """  // WILDLIFE GALLERY CONTROLLER WITH PAGINATION & LIGHTBOX
  window.wildlifeData = """ + json.dumps(items, ensure_ascii=False) + """;
  window.currentWildlifeIndex = 0;
  window.currentWildlifeCategory = 'all';
  window.wildlifeVisibleLimit = 21; // Initial 21 photos (7 per column)

  window.renderWildlifeCards = function() {
    var cards = document.querySelectorAll('.wildlife-card');
    var loadMoreContainer = document.getElementById('wildlife-load-more-container');
    var countBadge = document.getElementById('wildlife-count-badge');
    var loadMoreText = document.getElementById('wildlife-load-more-text');
    
    var visibleInCurrentCategory = 0;
    var totalInCurrentCategory = 0;

    cards.forEach(function(card) {
      var cat = card.getAttribute('data-category');
      var matchesCat = (window.currentWildlifeCategory === 'all' || cat === window.currentWildlifeCategory);
      
      if (matchesCat) {
        totalInCurrentCategory++;
        if (window.currentWildlifeCategory === 'all') {
          if (visibleInCurrentCategory < window.wildlifeVisibleLimit) {
            card.style.display = 'block';
            visibleInCurrentCategory++;
          } else {
            card.style.display = 'none';
          }
        } else {
          card.style.display = 'block';
          visibleInCurrentCategory++;
        }
      } else {
        card.style.display = 'none';
      }
    });

    if (window.currentWildlifeCategory === 'all') {
      if (loadMoreContainer) {
        if (visibleInCurrentCategory < totalInCurrentCategory) {
          loadMoreContainer.style.display = 'block';
          if (countBadge) countBadge.textContent = visibleInCurrentCategory + ' / ' + totalInCurrentCategory;
          if (loadMoreText) loadMoreText.textContent = 'Voir + de photos';
        } else {
          loadMoreContainer.style.display = 'none';
        }
      }
    } else {
      if (loadMoreContainer) loadMoreContainer.style.display = 'none';
    }
  };

  window.loadMoreWildlife = function() {
    window.wildlifeVisibleLimit += 10;
    window.renderWildlifeCards();
  };

  window.filterWildlife = function(category) {
    window.currentWildlifeCategory = category;
    if (category === 'all') {
      window.wildlifeVisibleLimit = 21; // reset to 21 when returning to all
    }
    
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

    window.renderWildlifeCards();
  };

  window.openWildlifeLightbox = function(index) {
    window.currentWildlifeIndex = index;
    window.updateWildlifeModalContent();
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal) {
      modal.classList.remove('hidden');
      requestAnimationFrame(function() {
        modal.classList.remove('opacity-0');
        modal.classList.add('opacity-100');
      });
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
    var locBadge = document.getElementById('wildlife-modal-location');
    var data = window.wildlifeData[window.currentWildlifeIndex];

    if (data) {
      if (img) {
        img.src = data.file;
        img.alt = data.title;
      }
      if (counter) counter.textContent = (window.currentWildlifeIndex + 1) + ' / ' + window.wildlifeData.length;
      if (topTitle) topTitle.textContent = data.title;
      if (caption) caption.textContent = data.desc;
      if (locBadge) locBadge.textContent = '📍 ' + data.location;
    }
  };

  window.prevWildlifePhoto = function(e) {
    if (e) e.stopPropagation();
    window.currentWildlifeIndex = (window.currentWildlifeIndex - 1 + window.wildlifeData.length) % window.wildlifeData.length;
    window.updateWildlifeModalContent();
  };

  window.nextWildlifePhoto = function(e) {
    if (e) e.stopPropagation();
    window.currentWildlifeIndex = (window.currentWildlifeIndex + 1) % window.wildlifeData.length;
    window.updateWildlifeModalContent();
  };

  document.addEventListener('keydown', function(e) {
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal && !modal.classList.contains('hidden')) {
      if (e.key === 'Escape') window.closeWildlifeLightbox();
      if (e.key === 'ArrowLeft') window.prevWildlifePhoto();
      if (e.key === 'ArrowRight') window.nextWildlifePhoto();
    }
  });

  document.addEventListener('DOMContentLoaded', function() {
    window.renderWildlifeCards();
  });
"""

# Read index.astro and replace section 5 and script
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace section 5
idx_content = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 5\. GALERIE COLLAGE SAUVAGE DU NÉPAL.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS',
    new_gallery_section + '\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS',
    idx_content,
    flags=re.DOTALL
)

# Replace script at the end
idx_content = re.sub(
    r'<script is:inline>\s*// WILDLIFE GALLERY CONTROLLER.*?</script>',
    f'<script is:inline>\n{wildlife_script_js}\n</script>',
    idx_content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Updated index.astro with complete responsive Lightbox Modal and ultra-smooth event handlers!")
