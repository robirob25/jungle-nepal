with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

old_block = """            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs font-semibold">
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Tigres à pied" class="rounded text-[#0e8354] focus:ring-[#0e8354]" checked />
                <span>🐅 Tigres à pied</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Rhinos Chitwan" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🦏 Rhinos Chitwan</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Panthère des neiges" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🐆 Panthère des neiges</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Montagne" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🏔️ Montagne</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Rencontre avec des locaux" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🤝 Rencontre avec des locaux</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Vie de village" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🏡 Vie de village</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Culture et temple" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🕉️ Culture et temple</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Bivouac jungle" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>⛺ Bivouac jungle</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Photo animalière" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>📸 Photo animalière</span>
              </label>
            </div>"""

new_block = """            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 text-xs font-semibold">
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Animaux" class="rounded text-[#0e8354] focus:ring-[#0e8354]" checked />
                <span>🐾 Animaux</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Expédition panthère des neiges" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🐆 Expédition panthère des neiges</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Trekking" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🥾 Trekking</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Montagne" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🏔️ Montagne</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Rencontre avec des locaux" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🤝 Rencontre avec des locaux</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Vie de village" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🏡 Vie de village</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Culture et temple" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🕉️ Culture et temple</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Bivouac jungle" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>⛺ Bivouac jungle</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Photo animalière" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>📸 Photo animalière</span>
              </label>
            </div>"""

c = c.replace(old_block, new_block)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Options cleaned and replaced with: Animaux, Expédition panthère des neiges, Trekking, Montagne, Rencontre avec des locaux, Vie de village, Culture et temple, Bivouac jungle, Photo animalière!")
