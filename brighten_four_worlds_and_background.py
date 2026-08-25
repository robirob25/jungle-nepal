with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Brighten the global section background (increase image opacity to 55% and remove heavy black overlay)
c = c.replace(
    'class="w-full h-full object-cover opacity-30 scale-105 filter brightness-75 contrast-110"',
    'class="w-full h-full object-cover opacity-55 scale-105 filter brightness-95 contrast-100"'
)
c = c.replace(
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/80 to-slate-950/90"></div>',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/40 to-slate-950/70"></div>'
)

# 2. Brighten all 4 card background photos:
# Increase image opacity from 45% to 75% and brightness from 75 to 95/100
# Soften gradient to transparent
c = c.replace(
    'class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-45 filter brightness-75"',
    'class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-75 filter brightness-95 contrast-105"'
)

c = c.replace(
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/70 to-slate-950/40"></div>',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/50 to-slate-950/20"></div>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Brightened all 4 card photos and section background in a-propos.astro!")
