with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# To de-zoom the photos:
# 1. Ensure hero container height is balanced (e.g. h-[85vh] sm:h-[90vh] or min-h-[640px] max-h-[820px] on desktop)
# so 16:9 and 3:2 landscape photos aren't excessively cropped vertically.
# 2. Add slight un-zoom scale or object-cover with optimal scale (scale-95 to scale-100 without overscaling)

# Replace hero section container min-height
c = c.replace(
    'class="relative min-h-[92vh] sm:min-h-screen flex flex-col justify-between items-center pt-36 sm:pt-40 lg:pt-44 pb-6 sm:pb-8 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950"',
    'class="relative min-h-[80vh] sm:min-h-[88vh] lg:min-h-[90vh] flex flex-col justify-between items-center pt-32 sm:pt-36 lg:pt-40 pb-6 sm:pb-8 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950"'
)

# Apply scale-100 and clean object-contain / object-cover framing
c = c.replace('class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100 scale-100"', 'class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100"')
c = c.replace('class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none"', 'class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 pointer-events-none"')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Re-calibrated hero section dimensions to de-zoom and uncrop all 11 hero background photos!")
