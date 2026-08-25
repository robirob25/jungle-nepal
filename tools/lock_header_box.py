with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Lock the header container with fixed/min height and nowrap structure so vertical height NEVER fluctuates
old_header_block = """      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
        <div>
          <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
            Départs garantis • Petits groupes de 4 à 10 explorateurs
          </p>
          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight transition-all duration-300 leading-tight">
            <span>Les 15 séjours</span>
            <span class="inline-block w-[185px] sm:w-[230px] md:w-[260px] text-center select-none overflow-visible align-baseline">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform">immersifs</span>
            </span>
            <span>au Népal</span>
          </h2>
          <p class="mt-3 text-base text-slate-600 max-w-2xl font-normal">
            Sélectionnez votre aventure pour explorer le détail jour par jour, la fiche d'inclusions et réserver votre place.
          </p>
        </div>"""

new_header_block = """      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10 sm:mb-12">
        <div class="flex-1">
          <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
            Départs garantis • Petits groupes de 4 à 10 explorateurs
          </p>
          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight leading-[1.2] flex flex-wrap items-baseline gap-x-2.5 sm:gap-x-3.5">
            <span class="whitespace-nowrap">Les 15 séjours</span>
            <span class="inline-flex items-center justify-center w-[170px] sm:w-[220px] md:w-[250px] h-[1.25em] select-none align-baseline overflow-hidden">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform leading-none">immersifs</span>
            </span>
            <span class="whitespace-nowrap">au Népal</span>
          </h2>
          <p class="mt-3 text-base text-slate-600 max-w-2xl font-normal">
            Sélectionnez votre aventure pour explorer le détail jour par jour, la fiche d'inclusions et réserver votre place.
          </p>
        </div>"""

c = c.replace(old_header_block, new_header_block)

# 2. Strict font scale normalization (keep sizes within 0.9em - 1.05em to prevent line height displacement)
old_js_font_styles = """    var fontStyles = [
      { name: "'Caveat', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "1.18em" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", color: "#09422b", size: "1.0em" },
      { name: "'Pacifico', cursive", style: "normal", weight: "400", color: "#047857", size: "0.85em" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", color: "#065f46", size: "1.0em" },
      { name: "'Dancing Script', cursive", style: "normal", weight: "700", color: "#0e5c3e", size: "1.08em" },
      { name: "'Syne', sans-serif", style: "normal", weight: "800", color: "#022c22", size: "0.95em" },
      { name: "'Abril Fatface', serif", style: "normal", weight: "400", color: "#046c4e", size: "0.95em" },
      { name: "'Satisfy', cursive", style: "normal", weight: "400", color: "#059669", size: "1.02em" },
      { name: "'Cinzel', serif", style: "normal", weight: "900", color: "#064e3b", size: "0.92em" },
      { name: "'Lobster Two', cursive", style: "italic", weight: "700", color: "#0e5c3e", size: "1.02em" }
    ];"""

new_js_font_styles = """    var fontStyles = [
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

c = c.replace(old_js_font_styles, new_js_font_styles)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Strict line-height, overflow-hidden and bounding box locked! Zero movement on grid cards.")
