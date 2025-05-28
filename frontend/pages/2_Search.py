import streamlit as st
from auth import ensure_auth
from api import run_search
from utils import to_df

st.set_page_config(page_title="Lead Search", layout="wide")
ensure_auth()

st.title("🔎 Lead Search")

# Initialize session state for results
if "search_results" not in st.session_state:
    st.session_state.search_results = None

# Build the search form
with st.form("search_form"):
    keywords = st.text_input("Keywords", key="sf_keywords")
    industry = st.text_input("Industry", key="sf_industry")
    country = st.text_input("Country", value="All", key="sf_country")
    services = st.text_area("Services (comma-separated)", key="sf_services")
    submitted = st.form_submit_button("Run Search")

# When the form is submitted, call the backend and show spinner
if submitted:
    payload = {
        "keywords": keywords.strip(),
        "industry": industry.strip(),
        "countries": country.strip(),
        # convert comma-separated string into a list of services
        "services": services.strip()
    }

    # Show loading spinner while awaiting the response
    with st.spinner("🔄 Searching for leads, please wait..."):
        try:
            results = run_search(payload)
            st.session_state.search_results = results
        except Exception as e:
            st.error(f"❌ Search failed: {e}")
            st.session_state.search_results = None

# If we have previous or new results, display them
if st.session_state.search_results:
    st.subheader(f"✅ Found {len(st.session_state.search_results)} Leads")
    df = to_df(st.session_state.search_results)
    st.dataframe(df, use_container_width=True)
    # Offer CSV export right under the table
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Export Leads to CSV",
        data=csv,
        file_name="leads_export.csv",
        mime="text/csv"
    )
