import os

# Define the folder and files structure directly in current directory
project_structure = {
    "backend": {
        "routes": ["auth.py", "leads.py", "search.py"],
        "services": ["agent_controller.py", "google_agent.py", "linkedin_agent.py", "email_validator.py"],
        "files": ["main.py", "database.py", "models.py", "schemas.py", "requirements.txt"]
    },
    "frontend": {
        "pages": ["login.jsx", "signup.jsx", "dashboard.jsx", "leads.jsx"],
        "components": ["SearchForm.jsx", "LeadsTable.jsx", "Filters.jsx", "DownloadButton.jsx"],
        "services": ["api.js"]
    },
    "ai_agents": {
        "files": ["agent_controller.py", "google_scraper.py", "linkedin_scraper.py", "rfpio_scraper.py"]
    },
    "files": [".env", "README.md"]
}

# Function to create folders and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if name == "files":
            for file_name in content:
                open(os.path.join(base_path, file_name), 'a').close()
        elif isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                open(os.path.join(path, file_name), 'a').close()

def setup_project():
    base_path = os.getcwd()
    create_structure(base_path, project_structure)
    print("✅ Project structure created directly in current folder!")

if __name__ == "__main__":
    setup_project()
