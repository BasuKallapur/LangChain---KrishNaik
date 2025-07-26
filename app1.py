#  USING OPEN AI Model

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template (Corrected spelling)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user query."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("LangChain demo with chatbot created using paid model")
inp_text = st.text_input("Please let me know your queries")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Output parser
output_parser = StrOutputParser()

# LangChain pipeline
chain = prompt | llm | output_parser

# Handle user input
if inp_text:
    st.write(chain.invoke({'question': inp_text}))
