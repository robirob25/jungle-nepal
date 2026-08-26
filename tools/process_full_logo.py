import os
from PIL import Image

src_path = '/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787762890754.png'
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets'

img = Image.open(src_path).convert('RGBA')

# Convert black background to transparent:
# Black is close to rgb(0,0,0)
datas = list(img.getdata())
new_data_white = []
new_data_dark = [] # Deep forest slate/green #041d13

for item in datas:
    brightness = (item[0] + item[1] + item[2]) / 3
    if brightness < 30:
        new_data_white.append((255, 255, 255, 0))
        new_data_dark.append((4, 29, 19, 0))
    else:
        alpha = int(min(255, brightness * 1.25))
        # Pure crisp white for dark backgrounds / footer / transparent hero
        new_data_white.append((255, 255, 255, alpha))
        # Deep dark forest green (#041d13) for white/light navbar
        new_data_dark.append((4, 29, 19, alpha))

img_white = Image.new('RGBA', img.size)
img_white.putdata(new_data_white)
bbox_white = img_white.getbbox()
if bbox_white:
    img_white = img_white.crop(bbox_white)

img_dark = Image.new('RGBA', img.size)
img_dark.putdata(new_data_dark)
if bbox_white:
    img_dark = img_dark.crop(bbox_white)

# Save to public/assets/
img_white.save(os.path.join(dest_dir, 'logo_nav_white.webp'), 'WEBP', quality=100)
img_white.save(os.path.join(dest_dir, 'logo.png'), 'PNG')
img_white.save(os.path.join(dest_dir, 'logo_nav_white.png'), 'PNG')

img_dark.save(os.path.join(dest_dir, 'logo_nav_dark.webp'), 'WEBP', quality=100)
img_dark.save(os.path.join(dest_dir, 'logo_dark.png'), 'PNG')
img_dark.save(os.path.join(dest_dir, 'logo_nav_dark.png'), 'PNG')

# Also update dist/assets
dist_assets = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/assets'
if os.path.exists(dist_assets):
    img_white.save(os.path.join(dist_assets, 'logo_nav_white.webp'), 'WEBP', quality=100)
    img_white.save(os.path.join(dist_assets, 'logo.png'), 'PNG')
    img_dark.save(os.path.join(dist_assets, 'logo_nav_dark.webp'), 'WEBP', quality=100)
    img_dark.save(os.path.join(dist_assets, 'logo_dark.png'), 'PNG')

print(f"✓ Processed complete logo with typography: White ({img_white.size}) & Dark ({img_dark.size})")
