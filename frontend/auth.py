import streamlit as st
import requests
from config import API_BASE_URL

def signup(name: str, email: str, password: str) -> str | None:
    """Call backend /auth/signup, return JWT or None."""
    try:
        res = requests.post(
            f"{API_BASE_URL}/auth/signup",
            json={"name": name, "email": email, "password": password},
        )
        res.raise_for_status()
        # FastAPI returns access_token only
        return res.json().get("access_token")
    except requests.RequestException:
        return None

def login(email: str, password: str) -> str | None:
    """Call backend /auth/login, return JWT or None."""
    try:
        res = requests.post(
            f"{API_BASE_URL}/auth/login",
            json={"email": email, "password": password},
        )
        res.raise_for_status()
        return res.json().get("access_token")
    except requests.RequestException:
        return None

def set_token(token: str):
    st.session_state.token = token

def get_token() -> str | None:
    return st.session_state.get("token")

def ensure_auth():
    if "token" not in st.session_state:
        st.error("🔒 Please login or sign up first.")
        st.stop()

def fetch_current_user() -> dict | None:
    """Retrieve the logged-in user's details from /auth/me."""
    token = st.session_state.get("token")
    if not token:
        return None
    try:
        res = requests.get(
            f"{API_BASE_URL}/auth/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        res.raise_for_status()
        return res.json()
    except requests.RequestException:
        return None