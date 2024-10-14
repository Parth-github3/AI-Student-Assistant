import streamlit as st


pages = {
    "Que": [
        st.Page("Assistant.py", title="que "),
        
    ],
    "Ans": [
        st.Page("Answer.py", title="ans"),

    ],
    "Concept": [
        st.Page("PL.py", title="Concept"),

    ],
}

if st.button("Que"):
    st.switch_page("Assistant.py")
if st.button("Ans"):
    st.switch_page("pages/Answer.py")
    st.session_state.clear()

pg = st.navigation(pages)
pg.run()