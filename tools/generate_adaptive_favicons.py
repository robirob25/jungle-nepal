from PIL import Image
import os

src_path = '/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787403940695.png'
im = Image.open(src_path).convert('RGBA')
width, height = im.size

# Extract alpha mask of the silhouette
# The silhouette is the non-white / colored pixels
datas = im.getdata()

# Find bounding box of the logo
min_x, min_y, max_x, max_y = width, height, 0, 0
mask = []

for y in range(height):
    for x in range(width):
        r, g, b, a = im.getpixel((x, y))
        # If it's not pure transparent/white background (detect the gold/khaki silhouette)
        # Background is white (255, 255, 255) or transparent
        if a > 30 and (r < 240 or g < 240 or b < 240):
            # It's part of the silhouette
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print(f"Original: {width}x{height}, Bounding box: ({min_x}, {min_y}) to ({max_x}, {max_y})")

# Crop tight with small padding
pad = 10
crop_box = (max(0, min_x - pad), max(0, min_y - pad), min(width, max_x + pad), min(height, max_y + pad))
cropped = im.crop(crop_box)
cw, ch = cropped.size

# Make a square image
max_dim = max(cw, ch)
sq_crop = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
offset = ((max_dim - cw) // 2, (max_dim - ch) // 2)
sq_crop.paste(cropped, offset)

# Generate Dark Favicon (Deep jungle black #041d13 / #0a0a0a for light browser)
dark_fav = Image.new('RGBA', sq_crop.size, (0, 0, 0, 0))
for y in range(sq_crop.size[1]):
    for x in range(sq_crop.size[0]):
        r, g, b, a = sq_crop.getpixel((x, y))
        if a > 30 and (r < 240 or g < 240 or b < 240):
            # Fill with dark slate/black #0b1912 with high opacity
            dark_fav.putpixel((x, y), (11, 25, 18, int(a * 1.0)))

# Generate Light Favicon (Pure White #ffffff / Light Gold for dark browser)
light_fav = Image.new('RGBA', sq_crop.size, (0, 0, 0, 0))
for y in range(sq_crop.size[1]):
    for x in range(sq_crop.size[0]):
        r, g, b, a = sq_crop.getpixel((x, y))
        if a > 30 and (r < 240 or g < 240 or b < 240):
            # Fill with crisp white #ffffff
            light_fav.putpixel((x, y), (255, 255, 255, int(a * 1.0)))

# Resize and save to public/ and root
dest_dirs = [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'
]

sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (180, 180), (192, 192), (512, 512)]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)
    
    # Save standard PNGs
    dark_fav.resize((512, 512), Image.Resampling.LANCZOS).save(os.path.join(d, 'favicon-dark.png'), 'PNG')
    light_fav.resize((512, 512), Image.Resampling.LANCZOS).save(os.path.join(d, 'favicon-light.png'), 'PNG')
    
    # 32x32 versions
    dark_fav.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(d, 'favicon-32x32.png'), 'PNG')
    light_fav.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(d, 'favicon-32x32-light.png'), 'PNG')
    
    # Apple Touch Icon
    dark_fav.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(d, 'apple-touch-icon.png'), 'PNG')
    
    # Default favicon.ico (multi-size ICO)
    dark_fav.save(os.path.join(d, 'favicon.ico'), format='ICO', sizes=[(16,16), (32,32), (48,48)])
    dark_fav.save(os.path.join(d, 'favicon.png'), 'PNG')

print("✓ Successfully generated favicon-dark.png, favicon-light.png, apple-touch-icon.png, and favicon.ico!")
