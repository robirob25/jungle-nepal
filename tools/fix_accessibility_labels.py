with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix accessibility aria-label and name on select elements
c = c.replace(
    '<select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">',
    '<select id="search-dest" name="destination" aria-label="Choisir une destination ou un type de séjour" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">'
)

c = c.replace(
    '<select id="search-date" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer pr-6 appearance-none">',
    '<select id="search-date" name="date" aria-label="Choisir une période de départ" class="w-full bg-transparent font-extrabold text-sm sm:text-base text-slate-900 focus:outline-none cursor-pointer pr-6 appearance-none">'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed accessible name on select elements in index.astro!")
