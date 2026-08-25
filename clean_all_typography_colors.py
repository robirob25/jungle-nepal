import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    # Replace light green text on dark backgrounds with clean warm white / subtle slate or rich forest green
    # In dark containers (nav, footer, badges): text-emerald-300, text-emerald-400 -> text-emerald-100 or text-white/90 or text-slate-300
    c = c.replace('text-emerald-300', 'text-slate-200')
    c = c.replace('text-emerald-400', 'text-slate-200')
    c = c.replace('text-teal-300', 'text-slate-300')
    c = c.replace('text-green-300', 'text-slate-200')
    c = c.replace('text-green-400', 'text-slate-200')
    c = c.replace('text-lime-400', 'text-amber-100')
    c = c.replace('text-cyan-400', 'text-slate-200')
    c = c.replace('text-amber-200', 'text-amber-100')
    c = c.replace('hover:text-emerald-300', 'hover:text-white')
    c = c.replace('hover:text-emerald-400', 'hover:text-white')
    c = c.replace('hover:text-amber-200', 'hover:text-white')
    
    # In light containers: replace any accidental bright colors
    # Ensure brand green is strictly rich deep forest green #0e5c3e or #0e8354
    c = c.replace('text-[#00ff]', 'text-[#0e5c3e]')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print(f"✓ Harmonized all typography colors across {len(astro_files)} files!")
