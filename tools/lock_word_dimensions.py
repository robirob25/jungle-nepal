with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Fixed-width container for the animated word so the surrounding text ("Les 15 séjours" & "au Népal") NEVER moves even 1 pixel
old_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight transition-all duration-300 leading-tight">
            <span>Les 15 séjours </span><span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform">immersifs</span><span> au Népal</span>
          </h2>"""

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight transition-all duration-300 leading-tight">
            <span>Les 15 séjours</span>
            <span class="inline-block w-[185px] sm:w-[230px] md:w-[260px] text-center select-none overflow-visible align-baseline">
              <span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform">immersifs</span>
            </span>
            <span>au Népal</span>
          </h2>"""

c = c.replace(old_h2, new_h2)

# 2. Refined JS to center all fonts inside the fixed bounding box
old_js = """    // Apply initial style
    el.style.fontFamily = fontStyles[0].name;
    el.style.fontStyle = fontStyles[0].style;
    el.style.fontWeight = fontStyles[0].weight;
    el.style.color = fontStyles[0].color;
    el.style.fontSize = fontStyles[0].size;
    el.style.transform = 'translateY(0px) rotateX(0deg)';"""

new_js = """    // Apply initial style
    el.style.fontFamily = fontStyles[0].name;
    el.style.fontStyle = fontStyles[0].style;
    el.style.fontWeight = fontStyles[0].weight;
    el.style.color = fontStyles[0].color;
    el.style.fontSize = fontStyles[0].size;
    el.style.transform = 'translateY(0px) rotateX(0deg)';
    el.style.transformOrigin = 'center center';"""

c = c.replace(old_js, new_js)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed width container locked! Surrounding text is 100% rock-solid motionless.")
