import re

for hp in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro'
]:
    with open(hp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Ensure scroll-mt-20 on section #prochains-departs
    if 'scroll-mt-20' not in c:
        c = c.replace('id="prochains-departs" class="', 'id="prochains-departs" class="scroll-mt-20 ')

    # Add scroll logic to filterTrips
    scroll_logic = """
      // Auto-scroll directly to tours anchor #prochains-departs
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

    # Check if already inserted
    if 'Auto-scroll directly to tours anchor' not in c:
        c = re.sub(
            r'(const badge = document\.getElementById\(\'trip-count-badge\'\);.*?\}\s*\n)',
            r'\1' + scroll_logic + '\n',
            c,
            flags=re.DOTALL
        )

    with open(hp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Successfully injected scroll-to-tours logic in filterTrips for FR and EN homepages!")
