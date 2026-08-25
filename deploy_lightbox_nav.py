import os
import re

new_lightbox_html = """  <!-- LIGHTBOX WITH PREV / NEXT ARROWS & COUNTER -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 hidden bg-black/95 backdrop-blur-xl flex items-center justify-center p-4 select-none" onclick="if(event.target === this) closeLightbox()">
    
    <!-- Close Button -->
    <button onclick="closeLightbox()" class="absolute top-6 right-6 text-white/80 hover:text-white p-3 hover:bg-white/10 rounded-full transition-all duration-200 z-50 cursor-pointer" aria-label="Fermer">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>

    <!-- Prev Arrow Button -->
    <button onclick="prevLightbox(event)" class="absolute left-4 sm:left-8 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-white/10 hover:bg-white/25 text-white border border-white/20 backdrop-blur-xl shadow-2xl flex items-center justify-center transition-all duration-200 hover:scale-110 active:scale-95 z-50 cursor-pointer group" aria-label="Photo précédente">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 group-hover:-translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
      </svg>
    </button>

    <!-- Image Container -->
    <div class="relative max-w-5xl max-h-[85vh] flex items-center justify-center">
      <img id="lightbox-img" src="" alt="Galerie Expédition" class="max-w-full max-h-[85vh] object-contain rounded-2xl sm:rounded-3xl shadow-2xl transition-all duration-300">
    </div>

    <!-- Next Arrow Button -->
    <button onclick="nextLightbox(event)" class="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-white/10 hover:bg-white/25 text-white border border-white/20 backdrop-blur-xl shadow-2xl flex items-center justify-center transition-all duration-200 hover:scale-110 active:scale-95 z-50 cursor-pointer group" aria-label="Photo suivante">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
      </svg>
    </button>

    <!-- Counter Badge -->
    <div class="absolute bottom-6 left-1/2 -translate-x-1/2 px-4 py-1.5 rounded-full bg-slate-950/80 backdrop-blur-md text-white text-xs font-black border border-white/20 tracking-wider">
      <span id="lightbox-counter">1 / 4</span>
    </div>

  </div>"""

new_lightbox_js_functions = """
    let currentLightboxIndex = 0;

    function updateLightboxImage() {
      const img = document.getElementById('lightbox-img');
      const counter = document.getElementById('lightbox-counter');
      if (img && typeof allImages !== 'undefined' && allImages.length > 0) {
        img.src = allImages[currentLightboxIndex];
      }
      if (counter && typeof allImages !== 'undefined' && allImages.length > 0) {
        counter.innerText = `${currentLightboxIndex + 1} / ${allImages.length}`;
      }
    }

    function openLightbox(index) {
      if (typeof allImages === 'undefined' || allImages.length === 0) return;
      currentLightboxIndex = index >= 0 && index < allImages.length ? index : 0;
      const modal = document.getElementById('lightbox-modal');
      updateLightboxImage();
      if (modal) modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
      const modal = document.getElementById('lightbox-modal');
      if (modal) modal.classList.add('hidden');
      document.body.style.overflow = 'auto';
    }

    function prevLightbox(e) {
      if (e) e.stopPropagation();
      if (typeof allImages === 'undefined' || allImages.length === 0) return;
      currentLightboxIndex = (currentLightboxIndex - 1 + allImages.length) % allImages.length;
      updateLightboxImage();
    }

    function nextLightbox(e) {
      if (e) e.stopPropagation();
      if (typeof allImages === 'undefined' || allImages.length === 0) return;
      currentLightboxIndex = (currentLightboxIndex + 1) % allImages.length;
      updateLightboxImage();
    }

    window.addEventListener('keydown', (e) => {
      const modal = document.getElementById('lightbox-modal');
      if (!modal || modal.classList.contains('hidden')) return;
      if (e.key === 'ArrowLeft') prevLightbox();
      if (e.key === 'ArrowRight') nextLightbox();
      if (e.key === 'Escape') closeLightbox();
    });
"""

# 1. Update all 14 tours in tours/*.html
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace old lightbox modal markup
    old_modal_pattern = r'<!-- LIGHTBOX -->\s*<div id="lightbox-modal".*?</div>\s*(?=<script)'
    c = re.sub(old_modal_pattern, new_lightbox_html, c, flags=re.DOTALL)

    # Replace old openLightbox/closeLightbox functions in JS
    old_js_pattern = r'function openLightbox\(index\)\s*\{.*?function closeLightbox\(\)\s*\{.*?document\.body\.style\.overflow = \'auto\';\s*\}'
    c = re.sub(old_js_pattern, new_lightbox_js_functions.strip(), c, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("1. Updated lightbox with arrows, keyboard shortcuts, and counter across all 14 tour pages!")

# 2. Update destinations/*.html to also support interactive lightbox with arrows
import json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/scraped_destinations_raw.json', 'r', encoding='utf-8') as f:
    dest_data = json.load(f)

# Re-run tailored destination update with gallery lightbox support
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
for fname in os.listdir(dest_dir):
    if not fname.endswith('.html') or fname == 'index.html':
        continue
    fpath = os.path.join(dest_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        dhtml = f.read()

    # Extract all gallery images in this page
    gallery_imgs = re.findall(r'<img src="([^"]+)" alt="[^"]+" class="[^"]*group-hover:scale-105[^"]*"', dhtml)
    if not gallery_imgs:
        gallery_imgs = re.findall(r'<div class="rounded-2xl overflow-hidden shadow-md h-60 group">\s*<img src="([^"]+)"', dhtml)

    # Make gallery cards clickable
    for i, gimg in enumerate(gallery_imgs):
        old_card = f'<div class="rounded-2xl overflow-hidden shadow-md h-60 group"><img src="{gimg}"'
        new_card = f'<div onclick="openLightbox({i})" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative"><img src="{gimg}"'
        dhtml = dhtml.replace(old_card, new_card)

    # Add lightbox modal and JS if not present
    if 'id="lightbox-modal"' not in dhtml:
        js_block = f"""
  {new_lightbox_html}

  <script>
    const allImages = {json.dumps(gallery_imgs)};
    {new_lightbox_js_functions}
  </script>
"""
        dhtml = dhtml.replace('</body>', js_block + '\n</body>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(dhtml)

print("2. Deployed interactive gallery lightbox on all destination pages!")
