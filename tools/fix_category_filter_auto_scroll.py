with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# When clicking ANY category pill ("Tous les séjours", "Safaris et grands félins", "Bivouacs...", "Rhinocéros...", etc.),
# filter the trips AND automatically smooth-scroll the page back up to the top of the tours catalog!

old_filter = """    function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;"""

new_filter = """    function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      // Automatically smooth scroll back up to the top of the tours section when clicking a category filter
      const toursSection = document.getElementById('prochains-departs');
      if (toursSection) {
        const headerHeight = 70;
        const rect = toursSection.getBoundingClientRect();
        const targetScrollTop = rect.top + window.pageYOffset - headerHeight;
        window.scrollTo({
          top: Math.max(0, targetScrollTop),
          behavior: 'smooth'
        });
      }"""

c = c.replace(old_filter, new_filter)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Added auto-scroll to top of tours section inside filterTrips() function!")
