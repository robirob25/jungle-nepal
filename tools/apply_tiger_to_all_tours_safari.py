import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    fname = fpath.split('/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # If the tour has the mosaic with julien_leopard_indien in col-span-2, let's make sure adrien_tigre1 is in col-span-2
    c = re.sub(
        r'<div class="md:col-span-2 h-full overflow-hidden">\s*<img src="/assets/drive_photos/julien_leopard_indien\.webp"[^>]*>\s*</div>\s*<div class="hidden md:block md:col-span-1 h-full overflow-hidden">\s*<img src="/assets/drive_photos/adrien_tigre1\.webp"[^>]*>\s*</div>',
        '''<div class="md:col-span-2 h-full overflow-hidden">
        <img src="/assets/drive_photos/adrien_tigre1.webp" alt="Tigre du Bengale en marche dans la jungle" class="w-full h-full object-cover object-center transition-transform duration-500 hover:scale-105 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="/assets/drive_photos/julien_photographes_jungle.webp" alt="Photographes en immersion dans la jungle" class="w-full h-full object-cover object-center transition-transform duration-500 hover:scale-105 cursor-pointer" onclick="openLightbox(1)"/>
      </div>''',
        c
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Applied wide horizontal tiger to {fname}")

print("Done!")
