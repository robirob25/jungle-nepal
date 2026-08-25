with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce top padding of #prochains-departs section:
# Change 'py-12 sm:py-16 lg:py-20' to 'pt-6 sm:pt-8 lg:pt-10 pb-16 sm:pb-20'
content = content.replace(
    '<section id="prochains-departs" class="scroll-mt-24 sm:scroll-mt-28 py-12 sm:py-16 lg:py-20 bg-[#faf8f5]">',
    '<section id="prochains-departs" class="scroll-mt-20 sm:scroll-mt-24 pt-6 sm:pt-8 lg:pt-10 pb-16 sm:pb-20 bg-[#faf8f5]">'
)

# 2. In filterTrips function, adjust scroll offset accordingly:
content = content.replace(
    'const headerOffset = (catBar ? catBar.offsetHeight : 70) + 20;',
    'const headerOffset = (catBar ? catBar.offsetHeight : 70) + 8;'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Spacing above 'Départs garantis' tightened cleanly!")
