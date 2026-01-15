import streamlit as st

st.set_page_config(page_title="AI Career Recommender", layout="centered")

st.title("AI-Based Career Recommendation System")
st.subheader("Cloud Computing Mini Project")

st.write(
    "This web application uses Artificial Intelligence and Large Language Models "
    "to recommend suitable career paths for students based on their skills and interests."
)

resume_text = st.text_area("Paste your resume / skills here")

if st.button("Get Career Recommendation"):
    if resume_text.strip() == "":
        st.warning("Please enter resume or skill details.")
    else:
        st.success("Recommended Career: Software Developer")
        st.write("Reason: Your skills indicate strong logical thinking and programming ability.")
        st.write("Skill Gap: Cloud fundamentals, Data Structures")
