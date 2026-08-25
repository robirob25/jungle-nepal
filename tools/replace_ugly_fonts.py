with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Replace Cinzel & Syne with top-tier premium Google Fonts (Marcellus, Great Vibes, Kaushan Script, Playfair, Italiana)
font_link_old = '<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Caveat:wght@700&family=Cinzel:wght@700;900&family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Dancing+Script:wght@700&family=DM+Serif+Display:ital@0;1&family=Fraunces:ital,opsz,wght@1,9..144,700;1,9..144,900&family=Lobster+Two:ital,wght@1,700&family=Newsreader:ital,opsz,wght@0,6..72,400..800;1,6..72,400..800&family=Pacifico&family=Playfair+Display:ital,wght@1,700;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Satisfy&family=Syne:wght@800&display=swap" rel="stylesheet">'

font_link_new = '<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Caveat:wght@700&family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Dancing+Script:wght@700&family=DM+Serif+Display:ital@0;1&family=Fraunces:ital,opsz,wght@1,9..144,700;1,9..144,900&family=Great+Vibes&family=Italiana&family=Kaushan+Script&family=Lobster+Two:ital,wght@1,700&family=Marcellus&family=Pacifico&family=Playfair+Display:ital,wght@1,700;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Satisfy&display=swap" rel="stylesheet">'

layout = layout.replace(font_link_old, font_link_new)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
print("✓ Updated font imports in Layout.astro")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 10 elite, elegant & expressive fonts (All clean lowercase-compatible, no stretched squished caps)
old_font_list = """    var fontStyles = [
      { name: "'Caveat', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "0.98em" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", color: "#09422b", size: "0.88em" },
      { name: "'Pacifico', cursive", style: "normal", weight: "400", color: "#047857", size: "0.75em" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", color: "#065f46", size: "0.88em" },
      { name: "'Dancing Script', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "0.92em" },
      { name: "'Syne', sans-serif", style: "normal", weight: "800", color: "#022c22", size: "0.80em" },
      { name: "'Abril Fatface', serif", style: "normal", weight: "400", color: "#046c4e", size: "0.80em" },
      { name: "'Satisfy', cursive", style: "normal", weight: "400", color: "#059669", size: "0.88em" },
      { name: "'Cinzel', serif", style: "normal", weight: "900", color: "#064e3b", size: "0.74em" },
      { name: "'Lobster Two', cursive", style: "italic", weight: "700", color: "#0e5c3e", size: "0.88em" }
    ];"""

new_font_list = """    var fontStyles = [
      { name: "'Caveat', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "0.98em" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", color: "#09422b", size: "0.88em" },
      { name: "'Pacifico', cursive", style: "normal", weight: "400", color: "#047857", size: "0.75em" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", color: "#065f46", size: "0.88em" },
      { name: "'Dancing Script', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "0.92em" },
      { name: "'Great Vibes', cursive", style: "normal", weight: "400", color: "#0b5337", size: "0.95em" },
      { name: "'Kaushan Script', cursive", style: "normal", weight: "400", color: "#046c4e", size: "0.82em" },
      { name: "'Satisfy', cursive", style: "normal", weight: "400", color: "#059669", size: "0.88em" },
      { name: "'Cormorant Garamond', serif", style: "italic", weight: "700", color: "#064e3b", size: "0.92em" },
      { name: "'Lobster Two', cursive", style: "italic", weight: "700", color: "#0e5c3e", size: "0.88em" }
    ];"""

c = c.replace(old_font_list, new_font_list)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced Syne and Cinzel with Great Vibes and Kaushan Script!")
