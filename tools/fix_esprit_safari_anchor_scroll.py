with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the scroll script to handle both local '#concept' anchors and cross-page '/index.html#concept' or '/#concept' cleanly
# and properly offset for fixed headers!

old_script = """      // Safe smooth scroll polyfill safeguard
      document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
          anchor.addEventListener('click', function(e) {
            var targetId = this.getAttribute('href');
            if (targetId && targetId.length > 1 && targetId.startsWith('#')) {
              var targetElement = document.querySelector(targetId);
              if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
              }
            }
          });
        });
      });"""

new_script = """      // Safe and Precise Smooth Scroll to Anchors with Fixed Header Offset
      document.addEventListener('DOMContentLoaded', function() {
        // Handle in-page smooth scrolls
        document.querySelectorAll('a[href^="#"], a[href^="/index.html#"], a[href^="/#"]').forEach(function(anchor) {
          anchor.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            var hashIndex = href.indexOf('#');
            if (hashIndex !== -1) {
              var targetId = href.substring(hashIndex);
              var isCurrentPage = (href.startsWith('#') || window.location.pathname === '/' || window.location.pathname.endsWith('/index.html') || window.location.pathname === '');
              if (isCurrentPage && targetId.length > 1) {
                var targetElement = document.querySelector(targetId);
                if (targetElement) {
                  e.preventDefault();
                  var headerOffset = 90;
                  var elementPosition = targetElement.getBoundingClientRect().top;
                  var offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                  window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                  });
                  if (history.pushState) {
                    history.pushState(null, null, targetId);
                  }
                }
              }
            }
          });
        });

        // Handle direct incoming page load with #hash in URL
        if (window.location.hash) {
          setTimeout(function() {
            var targetEl = document.querySelector(window.location.hash);
            if (targetEl) {
              var headerOffset = 90;
              var pos = targetEl.getBoundingClientRect().top + window.pageYOffset - headerOffset;
              window.scrollTo({ top: pos, behavior: 'smooth' });
            }
          }, 150);
        }
      });"""

c = c.replace(old_script, new_script)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Refined smooth scroll polyfill with perfect header offset for #concept in Layout.astro!")
