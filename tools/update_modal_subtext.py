with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

old_p = """            <p class="text-[11px] text-center text-slate-400 mt-2 font-medium">
              🔒 Réponse et devis personnalisés sans engagement sous 24h par Robin.
            </p>"""

new_p = """            <p class="text-[11px] text-center text-slate-400 mt-2 font-medium">
              Devis personnalisés sous 48h
            </p>"""

c = c.replace(old_p, new_p)

# Also in the success state inside Layout.astro
c = c.replace("vous recontacteront sous 24h", "vous recontacteront sous 48h")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated modal subtitle to 'Devis personnalisés sous 48h'!")
