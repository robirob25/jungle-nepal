import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

# Emoji list to strip out from UI elements across tour pages
emojis = ['🏕️', '⛺', '🥾', '🐆', '🐅', '🛕', '🎉', '🌿', '🔥', '🛡️', '🌟', '✨', '🐘', '🦏', '🦅', '🛶', '🧘', '🤝', '📸', '🌅', '🌲']

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    for e in emojis:
        c = c.replace(f'<span>{e}</span>', '')
        c = c.replace(f'<span> {e} </span>', '')
        c = c.replace(f'<span>{e} </span>', '')
        c = c.replace(e, '')

    # Clean empty spans
    c = c.replace('<span></span>', '')
    c = c.replace('<span> </span>', '')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Stripped emojis in {fpath.split('/')[-1]}")

print("Done cleaning all emojis across tour pages!")
