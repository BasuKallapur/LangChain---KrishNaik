from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API server"
)

# LLMs
llm1 = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash-lite-preview-06-17")
llm2 = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash")

# Prompts
prompt1 = ChatPromptTemplate.from_template("write me an essay on a topic {topic} around 200 words")
prompt2 = ChatPromptTemplate.from_template("write me a poem on a topic {topic} around 200 words")

# Routes
add_routes(app, llm1, path="/gemini_ai") 
add_routes(app, prompt1 | llm1, path="/essay")
add_routes(app, prompt2 | llm2, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)