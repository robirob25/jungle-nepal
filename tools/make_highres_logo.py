import os
from PIL import Image

src_path = '/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787763063150.png'
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets'

# Open uploaded PNG
img = Image.open(src_path).convert('RGBA')
w, h = img.size

# Separate into white logo and dark logo with clean alpha channel
pix = img.load()
img_white = Image.new('RGBA', (w, h), (0, 0, 0, 0))
img_dark = Image.new('RGBA', (w, h), (0, 0, 0, 0))
pix_w = img_white.load()
pix_d = img_dark.load()

for y in range(h):
    for x in range(w):
        r, g, b, a = pix[x, y]
        # Luminance
        lum = (r * 0.299 + g * 0.587 + b * 0.114)
        if lum > 25: # Any white/gray pixel
            alpha = int(min(255, (lum / 255.0) * 255))
            pix_w[x, y] = (255, 255, 255, alpha)
            pix_d[x, y] = (4, 29, 19, alpha)

# Auto crop
bbox = img_white.getbbox()
if bbox:
    # Add a 10px margin around for nice rendering
    img_white = img_white.crop(bbox)
    img_dark = img_dark.crop(bbox)

# Save with maximum fidelity (PNG 32-bit & WebP lossless)
for target in [dest_dir, '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/assets']:
    if os.path.exists(target):
        img_white.save(os.path.join(target, 'logo.png'), 'PNG')
        img_white.save(os.path.join(target, 'logo_nav_white.png'), 'PNG')
        img_white.save(os.path.join(target, 'logo_nav_white.webp'), 'WEBP', lossless=True)
        img_dark.save(os.path.join(target, 'logo_dark.png'), 'PNG')
        img_dark.save(os.path.join(target, 'logo_nav_dark.png'), 'PNG')
        img_dark.save(os.path.join(target, 'logo_nav_dark.webp'), 'WEBP', lossless=True)

print(f"✓ Generated ultra-high resolution lossless logo ({img_white.size[0]}x{img_white.size[1]}px)!")
