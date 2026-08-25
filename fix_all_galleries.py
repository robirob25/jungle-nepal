import json, re, glob, os

galleries = {
    "bardia-explorateur": [
        "/assets/original_site/tigre_bardia.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/adrien_bardia_forest.webp",
        "/assets/drive_photos/julien_cerf_axis.webp",
        "/assets/drive_photos/julien_tigre_bengale1.webp",
        "/assets/drive_photos/adrien_bardia_river.webp",
        "/assets/drive_photos/julien_rollier_oiseau.webp",
        "/assets/drive_photos/adrien_bardia_sunset.webp"
    ],
    "chitwan-culture": [
        "/assets/original_site/chitwan_rhino.webp",
        "/assets/drive_photos/adrien_tigre3.webp",
        "/assets/drive_photos/julien_elephant_mere_petit.webp",
        "/assets/drive_photos/adrien_bhaktapur1.webp",
        "/assets/drive_photos/julien_croco_gharial.webp",
        "/assets/original_site/elephants_river.webp",
        "/assets/drive_photos/adrien_katmandou2.webp",
        "/assets/drive_photos/antoine_wild2.webp"
    ],
    "rafting-safari": [
        "/assets/drive_photos/adrien_bardia_river.webp",
        "/assets/original_site/tigre_water_orig.webp",
        "/assets/original_site/rafting_wild.webp",
        "/assets/drive_photos/adrien_bardia_sunset.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/julien_croco_gharial.webp",
        "/assets/drive_photos/adrien_bardia_camp.webp",
        "/assets/drive_photos/julien_rollier_oiseau.webp"
    ],
    "bardia-nuit-sauvage": [
        "/assets/original_site/camping_sauvage_bardia.webp",
        "/assets/drive_photos/julien_tigre_bengale1.webp",
        "/assets/original_site/camping_experience.webp",
        "/assets/drive_photos/adrien_bardia_camp.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/original_site/bivouac_camp.webp",
        "/assets/drive_photos/adrien_bardia_forest.webp",
        "/assets/drive_photos/julien_cerf_axis.webp"
    ],
    "rara-lake-bardia": [
        "/assets/original_site/lac_rara_orig.webp",
        "/assets/original_site/tigre_bardia.webp",
        "/assets/drive_photos/fred_wild2.webp",
        "/assets/drive_photos/antoine_wild3.webp",
        "/assets/original_site/himalayas_sunrise_peaks.webp",
        "/assets/drive_photos/adrien_bardia_river.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/adrien_bardia_sunset.webp"
    ],
    "bardia-babai-camping": [
        "/assets/original_site/babai_walk.webp",
        "/assets/drive_photos/adrien_tigre4.webp",
        "/assets/drive_photos/julien_elephant_mere_petit.webp",
        "/assets/original_site/camping_sauvage_bardia.webp",
        "/assets/drive_photos/julien_tigre_bengale2.webp",
        "/assets/drive_photos/adrien_bardia_camp.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/julien_rollier_oiseau.webp"
    ],
    "nepal-immersion-totale": [
        "/assets/drive_photos/adrien_bhaktapur2.webp",
        "/assets/original_site/tigre_route.webp",
        "/assets/original_site/chitwan_rhino.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/adrien_bhaktapur1.webp",
        "/assets/drive_photos/adrien_bardia_river.webp",
        "/assets/original_site/temple_sacred.webp",
        "/assets/drive_photos/julien_cerf_axis.webp"
    ],
    "babai-special": [
        "/assets/original_site/elephant_bardia.webp",
        "/assets/drive_photos/adrien_tigre2.webp",
        "/assets/drive_photos/julien_elephant_jungle.webp",
        "/assets/drive_photos/adrien_bardia_sunset.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/original_site/babai_walk.webp",
        "/assets/drive_photos/julien_tigre_bengale1.webp",
        "/assets/drive_photos/julien_croco_gharial.webp"
    ],
    "chitwan-bardia-complete": [
        "/assets/drive_photos/julien_tigre_bengale2.webp",
        "/assets/original_site/chitwan_rhino.webp",
        "/assets/original_site/elephants_river.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/julien_croco_gharial.webp",
        "/assets/drive_photos/adrien_bardia_forest.webp",
        "/assets/drive_photos/adrien_bhaktapur1.webp",
        "/assets/drive_photos/julien_rollier_oiseau.webp"
    ],
    "tiji-mustang": [
        "/assets/original_site/tiji_festival_orig.webp",
        "/assets/original_site/mustang_panorama_orig.webp",
        "/assets/original_site/mustang_village_orig.webp",
        "/assets/drive_photos/fred_wild5.webp",
        "/assets/original_site/himalayas_sunrise_peaks.webp",
        "/assets/original_site/fishtail_sacred_himalaya.webp",
        "/assets/drive_photos/fred_wild1.webp",
        "/assets/drive_photos/adrien_katmandou1.webp"
    ],
    "carnet-de-voyage": [
        "/assets/drive_photos/antoine_wild5.webp",
        "/assets/drive_photos/julien_tigre_bengale3.webp",
        "/assets/drive_photos/julien_rollier_oiseau.webp",
        "/assets/drive_photos/adrien_bhaktapur2.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/original_site/chitwan_rhino.webp",
        "/assets/drive_photos/julien_croco_gharial.webp",
        "/assets/drive_photos/adrien_bardia_sunset.webp"
    ],
    "jungle-extreme": [
        "/assets/drive_photos/julien_leopard_indien.webp",
        "/assets/drive_photos/adrien_tigre1.webp",
        "/assets/drive_photos/julien_photographes_jungle.webp",
        "/assets/drive_photos/julien_tigre_bengale3.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/julien_elephant_jungle.webp",
        "/assets/drive_photos/adrien_bardia_forest.webp",
        "/assets/drive_photos/adrien_bardia_river.webp"
    ],
    "nepal-sauvage": [
        "/assets/original_site/himalayas_sunrise_peaks.webp",
        "/assets/drive_photos/adrien_tigre3.webp",
        "/assets/original_site/fishtail_sacred_himalaya.webp",
        "/assets/drive_photos/julien_cerf_axis.webp",
        "/assets/original_site/chitwan_rhino.webp",
        "/assets/drive_photos/julien_safari_a_pied.webp",
        "/assets/drive_photos/adrien_bardia_river.webp",
        "/assets/drive_photos/adrien_bardia_sunset.webp"
    ],
    "immersion-spirituelle": [
        "/assets/original_site/temple_sacred.webp",
        "/assets/drive_photos/adrien_bhaktapur1.webp",
        "/assets/drive_photos/adrien_katmandou1.webp",
        "/assets/original_site/nepal_landscape.webp",
        "/assets/original_site/fishtail_sacred_himalaya.webp",
        "/assets/drive_photos/adrien_bhaktapur2.webp",
        "/assets/drive_photos/adrien_katmandou2.webp",
        "/assets/original_site/himalayas_sunrise_peaks.webp"
    ],
    "panthere-des-neiges": [
        "/assets/snow-leopard/snow_leopard_portrait.webp",
        "/assets/snow-leopard/snow_leopard_wild_cliff.webp",
        "/assets/snow-leopard/annapurna_peaks.jpg",
        "/assets/snow-leopard/pokhara_lake.webp",
        "/assets/snow-leopard/snow_leopard_mountains.jpg",
        "/assets/original_site/himalayas_sunrise_peaks.webp",
        "/assets/original_site/fishtail_sacred_himalaya.webp",
        "/assets/drive_photos/fred_wild2.webp"
    ]
}

