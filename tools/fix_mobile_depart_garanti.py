with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the paragraph tag with a sleek, ultra-responsive single-line badge style:
c = c.replace(
    """          <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
            Départs garantis • Petits groupes de4 à 10 explorateurs
          </p>""",
    """          <p class="text-[9.5px] sm:text-xs font-black tracking-wider sm:tracking-widest uppercase text-[#0e8354] mb-2 whitespace-nowrap overflow-hidden text-ellipsis">
            Départs garantis • Petits groupes de 4 à 10 explorateurs
          </p>"""
)

# Also check for standard text match without line breaks if any
c = c.replace(
    '<p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">\n            Départs garantis • Petits groupes de 4 à 10 explorateurs\n          </p>',
    '<p class="text-[9.5px] sm:text-xs font-black tracking-wider sm:tracking-widest uppercase text-[#0e8354] mb-2 whitespace-nowrap overflow-hidden text-ellipsis">\n            Départs garantis • Petits groupes de 4 à 10 explorateurs\n          </p>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed 'Départs garantis' mobile typography to be smaller and on a single line!")
