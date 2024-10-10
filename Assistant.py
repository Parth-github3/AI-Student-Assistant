#Requirements
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

#LLM Model
llama = ChatGroq(
    model="LLaMA3-70B-8192",
    groq_api_key='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',
    temperature=0.0
)


base_summary_chain = (
    ChatPromptTemplate.from_template("""
Provide answers for the following list of questions with explapaination and also track which questions are repeated.
""")
    | llama
    | StrOutputParser()
    #|{"base_response": RunnablePassthrough()}
    )

    
    


# Title of the app
st.title("AI by PARTH")

# Introduction text


# Sidebar for additional information


    
    


# Get user input

# Load Groq compiled LLaMA model (replace with your actual model path)
@st.cache_resource

def generate_response(userinput):
    return base_summary_chain.invoke(userinput)
     

if "messages" not in st.session_state:
        st.session_state.messages = []

# getting User input
userinput = st.chat_input("Say something")
with st.chat_message("user"):
        st.write(userinput)

if userinput:
    message = st.chat_message("assistant")
    #message.write(cbt_chain.invoke(user_input))
    st.session_state.messages.append({"role": "user", "content": userinput})
    bot_response = generate_response(userinput)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Bot: {message['content']}")