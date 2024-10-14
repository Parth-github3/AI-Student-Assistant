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

class info:

        if pages == "Question":
            qinfo = "Enter pdf"
            st.sidebar.markdown(qinfo)
        elif pages == "Answer":
            ainfo = "Enter text ile"
            st.sidebar.markdown(ainfo)
st.sidebar.markdown("hi")
pg = st.navigation(pages)
pg.run()