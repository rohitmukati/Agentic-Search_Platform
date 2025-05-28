import os
from dotenv import load_dotenv

load_dotenv()

# Point this to your FastAPI base URL (include /api)
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api")
