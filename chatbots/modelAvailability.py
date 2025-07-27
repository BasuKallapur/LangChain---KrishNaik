import os
from dotenv import load_dotenv
from google.generativeai import list_models
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get the actual API key value from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
for m in list_models():
    print(m.name, m.supported_generation_methods)
