with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/js/translator.js', 'r', encoding='utf-8') as f:
    js = f.read()

helpers = """
// Language Switcher Dropdown Click / Touch Handler
function toggleLangMenu(btn) {
  const container = btn.closest('.group\\\/lang') || btn.parentElement;
  if (!container) return;
  const dropdown = container.querySelector('.lang-dropdown-box');
  if (!dropdown) return;

  const isOpen = dropdown.classList.contains('opacity-100');
  if (isOpen) {
    dropdown.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
    dropdown.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
  } else {
    dropdown.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
    dropdown.classList.remove('opacity-0', 'translate-y-2', 'pointer-events-none');
  }
}

function setLanguagePref(lang) {
  try {
    localStorage.setItem('jn_lang', lang);
  } catch (e) {}
}

document.addEventListener('click', (e) => {
  if (!e.target.closest('.group\\\/lang')) {
    document.querySelectorAll('.lang-dropdown-box').forEach(d => {
      d.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      d.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
    });
  }
});
"""

if 'function toggleLangMenu' not in js:
    js += '\n' + helpers
    with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/js/translator.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Added toggleLangMenu & setLanguagePref to translator.js!")
else:
    print("Helpers already present in translator.js")
