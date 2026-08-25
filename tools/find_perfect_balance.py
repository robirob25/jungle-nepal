import json, os, itertools

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# The 21 pool items
pool = items[:21]

best_score = 9999
best_cols = None

# We want 3 columns of 7 items each
indices = list(range(21))

for c1_idx in itertools.combinations(indices, 7):
    rem = [i for i in indices if i not in c1_idx]
    for c2_idx in itertools.combinations(rem, 7):
        c3_idx = [i for i in rem if i not in c2_idx]
        
        c1 = [pool[i] for i in c1_idx]
        c2 = [pool[i] for i in c2_idx]
        c3 = [pool[i] for i in c3_idx]
        
        h1 = sum(x['aspect'] for x in c1)
        h2 = sum(x['aspect'] for x in c2)
        h3 = sum(x['aspect'] for x in c3)
        
        # Check diff
        diff = max(h1, h2, h3) - min(h1, h2, h3)
        if diff < best_score:
            best_score = diff
            best_cols = (c1, c2, c3, h1, h2, h3)

c1, c2, c3, h1, h2, h3 = best_cols
print(f"Optimal balance found! Max difference: {best_score:.3f}")
print(f"Col 1 (7 items, height={h1:.3f}):")
for i in c1:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.3f})")
print(f"Col 2 (7 items, height={h2:.3f}):")
for i in c2:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.3f})")
print(f"Col 3 (7 items, height={h3:.3f}):")
for i in c3:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.3f})")

ordered_21 = c1 + c2 + c3
seen = set(i['file'] for i in ordered_21)
remaining = [i for i in items if i['file'] not in seen]
new_items = ordered_21 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(new_items, f, indent=2, ensure_ascii=False)

print("Saved perfectly balanced 21 photos gallery!")
