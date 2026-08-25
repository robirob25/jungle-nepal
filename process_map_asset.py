import shutil, os
from PIL import Image

src_img = "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787504898974.png"
dest_png = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/map_nepal_wildlife.png"
dest_webp = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/map_nepal_wildlife.webp"

im = Image.open(src_img)
print(f"Original map size: {im.size}, format: {im.format}, mode: {im.mode}")

# Save PNG
im.save(dest_png, format="PNG", optimize=True)

# Save WebP for ultra-fast loading
if im.mode in ('RGBA', 'LA'):
    im.save(dest_webp, format="WEBP", quality=95, method=6)
else:
    im.convert('RGB').save(dest_webp, format="WEBP", quality=95, method=6)

print("Saved map asset to public/assets/map_nepal_wildlife.webp and .png")
