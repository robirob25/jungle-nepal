with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the filterTrips function so it filters smoothly without overwriting the dynamic kinetic title,
# and updates the active states and card visibility flawlessly.

old_filter_fn = """    function filterTrips(category) {
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
      });

      cards.forEach(card => {
        const rawCats = card.getAttribute('data-category') || '';
        const cardCats = rawCats.toLowerCase().split(/\\s+/);
        
        let match = false;
        if (catLower === 'all') {
          match = true;
        } else if (catLower === 'mustang-himalaya' || catLower === 'mustang' || catLower === 'culture' || catLower === 'himalaya') {
          match = cardCats.includes('mustang-himalaya') || cardCats.includes('culture') || cardCats.includes('mustang');
        } else if (catLower === 'rafting') {
          match = cardCats.includes('rafting');
        } else {
          match = cardCats.includes(catLower);
        }

        if (match) {
          card.style.display = 'flex';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      const badge = document.getElementById('trip-count-badge');
      var badge = document.getElementById('trip-count-badge');
    if (badge) {
        badge.innerHTML = `Affichage de <strong>${visibleCount} circuit${visibleCount > 1 ? 's' : ''}</strong>`;
      }


      const sectionTitle = document.getElementById('tours-section-title');
      if (sectionTitle) {
        const titleMap = {
          'all': 'Les 15 séjours immersifs au Népal',
          'safari': '🐅 Safaris et grands félins',
          'bivouac': '⛺ Bivouacs et nuits sauvages en jungle',
          'chitwan': '🦏 Rhinocéros et parc national de Chitwan',
          'rafting': '🚣 Rafting et expéditions rivières',
          'mustang-himalaya': '🏔️ Himalaya, Mustang et spiritualité',
          'culture': '🏔️ Himalaya, Mustang et spiritualité',
          'grand-tour': '🇳🇵 Grands tours et immersion 360°'
        };
        sectionTitle.textContent = titleMap[catLower] || 'Les 15 séjours immersifs au Népal';
      }
      // Auto-scroll directly to tours anchor with perfect sticky category header offset
      const targetAnchor = document.getElementById('prochains-departs');
      if (targetAnchor) {
        const catBar = document.getElementById('categories');
        const headerOffset = (catBar ? catBar.offsetHeight : 70) + 8;
        const elementPosition = targetAnchor.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    }"""

new_filter_fn = """    function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      const catLower = (category || 'all').toLowerCase().trim();

      pills.forEach(pill => {
        const filterVal = (pill.getAttribute('data-filter') || '').toLowerCase().trim();
        if (filterVal === catLower) {
          pill.className = 'category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 transition-all duration-200 cursor-pointer shrink-0';
        } else {
          pill.className = 'category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0';
        }
      });

      cards.forEach(card => {
        const rawCats = card.getAttribute('data-category') || '';
        const cardCats = rawCats.toLowerCase().split(/\\s+/);
        
        let match = false;
        if (catLower === 'all') {
          match = true;
        } else if (catLower === 'mustang-himalaya' || catLower === 'mustang' || catLower === 'culture' || catLower === 'himalaya') {
          match = cardCats.includes('mustang-himalaya') || cardCats.includes('culture') || cardCats.includes('mustang') || cardCats.includes('himalaya');
        } else if (catLower === 'safari') {
          match = cardCats.includes('safari') || cardCats.includes('bardia') || cardCats.includes('suklaphanta') || cardCats.includes('tigre');
        } else if (catLower === 'bivouac') {
          match = cardCats.includes('bivouac') || cardCats.includes('camping');
        } else if (catLower === 'chitwan') {
          match = cardCats.includes('chitwan') || cardCats.includes('rhino');
        } else if (catLower === 'rafting') {
          match = cardCats.includes('rafting') || cardCats.includes('karnali');
        } else if (catLower === 'grand-tour') {
          match = cardCats.includes('grand-tour') || cardCats.includes('immersion');
        } else {
          match = cardCats.includes(catLower);
        }

        if (match) {
          card.style.display = 'flex';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });
    }"""

c = c.replace(old_filter_fn, new_filter_fn)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed filterTrips JavaScript logic in index.astro!")
