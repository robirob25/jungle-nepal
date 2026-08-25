import glob, os, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

old_pattern = re.compile(
    r'<a href="#programme" class="hover:text-\[#0e8354\] transition-colors whitespace-nowrap">Itinéraire</a>\s*'
    r'<a href="#inclusions" class="hover:text-\[#0e8354\] transition-colors whitespace-nowrap">Inclus</a>',
    re.MULTILINE
)

replacement = (
    '<a href="/index.html#concept" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">L\'esprit safari</a>\n'
    '          <a href="/index.html#pisteurs" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Maîtres pisteurs</a>'
)

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    new_c = old_pattern.sub(replacement, c)
    if new_c != c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Updated header nav in: {os.path.basename(fpath)}")
    else:
        print(f"Pattern not found in: {os.path.basename(fpath)}")

print("Done!")
