#Requirements
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import pdfplumber


#LLM Model
llama = ChatGroq(
    model="LLaMA3-70B-8192",
    groq_api_key='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',
    temperature=0.0
)


# Setting up chains

qchain= ( ChatPromptTemplate.from_template("Create and Provide a list of the repeated questions 'or' similar conceptual questions with their concept from the {base_response}. Also, If any questions are repeated then state their repetitions.")
                      | llama
                      | StrOutputParser()
                      #| {"q_response": RunnablePassthrough()}
                      
            )
basechain = ( ChatPromptTemplate.from_template("you are a expert analyst. Your task is to Analyzize these question papers {res} and find all the questions from each question paper according to their concept.")
                      | llama
                      | StrOutputParser()
                      |{"base_response": RunnablePassthrough()}
                      
            )

mainchainq = (
     basechain
     | qchain
)

# Load Groq compiled LLaMA model (replace with your actual model path)
@st.cache_resource


# Function to download response
def download_response_as_pdf(bot_response):
    st.download_button(
        label="Download as file",
        data=bot_response,
        file_name="Question_response.txt"
    )
     
if "messages" not in st.session_state:
    st.session_state.messages = []

# Getting user input
uploaded_files = st.file_uploader(
        "Upload your PYQ papers below. (Only .pdf is allowed)", accept_multiple_files=True
    )

# Function to extract text from files
def extract():
    
        extracted_text = []
        for file in uploaded_files:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    extracted_text.append(page.extract_text())
                   
        return extracted_text
res= extract()

# Submit button action
if st.button("Submit"):
     message = st.chat_message("assistant")
     bot_response = mainchainq.invoke(res)
     st.session_state.messages.append({"role": "assistant", "content": bot_response})
     download_response_as_pdf(bot_response)

# # Display chat history
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.write(f"bot: {message['content']}")



