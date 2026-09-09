import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    fname = fpath.split('/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. We put the Tiger (adrien_tigre1.webp) in the large 2-column main position (md:col-span-2)
    # 2. We put the vertical Photographers (julien_photographes_jungle.webp) in the single vertical slot (md:col-span-1)
    # 3. We put Leopard (top) and Tiger 3 (bottom) in the right stacked column
    
    old_gallery = """    <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 sm:gap-3 rounded-2xl sm:rounded-3xl overflow-hidden h-[280px] sm:h-[380px] md:h-[480px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="/assets/drive_photos/julien_leopard_indien.webp" alt="Léopard indien dans la jungle" class="w-full h-full object-cover object-[55%_40%] transition-opacity duration-300 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="/assets/drive_photos/adrien_tigre1.webp" alt="Tigre du Bengale en marche" class="w-full h-full object-cover object-[65%_45%] transition-opacity duration-300 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="/assets/drive_photos/julien_photographes_jungle.webp" alt="Expédition Népal Sauvage" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="/assets/drive_photos/julien_tigre_bengale3.webp" alt="Tigre du Bengale à l'affût" class="w-full h-full object-cover object-center transition-opacity duration-300 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>"""

    new_gallery = """    <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 sm:gap-3 rounded-2xl sm:rounded-3xl overflow-hidden h-[280px] sm:h-[380px] md:h-[480px] mb-8 relative shadow-lg">
      <!-- 1. Grande photo horizontale principale : Tigre du Bengale en entier dans son décor sauvage -->
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="/assets/drive_photos/adrien_tigre1.webp" alt="Tigre du Bengale en marche dans la jungle" class="w-full h-full object-cover object-center transition-transform duration-500 hover:scale-105 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <!-- 2. Photo verticale naturelle : Explorateurs et photographes sous la canopée -->
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="/assets/drive_photos/julien_photographes_jungle.webp" alt="Photographes en immersion dans la jungle" class="w-full h-full object-cover object-center transition-transform duration-500 hover:scale-105 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <!-- 3. Colonne droite : Léopard et Tigre à l'affût -->
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="/assets/drive_photos/julien_leopard_indien.webp" alt="Regard du Léopard indien" class="w-full h-full object-cover object-[55%_35%] transition-transform duration-500 hover:scale-105 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="/assets/drive_photos/julien_tigre_bengale3.webp" alt="Tigre du Bengale à l'affût" class="w-full h-full object-cover object-center transition-transform duration-500 hover:scale-105 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>"""

    c = c.replace(old_gallery, new_gallery)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Optimized horizontal tiger layout in {fname}")

print("All tour hero galleries updated with full horizontal tiger!")
