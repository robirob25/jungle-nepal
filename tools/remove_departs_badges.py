import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# Regex to match the Départs 2026/2027 badge span
pattern = r'\s*<span class="inline-flex items-center gap-1\.5 text-\[11px\] font-bold text-\[#0e8354\] bg-emerald-50 px-2\.5 py-1 rounded-full border border-emerald-200/80">\s*<span class="w-1\.5 h-1\.5 rounded-full bg-\[#0e8354\]"></span>\s*<span>Départs 2026/2027</span>\s*</span>'

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    new_c = re.sub(pattern, '', c)

    # Also handle any variant spacing
    alt_pattern = r'\s*<span class="inline-flex items-center gap-1\.5 text-\[11px\] font-bold text-\[#0e8354\] bg-emerald-50 px-2\.5 py-1 rounded-full border border-emerald-200/80">.*?Départs 2026/2027.*?</span>'
    new_c = re.sub(alt_pattern, '', new_c, flags=re.DOTALL)

    if new_c != c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"✓ Removed Départs 2026/2027 badge in {fpath.split('/')[-1]}")

print("Done removing Départs 2026/2027 badge across all tour cards!")
