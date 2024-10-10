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

def Assistant():
    base_summary_chain = (
    ChatPromptTemplate.from_template("""
Provide answers for the following list of questions with explapaination and also track which questions are repeated:{topic}
""")
    | llama
    | StrOutputParser()
    |{"base_response": RunnablePassthrough()}
    )
    res =base_summary_chain.invoke(userinput)
    return res


# Title of the app
st.title("AI by PARTH")

# Introduction text
with st.expander("About app..."):
    st.write("""
        Welcome to your Personal Health Partner (PHP) ! 
        My AI-powered (by LLaMA 3 70B) app is designed to provide you with reliable and accessible health information at your fingertips.\n
        This app compiles every field of your life, you want guidance for. Areas such as Health- Mental, Physical are coverd.\n
        Whether you have a specific health query or simply want to learn more about wellness,  PHP is here to assist you.\n
    """)

# Sidebar for additional information


    
    


# Get user input

# Load Groq compiled LLaMA model (replace with your actual model path)
@st.cache_resource

def yoo():
     var= ""

if "messages" not in st.session_state:
    st.session_state.messages = []

userinput = st.chat_input("Say something")
with st.chat_message("user"):
        st.write(userinput)

if userinput:
    message = st.chat_message("assistant")
    #message.write(cbt_chain.invoke(user_input))
    st.session_state.messages.append({"role": "user", "content": userinput})
    bot_response = Assistant(userinput)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# with st.chat_message:
#     user_input = st.text_input("You: ", key="user_input", help="Type your message and press Enter")

# If user has input a message, update the chat history and get response
# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     bot_response = cbt_chain.invoke(user_input)
#     st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Bot: {message['content']}")