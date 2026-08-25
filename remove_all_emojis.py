import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# List of emoji characters used across the footer, nav menus, badges and cards
emojis_to_clean = [
    '🐅', '🦏', '🦌', '🏔️', '🏔', '🕉️', '🕉', '🇳🇵', '🏛️', '🏛', '📜', '📍', '🌿', '✨', '🐾', '🧭', '📖', '✉️', '⭐'
]

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    # 1. Clean explicit icon emojis in destinations list
    # e.g., <li><a href="/destinations/bardia.html">🐅 Parc national de Bardia</a></li> -> <li><a href="/destinations/bardia.html">Parc national de Bardia</a></li>
    for emoji in emojis_to_clean:
        c = c.replace(f'{emoji} ', '')
        c = c.replace(f'{emoji}', '')

    # 2. Clean any remaining standalone emoji spans
    # e.g., <span>🐅</span> or <div ...>🐅</div>
    c = re.sub(r'<span>[\s]*</span>', '', c)
    c = re.sub(r'<div[^>]*>[\s]*</div>', '', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print(f"✓ Stripped all emojis across {len(astro_files)} files!")
