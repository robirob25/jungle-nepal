#!/usr/bin/env python3
import os
import re

print("=== 1. OPTIMIZING TOUR & DESTINATION ASTRO FILES (LAZY IMAGES & CSS CLEANUP) ===")

# Fix dangling sm: and repetitive scroll classes
def fix_classes(content):
    # Fix 'sm: pt-8' or repetitive scroll classes
    content = re.sub(r'class="scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36 sm:scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36 sm:\s*', 'class="scroll-mt-28 sm:scroll-mt-32 lg:scroll-mt-36 ', content)
    content = re.sub(r'\bsm:\s+pt-', 'sm:pt-', content)
    return content

# Add decoding="async" and loading="lazy" to non-hero images
def optimize_images(content):
    # Find all <img without decoding="async"
    def img_replacer(match):
        img_tag = match.group(0)
        # Don't touch if already has decoding
        if 'decoding=' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img decoding="async" ')
        # If not eager and not logo and no loading attribute
        if 'loading=' not in img_tag and 'logo' not in img_tag and 'fetchpriority="high"' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
        return img_tag

    return re.sub(r'<img\s+[^>]+>', img_replacer, content)

all_astro_files = []
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".astro"):
            all_astro_files.append(os.path.join(root, file))

modified_count = 0
for filepath in all_astro_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = fix_classes(content)
    new_content = optimize_images(new_content)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        modified_count += 1
        print(f"Optimized: {filepath}")

print(f"Total Astro files optimized: {modified_count}")
