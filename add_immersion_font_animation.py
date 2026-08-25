with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# 1. Add 10 diverse, high-character Google Fonts to Layout.astro
font_link_old = '<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..800;1,6..72,400..800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'

font_link_new = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Cormorant+Garamond:ital,wght@1,600;1,700&family=DM+Serif+Display:ital@0;1&family=Fraunces:ital,opsz,wght@1,9..144,700;1,9..144,900&family=Monoton&family=Newsreader:ital,opsz,wght@0,6..72,400..800;1,6..72,400..800&family=Outfit:wght@800;900&family=Playfair+Display:ital,wght@1,700;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@700&family=Syne:wght@800&family=UnifrakturMaguntia&family=Borel&family=Rock+Salt&display=swap" rel="stylesheet">'

layout = layout.replace(font_link_old, font_link_new)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
print("✓ Added 10 fonts to Layout.astro")

# 2. Update index.astro title to wrap "immersifs" in animated span and add kinetic font morph script
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Replace H2 in index.astro
old_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight transition-all duration-300">
            Les 15 séjours immersifs au Népal
          </h2>"""

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight transition-all duration-300 flex flex-wrap items-baseline gap-x-2.5 sm:gap-x-3.5">
            <span>Les 15 séjours</span>
            <span id="animated-immersion-word" class="inline-block text-[#0e5c3e] transition-all duration-300 transform font-normal min-w-[170px] sm:min-w-[220px] text-left select-none">immersifs</span>
            <span>au Népal</span>
          </h2>"""

idx = idx.replace(old_h2, new_h2)

# Add kinetic font cycler JS at bottom of index.astro
morph_script = """
<script is:inline>
  // Dynamic 10-Font Kinetic Animation for the word "immersifs"
  (function() {
    const fonts = [
      { name: "'Plus Jakarta Sans', sans-serif", style: "normal", weight: "900", color: "#0e5c3e", size: "1em", letterSpacing: "-0.03em" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", color: "#0a4d33", size: "1.08em", letterSpacing: "-0.01em" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", color: "#14532d", size: "1.06em", letterSpacing: "0.01em" },
      { name: "'Space Grotesk', sans-serif", style: "normal", weight: "700", color: "#064e3b", size: "0.98em", letterSpacing: "-0.04em" },
      { name: "'Cormorant Garamond', serif", style: "italic", weight: "700", color: "#047857", size: "1.18em", letterSpacing: "0.02em" },
      { name: "'Syne', sans-serif", style: "normal", weight: "800", color: "#065f46", size: "0.95em", letterSpacing: "-0.02em" },
      { name: "'DM Serif Display', serif", style: "italic", weight: "400", color: "#046c4e", size: "1.08em", letterSpacing: "0" },
      { name: "'Cinzel', serif", style: "normal", weight: "900", color: "#064e3b", size: "0.94em", letterSpacing: "0.05em" },
      { name: "'Outfit', sans-serif", style: "normal", weight: "900", color: "#0e5c3e", size: "1.02em", letterSpacing: "-0.03em" },
      { name: "'Newsreader', serif", style: "italic", weight: "700", color: "#059669", size: "1.12em", letterSpacing: "-0.01em" }
    ];

    let currentFontIndex = 0;
    const el = document.getElementById('animated-immersion-word');

    if (!el) return;

    function cycleFont() {
      currentFontIndex = (currentFontIndex + 1) % fonts.length;
      const f = fonts[currentFontIndex];

      // Subtle scale-fade transition
      el.style.opacity = '0.3';
      el.style.transform = 'translateY(-2px) scale(0.97)';

      setTimeout(() => {
        el.style.fontFamily = f.name;
        el.style.fontStyle = f.style;
        el.style.fontWeight = f.weight;
        el.style.color = f.color;
        el.style.fontSize = f.size;
        el.style.letterSpacing = f.letterSpacing;
        el.style.opacity = '1';
        el.style.transform = 'translateY(0) scale(1)';
      }, 120);
    }

    // Morph typography every 1.8 seconds with smooth easing
    setInterval(cycleFont, 1800);
  })();
</script>
"""

# Insert script before </body> or </Layout>
if "</Layout>" in idx:
    idx = idx.replace("</Layout>", morph_script + "\n</Layout>")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Successfully injected 10-font morph animation for 'immersifs'!")
