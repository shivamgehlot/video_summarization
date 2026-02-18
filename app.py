import streamlit as st
from main import run_pipeline

st.title("AI Video Summarizer")

tab1, tab2 = st.tabs(["YouTube URL", "Upload Video"])

# URL 
with tab1:
    url = st.text_input("Paste YouTube URL")
    if st.button("Summarize URL"):
        with st.spinner("Processing video..."):
            result = run_pipeline(url=url)
        st.write(result)

# Upload 
with tab2:
    uploaded_file = st.file_uploader("Upload video", type=["mp4", "mkv", "mov", "avi"])
    if uploaded_file and st.button("Summarize Upload"):
        with st.spinner("Processing video..."):
            result = run_pipeline(uploaded_file=uploaded_file)
        st.write(result)

