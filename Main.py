import streamlit as st


pages = {
    "Que": [
        st.Page("Assistant.py", title="que "),
        
    ],
    "Ans": [
        st.Page("Answer.py", title="Learn about us"),

    ],
}

pg = st.navigation(pages)
pg.run()