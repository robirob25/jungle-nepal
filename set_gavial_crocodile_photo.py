with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace card 4 image with the rare Gavial du Gange / Crocodile des rivières:
# /assets/curated_gallery/gavial_gange_nage_riviere.webp
c = c.replace(
    'src="/assets/original_site/rafting_wild.webp"',
    'src="/assets/curated_gallery/gavial_gange_nage_riviere.webp"'
)
c = c.replace(
    'alt="Expédition rivière et rafting"',
    'alt="Gavial du Gange rare nageant dans la rivière au Népal"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Set card 4 background photo to rare Gavial du Gange in river (/assets/curated_gallery/gavial_gange_nage_riviere.webp)!")
