with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Add universal and robust handleShareTour, copyTourLink, and share menu handling in Layout.astro
share_script = """    // Universal Tour Share Handler (Native Web Share API + Dropdown Fallback)
    window.handleShareTour = function(e) {
      if (e && e.stopPropagation) e.stopPropagation();
      var shareMenu = document.getElementById('share-menu');
      var pageUrl = window.location.href;
      var pageTitle = document.title || 'Jungle Nepal Adventure';

      // Update links inside share menu
      var waLink = document.getElementById('share-whatsapp');
      if (waLink) {
        waLink.href = 'https://api.whatsapp.com/send?text=' + encodeURIComponent(pageTitle + ' : ' + pageUrl);
      }
      var emailLink = document.getElementById('share-email');
      if (emailLink) {
        emailLink.href = 'mailto:?subject=' + encodeURIComponent(pageTitle) + '&body=' + encodeURIComponent('Découvre ce séjour exceptionnel au Népal avec Jungle Nepal Adventure :\\n\\n' + pageUrl);
      }

      // If Web Share API is natively supported (mobile devices / Safari / modern Chrome)
      if (navigator.share && /mobile|android|iphone|ipad/i.test(navigator.userAgent)) {
        navigator.share({
          title: pageTitle,
          text: 'Découvre ce séjour immersif au Népal avec Jungle Nepal Adventure',
          url: pageUrl
        }).catch(function() {});
        return;
      }

      // Desktop dropdown toggle
      if (shareMenu) {
        var isHidden = shareMenu.classList.contains('opacity-0');
        if (isHidden) {
          shareMenu.classList.remove('opacity-0', 'translate-y-2', 'pointer-events-none');
          shareMenu.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        } else {
          shareMenu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          shareMenu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }
    };

    window.copyTourLink = function(e) {
      if (e && e.stopPropagation) e.stopPropagation();
      var url = window.location.href;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function() {
          showCopySuccess();
        }).catch(function() {
          fallbackCopyText(url);
        });
      } else {
        fallbackCopyText(url);
      }
    };

    function fallbackCopyText(text) {
      var textArea = document.createElement('textarea');
      textArea.value = text;
      textArea.style.position = 'fixed';
      textArea.style.opacity = '0';
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        showCopySuccess();
      } catch (err) {}
      document.body.removeChild(textArea);
    }

    function showCopySuccess() {
      var shareBtn = document.getElementById('share-btn');
      if (shareBtn) {
        var originalHTML = shareBtn.innerHTML;
        shareBtn.innerHTML = '<span class="text-[#0e8354] font-black flex items-center gap-1.5"><svg class="w-4 h-4 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Lien copié !</span>';
        setTimeout(function() {
          shareBtn.innerHTML = originalHTML;
        }, 2500);
      }
      var shareMenu = document.getElementById('share-menu');
      if (shareMenu) {
        shareMenu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
        shareMenu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }
    }

    // Close share menu on outside click
    document.addEventListener('click', function(e) {
      var shareMenu = document.getElementById('share-menu');
      var shareBtn = document.getElementById('share-btn');
      if (shareMenu && !shareMenu.contains(e.target) && shareBtn && !shareBtn.contains(e.target)) {
        shareMenu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
        shareMenu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }
    });"""

# Insert before </script> at bottom of Layout.astro
c = c.replace('  </script>\n</body>', share_script + '\n  </script>\n</body>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Added universal share and copy functionality into Layout.astro!")
