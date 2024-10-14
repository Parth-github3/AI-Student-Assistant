#Requirements
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate ,PromptTemplate
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from io import StringIO

llama = ChatGroq(
    model="LLaMA3-70B-8192",
    groq_api_key='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',
    temperature=0.0
)

achain= ( ChatPromptTemplate.from_template("Provide responses for all the given questions with detail explanations by understang the concepts {base_response}. You shall continue until you finish every concept.")
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

uploaded_files = st.file_uploader(
        "Choose a file", accept_multiple_files=True
    )
def questions():
    for file in uploaded_files:
        file_bytes = file.read()
        decoded_text = file_bytes.decode("utf-8")
    return decoded_text
que = questions()

def download_response_as_pdf(bot_response):
    st.download_button(
        label="Download as file",
        data=bot_response,
        file_name="chatbot_response.txt",
        #mime="application/pdf"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("submit"):
     message = st.chat_message("assistant")
     #message.write(cbt_chain.invoke(user_input))
     #st.session_state.messages.append({"role": "user", "content":})
     bot_response = anschain.invoke(que)
     
     st.session_state.messages.append({"role": "assistant", "content": bot_response})
     download_response_as_pdf(bot_response)
