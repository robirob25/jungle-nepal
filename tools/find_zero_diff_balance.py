import json, itertools

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Pool of 21 photos
pool = items[:21]

# Let's see: can we find 3 columns of 7 photos where aspect ratios match?
# Let's inspect the aspects of the 21 items:
# Standard aspect values in this pool:
# 16:9 = 0.5625 (9/16)
# 3:2 = 0.6660 (2/3)
# 4:3 (approx 731/1024) = 0.7139
# 3:4 (approx 1024/768) = 1.3333
# 4:5 (approx 1024/819) = 1.2503
# 2:3 (approx 1024/682) = 1.5015
# 9:16 = 1.7778 (16/9)
# 9:16 vertical = 1.7809

# Let's run a fast solver over permutations
indices = list(range(21))
best_diff = 999
best_sol = None

for c1 in itertools.combinations(indices, 7):
    rem = [i for i in indices if i not in c1]
    s1 = sum(pool[i]['aspect'] for i in c1)
    for c2 in itertools.combinations(rem, 7):
        c3 = [i for i in rem if i not in c2]
        s2 = sum(pool[i]['aspect'] for i in c2)
        s3 = sum(pool[i]['aspect'] for i in c3)
        diff = max(s1, s2, s3) - min(s1, s2, s3)
        if diff < best_diff:
            best_diff = diff
            best_sol = (c1, c2, c3, s1, s2, s3)
            if diff < 0.005:
                break
    if best_diff < 0.005:
        break

c1, c2, c3, s1, s2, s3 = best_sol
print(f"Absolute best diff: {best_diff:.5f}")
print(f"Col 1: {s1:.4f}")
for i in c1:
    print(f" - {pool[i]['title']} ({pool[i]['aspect']:.4f})")
print(f"Col 2: {s2:.4f}")
for i in c2:
    print(f" - {pool[i]['title']} ({pool[i]['aspect']:.4f})")
print(f"Col 3: {s3:.4f}")
for i in c3:
    print(f" - {pool[i]['title']} ({pool[i]['aspect']:.4f})")

