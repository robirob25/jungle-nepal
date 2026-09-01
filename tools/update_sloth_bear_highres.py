with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Update Ours lippu in gallery to use the authentic 621KB HD photo directly:
c = c.replace(
    'src="/assets/curated_gallery/ours_lippu_sloth_bear.webp"',
    'src="/assets/drive_wildlife/Ours_lippu_1.webp"'
)

c = c.replace(
    '{"file": "/assets/curated_gallery/ours_lippu_sloth_bear.webp"',
    '{"file": "/assets/drive_wildlife/Ours_lippu_1.webp"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated Sloth Bear in gallery to the full HD drive photo (/assets/drive_wildlife/Ours_lippu_1.webp)!")
