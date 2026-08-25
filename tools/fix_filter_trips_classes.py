with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the filterTrips function in index.astro
old_js = """function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      const catLower = (category || 'all').toLowerCase();

      pills.forEach(pill => {
        const filterVal = (pill.getAttribute('data-filter') || '').toLowerCase();
        if (filterVal === catLower) {
          pill.classList.add('bg-white', 'text-slate-950', 'active');
          pill.classList.remove('bg-white/10', 'text-white', 'border-white/10');
        } else {
          pill.classList.remove('bg-white', 'text-slate-950', 'active');
          pill.classList.add('bg-white/10', 'text-white', 'border-white/10');
        }
      });"""

new_js = """function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      const catLower = (category || 'all').toLowerCase();

      pills.forEach(pill => {
        const filterVal = (pill.getAttribute('data-filter') || '').toLowerCase();
        if (filterVal === catLower) {
          pill.className = 'category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 transition-all duration-200 cursor-pointer shrink-0';
        } else {
          pill.className = 'category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0';
        }
      });"""

content = content.replace(old_js, new_js)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed filterTrips class assignment so unselected pills stay fully visible!")
