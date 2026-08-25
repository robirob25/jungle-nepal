import json, random

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Top 21 items
pool = items[:21]

best_diff = 999
best_sol = None

# Monte Carlo / Simulated Annealing search
for _ in range(500000):
    shuffled = random.sample(pool, 21)
    c1, c2, c3 = shuffled[0:7], shuffled[7:14], shuffled[14:21]
    s1 = sum(x['aspect'] for x in c1)
    s2 = sum(x['aspect'] for x in c2)
    s3 = sum(x['aspect'] for x in c3)
    diff = max(s1, s2, s3) - min(s1, s2, s3)
    if diff < best_diff:
        best_diff = diff
        best_sol = (c1, c2, c3, s1, s2, s3)
        if diff < 0.005:
            break

c1, c2, c3, s1, s2, s3 = best_sol
print(f"Best diff found in 500k iterations: {best_diff:.5f}")
print(f"Col 1 (height={s1:.4f}):")
for i in c1:
    print(f" - [{i['category']}] {i['title']} ({i['aspect']:.4f})")
print(f"Col 2 (height={s2:.4f}):")
for i in c2:
    print(f" - [{i['category']}] {i['title']} ({i['aspect']:.4f})")
print(f"Col 3 (height={s3:.4f}):")
for i in c3:
    print(f" - [{i['category']}] {i['title']} ({i['aspect']:.4f})")

