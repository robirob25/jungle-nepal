import re
import os

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Navbar completely with a sleek, perfectly spaced, zero-wrapping navbar
new_nav = """  <!-- 2. NAVBAR LUXE IMMERSIVE (Zéro retour à la ligne, espacements parfaits) -->
  <header id="main-nav" class="fixed top-8 left-0 right-0 z-40 transition-all duration-300 py-2 px-3 sm:px-6">
    <div class="max-w-7xl mx-auto">
      <div id="nav-container" class="flex items-center justify-between px-4 sm:px-6 py-2.5 rounded-2xl transition-all duration-300 bg-jungle-950/90 backdrop-blur-xl border border-white/15 text-white shadow-2xl gap-3">
        
        <!-- Logo -->
        <a href="#" class="flex items-center gap-2.5 group shrink-0">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-600 to-jungle-950 flex items-center justify-center text-amber-300 border border-amber-400/30 group-hover:scale-105 transition-transform shadow-md">
            <i data-lucide="footprints" class="w-4 h-4"></i>
          </div>
          <div class="flex flex-col">
            <span class="font-black text-base sm:text-lg tracking-tight text-white leading-none whitespace-nowrap">
              JUNGLE NEPAL
            </span>
            <span class="text-[8px] font-extrabold tracking-widest text-amber-300 uppercase mt-0.5 whitespace-nowrap">
              Adventure • 14 Circuits
            </span>
          </div>
        </a>

        <!-- Center Nav Links (Strictly single line whitespace-nowrap) -->
        <nav class="hidden xl:flex items-center gap-1.5 text-xs font-bold text-slate-200 shrink-0">
          <a href="#prochains-departs" class="px-3 py-1.5 rounded-full hover:bg-white/10 transition-colors flex items-center gap-1.5 whitespace-nowrap">
            <span>Les 14 Séjours</span>
            <span class="bg-fire-600 text-white text-[9px] font-black px-1.5 py-0.2 rounded-full">14</span>
          </a>
          <a href="#concept" class="px-3 py-1.5 rounded-full hover:bg-white/10 transition-colors whitespace-nowrap">
            L'Esprit Safari Sauvage
          </a>
          <a href="#pisteurs" class="px-3 py-1.5 rounded-full hover:bg-white/10 transition-colors whitespace-nowrap">
            Maîtres Pisteurs (BBC)
          </a>
          <a href="#avis" class="px-3 py-1.5 rounded-full hover:bg-white/10 transition-colors flex items-center gap-1 whitespace-nowrap">
            <span>Avis</span>
            <span class="text-amber-400 font-bold">★ 4.9/5</span>
          </a>
        </nav>

        <!-- Right Action Buttons (Strictly single line whitespace-nowrap) -->
        <div class="flex items-center gap-2 sm:gap-3 shrink-0">
          <button onclick="openCustomTripModal()" class="hidden md:inline-flex items-center gap-1.5 px-3.5 py-2 rounded-full text-xs font-bold bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 hover:border-amber-300/60 text-slate-100 hover:text-amber-200 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all whitespace-nowrap shrink-0">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-300 shrink-0"></i>
            <span>Privatisation & Sur-mesure</span>
          </button>

          <a href="#prochains-departs" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white text-xs sm:text-xs font-black px-4 sm:px-5 py-2.5 rounded-full shadow-[0_4px_16px_rgba(234,88,12,0.4)] hover:shadow-[0_6px_24px_rgba(234,88,12,0.6)] hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300 border-t border-white/25 whitespace-nowrap shrink-0">
            <span>Explorer les départs</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5 shrink-0"></i>
          </a>

          <button onclick="toggleMobileMenu()" class="xl:hidden p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white shrink-0" aria-label="Menu">
            <i data-lucide="menu" class="w-5 h-5"></i>
          </button>
        </div>

      </div>
    </div>"""

# Replace navbar
nav_pattern = r'<!-- 2\. NAVBAR LUXE IMMERSIVE.*?<!-- 3\. HERO SECTION'
html = re.sub(nav_pattern, new_nav + "\n\n  <!-- 3. HERO SECTION", html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Navbar updated with zero text-wrapping and perfect padding!")
