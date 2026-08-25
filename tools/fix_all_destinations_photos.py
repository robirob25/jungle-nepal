import re

# 1. FIX KATMANDOU (Pure Cultural, Buddhist Stupas, Newar Architecture, Medieval Temples)
# Gallery:
# 1. Swayambhunath Stupa (Boudha Stupa au soleil) -> /assets/drive_photos/adrien_katmandou1.webp
# 2. Bhaktapur Nyatapola & Royales -> /assets/drive_photos/adrien_bhaktapur1.webp
# 3. Moulins à prières sacrés -> https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg
# 4. Bhaktapur Vie locale & potiers -> /assets/drive_photos/adrien_bhaktapur2.webp

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/katmandou.astro', 'r', encoding='utf-8') as f:
    ktm = f.read()

# Replace gallery array in script
old_ktm_js = """  const galleryImages = [
    "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
    "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
    "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
    "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
  ];"""

new_ktm_js = """  const galleryImages = [
    "/assets/drive_photos/adrien_katmandou1.webp",
    "/assets/drive_photos/adrien_bhaktapur1.webp",
    "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
    "/assets/drive_photos/adrien_bhaktapur2.webp"
  ];"""

ktm = ktm.replace(old_ktm_js, new_ktm_js)

# Replace gallery markup
old_ktm_markup = """      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div onclick="openLightbox(0)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg" alt="Vallée de Katmandou" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
        <div onclick="openLightbox(1)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg" alt="Vallée de Katmandou" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
        <div onclick="openLightbox(2)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg" alt="Vallée de Katmandou" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
        <div onclick="openLightbox(3)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg" alt="Vallée de Katmandou" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
      </div>"""

new_ktm_markup = """      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div onclick="openLightbox(0)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="/assets/drive_photos/adrien_katmandou1.webp" alt="Stupa sacré de Katmandou" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
        <div onclick="openLightbox(1)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="/assets/drive_photos/adrien_bhaktapur1.webp" alt="Cité royale de Bhaktapur" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
        <div onclick="openLightbox(2)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg" alt="Moulins à prières bouddhistes" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
        <div onclick="openLightbox(3)" class="rounded-2xl overflow-hidden shadow-md h-60 group cursor-pointer relative">
          <img src="/assets/drive_photos/adrien_bhaktapur2.webp" alt="Ruelle historique & artisanat Newar" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        </div>
      </div>"""

ktm = ktm.replace(old_ktm_markup, new_ktm_markup)

# Replace group size badge 4-8 with 4-10 in tour cards of Katmandou
ktm = ktm.replace('4–8 pers.', '4 à 10 pers.')
ktm = ktm.replace('4-8 pers.', '4 à 10 pers.')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/katmandou.astro', 'w', encoding='utf-8') as f:
    f.write(ktm)
print("✓ Curated Katmandou destination gallery with 100% genuine cultural & heritage photos!")

# 2. FIX BARDIA (Tigers, walking safari, jungle camp, Tharu culture)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/bardia.astro', 'r', encoding='utf-8') as f:
    bar = f.read()

bar = bar.replace(
    'src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png"',
    'src="/assets/original_site/tigre_bardia.webp"'
)
bar = bar.replace('4–8 pers.', '4 à 10 pers.')
bar = bar.replace('4-8 pers.', '4 à 10 pers.')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/bardia.astro', 'w', encoding='utf-8') as f:
    f.write(bar)
print("✓ Cleaned Bardia destination page")

# 3. FIX CHITWAN (One-horned rhinos, canoe on Rapti, jungle)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/chitwan.astro', 'r', encoding='utf-8') as f:
    cht = f.read()

cht = cht.replace(
    'https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg',
    '/assets/curated_gallery/rhino_unicorne_brume.webp'
)
cht = cht.replace('4–8 pers.', '4 à 10 pers.')
cht = cht.replace('4-8 pers.', '4 à 10 pers.')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/chitwan.astro', 'w', encoding='utf-8') as f:
    f.write(cht)
print("✓ Cleaned Chitwan destination page")

# 4. FIX ANNAPURNA (Mountains, Machapuchare, Himalayan ridges)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/annapurna.astro', 'r', encoding='utf-8') as f:
    ann = f.read()

ann = ann.replace(
    'https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg',
    '/assets/original_site/machapuchare.webp'
)
ann = ann.replace('4–8 pers.', '4 à 10 pers.')
ann = ann.replace('4-8 pers.', '4 à 10 pers.')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/annapurna.astro', 'w', encoding='utf-8') as f:
    f.write(ann)
print("✓ Cleaned Annapurna destination page")

# 5. FIX SUKLAPHANTA (Swamp deers, wild grasslands, Terai)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/suklaphanta.astro', 'r', encoding='utf-8') as f:
    suk = f.read()

suk = suk.replace(
    'https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png',
    '/assets/original_site/suklaphanta.webp'
)
suk = suk.replace('4–8 pers.', '4 à 10 pers.')
suk = suk.replace('4-8 pers.', '4 à 10 pers.')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/suklaphanta.astro', 'w', encoding='utf-8') as f:
    f.write(suk)
print("✓ Cleaned Suklaphanta destination page")

# 6. Also clean destinations/index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'r', encoding='utf-8') as f:
    d_idx = f.read()

d_idx = d_idx.replace('4–8 pers.', '4 à 10 pers.')
d_idx = d_idx.replace('4-8 pers.', '4 à 10 pers.')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'w', encoding='utf-8') as f:
    f.write(d_idx)
print("✓ Cleaned destinations/index.astro")
