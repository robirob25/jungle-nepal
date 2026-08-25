import os
import re

back_to_top_html = """
  <!-- BOUTON RETOUR EN HAUT (DESKTOP) -->
  <button 
    id="back-to-top" 
    onclick="window.scrollTo({ top: 0, behavior: 'smooth' })" 
    class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 z-40 hidden sm:flex items-center justify-center w-11 h-11 sm:w-12 sm:h-12 rounded-full bg-slate-950/90 hover:bg-[#0e8354] text-white border border-white/20 shadow-[0_8px_30px_rgba(0,0,0,0.35)] backdrop-blur-md transition-all duration-300 opacity-0 translate-y-4 pointer-events-none hover:scale-110 active:scale-95 group cursor-pointer"
    aria-label="Retour en haut"
  >
    <i data-lucide="arrow-up" class="w-5 h-5 group-hover:-translate-y-0.5 transition-transform duration-200"></i>
  </button>

  <script>
    // Gestionnaire d'affichage du bouton retour en haut
    window.addEventListener('scroll', () => {
      const btn = document.getElementById('back-to-top');
      if (!btn) return;
      if (window.scrollY > 350) {
        btn.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      } else {
        btn.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }
    });
  </script>
"""

# 1. Update index.html, a-propos.html, contact.html
for fname in ['index.html', 'a-propos.html', 'contact.html']:
    fpath = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal', fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove previous if exists
    content = re.sub(r'<!-- BOUTON RETOUR EN HAUT.*?<\/script>', '', content, flags=re.DOTALL)
    
    # Insert before </body>
    content = content.replace('</body>', back_to_top_html + '\n</body>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update all 14 tour pages
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'<!-- BOUTON RETOUR EN HAUT.*?<\/script>', '', content, flags=re.DOTALL)
    content = content.replace('</body>', back_to_top_html + '\n</body>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Back to Top floating button successfully added to all pages!")
