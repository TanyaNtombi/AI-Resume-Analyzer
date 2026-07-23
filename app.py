import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")
st.write("Welcome to your AI Resume Analyzer!")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)", type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description"
)

if st.button("Analyze Resume"):
    if uploaded_file and job_description:
        st.success("Everything is working! 🎉")
    else:
        st.warning("Please upload a resume and paste a job description.")