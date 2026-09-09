import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    fname = fpath.split('/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Leopard photo (julien_leopard_indien.webp) -> leopard head is in top center
    c = c.replace(
        'src="/assets/drive_photos/julien_leopard_indien.webp" alt="Expédition Népal Sauvage" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer"',
        'src="/assets/drive_photos/julien_leopard_indien.webp" alt="Léopard indien dans la jungle" class="w-full h-full object-cover object-[55%_40%] transition-opacity duration-300 cursor-pointer"'
    )

    # 2. Tiger photo (adrien_tigre1.webp) -> tiger head is in center-right
    c = c.replace(
        'src="/assets/drive_photos/adrien_tigre1.webp" alt="Expédition Népal Sauvage" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer"',
        'src="/assets/drive_photos/adrien_tigre1.webp" alt="Tigre du Bengale en marche" class="w-full h-full object-cover object-[65%_45%] transition-opacity duration-300 cursor-pointer"'
    )
    
    # 3. Tiger photo 3 (julien_tigre_bengale3.webp) -> center head
    c = c.replace(
        'src="/assets/drive_photos/julien_tigre_bengale3.webp" alt="Expédition Népal Sauvage" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer"',
        'src="/assets/drive_photos/julien_tigre_bengale3.webp" alt="Tigre du Bengale à l\'affût" class="w-full h-full object-cover object-center transition-opacity duration-300 cursor-pointer"'
    )

    # Increase container height slightly on desktop if helpful for full facial framing
    c = c.replace('h-[280px] sm:h-[380px] md:h-[460px]', 'h-[280px] sm:h-[380px] md:h-[480px]')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Adjusted feline focal point crops in {fname}")

print("All tour photo gallery feline crops perfected!")
