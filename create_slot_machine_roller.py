with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# 1. Update the H2 with a 3D slot-machine / odometer roller window
old_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight transition-all duration-300 flex flex-wrap items-baseline gap-x-2.5 sm:gap-x-3.5">
            <span>Les 15 séjours</span>
            <span id="animated-immersion-word" class="inline-block text-[#0e5c3e] transition-all duration-300 transform font-normal min-w-[170px] sm:min-w-[220px] text-left select-none">immersifs</span>
            <span>au Népal</span>
          </h2>"""

new_h2 = """          <h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight transition-all duration-300 flex flex-wrap items-center gap-x-2.5 sm:gap-x-3.5">
            <span>Les 15 séjours</span>
            <!-- 3D Rolling Slot Machine Wheel for 'immersifs' -->
            <span class="inline-block relative h-[1.3em] overflow-hidden align-middle select-none px-2 sm:px-3 py-0.5 rounded-xl bg-emerald-950/5 border border-emerald-800/15 shadow-inner">
              <span id="roller-wheel" class="flex flex-col text-left transition-transform duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)]">
                <span class="h-[1.3em] flex items-center text-[#0e5c3e] font-sans font-black tracking-tight">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#0a4d33] font-serif italic font-extrabold" style="font-family: 'Fraunces', serif;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#14532d] font-serif italic font-black" style="font-family: 'Playfair Display', serif;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#064e3b] font-mono font-black tracking-tighter" style="font-family: 'Space Grotesk', sans-serif;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#047857] font-serif italic font-bold" style="font-family: 'Cormorant Garamond', serif; font-size: 1.15em;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#065f46] font-sans font-black tracking-wide" style="font-family: 'Syne', sans-serif;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#046c4e] font-serif italic" style="font-family: 'DM Serif Display', serif;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#064e3b] font-serif font-black tracking-wider" style="font-family: 'Cinzel', serif; font-size: 0.9em;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#0e5c3e] font-sans font-black" style="font-family: 'Outfit', sans-serif;">immersifs</span>
                <span class="h-[1.3em] flex items-center text-[#059669] font-serif italic font-bold" style="font-family: 'Newsreader', serif; font-size: 1.1em;">immersifs</span>
                <!-- Loop duplicate of first item for seamless infinite roll -->
                <span class="h-[1.3em] flex items-center text-[#0e5c3e] font-sans font-black tracking-tight">immersifs</span>
              </span>
            </span>
            <span>au Népal</span>
          </h2>"""

idx = idx.replace(old_h2, new_h2)

# 2. Update the script to handle 3D continuous vertical rolling (odometer / slot machine physics)
old_script_marker = "<script is:inline>\n  // Dynamic 10-Font Kinetic Animation for the word \"immersifs\""
old_script_end = "</script>\n</Layout>"

new_script = """<script is:inline>
  // 3D Infinite Rolling Cylinder Animation (10 Font Types)
  (function() {
    var wheel = document.getElementById('roller-wheel');
    if (!wheel) return;

    var totalItems = 10;
    var currentIndex = 0;
    var isRolling = false;

    function rollToNext() {
      if (isRolling) return;
      isRolling = true;
      currentIndex++;

      wheel.style.transition = 'transform 700ms cubic-bezier(0.34, 1.4, 0.64, 1)';
      wheel.style.transform = 'translateY(' + (-currentIndex * 1.3) + 'em)';

      setTimeout(function() {
        if (currentIndex >= totalItems) {
          // Instantly snap back to 0 without transition for infinite loop
          wheel.style.transition = 'none';
          currentIndex = 0;
          wheel.style.transform = 'translateY(0em)';
        }
        isRolling = false;
      }, 720);
    }

    // Roll every 2 seconds
    setInterval(rollToNext, 2000);
  })();
</script>
</Layout>"""

# Locate old script
s_idx = idx.find(old_script_marker)
if s_idx != -1:
    idx = idx[:s_idx] + new_script
else:
    if "</Layout>" in idx:
        idx = idx.replace("</Layout>", new_script)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Created high-end 3D rolling slot-machine animation for 'immersifs'!")
