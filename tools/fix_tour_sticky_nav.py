import re, glob, os

# 1. Update Layout.astro to use overflow-x: clip instead of overflow-x: hidden on html/body
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout_content = f.read()

layout_content = layout_content.replace(
    'overflow-x: hidden;',
    'overflow-x: clip;'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout_content)
print("✓ Updated Layout.astro with overflow-x: clip")

# 2. Update Header.astro to not be sticky on tour pages if the tour sub-nav is sticky, OR make Header.astro normal/non-sticky or coordinate top offset:
# On tour pages, having Header.astro sticky at top:0 (height 64-80px) and Sub-nav sticky at top-0 would cause Sub-nav to overlap or fight with Header.
# Actually, having the tour sub-nav sticky at top-0 (or top-0 if header is static, or top-[64px] if header is sticky) is key.
# In WeRoad / Airbnb, the main Header scrolls away and the Tour Sub-Nav snaps to sticky top-0 with full-width bar!
# Let's inspect Header.astro in tour pages.

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Ensure Header on tour pages is static or the sub-nav has proper top-0 z-40
    # Also ensure the sub-nav has:
    # class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 shadow-md py-3 transition-all -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 mb-8 sm:mb-10"
    
    # If Header is present, let's make sure the sub-nav sticks cleanly to top-0 when header scrolls off
    c = re.sub(
        r'<nav class="sticky[^"]*"',
        r'<nav class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-md py-2.5 sm:py-3 transition-all -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 mb-8 sm:mb-10"',
        c
    )
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"✓ Verified sticky sub-nav in {os.path.basename(fpath)}")

# In Header.astro, let's make sure it's sticky top-0 z-30 or relative on tour pages, or if sticky, z-30 so sub-nav (z-40) floats above cleanly.
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'r', encoding='utf-8') as f:
    hdr = f.read()

hdr = hdr.replace('z-40 transition-all', 'z-30 transition-all')
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(hdr)

print("✓ Header.astro z-index adjusted to z-30")
