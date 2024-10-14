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

st.write("hello")