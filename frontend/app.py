import streamlit as st
from auth import login, signup, set_token, get_token, fetch_current_user
from config import API_BASE_URL

st.set_page_config(page_title="Agentic Leads", layout="wide")

# --- If user is already authenticated ---
if get_token():
    # Ensure we have the user object in session
    if "user" not in st.session_state:
        st.session_state.user = fetch_current_user() or {}

    user = st.session_state.user

    # Sidebar: My Profile + Logout
    st.sidebar.header("👤 My Profile")
    if user.get("name"):
        st.sidebar.markdown(f"**Hello, {user['name']}!**")
    else:
        st.sidebar.markdown("**Hello!**")

    if st.sidebar.button("Logout"):
        st.session_state.clear()

    # Main welcome area
    st.markdown("# 🎉 Welcome to Agentic Leads Dashboard!")
    st.markdown(
        """
        You’re all set to generate and manage high-quality leads.  
        🚀 Run a search to discover new opportunities.  
        📊 Track your top searches and services on the Dashboard.  
        💾 Export your leads to CSV with one click.
        """
    )
    st.markdown(
    """
    <div style="text-align:center;">
      <svg width="120" height="120" viewBox="0 0 24 24" fill="#4F46E5">
        <path d="M5 4v16h14V4H5zm12 14H7V6h10v12z"/>
        <path d="M9 8h6v2H9zm0 4h6v2H9z"/>
      </svg>
      <p style="font-size:18px;">Agentic Leads</p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- If user is not authenticated: show Login/Sign-Up ---
else:
    st.title("🔐 Welcome! Please Sign Up or Log In")
    choice = st.radio("Choose an action:", ("Login", "Sign Up"))

    if choice == "Sign Up":
        st.subheader("🆕 Create a new account")
        name = st.text_input("Full Name", key="su_name")
        email = st.text_input("Email", key="su_email")
        pwd = st.text_input("Password", type="password", key="su_pwd")
        if st.button("Sign Up"):
            token = signup(name, email, pwd)
            if token:
                set_token(token)
                # Immediately fetch and store user info
                st.session_state.user = fetch_current_user() or {}
                st.success("✅ Account created! Welcome aboard.")
            else:
                st.error("❌ Sign-up failed. Email might already be registered.")

    else:
        st.subheader("🔑 Log in to your account")
        email = st.text_input("Email", key="li_email")
        pwd = st.text_input("Password", type="password", key="li_pwd")
        if st.button("Login"):
            token = login(email, pwd)
            if token:
                set_token(token)
                # Immediately fetch and store user info
                st.session_state.user = fetch_current_user() or {}
                st.success("✅ Logged in successfully!")
            else:
                st.error("❌ Login failed. Please check your credentials.")
