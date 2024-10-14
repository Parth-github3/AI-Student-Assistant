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
    st.switch_page("pages/Que.py")
if st.button("Ans"):
    st.switch_page("pages/Ans.py")
    st.session_state.clear()

pg = st.navigation(pages)
pg.run()