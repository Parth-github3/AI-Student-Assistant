#Requirements
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


#LLM Model
llama = ChatGroq(
    model="LLaMA3-70B-8192",
    groq_api_key='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',
    temperature=0.0
)

# Setting up chains
achain= ( ChatPromptTemplate.from_template("You are an intelligent ai made for assisting students for completing their assingnments. Generate informative answers  of minimum 700 words for every question in this assignment {que}")
                      | llama
                      | StrOutputParser()
            )
basechain = ( ChatPromptTemplate.from_template("you are a expert analyst. Your task is to Analyzize these questions {que} with their concepts.")
                      | llama
                      | StrOutputParser()
                      |{"base_response": RunnablePassthrough()}
)
anschain= (
    basechain
    | achain
)

# Getting user input
uploaded_files = st.file_uploader(
        "Note: Only upload the Question_response.txt file", accept_multiple_files=True
    )

# Function to extract text from files
def questions():
    decoded_text = []
    for file in uploaded_files:
        file_bytes = file.read()
        decoded_text = file_bytes.decode("utf-8")
    return decoded_text
que = questions()

# Function to download response
def download_response_as_pdf(bot_response):
    st.download_button(
        label="Download as file",
        data=bot_response,
        file_name="Ans_response.txt"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# Submit button action
if st.button("Submit"):
     message = st.chat_message("assistant")
     bot_response = achain.invoke(que)
     st.session_state.messages.append({"role": "assistant", "content": bot_response})
     download_response_as_pdf(bot_response)

for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.write(f"bot: {message['content']}")