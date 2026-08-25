import re, glob, os

# 1. Update index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Replace WhatsApp Direct in desktop header
idx = idx.replace(
    '<span>WhatsApp Direct</span>',
    '<span>WhatsApp</span>'
)
idx = idx.replace(
    '<span>WhatsApp Direct (+33 6 95 41 32 27)</span>',
    '<span>WhatsApp (+33 6 95 41 32 27)</span>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)
print("✓ Updated index.astro")

# 2. Update Header.astro & all other pages
all_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    c = c.replace('WhatsApp Direct (+33 6 95 41 32 27)', 'WhatsApp (+33 6 95 41 32 27)')
    c = c.replace('WhatsApp Direct', 'WhatsApp')
    c = c.replace('WhatsApp direct', 'WhatsApp')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Updated WhatsApp text in {os.path.basename(fpath)}")

print("All WhatsApp buttons simplified to 'WhatsApp'!")
