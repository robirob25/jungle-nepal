from PIL import Image

im_dark = Image.open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_dark.png').convert('RGBA')
bbox = im_dark.getbbox()
print("logo_dark bbox:", bbox)

# Expand bounding box with 30px padding on all sides
pad = 30
crop_box = (
    max(0, bbox[0] - pad),
    max(0, bbox[1] - pad),
    min(im_dark.size[0], bbox[2] + pad),
    min(im_dark.size[1], bbox[3] + pad)
)
print("Crop box:", crop_box)

# 1. Dark cropped version
dark_cropped = im_dark.crop(crop_box)
dark_cropped.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_dark.png', 'PNG')
dark_cropped.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_dark.webp', 'WEBP', quality=95)

# 2. White version generated from the exact same unclipped geometry:
# Turn all visible non-transparent pixels into crisp white (255, 255, 255) with their original alpha!
r, g, b, a = dark_cropped.split()
white_img = Image.new('RGB', dark_cropped.size, (255, 255, 255))
white_logo = Image.merge('RGBA', (white_img.split()[0], white_img.split()[1], white_img.split()[2], a))

white_logo.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_white.png', 'PNG')
white_logo.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_white.webp', 'WEBP', quality=95)

print("Generated pristine, 100% unclipped logo_nav_white and logo_nav_dark!")
