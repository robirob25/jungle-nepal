with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the non-existent /assets/drive_photos/adrien_enfants_ecole.webp with the authentic /assets/drive_photos/antoine_wild5.webp
# (which depicts local village children smiling on bicycles in Terai!)
c = c.replace(
    'src="/assets/drive_photos/adrien_enfants_ecole.webp"',
    'src="/assets/drive_photos/antoine_wild5.webp"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed card 4 image: using authentic local village children photo /assets/drive_photos/antoine_wild5.webp!")
