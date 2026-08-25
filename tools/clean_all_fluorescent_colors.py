import glob, re

# All source files
astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# Replacements:
# Fluorescent green text: text-[#10b981], text-emerald-400, text-emerald-300, text-teal-400 -> text-[#0e8354] (on light) or text-emerald-300/text-slate-200 / text-amber-200/90
# Fluorescent borders: border-emerald-500/30, border-emerald-400/40, border-[#10b981] -> border-emerald-800/40 or border-white/10
# Fluorescent badge backgrounds: bg-emerald-500/20, bg-emerald-400/20 -> bg-emerald-900/40 (on dark) or bg-emerald-50 (on light)
# Fluorescent amber: text-amber-300 -> text-amber-200, hover:text-amber-300 -> hover:text-amber-200

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    # Replace fluorescent green text
    c = c.replace('text-[#10b981]', 'text-emerald-300')
    c = c.replace('text-emerald-400', 'text-emerald-300')
    c = c.replace('text-teal-400', 'text-slate-300')
    c = c.replace('bg-emerald-500/20', 'bg-white/10')
    c = c.replace('border-emerald-500/30', 'border-white/10')
    c = c.replace('border-emerald-400/40', 'border-white/10')
    c = c.replace('hover:text-amber-300', 'hover:text-amber-200')
    c = c.replace('text-amber-300', 'text-amber-200')
    
    # Specific map pins and cards in index.astro
    # Replace fluorescent badges on the map:
    # bg-emerald-500/20 text-[#10b981] -> bg-emerald-950/60 text-emerald-200 border-emerald-800/50
    c = re.sub(r'border-emerald-500/(\d+)', r'border-emerald-800/\1', c)
    c = re.sub(r'bg-emerald-500/(\d+)', r'bg-emerald-900/\1', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print(f"✓ Cleaned fluorescent colors across {len(astro_files)} files!")
