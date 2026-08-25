with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Add -scale-x-100 (horizontal mirror) to the tiger image so it faces left towards the text
c = c.replace(
    'class="w-full h-[460px] object-cover"',
    'class="w-full h-[460px] object-cover -scale-x-100 transform"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Applied horizontal mirror flip (-scale-x-100) to tiger image in a-propos.astro!")
