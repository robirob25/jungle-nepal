with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the anchor click handler with a bulletproof cross-page navigation handler
old_anchor_handler = """      // Safe and Precise Smooth Scroll to Anchors with Fixed Header Offset
      document.addEventListener('DOMContentLoaded', function() {
        // Direct click handler on all internal anchor links
        document.querySelectorAll('a[href*="#"]').forEach(function(anchor) {
          anchor.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            if (!href) return;
            var hashIndex = href.indexOf('#');
            if (hashIndex !== -1) {
              var targetId = href.substring(hashIndex);
              var isCurrentPage = (href.startsWith('#') || window.location.pathname === '/' || window.location.pathname.endsWith('/') || window.location.pathname === '');
              if (isCurrentPage && targetId.length > 1) {
                var targetElement = document.querySelector(targetId);
                if (targetElement) {
                  e.preventDefault();
                  var headerHeight = 70;
                  var rect = targetElement.getBoundingClientRect();
                  var targetScrollTop = rect.top + window.pageYOffset - headerHeight;
                  window.scrollTo({
                    top: Math.max(0, targetScrollTop),
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

        // Handle URL hash on initial page load
        if (window.location.hash) {
          setTimeout(function() {
            var targetEl = document.querySelector(window.location.hash);
            if (targetEl) {
              var headerHeight = 70;
              var pos = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight;
              window.scrollTo({ top: Math.max(0, pos), behavior: 'smooth' });
            }
          }, 150);
        }
      });"""

new_anchor_handler = """      // Bulletproof Cross-Page & In-Page Smooth Scroll Navigation
      document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('a[href*="#"]').forEach(function(anchor) {
          anchor.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            if (!href) return;
            var hashIndex = href.indexOf('#');
            if (hashIndex === -1) return;

            var targetId = href.substring(hashIndex);
            if (targetId.length <= 1) return;

            var linkPath = href.substring(0, hashIndex);
            var currentPath = window.location.pathname;

            var isSamePage = !linkPath || 
                             linkPath === currentPath || 
                             (linkPath === '/' && (currentPath === '/' || currentPath === '/index.html' || currentPath === '')) ||
                             (linkPath.replace(/\\.html$/, '') === currentPath.replace(/\\.html$/, ''));

            if (isSamePage) {
              var targetElement = document.querySelector(targetId);
              if (targetElement) {
                e.preventDefault();
                var headerHeight = 80;
                var rect = targetElement.getBoundingClientRect();
                var targetScrollTop = rect.top + window.pageYOffset - headerHeight;
                window.scrollTo({
                  top: Math.max(0, targetScrollTop),
                  behavior: 'smooth'
                });
                if (history.pushState) {
                  history.pushState(null, null, targetId);
                }
              }
            }
          });
        });

        // Handle URL hash on initial page load / after cross-page jump
        if (window.location.hash && window.location.hash.length > 1) {
          setTimeout(function() {
            var targetEl = document.querySelector(window.location.hash);
            if (targetEl) {
              var headerHeight = 80;
              var pos = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight;
              window.scrollTo({ top: Math.max(0, pos), behavior: 'smooth' });
            }
          }, 200);
        }
      });"""

c = c.replace(old_anchor_handler, new_anchor_handler)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed cross-page anchor navigation in Layout.astro!")
