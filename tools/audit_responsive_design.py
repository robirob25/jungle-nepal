import glob, re

pages = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

issues = []

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for hardcoded min-w or fixed widths that cause horizontal scroll on mobile (< 375px)
    fixed_widths = re.findall(r'min-w-\[(\d+)px\]', content)
    for fw in fixed_widths:
        if int(fw) > 340:
            issues.append(f"High fixed min-w-[{fw}px] in {p.split('/')[-1]}")

    # Check for tables without overflow-x-auto
    if '<table' in content and 'overflow-x-auto' not in content:
        issues.append(f"Table without overflow wrapper in {p.split('/')[-1]}")

print("Responsive Audit Report:")
if not issues:
    print("✓ Zero breaking horizontal overflows found across all Astro files!")
else:
    for i in set(issues):
        print(f"- {i}")
