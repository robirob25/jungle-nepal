with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove the "L'histoire d'une alliance franco-népalaise" badge
old_badge = """      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-950/70 backdrop-blur-md border border-emerald-400/40 text-amber-300 text-xs font-black uppercase tracking-widest mb-6 shadow-xl">
        <span>🇳🇵 L'histoire d'une alliance franco-népalaise</span>
      </div>"""

c = c.replace(old_badge + "\n", "")
c = c.replace(old_badge, "")

# 2. Also clean the other pill badges in a-propos.astro to match the elegant clean typography
c = c.replace(
    """          <div class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wider text-[#0e8354] bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
            <span>Notre manifeste</span>
          </div>""",
    """          <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
            Notre manifeste
          </p>"""
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed 'L'histoire d'une alliance franco-népalaise' badge successfully!")
