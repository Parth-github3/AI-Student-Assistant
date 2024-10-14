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

cchain= ( ChatPromptTemplate.from_template("Create a hierarchal plan for studying these concepts {concepts} and represent it with flow chart. Also, explain the plan. ")
                      | llama
                      | StrOutputParser()
            )
basechain = ( ChatPromptTemplate.from_template("you are a expert analyst. Your task is to Analyzize the given text {txt} and find out the concepts covered in it.")
                      | llama
                      | StrOutputParser()
                      |{"concepts": RunnablePassthrough()}
)
conchain= (
    basechain
    | cchain
)

uploaded_files = st.file_uploader(
        "Choose a file", accept_multiple_files=True
    )
def concept():
    for file in uploaded_files:
        file_bytes = file.read()
        decoded_text = file_bytes.decode("utf-8")
    return decoded_text
txt = concept()

def download_response_as_pdf(bot_response):
    st.download_button(
        label="Download as file",
        data=bot_response,
        file_name="Ans_response.txt",
        #mime="application/pdf"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("submit"):
     message = st.chat_message("assistant")
     #message.write(cbt_chain.invoke(user_input))
     #st.session_state.messages.append({"role": "user", "content":})
     bot_response = conchain.invoke(txt)
     
     st.session_state.messages.append({"role": "assistant", "content": bot_response})
     download_response_as_pdf(bot_response)

for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.write(f"bot: {message['content']}")