with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Revert hero container height back to the full-screen cinematic height:
c = c.replace(
    'class="relative min-h-[80vh] sm:min-h-[88vh] lg:min-h-[90vh] flex flex-col justify-between items-center pt-32 sm:pt-36 lg:pt-40 pb-6 sm:pb-8 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950"',
    'class="relative min-h-[92vh] sm:min-h-screen flex flex-col justify-between items-center pt-36 sm:pt-40 lg:pt-44 pb-6 sm:pb-8 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950"'
)

c = c.replace('class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100"', 'class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100 scale-100"')
c = c.replace('class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 pointer-events-none"', 'class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none"')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Reverted hero section back to the previous full-height setup!")
