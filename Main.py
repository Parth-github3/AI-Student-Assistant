import streamlit as st


pages = {
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


pg = st.navigation(pages)
pg.run()