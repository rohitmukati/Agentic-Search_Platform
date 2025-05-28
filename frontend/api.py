import requests
from config import API_BASE_URL
from auth import get_token

def _headers():
    token = get_token()
    return {"Authorization": f"Bearer {token}"} if token else {}

def get_dashboard_counts() -> tuple[int,int]:
    logs = requests.get(f"{API_BASE_URL}/searchlogs", headers=_headers()).json()
    leads = requests.get(f"{API_BASE_URL}/leads", headers=_headers()).json()
    return len(logs), len(leads)

def run_search(payload: dict) -> list[dict]:
    return requests.post(f"{API_BASE_URL}/search/run", json=payload, headers=_headers()).json()

def fetch_leads() -> list[dict]:
    return requests.get(f"{API_BASE_URL}/leads", headers=_headers()).json()

def fetch_logs() -> list[dict]:
    return requests.get(f"{API_BASE_URL}/searchlogs", headers=_headers()).json()

def fetch_analytics() -> dict:
    res = requests.get(f"{API_BASE_URL}/searchlogs/analytics", headers=_headers())
    res.raise_for_status()
    return res.json()