lightbox_modal_replacement = """  <!-- BULLETPROOF LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 bg-slate-950/95 backdrop-blur-xl z-50 hidden opacity-0 transition-opacity duration-300 flex items-center justify-center p-4" onclick="if(event.target===this)closeLightbox()">
    
    <!-- Top Bar with Counter & Close -->
    <div class="absolute top-6 left-6 right-6 flex items-center justify-between text-white z-30">
      <div id="lightbox-counter" class="bg-white/10 backdrop-blur-md px-4 py-1.5 rounded-full text-xs font-black border border-white/20">
        1 / 8
      </div>
      <button onclick="closeLightbox()" class="w-11 h-11 rounded-full bg-white/10 hover:bg-white/25 border border-white/20 flex items-center justify-center text-white transition-all hover:scale-105 active:scale-95 cursor-pointer shadow-xl" aria-label="Fermer la galerie">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
    </div>

    <!-- Navigation Arrows -->
    <button onclick="prevLightboxImage(event)" class="absolute left-3 sm:left-6 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-900/80 hover:bg-slate-900 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-30 shadow-2xl cursor-pointer" aria-label="Photo précédente">
      <svg class="w-6 h-6 sm:w-7 sm:h-7" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path></svg>
    </button>
    <button onclick="nextLightboxImage(event)" class="absolute right-3 sm:right-6 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-900/80 hover:bg-slate-900 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-30 shadow-2xl cursor-pointer" aria-label="Photo suivante">
      <svg class="w-6 h-6 sm:w-7 sm:h-7" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
    </button>

    <!-- Main Image Container -->
    <div class="relative max-w-5xl max-h-[85vh] flex items-center justify-center z-20">
      <img id="lightbox-image" src="" alt="Photo agrandie du séjour" class="max-w-full max-h-[82vh] object-contain rounded-2xl shadow-2xl transition-all duration-300">
    </div>
  </div>"""

