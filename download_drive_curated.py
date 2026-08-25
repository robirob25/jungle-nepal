import urllib.request, os, json, time

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_photos'
os.makedirs(dest_dir, exist_ok=True)

# Curated list of high-value photos from Adrien, Julien, Antoine, Frederic
curated_photos = [
    # --- ADRIEN (Tigers, Cultural Katmandou/Bhaktapur, Bardia Jungle) ---
    ("adrien_tigre1.jpg", "1dv2JFd9nPLSacavkvuKAsedgYEONw_Vd"),
    ("adrien_tigre2.jpg", "1WoOlC7MLIgHOt1kYfHR5PNuQMJJnOm7Q"),
    ("adrien_tigre3.jpg", "1PDSSc1qT9Wj32fHVr3VO7LJrIQzwYvDh"),
    ("adrien_tigre4.jpg", "1zFyvEvr_l7sswJz4zVG9pB7-S6AZ88lT"),
    ("adrien_bhaktapur1.jpg", "1H1PE4RUBP9rhXekChqABSy1Ssz2r7gLe"),
    ("adrien_bhaktapur2.jpg", "1TuXMhLvGimF2AGqbcvJDTOgIqtBu079v"),
    ("adrien_katmandou1.jpg", "1TpUrS0SF3LKfL5bvIVXUgRD_nVSuFIfQ"),
    ("adrien_trackers_staff.jpg", "1VKqQZompr058-K8I5Z_0RQIHjrU6jINX"),
    ("adrien_bardia_river.jpg", "1Sk2IN9YbVLRg9p_dxw9NPEhupzqlaswU"),
    ("adrien_bardia_camp.jpg", "1moXR1U_NANWHto54csmhIA1HlitJNy16"),
    ("adrien_bardia_forest.jpg", "17iAr8_Pmqu8TF7bE4EjseoVQ1XwmL-jU"),
    ("adrien_bardia_sunset.jpg", "1vvtRPQ5HR9DPvbBorpzd_fnKkk_yx8u7"),

    # --- JULIEN (Leopard, Bengal Tigers, Wild Elephants, Dolphins, Walking safari) ---
    ("julien_leopard_indien.jpg", "1qDo4IeF4NhlnE3Qc3-ugPfI3bpDQoHkj"),
    ("julien_tigre_bengale1.jpg", "1EN_sM2tGd6nP0wMxGqatNaCS0lqOfDj7"),
    ("julien_tigre_bengale2.jpg", "14iafGGO6AIRVXnGaZrBtVyRLK_pLL6pB"),
    ("julien_tigre_bengale3.jpg", "18z5A5GxaxJriBq4PnZtYhCYUgXmsYiTd"),
    ("julien_elephant_mere_petit.jpg", "1GtsXVXPSVpFh7IStFHQNf7hssXSexRMh"),
    ("julien_elephant_jungle.jpg", "1FSPlorKvUGrPeXFH0ak_jBJRdTif0Sot"),
    ("julien_gangetic_dolphin.jpg", "1CLTDW7lRvuuU4uMRu2hrS6tr4nlMbTJo"),
    ("julien_safari_a_pied.jpg", "1xVDJT_lN-KlMO5YAuJxUFv-k7UYl5J9o"),
    ("julien_photographes_jungle.jpg", "13e2RtR_sYmBslpB-8rWygHnWLM8G4--y"),
    ("julien_cerf_axis.jpg", "1QgH4TRZrg0h-HxbVa7ui-lAf3GoUOh1i"),
    ("julien_cerf_cochon.jpg", "1h_kNGPGA-iZVm7Nuu1Z62n8zBYC3nwP8"),
    ("julien_rollier_oiseau.jpg", "1kEgPb04eRxb3MXbFLW-w7gqdytjEpgXL"),

    # --- ANTOINE (Wilderness, Portraits & Nature) ---
    ("antoine_wild1.jpg", "1TmZpOJfEJ9lUj6grsI9vjk25UuCsTI1y"),
    ("antoine_wild2.jpg", "1X9O4j_auSWVjSzj0DlYblCQ9B1Y7ux7J"),
    ("antoine_wild3.jpg", "1i9DfqL_NpxrDQ1aTU5enfPXIZX0CBr38"),
    ("antoine_wild4.jpg", "1Wkvyt8M1XA5wCJ-OAWFyMAD_oe6jKDGF"),
    ("antoine_wild5.jpg", "1BPLF9UrosQTHaCRXgijLK6SU-d6vyT2D"),

    # --- FREDERIC (High-End DSLR Wildlife & Jungle Scenes) ---
    ("fred_wild1.jpg", "19Q0qe2hguWlj1igE0xlATLhajZ8C5oxh"),
    ("fred_wild2.jpg", "1gvZ0jkezZH0b2M9E5a1MCWWMdk6utPy0"),
    ("fred_wild3.jpg", "1g6hgpTZ1rI5JwWiWgJdkLT9DdUvJnxwD"),
    ("fred_wild4.jpg", "1bTS5-kUPVQpnc5kCEfdE8JZOjg01dbhz"),
    ("fred_wild5.jpg", "1IoYqGPyi0jce8Z8YYUEzm5s1_kMNEODA")
]

downloaded = 0
for filename, file_id in curated_photos:
    target_path = os.path.join(dest_dir, filename)
    if os.path.exists(target_path) and os.path.getsize(target_path) > 5000:
        downloaded += 1
        continue

    url = f"https://lh3.googleusercontent.com/d/{file_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 5000:
                with open(target_path, 'wb') as f:
                    f.write(data)
                downloaded += 1
                print(f"✓ Downloaded {filename} ({len(data)//1024} KB)")
            else:
                print(f"⚠ Skipping {filename}: response too small ({len(data)} bytes)")
    except Exception as e:
        print(f"✗ Failed {filename} ({file_id}): {e}")

print(f"\nSuccessfully downloaded {downloaded}/{len(curated_photos)} curated Drive photos into public/assets/drive_photos/!")
