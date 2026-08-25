from PIL import Image
import glob, os

files = [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Chital_1.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Chital_2.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Chital_3.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Chital_3-2.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_1.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_2.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_3.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_4.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_5.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_6.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_7.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_8.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_9.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_10.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_11.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_12.webp',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife/Tigre_du_bengale_13.webp',
]

for fp in files:
    if os.path.exists(fp):
        im = Image.open(fp)
        print(f"{os.path.basename(fp)}: {im.size}")
