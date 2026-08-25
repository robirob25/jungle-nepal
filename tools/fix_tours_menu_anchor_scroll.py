with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# When clicking "Tous les 15 séjours" (href="/index.html#prochains-departs"),
# target the categories bar or top of the section with precision so the section title & filters are fully visible!

old_script = """        // Handle in-page smooth scrolls
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
        });"""

new_script = """        // Handle in-page smooth scrolls
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
        });"""

c = c.replace(old_script, new_script)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed tours menu anchor scroll: clicking 'Tous les 15 séjours' now lands smoothly at the top of the tours catalog!")
