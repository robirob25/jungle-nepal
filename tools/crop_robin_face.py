from PIL import Image

# banner_duo.webp contains Robin (left, caucasian) and Kiran (right, nepalese)
# Let's inspect size and crop Robin with circle transparency / portrait framing
img = Image.open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/banner_duo.webp')
w, h = img.size
print(f"Banner Duo size: {w}x{h}")

# Robin is on the left side of banner_duo (from x=0 to x=w*0.55)
# Let's crop his upper body / head portrait
# Robin's head and chest are roughly in: x: (0, int(w*0.55)), y: (0, int(h*0.75))
# Let's make a square 800x800 high-res portrait of Robin
bbox = (int(w * 0.05), int(h * 0.02), int(w * 0.52), int(h * 0.65))
robin_crop = img.crop(bbox)
robin_crop.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/robin_portrait.webp', 'WEBP', quality=95)
robin_crop.save('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/assets/robin_portrait.webp', 'WEBP', quality=95)
print("✓ Saved /assets/robin_portrait.webp successfully!")
