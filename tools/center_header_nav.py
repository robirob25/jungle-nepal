import glob, re

# In index.astro and Header.astro:
# Use a 3-column equal grid layout or flex-1 centered nav structure:
# Left: w-1/4 or shrink-0
# Center: absolute left-1/2 -translate-x-1/2 OR flex-1 flex justify-center
# Right: w-1/4 flex justify-end

# 1. Update index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Update header container
c = c.replace(
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">',
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between relative">'
)

# Nav centered with flex justify-center or relative alignment
c = c.replace(
    '<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-white/90 drop-shadow">',
    '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold text-white/90 drop-shadow absolute left-1/2 -translate-x-1/2">'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

# 2. Update Header.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'r', encoding='utf-8') as f:
    hc = f.read()

hc = hc.replace(
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-20">',
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-20 relative">'
)
hc = hc.replace(
    '<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold">',
    '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold absolute left-1/2 -translate-x-1/2">'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(hc)

# 3. Update all other .astro pages having header tags (a-propos, contact, destinations, tours)
all_astro = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)
for fpath in all_astro:
    if fpath.endswith('Header.astro') or fpath.endswith('index.astro'):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    content = content.replace(
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-20">',
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-20 relative">'
    )
    content = content.replace(
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">',
        '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between relative">'
    )
    content = content.replace(
        '<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold',
        '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold absolute left-1/2 -translate-x-1/2'
    )
    content = content.replace(
        '<nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-xs sm:text-sm font-bold',
        '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold absolute left-1/2 -translate-x-1/2'
    )

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Centered header nav in {fpath.split('/')[-1]}")

print("Done centering header navigation bar perfectly across the whole website!")
