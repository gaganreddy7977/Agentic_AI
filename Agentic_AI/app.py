import streamlit as st
import os
from agents.orchestrator import OrchestratorAgent

st.set_page_config(page_title="Agentic AI Analyzer", layout="centered")

st.title("📊 Agentic AI Data Analyzer")

st.write("Upload a CSV or Excel file to generate AI analysis report.")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)

orch = OrchestratorAgent()

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully")

    if st.button("Generate PDF Report"):

        with st.spinner("Analyzing data..."):

            pdf_path = orch.run_file_pipeline(file_path)

        st.success("Report Generated!")

        st.download_button(
            label="Download PDF",
            data=open(pdf_path, "rb"),
            file_name=os.path.basename(pdf_path),
            mime="application/pdf"
        )