import glob, re

# In index.astro and Header.astro, make the logo height generous (h-14 sm:h-16) and remove any drop-shadow
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    'class="h-12 sm:h-14 w-auto object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-300"',
    'class="h-14 sm:h-16 w-auto object-contain group-hover:scale-105 transition-transform duration-300"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated logo dimensions without shadow in index.astro!")
