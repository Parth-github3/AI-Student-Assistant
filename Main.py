import streamlit as st


pages = {
    "Question": [
        st.Page("Que.py", title="Question"),
        
    ],
    "Answer": [
        st.Page("Answer.py", title="Answer"),

    ],
    "Concept-Learning Plan": [
        st.Page("PL.py", title="Concept-Learning Plan"),

    ],
}

if st.sidebar.button("Clear History"):
    st.session_state.clear()

def info(pages):
    match pages:
        case "Question":
            qinfo = "Enter pdf"
            return qinfo
        case "Answer":
            ainfo = "Enter text ile"
            return ainfo
st.sidebar.markdown(info(pages=pages))
pg = st.navigation(pages)
pg.run()