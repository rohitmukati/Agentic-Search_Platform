import os

BASE = "frontend"
PAGES = ["1_Dashboard.py", "2_Search.py", "3_Leads.py", "4_Logs.py"]
ROOT_FILES = ["app.py", "auth.py", "api.py", "utils.py", "config.py", "requirements.txt"]

# Create root and pages folder
os.makedirs(BASE, exist_ok=True)
os.makedirs(f"{BASE}/pages", exist_ok=True)

# Create root files
for filename in ROOT_FILES:
    path = os.path.join(BASE, filename)
    with open(path, "w") as f:
        f.write("")  # placeholder
    print(f"Created {path}")

# Create page files
for page in PAGES:
    path = os.path.join(BASE, "pages", page)
    with open(path, "w") as f:
        f.write("")  
    print(f"Created {path}")

print("✅ Frontend structure generated.")
