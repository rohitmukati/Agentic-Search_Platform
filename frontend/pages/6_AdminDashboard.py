# frontend/pages/AdminDashboard.py

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from auth import get_token, ensure_auth
from config import API_BASE_URL

# --- Auth & Page Setup ---
ensure_auth()
user = st.session_state.user
if not user.get("is_admin", False):
    st.error("🚫 Admin access only")
    st.stop()

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("🛠️ Admin Dashboard")

# --- 1) Fetch Overall Dashboard Data ---
res_overall = requests.get(
    f"{API_BASE_URL}/admin/dashboard",
    headers={"Authorization": f"Bearer {get_token()}"}
)
overall = res_overall.json()

# --- 2) Overall Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Users",    overall["total_users"])
col2.metric("🔍 Total Searches", overall["total_searches"])
col3.metric("📈 Total Leads",    overall["total_leads"])

# --- 3) Global Top-5 Charts ---
st.subheader("🌐 Global Top 5 Across All Users")

def render_bar(title, data):
    df = pd.DataFrame(data, columns=["name", "count"]).set_index("name")
    st.markdown(f"**{title}**")
    st.bar_chart(df["count"])

g1, g2, g3 = st.columns(3)
with g1:
    render_bar("📍 Top Countries",  overall["top_countries"])
with g2:
    render_bar("🏭 Top Industries", overall["top_industries"])
with g3:
    render_bar("🛠️ Top Services",   overall["top_services"])

# --- 4) Top Users by Searches ---
st.subheader("🏆 Top Users by Searches")
df_top = pd.DataFrame(overall["top_users"]).rename(columns={"count": "search_count"})
st.table(df_top[["name", "search_count"]])

# --- 5) All Users Overview & Per-User Analytics ---
st.subheader("🗂️ All Users Overview")
res_users = requests.get(
    f"{API_BASE_URL}/admin/users",
    headers={"Authorization": f"Bearer {get_token()}"}
)
users = res_users.json()
current_admin_id = user["id"]

for u in users:
    with st.expander(f"👤 {u['name']} — {u['searches']} searches, {u['leads']} leads"):
        cols = st.columns([4, 1, 1])
        cols[0].write(f"**User ID:** {u['user_id']}")
        cols[1].write(f"🔍 {u['searches']} searches")
        cols[1].write(f"📈 {u['leads']} leads")

        # View per-user analytics (pie charts)
        if cols[2].button("🔎 View Analytics", key=f"view_{u['user_id']}"):
            resp = requests.get(
                f"{API_BASE_URL}/admin/users/{u['user_id']}",
                headers={"Authorization": f"Bearer {get_token()}"}
            )
            details = resp.json()

            st.markdown(f"### 📊 Analytics for **{details['name']}**")
            st.write(f"- **Total Searches:** {details['total_searches']}")
            st.write(f"- **Total Leads:** {details['total_leads']}")

            def plot_pie(data, title):
                if not data:
                    st.write(f"No data for {title}")
                    return
                labels, sizes = zip(*data)
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
                ax.axis("equal")
                ax.set_title(title)
                st.pyplot(fig)

            p1, p2, p3 = st.columns(3)
            with p1:
                plot_pie(details["top_industries"], "🏭 Top Industries")
            with p2:
                plot_pie(details["top_countries"], "📍 Top Countries")
            with p3:
                plot_pie(details["top_services"], "🛠️ Top Services")

        # Delete with confirmation, only for non-admin others
        can_delete = (u["user_id"] != current_admin_id) and (not u.get("is_admin", False))
        if can_delete:
            del_key    = f"del_{u['user_id']}"
            conf_key   = f"confirm_{u['user_id']}"
            cancel_key = f"cancel_{u['user_id']}"

            if cols[2].button("❌ Delete User", key=del_key):
                st.session_state["pending_delete"] = u["user_id"]

            if st.session_state.get("pending_delete") == u["user_id"]:
                st.warning(f"⚠️ Are you sure you want to delete **{u['name']}** and ALL their data?")
                yes_col, no_col = st.columns(2)
                if yes_col.button("Yes, delete", key=conf_key):
                    requests.delete(
                        f"{API_BASE_URL}/admin/users/{u['user_id']}",
                        headers={"Authorization": f"Bearer {get_token()}"}
                    )
                    st.success(f"Deleted user **{u['name']}** and all their data")
                    del st.session_state["pending_delete"]
                if no_col.button("Cancel", key=cancel_key):
                    del st.session_state["pending_delete"]
                    st.info("Deletion cancelled")
        else:
            cols[2].write("🛑 Cannot delete admin")
