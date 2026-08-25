import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Pattern 1: Dropdown sessions:
    # <div class="space-y-1.5">\s*<div class="flex items-center justify-between text-xs font-bold">\s*<label class="text-slate-700 uppercase tracking-wider text-\[11px\]">Prochaine session :</label>.*?</div>\s*<select.*?</select>\s*</div>
    c = re.sub(
        r'<div class="space-y-1\.5">\s*<div class="flex items-center justify-between text-xs font-bold">\s*<label class="text-slate-700 uppercase tracking-wider text-\[11px\]">Prochaine session\s*:?</label>.*?</div>\s*<select.*?</select>\s*</div>',
        '',
        c,
        flags=re.DOTALL
    )

    # Pattern 2: Date input field ("DATE DE DÉPART SOUHAITÉE :" / input date):
    # <div class="space-y-1.5">\s*<div class="flex items-center justify-between text-xs font-bold">\s*<label class="text-slate-700 uppercase tracking-wider text-\[10px\] sm:text-\[11px\]">Date de départ souhaitée\s*:?</label>.*?</div>\s*<input type="date".*?</div>
    c = re.sub(
        r'<div class="space-y-1\.5">\s*<div class="flex items-center justify-between text-xs font-bold">\s*<label[^>]*>Date de départ souhaitée\s*:?</label>.*?</div>\s*<div class="relative">\s*<input type="date".*?</div>\s*</div>',
        '',
        c,
        flags=re.DOTALL
    )
    
    # Catch any remaining Date/Prochaine session blocks before the primary CTA button
    c = re.sub(
        r'<!-- Departures Selector.*?-->\s*<div class="space-y-1\.5">.*?</div>\s*(?=<!-- Primary CTA Button)',
        '',
        c,
        flags=re.DOTALL
    )
    c = re.sub(
        r'<!-- Date Selector.*?-->\s*<div class="space-y-1\.5">.*?</div>\s*(?=<!-- Primary CTA Button)',
        '',
        c,
        flags=re.DOTALL
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Removed calendar / session selector in {fpath.split('/')[-1]}")

print("Done removing date/calendar session pickers across all tours!")
