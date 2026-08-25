with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/chitwan.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace duplicate rhino image with authentic Chitwan wildlife/nature photo:
# Image 0 is 68.png (rhino) and Image 3 is rhinoceros-Nepal.png (same rhino).
# Replace Image 3 with /assets/curated_gallery/crocodile_marais_rapti.webp or /assets/curated_gallery/calao_bicorne_canopee.webp

c = c.replace(
    'https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png',
    '/assets/curated_gallery/crocodile_marais_rapti.webp'
)
c = c.replace(
    'https://junglenepal.com/wp-content/uploads/2025/03/68.png',
    '/assets/original_site/chitwan_rhino.webp'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/chitwan.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed duplicate photo in Chitwan destination gallery!")
