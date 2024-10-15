import streamlit as st

# Title
st.title("AI EXAM PREPPER by PARTH\n &mdash; :books::magic_wand::sparkles:")

# Pages defined Home, Question, Answer, Concept-Learning Plan
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

#Clear history button
st.sidebar.markdown("""
                    **This button will clear the response history.** &mdash; :point_down:\n 
                    Recommended if you are switching pages.
                    """)
if st.sidebar.button("Clear History"):
    st.session_state.clear()

# Navigation page execution
pg = st.navigation(pages)
pg.run()