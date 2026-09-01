with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove history.pushState and clean hash from URL bar automatically
old_code = """                if (history.pushState) {
                  history.pushState(null, null, targetId);
                }"""

new_code = """                // Keep URL pristine without adding # hash to address bar
                if (history.replaceState) {
                  history.replaceState(null, null, window.location.pathname + window.location.search);
                }"""

c = c.replace(old_code, new_code)

# Also clean hash on page load if arriving with a hash from another page
old_hash_load = """        // Handle URL hash on initial page load / after cross-page jump
        if (window.location.hash && window.location.hash.length > 1) {
          setTimeout(function() {
            var targetEl = document.querySelector(window.location.hash);
            if (targetEl) {
              var headerHeight = 80;
              var pos = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight;
              window.scrollTo({ top: Math.max(0, pos), behavior: 'smooth' });
            }
          }, 200);
        }"""

new_hash_load = """        // Handle URL hash on initial page load / after cross-page jump, then clean the address bar
        if (window.location.hash && window.location.hash.length > 1) {
          var initialHash = window.location.hash;
          setTimeout(function() {
            var targetEl = document.querySelector(initialHash);
            if (targetEl) {
              var headerHeight = 80;
              var pos = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight;
              window.scrollTo({ top: Math.max(0, pos), behavior: 'smooth' });
              // Clean URL bar silently
              if (history.replaceState) {
                history.replaceState(null, null, window.location.pathname + window.location.search);
              }
            }
          }, 200);
        }"""

c = c.replace(old_hash_load, new_hash_load)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed # hash from URL address bar in Layout.astro!")
