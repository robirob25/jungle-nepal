import glob, os, re

dest_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/*.astro')
for f in dest_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    print("===", os.path.basename(f), "===")
    # find images in gallery
    imgs = re.findall(r'<img\s+src="([^"]+)"', content)
    for img in imgs[:8]:
        print("  -", img)
