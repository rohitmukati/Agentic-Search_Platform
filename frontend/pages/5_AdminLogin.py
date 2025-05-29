import streamlit as st
from auth import login, get_token, set_token

st.title("🔒 Admin Login")
if get_token() and st.session_state.user.get("is_admin"):
    st.success("Already logged in as Admin")
else:
    email = st.text_input("Admin Email")
    pwd = st.text_input("Password", type="password")
    if st.button("Login as Admin"):
        token = login(email, pwd)
        if token:
            st.session_state.token = token
            # fetch current user and check is_admin
            from auth import fetch_current_user
            st.session_state.user = fetch_current_user()
            if st.session_state.user.get("is_admin"):
                st.success("✅ Admin logged in")
            else:
                st.error("❌ Not an admin user")
        else:
            st.error("❌ Login failed")
