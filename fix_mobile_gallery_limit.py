with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the initial gallery limit and reset logic:
old_init_limit = """  window.currentWildlifeIndex = 0;
  window.currentWildlifeCategory = 'all';
  window.wildlifeVisibleLimit = 21; // Initial 21 photos (7 per column)"""

new_init_limit = """  window.currentWildlifeIndex = 0;
  window.currentWildlifeCategory = 'all';
  // Check if mobile screen (width < 640px) -> show exactly 6 photos, otherwise 21 on desktop
  var isMobile = (window.innerWidth < 640);
  window.wildlifeDefaultLimit = isMobile ? 6 : 21;
  window.wildlifeVisibleLimit = window.wildlifeDefaultLimit;"""

content = content.replace(old_init_limit, new_init_limit)

old_reset_limit = """    if (category === 'all') {
      window.wildlifeVisibleLimit = 21; // reset to 21 when returning to all
    }"""

new_reset_limit = """    if (category === 'all') {
      var isMobile = (window.innerWidth < 640);
      window.wildlifeVisibleLimit = isMobile ? 6 : 21;
    }"""

content = content.replace(old_reset_limit, new_reset_limit)

# Also update loadMore increment to be mobile friendly (6 on mobile, 12 on desktop):
old_load_more = """  window.loadMoreWildlife = function() {
    window.wildlifeVisibleLimit += 10;
    window.renderWildlifeCards();
  };"""

new_load_more = """  window.loadMoreWildlife = function() {
    var isMobile = (window.innerWidth < 640);
    window.wildlifeVisibleLimit += (isMobile ? 6 : 12);
    window.renderWildlifeCards();
  };"""

content = content.replace(old_load_more, new_load_more)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Mobile gallery initial limit set to exactly 6 photos!")
