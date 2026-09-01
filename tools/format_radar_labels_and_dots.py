import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

dot_active = '<span class="w-2.5 h-2.5 rounded-full bg-[#0e8354]"></span>'
dot_inactive = '<span class="w-2.5 h-2.5 rounded-full bg-slate-200"></span>'

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Standardize text labels to lowercase except first letter:
    # "Faune & pistage"
    # "Nature & aventure"
    # "Culture & vie locale"
    # "Relax & contemplation"
    # "Soirées & fête"
    # "Rythme & effort :"

    # Remove any leftover emojis like 🛕, 🎉, etc. inside the radar section:
    c = re.sub(r'<span>🛕</span>\s*', '', c)
    c = re.sub(r'<span>🎉</span>\s*', '', c)
    c = re.sub(r'<span>🥾</span>\s*', '', c)
    c = re.sub(r'<span>🏕️</span>\s*', '', c)
    c = re.sub(r'<span>🌿</span>\s*', '', c)
    c = re.sub(r'<span></span>\s*', '', c)

    c = re.sub(r'>\s*Faune\s*&\s*Pistage\s*<', '>Faune & pistage<', c)
    c = re.sub(r'>\s*Nature\s*&\s*Aventure\s*<', '>Nature & aventure<', c)
    c = re.sub(r'>\s*Culture\s*&\s*Vie\s*[Ll]ocale\s*<', '>Culture & vie locale<', c)
    c = re.sub(r'>\s*Relax\s*&\s*Contemplation\s*<', '>Relax & contemplation<', c)
    c = re.sub(r'>\s*Soirées\s*&\s*Fête\s*<', '>Soirées & fête<', c)
    c = re.sub(r'>\s*Soirée\s*&\s*Fête\s*<', '>Soirée & fête<', c)
    c = re.sub(r'>\s*Rythme\s*&\s*Effort\s*:\s*<', '>Rythme & effort :<', c)

    # 2. Rule: "Soirées & fête" must always have at least 1 dot (1 active dot + 4 inactive dots)
    # Pattern for 0 dots (5 inactive dots):
    pattern_soiree_0 = r'(Soirées? & fête.*?<div class="flex gap-1\.5">)' + r'(\s*<span class="w-2\.5 h-2\.5 rounded-full bg-slate-200"></span>){5}'
    replacement_soiree_1 = r'\1' + dot_active + dot_inactive * 4
    c = re.sub(pattern_soiree_0, replacement_soiree_1, c, flags=re.DOTALL)

    # 3. Rule: "Culture & vie locale" must always have at least 3 dots (3 active dots + 2 inactive dots) if currently less than 3
    pattern_culture_2 = r'(Culture & vie locale.*?<div class="flex gap-1\.5">)' + r'(\s*<span class="w-2\.5 h-2\.5 rounded-full bg-\[#0e8354\]"></span>){2}' + r'(\s*<span class="w-2\.5 h-2\.5 rounded-full bg-slate-200"></span>){3}'
    replacement_culture_3 = r'\1' + dot_active * 3 + dot_inactive * 2
    c = re.sub(pattern_culture_2, replacement_culture_3, c, flags=re.DOTALL)

    pattern_culture_1 = r'(Culture & vie locale.*?<div class="flex gap-1\.5">)' + r'(\s*<span class="w-2\.5 h-2\.5 rounded-full bg-\[#0e8354\]"></span>){1}' + r'(\s*<span class="w-2\.5 h-2\.5 rounded-full bg-slate-200"></span>){4}'
    c = re.sub(pattern_culture_1, replacement_culture_3, c, flags=re.DOTALL)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Updated radar typography and dots in {fpath.split('/')[-1]}")

print("Done updating radar section across all 15 tour pages!")
