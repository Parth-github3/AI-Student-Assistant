import streamlit as st

st.title("AI EXAM PREPPER by PARTH")

pages = {
    "Home": [
        st.Page("Home.py", title="Welcome!"),
    ],
    "Question": [
        st.Page("Que.py", title="Upload your PYQ papers."),
        
    ],
    "Answer": [
        st.Page("Answer.py", title="Enter the question text file."),

    ],
    "Concept-Learning Plan": [
        st.Page("PL.py", title="Enter the question text file."),

    ],
}

if st.sidebar.button("Clear History"):
    st.session_state.clear()

class info:
    if pages == "Question":
        st.sidebar.markdown("ji")

pg = st.navigation(pages)
pg.run()