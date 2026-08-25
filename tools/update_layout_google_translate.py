with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

google_translate_head = """  <!-- Adaptive Favicons (Dark for light theme, Light for dark theme) -->
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

  <!-- Google Translate In-Place Translation Widget Initialization -->
  <script type="text/javascript">
    function googleTranslateElementInit() {
      new google.translate.TranslateElement({
        pageLanguage: 'fr',
        includedLanguages: 'en,fr,de,es,it,nl',
        autoDisplay: false,
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE
      }, 'google_translate_element');
    }
  </script>
  <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>"""

# Replace favicon tags / add google translate to head
import re
layout = re.sub(r'<!-- Adaptive Favicons.*?<!-- Open Graph -->', google_translate_head + '\n\n  <!-- Open Graph -->', layout, flags=re.DOTALL)

# Add custom translation styles and scripts before </body>
google_translate_body = """  <!-- Hidden Container for Google Translate Core -->
  <div id="google_translate_element" style="display:none; visibility:hidden; position:absolute; left:-9999px;"></div>

  <style is:global>
    body { font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; top: 0px !important; position: static !important; }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    
    /* Clean UI - Strip Google Translate Default Banners & Overlays */
    .goog-te-banner-frame.skiptranslate, iframe.goog-te-banner-frame { display: none !important; }
    .goog-tooltip, #goog-gt-tt, .goog-te-balloon-frame { display: none !important; }
    .goog-tooltip:hover { display: none !important; }
    .goog-text-highlight { background-color: transparent !important; border: none !important; box-shadow: none !important; }
    .goog-te-gadget { display: none !important; }
    body > .skiptranslate { display: none !important; }
    .goog-te-spinner-pos { display: none !important; }
  </style>

  <script is:inline>
    // Universal In-Place Language Switcher
    function changeLanguage(langCode) {
      const hostname = window.location.hostname;
      
      if (langCode === 'fr') {
        // Reset to original French
        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=.${hostname}; path=/;`;
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=${hostname}; path=/;`;
        localStorage.setItem('user_lang', 'fr');
      } else {
        // Set Google Translate target language cookie
        document.cookie = `googtrans=/fr/${langCode}; path=/;`;
        document.cookie = `googtrans=/fr/${langCode}; domain=.${hostname}; path=/;`;
        document.cookie = `googtrans=/fr/${langCode}; domain=${hostname}; path=/;`;
        localStorage.setItem('user_lang', langCode);
      }

      // If Google Translate combo is already loaded, trigger event
      const combo = document.querySelector('.goog-te-combo');
      if (combo) {
        combo.value = langCode;
        combo.dispatchEvent(new Event('change'));
      } else {
        window.location.reload();
      }

      updateActiveLangUI(langCode);
      
      // Close dropdown if open
      document.querySelectorAll('.lang-dropdown-box').forEach(el => {
        el.classList.add('opacity-0', 'pointer-events-none');
      });
    }

    function updateActiveLangUI(langCode) {
      document.querySelectorAll('[data-lang-btn]').forEach(btn => {
        const code = btn.getAttribute('data-lang-btn');
        if (code === langCode) {
          btn.classList.add('bg-white/20', 'text-[#10b981]');
          btn.classList.remove('text-slate-300');
        } else {
          btn.classList.remove('bg-white/20', 'text-[#10b981]');
          btn.classList.add('text-slate-300');
        }
      });
    }

    function toggleLangMenu(button) {
      const parent = button.closest('.group\\/lang') || button.parentElement;
      const menu = parent ? parent.querySelector('.lang-dropdown-box') : null;
      if (menu) {
        menu.classList.toggle('opacity-0');
        menu.classList.toggle('pointer-events-none');
        menu.classList.toggle('opacity-100');
        menu.classList.toggle('pointer-events-auto');
      }
    }

    // Auto-sync on DOM ready
    document.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('user_lang') || 'fr';
      updateActiveLangUI(savedLang);
      
      if (savedLang !== 'fr') {
        const interval = setInterval(() => {
          const combo = document.querySelector('.goog-te-combo');
          if (combo) {
            if (combo.value !== savedLang) {
              combo.value = savedLang;
              combo.dispatchEvent(new Event('change'));
            }
            clearInterval(interval);
          }
        }, 300);
        setTimeout(() => clearInterval(interval), 5000);
      }
    });
  </script>"""

layout = layout.replace('</body>', google_translate_body + '\n</body>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

print("Updated Layout.astro with universal Google Translate in-place translation engine!")
