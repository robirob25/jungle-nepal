with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. In index.astro Header:
# Replace <a href="#prochains-departs" class="hover:text-amber-100 transition-colors">Départs</a>
# with <a href="#prochains-departs" class="hover:text-amber-100 transition-colors">Tous les 15 séjours</a>

c = c.replace(
    '<a href="#prochains-departs" class="hover:text-amber-100 transition-colors">Départs</a>',
    '<a href="#prochains-departs" class="hover:text-amber-100 transition-colors">Tous les 15 séjours</a>'
)

# 2. Add id="prochains-departs" precisely on the title or section start of tours,
# and ensure scroll-margin is calibrated:
# <section id="prochains-departs" class="scroll-mt-16 pt-6 sm:pt-8 lg:pt-10 pb-16 sm:pb-20 bg-[#faf8f5]">

c = c.replace(
    'class="scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36 sm:scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36 pt-6 sm:pt-8 lg:pt-10 pb-16 sm:pb-20 bg-[#faf8f5]"',
    'class="scroll-mt-16 sm:scroll-mt-20 pt-6 sm:pt-8 lg:pt-10 pb-16 sm:pb-20 bg-[#faf8f5]"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

# 3. In Layout.astro, fix smooth scrolling so clicking #prochains-departs scrolls to the exact top of the tours section:
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout_c = f.read()

old_scroll = """      // Safe and Precise Smooth Scroll to Anchors with Fixed Header Offset
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
                // If targeting #prochains-departs, scroll directly to categories bar or section top
                var targetElement = (targetId === '#prochains-departs') ? (document.getElementById('categories') || document.querySelector(targetId)) : document.querySelector(targetId);
                if (targetElement) {
                  e.preventDefault();
                  var headerOffset = (targetId === '#prochains-departs') ? 0 : 80;
                  var elementPosition = targetElement.getBoundingClientRect().top;
                  var offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                  window.scrollTo({
                    top: Math.max(0, offsetPosition),
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

new_scroll = """      // Safe and Precise Smooth Scroll to Anchors with Fixed Header Offset
      document.addEventListener('DOMContentLoaded', function() {
        // Direct click handler on all internal anchor links
        document.querySelectorAll('a[href*="#"]').forEach(function(anchor) {
          anchor.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            if (!href) return;
            var hashIndex = href.indexOf('#');
            if (hashIndex !== -1) {
              var targetId = href.substring(hashIndex);
              var isCurrentPage = (href.startsWith('#') || window.location.pathname === '/' || window.location.pathname.endsWith('/index.html') || window.location.pathname === '');
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

layout_c = layout_c.replace(old_scroll, new_scroll)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout_c)

print("✓ Fixed Header link text to 'Tous les 15 séjours' and calibrated anchor scroll directly to the top of #prochains-departs!")
