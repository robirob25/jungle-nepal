import re
import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

tour_cat_str = {t['slug']: ",".join(t['categories']) for t in tours}

filter_script = """<script is:inline>
    window.scrollCategories = function(amount) {
      const el = document.getElementById('categories-scroll-container');
      if (el) el.scrollBy({ left: amount, behavior: 'smooth' });
    };

    window.filterTrips = function(category) {
      const pills = document.querySelectorAll('.category-pill');
      pills.forEach(p => {
        if (p.getAttribute('data-filter') === category) {
          p.classList.add('bg-slate-950', 'text-white', 'border-slate-900');
          p.classList.remove('bg-white', 'text-slate-900');
        } else {
          p.classList.remove('bg-slate-950', 'text-white', 'border-slate-900');
          p.classList.add('bg-white', 'text-slate-900');
        }
      });

      const cards = document.querySelectorAll('.trip-card');
      let visible = 0;
      cards.forEach(card => {
        const cats = (card.getAttribute('data-category') || '').split(',');
        if (category === 'all' || cats.includes(category)) {
          card.style.display = 'flex';
          visible++;
        } else {
          card.style.display = 'none';
        }
      });

      const countEl = document.getElementById('trip-count');
      if (countEl) countEl.textContent = visible;
    };

    window.filterFromHero = function() {
      const select = document.getElementById('hero-dest-select');
      if (select) {
        filterTrips(select.value);
        document.getElementById('prochains-departs').scrollIntoView({ behavior: 'smooth' });
      }
    };
</script>"""

raw_filter_script = filter_script.replace('is:inline', '')

for fpath in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro'
]:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'<script\s+is:inline>.*?window\.filterTrips.*?</script>', filter_script, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

for fpath in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html'
]:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'window.filterTrips' in c:
        c = re.sub(r'<script>\s*window\.scrollCategories.*?window\.filterFromHero.*?</script>', raw_filter_script, c, flags=re.DOTALL)
    else:
        c = c.replace('</body>', raw_filter_script + '\n</body>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Injected exact robust multi-category filter JS across all homepage files!")
