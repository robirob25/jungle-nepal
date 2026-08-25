import os, glob

# List of root python migration/patch scripts to move into a clean build_tools/ or internal folder
# so the GitHub repository root stays 100% clean and professional like a top-tier open-source SaaS!

root_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
tools_dir = os.path.join(root_dir, 'tools')
os.makedirs(tools_dir, exist_ok=True)

py_files = [f for f in os.listdir(root_dir) if f.endswith('.py') and f != 'ensure_dual_routes.py']
html_tests = [f for f in os.listdir(root_dir) if f.startswith('test_') and f.endswith('.html')]

moved_count = 0
for f in py_files + html_tests:
    src_path = os.path.join(root_dir, f)
    dst_path = os.path.join(tools_dir, f)
    os.rename(src_path, dst_path)
    moved_count += 1

print(f"✓ Moved {moved_count} temporary utility scripts into tools/ directory!")
