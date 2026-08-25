from PIL import Image
import os

src = Image.open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_cropped.png').convert('RGBA')
bbox = src.getbbox()
cropped = src.crop(bbox)

# Target height: 120px for razor-sharp retina display
aspect = cropped.width / cropped.height
target_h = 120
target_w = int(target_h * aspect)

resized = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

# 1. White / Light Gold logo for dark backgrounds (Hero headers)
white_logo = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))
for y in range(target_h):
    for x in range(target_w):
        r, g, b, a = resized.getpixel((x, y))
        if a > 20:
            # Clean crisp white with original alpha
            white_logo.putpixel((x, y), (255, 255, 255, a))

# 2. Dark Green / Slate logo for light backgrounds (Tour detail headers)
dark_logo = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))
for y in range(target_h):
    for x in range(target_w):
        r, g, b, a = resized.getpixel((x, y))
        if a > 20:
            # Deep rich jungle forest green #073021
            dark_logo.putpixel((x, y), (7, 48, 33, a))

white_logo.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_white.png', 'PNG')
dark_logo.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_dark.png', 'PNG')

print(f"Generated logo_nav_white.png and logo_nav_dark.png ({target_w}x{target_h})!")
