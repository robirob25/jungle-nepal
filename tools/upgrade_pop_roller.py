# 1. Add top expressive fonts (Caveat, Dancing Script, Pacifico, Playfair, Syne, Fraunces, Abril Fatface, Lobster Two, Clash Display, Monoton)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

font_link_old = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Cormorant+Garamond:ital,wght@1,600;1,700&family=DM+Serif+Display:ital@0;1&family=Fraunces:ital,opsz,wght@1,9..144,700;1,9..144,900&family=Monoton&family=Newsreader:ital,opsz,wght@0,6..72,400..800;1,6..72,400..800&family=Outfit:wght@800;900&family=Playfair+Display:ital,wght@1,700;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@700&family=Syne:wght@800&family=UnifrakturMaguntia&family=Borel&family=Rock+Salt&display=swap" rel="stylesheet">'

font_link_new = '<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Caveat:wght@700&family=Cinzel:wght@700;900&family=Cormorant+Garamond:ital,wght@1,600;1,700&family=Dancing+Script:wght@700&family=DM+Serif+Display:ital@0;1&family=Fraunces:ital,opsz,wght@1,9..144,700;1,9..144,900&family=Lobster+Two:ital,wght@1,700&family=Newsreader:ital,opsz,wght@0,6..72,400..800;1,6..72,400..800&family=Pacifico&family=Playfair+Display:ital,wght@1,700;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Satisfy&family=Syne:wght@800&display=swap" rel="stylesheet">'

layout = layout.replace(font_link_old, font_link_new)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
print("✓ Added expressive fonts to Layout.astro")

# 2. Update index.astro to remove the gray block completely, use an inline-flex vertical wheel with dynamic auto-sizing and fast snappy rolling
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Replace H2
old_h2_start = '          <h2 id="tours-section-title"'
old_h2_end = '          </h2>'

