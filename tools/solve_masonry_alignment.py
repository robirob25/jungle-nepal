import json, os
from PIL import Image

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Get aspect ratio (height / width) for all items
base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public'

for i in items:
    p = os.path.join(base_dir, i['file'].lstrip('/'))
    if os.path.exists(p):
        im = Image.open(p)
        i['aspect'] = im.size[1] / float(im.size[0]) # height / width
        i['w'], i['h'] = im.size
    else:
        i['aspect'] = 0.666

# In a 3-column CSS masonry layout, CSS distributes items into 3 columns such that column heights are balanced, OR it puts 1..k in col1, k+1..m in col2, m+1..N in col3.
# Let's see what CSS columns does: multi-column layout breaks content evenly across columns.
# If we have 21 items (7 per column), or if we use an explicit 3-column flex/grid where we place items into 3 columns, or if we balance the sequential heights!
print("First 20 items aspect ratios:")
total_aspect = 0
for idx, i in enumerate(items[:20]):
    print(f" {idx+1}. {i['title']} -> aspect={i['aspect']:.3f} ({i['w']}x{i['h']})")
    total_aspect += i['aspect']

print(f"Total aspect sum of 20 items: {total_aspect:.3f}")
print(f"Target per column: {total_aspect/3:.3f}")

