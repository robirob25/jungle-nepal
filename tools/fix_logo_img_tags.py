import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    # Adjust logo class to h-11 sm:h-12 w-auto object-contain
    c = re.sub(
        r'src=[\'"]/assets/logo_nav_dark\.(?:webp|png)[\'"]\s+alt=[\'"]Jungle Nepal Adventure[\'"]\s+class=[\'"][^\'"]*[\'"]',
        'src="/assets/logo_nav_dark.webp" alt="Jungle Nepal Adventure" class="h-11 sm:h-12 w-auto object-contain group-hover:scale-105 transition-transform"',
        c
    )
    c = re.sub(
        r'src=[\'"]/assets/logo_nav_white\.(?:webp|png)[\'"]\s+alt=[\'"]Jungle Nepal Adventure[\'"]\s+class=[\'"][^\'"]*[\'"]',
        'src="/assets/logo_nav_white.webp" alt="Jungle Nepal Adventure" class="h-11 sm:h-12 w-auto object-contain group-hover:scale-105 transition-transform"',
        c
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print("Updated logo display classes across all templates!")