old_h2_idx_start = idx.find(old_h2_start)
old_h2_idx_end = idx.find(old_h2_end, old_h2_idx_start) + len(old_h2_end)

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight transition-all duration-300 flex flex-wrap items-baseline gap-x-2.5 sm:gap-x-3.5 leading-tight">
            <span>Les 15 séjours</span>
            <!-- Pure Transparent Seamless Rolling Word (Zero Gray Box) -->
            <span class="inline-block relative overflow-hidden align-baseline select-none h-[1.15em] transition-all duration-300" id="roller-mask">
              <span id="roller-wheel" class="flex flex-col text-left transition-transform duration-450 ease-[cubic-bezier(0.16,1,0.3,1)]">
                <!-- 1. Cursive handwritten pop (Caveat) -->
                <span class="h-[1.15em] flex items-center text-[#0e5c3e] whitespace-nowrap px-1" style="font-family: 'Caveat', cursive; font-size: 1.35em; font-weight: 700;">immersifs</span>
                <!-- 2. Editorial Luxury (Playfair Display) -->
                <span class="h-[1.15em] flex items-center text-[#09422b] whitespace-nowrap px-1" style="font-family: 'Playfair Display', serif; font-style: italic; font-weight: 900;">immersifs</span>
                <!-- 3. Retro Brush Cursive (Pacifico) -->
                <span class="h-[1.15em] flex items-center text-[#059669] whitespace-nowrap px-1" style="font-family: 'Pacifico', cursive; font-size: 0.95em;">immersifs</span>
                <!-- 4. High-End Editorial Serif (Fraunces) -->
                <span class="h-[1.15em] flex items-center text-[#047857] whitespace-nowrap px-1" style="font-family: 'Fraunces', serif; font-style: italic; font-weight: 800;">immersifs</span>
                <!-- 5. Elegant Signature (Dancing Script) -->
                <span class="h-[1.15em] flex items-center text-[#0e5c3e] whitespace-nowrap px-1" style="font-family: 'Dancing Script', cursive; font-size: 1.25em; font-weight: 700;">immersifs</span>
                <!-- 6. Heavy Bold Display (Syne) -->
                <span class="h-[1.15em] flex items-center text-[#022c22] whitespace-nowrap px-1" style="font-family: 'Syne', sans-serif; font-weight: 800; letter-spacing: -0.02em;">immersifs</span>
                <!-- 7. Magazine Vogue Serif (Abril Fatface) -->
                <span class="h-[1.15em] flex items-center text-[#065f46] whitespace-nowrap px-1" style="font-family: 'Abril Fatface', serif; font-size: 1.05em;">immersifs</span>
                <!-- 8. Sensual Cursive (Satisfy) -->
                <span class="h-[1.15em] flex items-center text-[#059669] whitespace-nowrap px-1" style="font-family: 'Satisfy', cursive; font-size: 1.15em;">immersifs</span>
                <!-- 9. Classic Roman (Cinzel) -->
                <span class="h-[1.15em] flex items-center text-[#064e3b] whitespace-nowrap px-1" style="font-family: 'Cinzel', serif; font-weight: 900; font-size: 0.92em; letter-spacing: 0.05em;">immersifs</span>
                <!-- 10. Vintage Script (Lobster Two) -->
                <span class="h-[1.15em] flex items-center text-[#0e5c3e] whitespace-nowrap px-1" style="font-family: 'Lobster Two', cursive; font-style: italic; font-weight: 700; font-size: 1.15em;">immersifs</span>
                <!-- Loop duplicate of first item for infinite seamless loop -->
                <span class="h-[1.15em] flex items-center text-[#0e5c3e] whitespace-nowrap px-1" style="font-family: 'Caveat', cursive; font-size: 1.35em; font-weight: 700;">immersifs</span>
              </span>
            </span>
            <span>au Népal</span>
          </h2>"""

idx = idx[:old_h2_idx_start] + new_h2 + idx[old_h2_idx_end:]

# Update JS rolling script for fast snappy roll (every 1.3s, 400ms transition)
old_script_start = "<script is:inline>\n  // 3D Infinite Rolling Cylinder Animation"
new_script = """<script is:inline>
  // High-End Seamless Kinetic Font Roller (Zero Gray Box, Pure Pop Cursive & Serif Fonts)
  (function() {
    var wheel = document.getElementById('roller-wheel');
    var mask = document.getElementById('roller-mask');
    if (!wheel || !mask) return;

    var items = wheel.children;
    var totalItems = 10;
    var currentIndex = 0;
    var isRolling = false;

    // Dynamically adjust mask width to fit current font smoothly
    function updateMaskWidth(idx) {
      var activeItem = items[idx % totalItems];
      if (activeItem) {
        var w = activeItem.getBoundingClientRect().width;
        if (w > 0) {
          mask.style.width = (w + 4) + 'px';
        }
      }
    }

    // Init width
    setTimeout(function() { updateMaskWidth(0); }, 100);
    window.addEventListener('resize', function() { updateMaskWidth(currentIndex); });

    function rollToNext() {
      if (isRolling) return;
      isRolling = true;
      currentIndex++;

      updateMaskWidth(currentIndex);

      wheel.style.transition = 'transform 420ms cubic-bezier(0.16, 1, 0.3, 1)';
      wheel.style.transform = 'translateY(' + (-currentIndex * 1.15) + 'em)';

      setTimeout(function() {
        if (currentIndex >= totalItems) {
          wheel.style.transition = 'none';
          currentIndex = 0;
          wheel.style.transform = 'translateY(0em)';
          updateMaskWidth(0);
        }
        isRolling = false;
      }, 440);
    }

    // Snappy roll every 1.4 seconds
    setInterval(rollToNext, 1400);
  })();
</script>
</Layout>"""

s_idx = idx.find(old_script_start)
if s_idx != -1:
    idx = idx[:s_idx] + new_script

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Upgraded to POP Wow Cursive kinetic roller with transparent background!")
