from PIL import Image

im = Image.open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_dark.png')
bbox = im.getbbox()
print("logo_dark bounding box:", bbox)

# Expand bounding box by 20px on all sides for breathing room
w, h = im.size
pad = 20
crop_box = (
    max(0, bbox[0] - pad),
    max(0, bbox[1] - pad),
    min(w, bbox[2] + pad),
    min(h, bbox[3] + pad)
)
print("Crop box with padding:", crop_box)

cropped = im.crop(crop_box)
cropped.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_dark.png', 'PNG')
cropped.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_dark.webp', 'WEBP', quality=95)

# Also for white logo
im_w = Image.open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_cropped.png')
bbox_w = im_w.getbbox()
crop_box_w = (
    max(0, bbox_w[0] - pad),
    max(0, bbox_w[1] - pad),
    min(im_w.size[0], bbox_w[2] + pad),
    min(im_w.size[1], bbox_w[3] + pad)
)
cropped_w = im_w.crop(crop_box_w)
cropped_w.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_white.png', 'PNG')
cropped_w.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/logo_nav_white.webp', 'WEBP', quality=95)

print("Generated new unclipped logo_nav_dark and logo_nav_white!")
