with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the heavy double-dark overlay with a balanced, clearly visible image
# Use high-res local asset or authentic URL with high opacity and luminous brightness

old_hero_bg = """    <div class="absolute inset-0 z-0">
      <img src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" alt="Tigre de Bardia" class="w-full h-full object-cover opacity-45 filter brightness-50 contrast-110"/>
      <div class="absolute inset-0 bg-slate-950/40"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/75 to-black/85"></div>
    </div>"""

new_hero_bg = """    <div class="absolute inset-0 z-0">
      <img src="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg" alt="Tigre de Bardia" class="w-full h-full object-cover opacity-75 filter brightness-85 contrast-105"/>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/40 to-slate-950/60"></div>
    </div>"""

c = c.replace(old_hero_bg, new_hero_bg)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Re-illuminated the tiger photo in destinations hub hero!")
