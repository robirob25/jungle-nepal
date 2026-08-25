with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the section id="prochains-departs" classes and scroll-mt
content = content.replace(
    '<section id="prochains-departs" class="scroll-mt-16 sm:scroll-mt-20 sm: py-16 sm:py-24 lg:py-28 bg-[#faf8f5]">',
    '<section id="prochains-departs" class="scroll-mt-24 sm:scroll-mt-28 py-12 sm:py-16 lg:py-20 bg-[#faf8f5]">'
)

# 2. Update filterTrips so it calculates the exact header and category bar height before scrolling
old_scroll_code = """      // Auto-scroll directly to tours anchor #prochains-departs
      const targetAnchor = document.getElementById('prochains-departs');
      if (targetAnchor) {
        const headerOffset = 60;
        const elementPosition = targetAnchor.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }"""

new_scroll_code = """      // Auto-scroll directly to tours anchor with perfect sticky category header offset
      const targetAnchor = document.getElementById('prochains-departs');
      if (targetAnchor) {
        const catBar = document.getElementById('categories');
        const headerOffset = (catBar ? catBar.offsetHeight : 70) + 20;
        const elementPosition = targetAnchor.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }"""

content = content.replace(old_scroll_code, new_scroll_code)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed anchor scroll calculation in filterTrips!")
