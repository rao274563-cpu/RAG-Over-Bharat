# Step1
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("AQ.Ab8RN6LAHZJetysD1qlpFsfIJFTqreIu5aROirIR2w0tgEfjwA")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Explain Retrieval Augmented Generation in one sentence."
)

print(response.text)