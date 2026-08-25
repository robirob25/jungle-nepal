import glob, re

# 1. Update Layout.astro with a universal CSS scroll-margin-top & scroll-padding-top rule
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

scroll_css = """
  /* Global Sticky Header Anchor Offset Calibration (Fixes sections landing too high) */
  html {
    scroll-padding-top: 100px;
  }
  @media (min-width: 640px) {
    html {
      scroll-padding-top: 120px;
    }
  }
  @media (min-width: 1024px) {
    html {
      scroll-padding-top: 130px;
    }
  }

  [id] {
    scroll-margin-top: 100px;
  }
  @media (min-width: 640px) {
    [id] {
      scroll-margin-top: 120px;
    }
  }
  @media (min-width: 1024px) {
    [id] {
      scroll-margin-top: 130px;
    }
  }
"""

if "/* Global Sticky Header Anchor Offset" not in layout:
    layout = layout.replace('</style>', scroll_css + '\n</style>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

print("✓ Added global scroll-margin-top & scroll-padding-top to Layout.astro")

# 2. Adjust specific inline Tailwind scroll-margin classes on homepage and tours
all_astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in all_astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c

    # Replace scroll-mt-20, scroll-mt-24, scroll-mt-28 with larger, perfectly padded offsets (scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36)
    c = re.sub(r'scroll-mt-(?:16|20|24|28)', 'scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print(f"✓ Calibrated all scroll anchors across {len(all_astro_files)} files!")
