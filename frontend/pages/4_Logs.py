import streamlit as st
from api import fetch_logs
from utils import to_df
from auth import ensure_auth
import pandas as pd

st.set_page_config(page_title="Search Logs", layout="wide")
ensure_auth()

st.title("📜 Search Logs")

# Fetch logs data
logs = fetch_logs()
if not logs:
    st.info("No search logs found.")
    st.stop()

# Convert to DataFrame and parse timestamps
df = to_df(logs)
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort control
sort_order = st.selectbox(
    "Sort by Timestamp:",
    options=["Latest first", "Earliest first"]
)
ascending = True if sort_order == "Earliest first" else False
df = df.sort_values("timestamp", ascending=ascending)

# Display table
st.dataframe(df, use_container_width=True)

# (Optional) allow CSV export of logs too
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Export Logs to CSV",
    data=csv,
    file_name="logs_sorted.csv",
    mime="text/csv"
)
