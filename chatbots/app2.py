#  USING Gemini Model

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user query."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("LangChain Gemini Chatbot (using Gemini Pro)")
inp_text = st.text_input("Please let me know your queries")

# Gemini LLM via LangChain
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-pro")

# Output parser
output_parser = StrOutputParser()

# LangChain pipeline
chain = prompt | llm | output_parser

# Handle user input
if inp_text:
    st.write(chain.invoke({'question': inp_text}))
