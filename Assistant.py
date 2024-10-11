#Requirements
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate ,PromptTemplate
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
    ChatPromptTemplate.from_template("Provide answers for the following list of questions {questions} with explapaination and also track which questions are repeated.")
    | llama
    | StrOutputParser()
    #|{"base_response": RunnablePassthrough()}
)
basechain = (
    ChatPromptTemplate.from_template("You are a proficient ai developer who uses langchain for creating projects. Provide a project code as per the given project requirements {requirements} by the client.")
    | llama
    | StrOutputParser()
    #|{"base_response": RunnablePassthrough()}
)
    
import os
import pdfplumber

# # Set up the LangChain model
# llama

# # Define the prompt template for identifying questions
# question_prompt_template = PromptTemplate(
#     "Identify the questions in the following text:",
#     "{text}",
#     "Questions: {questions}"
# )

# # Define the prompt template for answering repeated questions
# answer_prompt_template = PromptTemplate(
#     "Answer the following repeated question:",
#     "{question}",
#     "Answer: {answer}"
# )

# # Load the PDF files
# pdf_files = [f for f in os.listdir("pdfs") if f.endswith(".pdf")]

# # Create a dictionary to store the questions and their frequencies
# questions_freq = {}

# # Process each PDF file
# for pdf_file in pdf_files:
#     with pdfplumber.open(f"pdfs/{pdf_file}") as pdf:
#         # Extract the text from the PDF
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()

#         # Identify the questions in the text
#         prompt = question_prompt_template.format(text=text)
#         response = llama(prompt)
#         questions = [q.strip() for q in response.split("Questions:")[1].splitlines() if q.strip()]

#         # Update the questions frequency dictionary
#         for question in questions:
#             if question not in questions_freq:
#                 questions_freq[question] = 1
#             else:
#                 questions_freq[question] += 1

# # Identify the repeated questions
# repeated_questions = [q for q, freq in questions_freq.items() if freq > 1]

# # Answer the repeated questions
# answers = {}
# for question in repeated_questions:
#     prompt = answer_prompt_template.format(question=question)
#     response = llama(prompt)
#     answers[question] = response.split("Answer:")[1].strip()

# # Print the answers
# for question, answer in answers.items():
#     print(f"Question: {question}")
#     print(f"Answer: {answer}")
#     print()
import os
import pdfplumber

# Set up the LangChain model
llama

# Define the prompt template for identifying questions
prompt = ( 
    PromptTemplate(template ="Identify the questions in the following text: {text} and only give the repeated Questions.")
    | llama
)


# Define the prompt template for answering repeated questions
aprompt = ( 
    PromptTemplate(template ="Answer the given questions in detail. Answer: {answer}")
    | llama
)
# Load the PDF files
#pdf_files = [f for f in os.listdir("pdfs") if f.endswith(".pdf")]

# Create a dictionary to store the questions and their frequencies
questions_freq = {}

# Process each PDF file
# for pdf_file in pdf_files:
#     with pdfplumber.open(f"pdfs/{pdf_file}") as pdf:
#         # Extract the text from the PDF
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()

        # Identify the questions in the text
        #prompt = question_prompt_template.format(text=text)
# response = prompt.invoke(text)
# questions = response#[q.strip() for q in response.split("Questions:")[1].splitlines() if q.strip()]

        # Update the questions frequency dictionary
        # for question in questions:
        #     if question not in questions_freq:
        #         questions_freq[question] = 1
        #     else:
        #         questions_freq[question] += 1

# Identify the repeated questions
repeated_questions = [q for q, freq in questions_freq.items() if freq > 1]

# # Answer the repeated questions
# answers = {}
# for question in questions:
#     #aprompt = answer_prompt_template.format(question=question)
#     aresponse = aprompt.invoke(question)
    #answers[question] = response.split("Answer:")[1].strip()

# Print the answers

# Title of the app
st.title("AI by PARTH")

# Introduction text


# Sidebar for additional information


    
    


# Get user input

# Load Groq compiled LLaMA model (replace with your actual model path)
@st.cache_resource

def generate_response(userinput):
    return basechain.invoke(userinput)
     
# if "messages" not in st.session_state:
#     st.session_state.messages = []

uploaded_files = st.file_uploader(
        "Choose a file", accept_multiple_files=True
    )

for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        with pdfplumber.open(uploaded_file) as pdf:
            # Extract the text from the PDF
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
                response = prompt.invoke(text)
                questions = response

        # Answer the repeated questions


            for question in questions:
        #aprompt = answer_prompt_template.format(question=question)
                answers = aprompt.invoke(question)
 
                st.write(answers)     
# getting User input
# userinput = st.chat_input("Say something")
# with st.chat_message("user"):
#         st.write(userinput)

# if userinput:
#     message = st.chat_message("assistant")
#     #message.write(cbt_chain.invoke(user_input))
#     st.session_state.messages.append({"role": "user", "content": userinput})
#     bot_response = ans(questions)
#     st.session_state.messages.append({"role": "assistant", "content": bot_response})


# # Display chat history
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.write(f"You: {message['content']}")
#     else:
#         st.write(f"Bot: {message['content']}")


