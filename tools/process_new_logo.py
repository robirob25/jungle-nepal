import os
from PIL import Image, ImageOps

src_path = '/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787762724088.png'
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets'

# Load the uploaded logo image (white silhouette with mountain and tiger on black background)
img = Image.open(src_path).convert('RGBA')

# 1. Create transparent White Logo (for dark headers, footers & hero overlay)
# The uploaded image is white graphics on pure black background.
# Convert black pixels to transparent alpha:
datas = img.getdata()
new_data_white = []
new_data_dark = [] # Deep forest green/dark slate for light headers (#041d13 or #0e5c3e)

for item in datas:
    # item is (r, g, b, a)
    # Brightness / luminance
    brightness = (item[0] + item[1] + item[2]) / 3
    if brightness < 35:
        # Black background -> transparent
        new_data_white.append((255, 255, 255, 0))
        new_data_dark.append((4, 29, 19, 0))
    else:
        # White graphics -> crisp white with anti-aliasing alpha
        alpha = int(min(255, brightness * 1.2))
        new_data_white.append((255, 255, 255, alpha))
        # Dark green / slate (#041d13)
        new_data_dark.append((4, 29, 19, alpha))

img_white = Image.new('RGBA', img.size)
img_white.putdata(new_data_white)

# Crop tight bounding box
bbox_white = img_white.getbbox()
if bbox_white:
    img_white = img_white.crop(bbox_white)

img_dark = Image.new('RGBA', img.size)
img_dark.putdata(new_data_dark)
if bbox_white:
    img_dark = img_dark.crop(bbox_white)

# Save to public/assets/ with various formats and fallbacks
# White logos (for dark backgrounds / hero / footer)
img_white.save(os.path.join(dest_dir, 'logo_nav_white.webp'), 'WEBP', quality=100)
img_white.save(os.path.join(dest_dir, 'logo.png'), 'PNG')
img_white.save(os.path.join(dest_dir, 'logo_nav_white.png'), 'PNG')

# Dark logos (for light backgrounds / white navbar)
img_dark.save(os.path.join(dest_dir, 'logo_nav_dark.webp'), 'WEBP', quality=100)
img_dark.save(os.path.join(dest_dir, 'logo_dark.png'), 'PNG')
img_dark.save(os.path.join(dest_dir, 'logo_nav_dark.png'), 'PNG')

# Also copy to dist if dist exists
dist_assets = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/assets'
if os.path.exists(dist_assets):
    img_white.save(os.path.join(dist_assets, 'logo_nav_white.webp'), 'WEBP', quality=100)
    img_white.save(os.path.join(dist_assets, 'logo.png'), 'PNG')
    img_dark.save(os.path.join(dist_assets, 'logo_nav_dark.webp'), 'WEBP', quality=100)
    img_dark.save(os.path.join(dist_assets, 'logo_dark.png'), 'PNG')

print(f"✓ Processed and exported new logo: White ({img_white.size}) & Dark ({img_dark.size}) transparent assets!")
