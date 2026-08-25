import re

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

fr_badges = """        <!-- 3 Concrete Quick Fact Badges -->
        <div class="mt-10 grid grid-cols-1 sm:grid-cols-3 gap-4 text-center max-w-3xl mx-auto">
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Territoire</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">Bardia National Park</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Approche</p>
            <p class="text-sm sm:text-base font-black text-[#10b981] mt-1">À pied et en jeep</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Saison</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">Mai</p>
          </div>
        </div>"""

pattern = r'<!-- 4 Concrete Quick Fact Badges -->.*?</div>\s*</div>\s*(?=\s*<!-- Direct Action Bar -->)'
html = re.sub(pattern, fr_badges, html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("1. Updated badges in index.html to exactly 3 facts!")

# 2. Update en/index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

en_badges = """        <!-- 3 Concrete Quick Fact Badges -->
        <div class="mt-10 grid grid-cols-1 sm:grid-cols-3 gap-4 text-center max-w-3xl mx-auto">
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Territory</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">Bardia National Park</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Approach</p>
            <p class="text-sm sm:text-base font-black text-[#10b981] mt-1">On foot and by jeep</p>
          </div>
          <div class="p-5 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <p class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400">Season</p>
            <p class="text-sm sm:text-base font-black text-white mt-1">May</p>
          </div>
        </div>"""

en_html = re.sub(pattern, en_badges, en_html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print("2. Updated badges in en/index.html to exactly 3 facts!")
