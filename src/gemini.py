import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# LangChain wrapper for Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

def call_gemini(prompt: str) -> str:
    """Call Gemini LLM with a prompt and return text."""
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text
