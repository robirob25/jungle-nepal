with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the heavy double box frame with a clean borderless map container
old_map_container = """      <!-- Map Canvas Seule (Pleine Largeur & Centrée) -->
      <div class="max-w-4xl mx-auto">
        <div class="relative rounded-3xl overflow-hidden border border-white/15 bg-gradient-to-b from-[#141e17] via-[#0d1610] to-[#080d0a] shadow-2xl p-3 sm:p-5 lg:p-7">
          
          <!-- Map Container with Parchment Rendering -->
          <div class="relative rounded-2xl overflow-hidden bg-[#f0ebd9] shadow-inner border border-[#d4c9aa]">
            <img
              src="/nepal-map-illustrated.png"
              alt="Carte illustrée du Népal - Bardia, Chitwan, Annapurna, Katmandou"
              class="w-full h-auto object-contain filter contrast-[1.03] saturate-[0.95]"
              loading="lazy"
            />"""

new_map_container = """      <!-- Map Canvas Seule (Pleine Largeur, Centrée, Sans Bordures Lourdes) -->
      <div class="max-w-4xl mx-auto">
        <div class="relative rounded-3xl overflow-hidden shadow-2xl">
          
          <!-- Map Container Direct -->
          <div class="relative overflow-hidden bg-[#f0ebd9]">
            <img
              src="/nepal-map-illustrated.png"
              alt="Carte illustrée du Népal - Bardia, Chitwan, Annapurna, Katmandou"
              class="w-full h-auto object-contain"
              loading="lazy"
            />"""

c = c.replace(old_map_container, new_map_container)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed outer dark border and parchment border from map container!")
