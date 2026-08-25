with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

old_heading = """        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">
          Ceux qui vous ouvrent les portes <span class="font-serif italic font-normal text-[#0e8354]">du Teraï</span>
        </h2>"""

new_heading = """        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">
          Ceux qui vous ouvrent les portes <span class="font-serif italic font-normal text-[#0e8354]">du Népal</span>
        </h2>"""

c = c.replace(old_heading, new_heading)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced 'du Teraï' by 'du Népal' in pisteurs section heading!")
