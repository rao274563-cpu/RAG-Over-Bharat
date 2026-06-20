# Step5: Embeddings
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AQ.Ab8RN6LAHZJetysD1qlpFsfIJFTqreIu5aROirIR2w0tgEfjwA")
)

def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents = text
    )

    return response.embeddings[0].values