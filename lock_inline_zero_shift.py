with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Make the wrapper a fixed-width grid container with centered placement
# so neither "Les 15 séjours" (on the left) nor "au Népal" (on the right) can ever budge a single millimeter.
old_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight leading-[1.2] flex flex-wrap items-baseline gap-x-2.5 sm:gap-x-3.5">
            <span class="whitespace-nowrap">Les 15 séjours</span>
            <span class="inline-flex items-center justify-center w-[170px] sm:w-[220px] md:w-[250px] h-[1.25em] select-none align-baseline overflow-hidden">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform leading-none">immersifs</span>
            </span>
            <span class="whitespace-nowrap">au Népal</span>
          </h2>"""

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight leading-[1.2] inline-flex flex-wrap items-center">
            <span class="whitespace-nowrap shrink-0">Les 15 séjours&nbsp;</span>
            <span class="inline-grid place-items-center w-[150px] sm:w-[190px] md:w-[225px] h-[1.3em] select-none overflow-hidden shrink-0 align-middle">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform text-center leading-none">immersifs</span>
            </span>
            <span class="whitespace-nowrap shrink-0">&nbsp;au Népal</span>
          </h2>"""

c = c.replace(old_h2, new_h2)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Locked zero-shift grid architecture!")
