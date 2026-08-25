from PIL import Image
import os, glob

# Map of raw authentic photos to hero slide files
# Let's check which raw photos correspond to each hero slide:

hero_mappings = {
    # 1. Tiger water / grass (hero_1): Tigre_du_bengale_2.webp (1600x900) or adrien_tigre1.webp (1600x1067)
    'hero_1_tiger_water.webp': '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_2.webp',
    
    # 2. Elephant in jungle: Tigre_du_bengale / julien_elephant_jungle.webp / wildlife_elephant
    'hero_6_elephant_jungle.webp': '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/julien_elephant_jungle.webp',
    
    # 3. Rhino: chitwan_rhino.png / wildlife_rhino
    'hero_2_rhino_mist.webp': '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/original_site/chitwan_rhino.webp',
    
    # 4. Tiger stalk / walk in jungle: adrien_tigre1.webp (1600x1067) / Tigre_du_bengale_6.webp
    'hero_7_tiger_stalk.webp': '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/adrien_tigre1.webp',
    
    # 5. Deer plain: Chital_2.webp (1600x900) or Chital_3.webp (1600x1067)
    'hero_4_deer_plain.webp': '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Chital_3.webp',
    
    # 6. Tiger in forest walking: adrien_tigre3.webp (1600x1067) or Tigre_du_bengale_4.webp
    'hero_3_tiger_jungle.webp': '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos/adrien_tigre3.webp'
}

hero_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/hero'

for hero_name, src_path in hero_mappings.items():
    if os.path.exists(src_path):
        im = Image.open(src_path)
        # Convert to RGB if needed
        if im.mode in ('RGBA', 'P'):
            im = im.convert('RGB')
        
        # Save at high quality WebP (1920px width max without aggressive crop!)
        out_path = os.path.join(hero_dir, hero_name)
        
        # Resize cleanly to 1920 maintaining full aspect ratio without cropping away the animal!
        w, h = im.size
        target_w = min(1920, w)
        target_h = int(h * (target_w / w))
        
        im_resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im_resized.save(out_path, 'WEBP', quality=88, method=6)
        print(f"✓ Re-saved {hero_name} from raw source {os.path.basename(src_path)} ({target_w}x{target_h}) without zoom!")

