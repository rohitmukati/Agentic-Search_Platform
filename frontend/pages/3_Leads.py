import streamlit as st
from api import fetch_leads
from utils import to_df
from auth import ensure_auth
import pandas as pd

st.set_page_config(page_title="Leads", layout="wide")
ensure_auth()

st.title("📬 Leads Table")

# Fetch leads data
leads = fetch_leads()
if not leads:
    st.info("No leads found.")
    st.stop()

# Convert to DataFrame and parse dates
df = to_df(leads)
if "created_at" in df.columns:
    df["created_at"] = pd.to_datetime(df["created_at"])

# Sort control
sort_order = st.selectbox(
    "Sort by Date Created:",
    options=["Latest first", "Earliest first"]
)
ascending = True if sort_order == "Earliest first" else False
df = df.sort_values("created_at", ascending=ascending)

# Display table
st.dataframe(df, use_container_width=True)

# CSV Export
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Export Leads to CSV",
    data=csv,
    file_name="leads_sorted.csv",
    mime="text/csv"
)
