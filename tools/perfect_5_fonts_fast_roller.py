with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 5 strictly calibrated fonts with identical brand forest green (#0e5c3e) and precise matching cap-heights
old_js = """    var fontStyles = [
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

new_js = """    var fontStyles = [
      { name: "'Caveat', cursive", style: "normal", weight: "700", size: "1.05em", yOffset: "0px" },
      { name: "'Playfair Display', serif", style: "italic", weight: "900", size: "0.92em", yOffset: "0px" },
      { name: "'Dancing Script', cursive", style: "normal", weight: "700", size: "0.98em", yOffset: "0px" },
      { name: "'Fraunces', serif", style: "italic", weight: "800", size: "0.92em", yOffset: "0px" },
      { name: "'Great Vibes', cursive", style: "normal", weight: "400", size: "1.08em", yOffset: "0px" }
    ];"""

c = c.replace(old_js, new_js)

# Enforce uniform brand color (#0e5c3e) everywhere and increase speed (roll every 1000ms, faster snappier flip 140ms/200ms)
old_anim_block = """      // Phase 1: Fast Roll UP & Out
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
    setInterval(rollNextFont, 1500);"""

new_anim_block = """      // Phase 1: Snappy Roll UP & Out
      el.style.transition = 'transform 130ms cubic-bezier(0.4, 0, 1, 1), opacity 130ms ease-in';
      el.style.transform = 'translateY(-12px) rotateX(70deg)';
      el.style.opacity = '0';

      setTimeout(function() {
        currentIndex = (currentIndex + 1) % fontStyles.length;
        var f = fontStyles[currentIndex];

        el.style.fontFamily = f.name;
        el.style.fontStyle = f.style;
        el.style.fontWeight = f.weight;
        el.style.fontSize = f.size;
        el.style.color = '#0e5c3e'; // 100% Uniform Brand Color

        // Prepare at bottom ready to roll in
        el.style.transition = 'none';
        el.style.transform = 'translateY(12px) rotateX(-70deg)';
        el.style.opacity = '0';

        // Force reflow
        void el.offsetHeight;

        // Phase 2: Fast Snap & Pop in strictly aligned
        el.style.transition = 'transform 200ms cubic-bezier(0, 0, 0.2, 1.3), opacity 160ms ease-out';
        el.style.transform = 'translateY(' + f.yOffset + ') rotateX(0deg)';
        el.style.opacity = '1';

        setTimeout(function() {
          isAnimating = false;
        }, 210);
      }, 140);
    }

    // Fast snappy rolling cycle every 1.0 second
    setInterval(rollNextFont, 1000);"""

c = c.replace(old_anim_block, new_anim_block)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ 5 elite fonts, 100% uniform color (#0e5c3e), calibrated height and faster 1.0s cycle!")