for slug, img_list in galleries.items():
    fpath = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro'
    if not os.path.exists(fpath):
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Replace Lightbox Modal HTML
    c = re.sub(
        r'<div id=[\'"]lightbox-modal[\'"].*?<\/div>\s*<\/div>',
        lightbox_modal_replacement,
        c,
        flags=re.DOTALL
    )

    # 2. Build bulletproof script
    imgs_json = json.dumps(img_list, indent=6)
    script_content = """  <script is:inline>
    // Bulletproof Global Lightbox Controller
    window.galleryImages = """ + imgs_json + """;
    window.currentImageIndex = 0;

    window.openLightbox = function(index) {
      window.currentImageIndex = typeof index === 'number' ? index : 0;
      window.updateLightboxContent();
      var modal = document.getElementById('lightbox-modal');
      if (modal) {
        modal.classList.remove('hidden');
        setTimeout(function() {
          modal.classList.remove('opacity-0');
          modal.classList.add('opacity-100');
        }, 10);
      }
      document.body.style.overflow = 'hidden';
    };

    window.closeLightbox = function() {
      var modal = document.getElementById('lightbox-modal');
      if (modal) {
        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0');
        setTimeout(function() {
          modal.classList.add('hidden');
          document.body.style.overflow = '';
        }, 300);
      }
    };

    window.updateLightboxContent = function() {
      var img = document.getElementById('lightbox-image');
      var counter = document.getElementById('lightbox-counter');
      if (img && window.galleryImages && window.galleryImages[window.currentImageIndex]) {
        img.src = window.galleryImages[window.currentImageIndex];
      }
      if (counter && window.galleryImages) {
        counter.textContent = (window.currentImageIndex + 1) + ' / ' + window.galleryImages.length;
      }
    };

    window.prevLightboxImage = function(e) {
      if (e && e.stopPropagation) e.stopPropagation();
      if (!window.galleryImages || !window.galleryImages.length) return;
      window.currentImageIndex = (window.currentImageIndex - 1 + window.galleryImages.length) % window.galleryImages.length;
      window.updateLightboxContent();
    };

    window.nextLightboxImage = function(e) {
      if (e && e.stopPropagation) e.stopPropagation();
      if (!window.galleryImages || !window.galleryImages.length) return;
      window.currentImageIndex = (window.currentImageIndex + 1) % window.galleryImages.length;
      window.updateLightboxContent();
    };

    document.addEventListener('keydown', function(e) {
      var modal = document.getElementById('lightbox-modal');
      if (modal && !modal.classList.contains('hidden')) {
        if (e.key === 'Escape') window.closeLightbox();
        if (e.key === 'ArrowLeft') window.prevLightboxImage();
        if (e.key === 'ArrowRight') window.nextLightboxImage();
      }
    });

    try {
      if (typeof lucide !== 'undefined' && lucide.createIcons) {
        lucide.createIcons();
      }
    } catch(err) {
      console.warn('Lucide icons warning:', err);
    }
  </script>"""

    # Replace the gallery & lightbox script block
    c = re.sub(
        r'<script is:inline>\s*(?:lucide\.createIcons\(\);)?\s*\/\/\s*GALLERY & LIGHTBOX.*?<\/script>',
        script_content,
        c,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Upgraded Lightbox modal & scripts with bulletproof architecture across all 15 tour detail pages!")
