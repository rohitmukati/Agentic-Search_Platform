import streamlit as st
from api import get_dashboard_counts, fetch_analytics
from auth import ensure_auth
from utils import to_df
import pandas as pd

st.set_page_config(page_title="Dashboard", layout="wide")
ensure_auth()

st.title("📊 Dashboard Summary")

# 1️⃣ Total Counts
total_searches, total_leads = get_dashboard_counts()
col1, col2 = st.columns(2)
col1.metric("🔍 Total Searches", total_searches)
col2.metric("📈 Total Leads", total_leads)

# 2️⃣ Fetch detailed analytics
analytics = fetch_analytics()

# Convert top-n lists to DataFrames for charting
def to_chart_df(items):
    # items is a list of [key, count] pairs
    df = pd.DataFrame(items, columns=["name", "count"])
    df.index = df["name"]
    return df

kw_df = to_chart_df(analytics["top_keywords"])
ind_df = to_chart_df(analytics["top_industries"])
loc_df = to_chart_df(analytics["top_countries"])
srv_df = to_chart_df(analytics["top_services"])

# 3️⃣ Display bar charts in a 2×2 grid
st.subheader("Top 10 Searches & Categories")
chart_cols = st.columns(2)

with chart_cols[0]:
    st.markdown("**🔑 Top 10 Search Keywords**")
    st.bar_chart(kw_df["count"])

with chart_cols[1]:
    st.markdown("**🏭 Top 10 Industries**")
    st.bar_chart(ind_df["count"])

chart_cols = st.columns(2)
with chart_cols[0]:
    st.markdown("**📍 Top 10 Locations**")
    st.bar_chart(loc_df["count"])

with chart_cols[1]:
    st.markdown("**🛠️ Top 10 Services**")
    st.bar_chart(srv_df["count"])
