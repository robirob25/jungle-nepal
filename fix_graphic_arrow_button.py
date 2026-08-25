import os
import re

graphic_arrow_html = """
  <!-- BOUTON RETOUR EN HAUT ÉLÉGANT & GRAPHIQUE -->
  <button 
    id="back-to-top" 
    onclick="window.scrollTo({ top: 0, behavior: 'smooth' })" 
    class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 z-40 hidden sm:flex items-center justify-center w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-950/90 hover:bg-[#0e8354] text-white border border-white/25 shadow-[0_10px_30px_rgba(0,0,0,0.45)] backdrop-blur-xl transition-all duration-300 opacity-0 translate-y-4 pointer-events-none hover:scale-110 active:scale-95 group cursor-pointer"
    aria-label="Retour en haut de la page"
  >
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white group-hover:-translate-y-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
  </button>

  <script>
    (function() {
      const btn = document.getElementById('back-to-top');
      if (!btn) return;
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          btn.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
          btn.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        } else {
          btn.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
          btn.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      });
    })();
  </script>
"""

# 1. Update index.html, a-propos.html, contact.html
for fname in ['index.html', 'a-propos.html', 'contact.html']:
    fpath = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal', fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove previous button block
    content = re.sub(r'<!-- BOUTON RETOUR EN HAUT.*?<\/script>', '', content, flags=re.DOTALL)
    
    # Insert new graphic button
    content = content.replace('</body>', graphic_arrow_html + '\n</body>')
    
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
    content = content.replace('</body>', graphic_arrow_html + '\n</body>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Graphic inline SVG arrow button installed across all pages successfully!")
