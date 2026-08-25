with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace with the authentic rafting on the wild river photo: /assets/original_site/rafting_wild.webp
c = c.replace(
    'src="/assets/drive_photos/adrien_bardia_river.webp"',
    'src="/assets/original_site/rafting_wild.webp"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced card 4 photo with authentic river rafting photo: /assets/original_site/rafting_wild.webp!")
