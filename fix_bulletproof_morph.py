with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Clean Title Structure:
# "Les 15 séjours <span id='morphing-word'>immersifs</span> au Népal"
old_h2_start = '          <h2 id="tours-section-title"'
old_h2_end = '          </h2>'

idx_start = c.find(old_h2_start)
idx_end = c.find(old_h2_end, idx_start) + len(old_h2_end)

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl lg:text-[54px] text-slate-900 tracking-tight transition-all duration-300 leading-tight">
            <span>Les 15 séjours </span><span id="kinetic-immersion" class="inline-block text-[#0e5c3e] transition-all duration-200 transform">immersifs</span><span> au Népal</span>
          </h2>"""

c = c[:idx_start] + new_h2 + c[idx_end:]

# 2. Modern 3D Flip/Roll Kinetic Typography Engine
old_script_start = "<script is:inline>\n  // High-End Seamless Kinetic Font Roller"
new_script = """<script is:inline>
  // High-End 3D Kinetic Font Roll & Pop Engine
  (function() {
    var el = document.getElementById('kinetic-immersion');
    if (!el) return;

    var fontStyles = [
      { name: "'Caveat', cursive", style: "normal", weight: "700", color: "#0e5c3e", scale: "1.28", y: "0px" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", color: "#0a4d33", scale: "1.02", y: "0px" },
      { name: "'Pacifico', cursive", style: "normal", weight: "400", color: "#047857", scale: "0.98", y: "1px" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", color: "#065f46", scale: "1.08", y: "0px" },
      { name: "'Dancing Script', cursive", style: "normal", weight: "700", color: "#0e5c3e", scale: "1.25", y: "-1px" },
      { name: "'Syne', sans-serif", style: "normal", weight: "800", color: "#022c22", scale: "0.95", y: "0px" },
      { name: "'Abril Fatface', serif", style: "normal", weight: "400", color: "#046c4e", scale: "1.05", y: "0px" },
      { name: "'Satisfy', cursive", style: "normal", weight: "400", color: "#059669", scale: "1.18", y: "-1px" },
      { name: "'Cinzel', serif", style: "normal", weight: "900", color: "#064e3b", scale: "0.92", y: "0px" },
      { name: "'Lobster Two', cursive", style: "italic", weight: "700", color: "#0e5c3e", scale: "1.15", y: "0px" }
    ];

    var currentIndex = 0;
    var isAnimating = false;

    // Apply initial style
    el.style.fontFamily = fontStyles[0].name;
    el.style.fontStyle = fontStyles[0].style;
    el.style.fontWeight = fontStyles[0].weight;
    el.style.color = fontStyles[0].color;
    el.style.transform = 'scale(' + fontStyles[0].scale + ')';
    el.style.transformOrigin = 'left center';

    function rollNextFont() {
      if (isAnimating) return;
      isAnimating = true;

      // Phase 1: Fast Roll UP & Out
      el.style.transition = 'transform 180ms cubic-bezier(0.4, 0, 1, 1), opacity 180ms ease-in';
      el.style.transform = 'translateY(-14px) rotateX(75deg) scale(0.9)';
      el.style.opacity = '0';

      setTimeout(function() {
        // Switch font while invisible
        currentIndex = (currentIndex + 1) % fontStyles.length;
        var f = fontStyles[currentIndex];

        el.style.fontFamily = f.name;
        el.style.fontStyle = f.style;
        el.style.fontWeight = f.weight;
        el.style.color = f.color;

        // Position at bottom ready to roll in
        el.style.transition = 'none';
        el.style.transform = 'translateY(14px) rotateX(-75deg) scale(' + f.scale + ')';
        el.style.opacity = '0';

        // Force reflow
        void el.offsetHeight;

        // Phase 2: Snap & Pop in from bottom
        el.style.transition = 'transform 260ms cubic-bezier(0, 0, 0.2, 1.4), opacity 220ms ease-out';
        el.style.transform = 'translateY(' + f.y + ') rotateX(0deg) scale(' + f.scale + ')';
        el.style.opacity = '1';

        setTimeout(function() {
          isAnimating = false;
        }, 280);
      }, 190);
    }

    // Roll dynamically every 1.5s
    setInterval(rollNextFont, 1500);
  })();
</script>
</Layout>"""

s_idx = c.find(old_script_start)
if s_idx != -1:
    c = c[:s_idx] + new_script
else:
    c = c.replace("</Layout>", new_script)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced with robust 3D Flip & Roll kinetic typography engine!")
