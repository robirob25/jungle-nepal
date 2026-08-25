import json, os
from PIL import Image

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public'

for i in items:
    p = os.path.join(base_dir, i['file'].lstrip('/'))
    if os.path.exists(p):
        im = Image.open(p)
        i['aspect'] = im.size[1] / float(im.size[0])
        i['w'], i['h'] = im.size

# Let's inspect all candidate photos in items:
for idx, i in enumerate(items[:30]):
    print(f"{idx+1}. {i['title']}: aspect={i['aspect']:.4f} ({i['w']}x{i['h']}) [{i['category']}]")

