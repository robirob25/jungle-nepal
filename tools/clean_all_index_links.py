import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Replace /index.html# with /# or directly #
    c = c.replace('/index.html#', '/#')
    c = c.replace('/index.html', '/')
    c = c.replace('/index#', '/#')
    c = c.replace('/index', '/')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Cleaned index links in {fpath.split('/')[-1]}")

print("Done cleaning all index references across all pages!")
