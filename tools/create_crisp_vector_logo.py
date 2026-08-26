import os
from PIL import Image

src_path = '/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787762890754.png'
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets'

img = Image.open(src_path).convert('L')
pixels = img.load()
w, h = img.size

# High quality clean alpha thresholding with smooth edge anti-aliasing
img_white = Image.new('RGBA', (w, h), (255, 255, 255, 0))
img_dark = Image.new('RGBA', (w, h), (4, 29, 19, 0))
pix_white = img_white.load()
pix_dark = img_dark.load()

for y in range(h):
    for x in range(w):
        val = pixels[x, y]
        if val > 60:
            # Smoothly calculate alpha
            if val >= 180:
                alpha = 255
            else:
                alpha = int(((val - 60) / (180 - 60)) * 255)
            pix_white[x, y] = (255, 255, 255, alpha)
            pix_dark[x, y] = (4, 29, 19, alpha)

bbox = img_white.getbbox()
if bbox:
    img_white = img_white.crop(bbox)
    img_dark = img_dark.crop(bbox)

for d in [dest_dir, '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/assets']:
    if os.path.exists(d):
        img_white.save(os.path.join(d, 'logo_nav_white.webp'), 'WEBP', quality=100)
        img_white.save(os.path.join(d, 'logo.png'), 'PNG')
        img_white.save(os.path.join(d, 'logo_nav_white.png'), 'PNG')
        img_dark.save(os.path.join(d, 'logo_nav_dark.webp'), 'WEBP', quality=100)
        img_dark.save(os.path.join(d, 'logo_dark.png'), 'PNG')
        img_dark.save(os.path.join(d, 'logo_nav_dark.png'), 'PNG')

print("✓ Created clean, perfectly rasterized anti-aliased logo!")
