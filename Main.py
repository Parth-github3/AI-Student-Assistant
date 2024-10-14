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

pg = st.navigation(pages)
pg.run()