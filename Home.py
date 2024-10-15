import streamlit as st

st.markdown("""
### Hello students! Hope you find this app when your exam is near.\n
This app will make your exam preparations smooth as butter!\n
        There are 3 functions of this app:\n
            1. Question
            2. Answer
            3. Concept-Learning Plan
""")
st.header("How to use?")
with st.expander("About Question..."):
    st.markdown("""
    "Question" is a place where you upload your Past Year Question papers and get your imp questions in seconds.\n
    Input: Question papers(one or more) **Format:** PDF\n
    Task: It will generate you a list of questions which are repeated and catagorize it on concept base.\n
    Output: List of imp questions. Also, you can download it as a file.
    """)