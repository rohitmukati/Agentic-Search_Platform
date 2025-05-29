import streamlit as st
import requests
import pandas as pd
from auth import login, signup, set_token, get_token, fetch_current_user
from config import API_BASE_URL

st.set_page_config(page_title="Agentic Leads", layout="wide")


# ---------------------------- AUTHENTICATED SECTION ----------------------------

if get_token():
    if "user" not in st.session_state:
        st.session_state.user = fetch_current_user() or {}

    user = st.session_state.user
    is_admin = user.get("is_admin", False)

    st.sidebar.header("👤 My Profile")
    st.sidebar.markdown(f"**Hello, {user['name']}!**")
    if st.sidebar.button("Logout"):
        st.session_state.clear()

    if is_admin:
        st.title("🛠️ Admin Dashboard")

        # # 1. Overall Analytics
        # res = requests.get(f"{API_BASE_URL}/admin/dashboard", headers={"Authorization": f"Bearer {get_token()}"})
        # data = res.json()

        # col1, col2, col3 = st.columns(3)
        # col1.metric("👥 Total Users", data["total_users"])
        # col2.metric("🔍 Total Searches", data["total_searches"])
        # col3.metric("📈 Total Leads", data["total_leads"])

        # # 2. Top Users
        # st.subheader("🏆 Top Users by Searches")
        # df_top = pd.DataFrame(data["top_users"])
        # st.table(df_top)

        # # 3. All Users List
        # st.subheader("🗂️ All Users Overview")
        # users = requests.get(f"{API_BASE_URL}/admin/users", headers={"Authorization": f"Bearer {get_token()}"}).json()

        # for u in users:
        #     with st.expander(f"👤 {u['name']} ({u['searches']} searches)"):
        #         col1, col2, col3 = st.columns([4, 3, 2])
        #         col1.write(f"**User ID**: {u['user_id']}")
        #         col2.write(f"🔍 Searches: {u['searches']}")
        #         col2.write(f"📈 Leads: {u['leads']}")
                
        #         if col3.button("View Analytics", key="view_" + u["user_id"]):
        #             details = requests.get(f"{API_BASE_URL}/admin/users/{u['user_id']}", headers={"Authorization": f"Bearer {get_token()}"}).json()
        #             st.json(details)

        #         if col3.button("❌ Delete User", key="del_" + u["user_id"]):
        #             requests.delete(f"{API_BASE_URL}/admin/users/{u['user_id']}", headers={"Authorization": f"Bearer {get_token()}"})
        #             st.success(f"Deleted user {u['name']}")
        
        st.markdown("# 🎉 Welcome to Agentic Leads Dashboard!")
        st.markdown(
            """
            You’re all set to manage the entire Agentic Leads platform.  
            🤖 **Admin Quick Actions**  
            - 🚀 **Run a Search**: Kick off lead-generation jobs for any user.  
            - 📊 **Platform Analytics**: Monitor global KPIs—top users, countries, industries, and services.  
            - 🗂️ **User Management**: Approve, deactivate, or delete accounts safely.  
            - 🔔 **Audit Logs**: Review every search query and export logs for compliance.  
            - 🛡️ **Security Controls**: Rotate API keys, enforce password policies, and view login history.  
            - 📥 **Export Data**: Download CSVs of leads, logs, or user lists on demand.  
            - ⚙️ **Configuration**: Tune your agents’ search parameters and global settings.  
            - 🎉 **Stay Informed**: Get notified of new users, failed searches, or quota limits.  
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
                    
    else:
        # 🧑‍💼 Regular User Dashboard
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


# ---------------------------- UNAUTHENTICATED SECTION ----------------------------

else:
    st.title("🔐 Welcome! Please Sign Up or Log In")
    choice = st.radio("Choose an action:", ("Login", "Sign Up", "Admin Login"))

    if choice == "Sign Up":
        st.subheader("🆕 Create a new account")
        name = st.text_input("Full Name", key="su_name")
        email = st.text_input("Email", key="su_email")
        pwd = st.text_input("Password", type="password", key="su_pwd")
        if st.button("Sign Up"):
            token = signup(name, email, pwd)
            if token:
                set_token(token)
                st.session_state.user = fetch_current_user() or {}
                st.success("✅ Account created! Welcome aboard.")
                
            else:
                st.error("❌ Sign-up failed. Email might already be registered.")

    elif choice == "Login":
        st.subheader("🔑 Log in to your account")
        email = st.text_input("Email", key="li_email")
        pwd = st.text_input("Password", type="password", key="li_pwd")
        if st.button("Login"):
            token = login(email, pwd)
            if token:
                set_token(token)
                st.session_state.user = fetch_current_user() or {}
                st.success("✅ Logged in successfully!")
                
            else:
                st.error("❌ Login failed. Please check your credentials.")

    elif choice == "Admin Login":
        st.subheader("🛡️ Admin Access Only")
        email = st.text_input("Admin Email", key="ad_email")
        pwd = st.text_input("Password", type="password", key="ad_pwd")
        if st.button("Admin Login"):
            token = login(email, pwd)
            if token:
                set_token(token)
                st.session_state.user = fetch_current_user() or {}
                if st.session_state.user.get("is_admin"):
                    st.success("✅ Admin access granted")
                    
                else:
                    st.error("⚠️ You are not an admin")
            else:
                st.error("❌ Login failed. Try again.")
