import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI DevOps Analyzer", layout="wide")

st.title("🧠 AI DevOps Log Analyzer")
# ------------------------
# Upload Logs
# ------------------------

st.header("📂 Upload Logs")

log_input = st.text_area("Paste your logs here", height=200)

if st.button("Upload Logs"):
    if log_input.strip():
        res = requests.post(
            f"{API_URL}/upload",
            json={"log": log_input}
        )
        st.success("Logs uploaded successfully ✅")
    else:
        st.warning("Please enter logs")

# ------------------------
# Query Section
# ------------------------

st.header("🔍 Ask Questions")

query = st.text_input("Ask something about logs")

if st.button("Analyze"):
    if query.strip():
        with st.spinner("Analyzing logs..."):
            res = requests.post(
                f"{API_URL}/query",
                json={"query": query}
            )

            data = res.json()

            st.subheader("🧠 AI Analysis")

            answer = data.get("answer")

            # Try structured output
            try:
                import json
                parsed = json.loads(answer)

                st.success(f"Summary: {parsed.get('summary')}")
                st.error(f"Root Cause: {parsed.get('root_cause')}")
                st.info(f"Fix: {parsed.get('fix')}")
                st.warning(f"Severity: {parsed.get('severity')}")

            except:
                st.write(answer)

    else:
        st.warning("Enter a query")
