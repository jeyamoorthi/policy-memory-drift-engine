import streamlit as st
import requests
import os

# Configurable API URL via environment variable
API_BASE = os.getenv("POLICY_API_URL", "http://localhost:9000")
API_URL = f"{API_BASE}/latest-with-recommendations"
HEALTH_URL = f"{API_BASE}/health"

st.set_page_config(page_title="Policy Impact Simulator", layout="centered")
st.title("🧠 Policy Impact Simulator")


# Check API connectivity on load
def check_api_health():
    """Check if the API is reachable."""
    try:
        res = requests.get(HEALTH_URL, timeout=5)
        return res.status_code == 200
    except:
        return False


# Show API status in sidebar
with st.sidebar:
    st.subheader("System Status")
    if check_api_health():
        st.success("✅ API Connected")
    else:
        st.error("❌ API Offline")
        st.caption(f"Expected at: {API_BASE}")


if st.button("Fetch Latest Policy Analysis"):
    try:
        res = requests.get(API_URL, timeout=10)
        res.raise_for_status()
        data = res.json()

        if "error" in data:
            st.error(f"Server Error: {data['error']}")
        elif "status" in data:
            st.warning("No policy data yet.")
        else:
            st.success("Latest Policy Signal Analyzed")

            st.metric("Signal", data["signal"])
            st.metric("Domain", data["domain"])
            st.metric("Impact Score", data["impact"])

            st.subheader("Affected Stakeholders")
            st.write(data["stakeholders"])

            if "recommendations" in data:
                st.subheader("AI Policy Recommendations")
                st.write(data["recommendations"])

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to API. Is the server running?")
        st.caption(f"Trying to reach: {API_URL}")
    except requests.exceptions.Timeout:
        st.error("⏳ API request timed out after 10 seconds")
    except requests.exceptions.HTTPError as e:
        st.error(f"❌ HTTP Error: {e.response.status_code}")
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
