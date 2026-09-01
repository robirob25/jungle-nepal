import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Replace bare lucide.createIcons(); with safe guarded execution
    c = re.sub(
        r'^\s*lucide\.createIcons\(\);\s*$',
        '    if (typeof lucide !== \'undefined\' && lucide && lucide.createIcons) { lucide.createIcons(); }',
        c,
        flags=re.MULTILINE
    )

    # In index.astro replace leftover data-lucide tags with direct inline SVGs
    c = c.replace('<i data-lucide="external-link" class="w-4 h-4 text-slate-400"></i>', '<svg class="w-4 h-4 text-slate-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>')
    c = c.replace('<i data-lucide="x" class="w-5 h-5"></i>', '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>')
    c = c.replace('<i data-lucide="sparkles" class="w-5 h-5"></i>', '<svg class="w-5 h-5 text-amber-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.4 7.2L22 12l-7.6 2.8L12 22l-2.4-7.2L2 12l7.6-2.8z"></path></svg>')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Fixed lucide guards in {fpath.split('/')[-1]}")

print("Done guarding all Lucide calls across the whole site!")
