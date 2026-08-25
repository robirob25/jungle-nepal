with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

old_script = """  // High-End 3D Kinetic Font Roll & Pop Engine
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
  })();"""

new_script = """  // High-End 3D Kinetic Font Roll & Pop Engine (Strictly Uniform Cap-Height & Font Size)
  (function() {
    var el = document.getElementById('kinetic-immersion');
    if (!el) return;

    var fontStyles = [
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
    ];

    var currentIndex = 0;
    var isAnimating = false;

    // Apply initial style
    el.style.fontFamily = fontStyles[0].name;
    el.style.fontStyle = fontStyles[0].style;
    el.style.fontWeight = fontStyles[0].weight;
    el.style.color = fontStyles[0].color;
    el.style.fontSize = fontStyles[0].size;
    el.style.transform = 'translateY(0px) rotateX(0deg)';

    function rollNextFont() {
      if (isAnimating) return;
      isAnimating = true;

      // Phase 1: Fast Roll UP & Out
      el.style.transition = 'transform 180ms cubic-bezier(0.4, 0, 1, 1), opacity 180ms ease-in';
      el.style.transform = 'translateY(-14px) rotateX(75deg)';
      el.style.opacity = '0';

      setTimeout(function() {
        currentIndex = (currentIndex + 1) % fontStyles.length;
        var f = fontStyles[currentIndex];

        el.style.fontFamily = f.name;
        el.style.fontStyle = f.style;
        el.style.fontWeight = f.weight;
        el.style.color = f.color;
        el.style.fontSize = f.size;

        // Prepare at bottom ready to roll in
        el.style.transition = 'none';
        el.style.transform = 'translateY(14px) rotateX(-75deg)';
        el.style.opacity = '0';

        // Force reflow
        void el.offsetHeight;

        // Phase 2: Snap & Pop in strictly aligned
        el.style.transition = 'transform 260ms cubic-bezier(0, 0, 0.2, 1.4), opacity 220ms ease-out';
        el.style.transform = 'translateY(0px) rotateX(0deg)';
        el.style.opacity = '1';

        setTimeout(function() {
          isAnimating = false;
        }, 280);
      }, 190);
    }

    // Roll dynamically every 1.5s
    setInterval(rollNextFont, 1500);
  })();"""

c = c.replace(old_script, new_script)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Font sizes perfectly uniformized and aligned!")
