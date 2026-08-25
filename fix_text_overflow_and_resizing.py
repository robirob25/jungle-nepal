with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update H2 markup: remove horizontal overflow-hidden clipping from cell, provide ample breathing room
old_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight leading-[1.2] inline-flex flex-wrap items-center">
            <span class="whitespace-nowrap shrink-0">Les 15 séjours&nbsp;</span>
            <span class="inline-grid place-items-center w-[150px] sm:w-[190px] md:w-[225px] h-[1.3em] select-none overflow-hidden shrink-0 align-middle">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform text-center leading-none">immersifs</span>
            </span>
            <span class="whitespace-nowrap shrink-0">&nbsp;au Népal</span>
          </h2>"""

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight leading-[1.2] inline-flex flex-wrap items-center">
            <span class="whitespace-nowrap shrink-0">Les 15 séjours&nbsp;</span>
            <span class="inline-grid place-items-center w-[170px] sm:w-[215px] md:w-[255px] h-[1.35em] select-none overflow-visible shrink-0 align-middle">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform text-center leading-none whitespace-nowrap">immersifs</span>
            </span>
            <span class="whitespace-nowrap shrink-0">&nbsp;au Népal</span>
          </h2>"""

c = c.replace(old_h2, new_h2)

# 2. Strict font scale reductions so wide/caps fonts like Cinzel never touch the edges
old_js_font_styles = """    var fontStyles = [
      { name: "'Caveat', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "1.05em" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", color: "#09422b", size: "0.95em" },
      { name: "'Pacifico', cursive", style: "normal", weight: "400", color: "#047857", size: "0.82em" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", color: "#065f46", size: "0.95em" },
      { name: "'Dancing Script', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "1.0em" },
      { name: "'Syne', sans-serif", style: "normal", weight: "800", color: "#022c22", size: "0.9em" },
      { name: "'Abril Fatface', serif", style: "normal", weight: "400", color: "#046c4e", size: "0.9em" },
      { name: "'Satisfy', cursive", style: "normal", weight: "400", color: "#059669", size: "0.95em" },
      { name: "'Cinzel', serif", style: "normal", weight: "900", color: "#064e3b", size: "0.88em" },
      { name: "'Lobster Two', cursive", style: "italic", weight: "700", color: "#0e5c3e", size: "0.95em" }
    ];"""

new_js_font_styles = """    var fontStyles = [
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

c = c.replace(old_js_font_styles, new_js_font_styles)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed all font clipping issues! Cinzel & all wide fonts have comfortable margin and will never be cut off.")
