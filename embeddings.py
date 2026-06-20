# # Step5: Embeddings
# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# def get_embedding(text):
#     response = client.models.embed_content(
#         model="gemini-embedding-001",
#         contents = text
#     )

#     return response.embeddings[0].values

# Step5: Embeddings
import os
from dotenv import load_dotenv
from google import genai
import streamlit as st

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_embedding(text):
    try:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values

    except Exception as e:
        st.error(f"Embedding Error: {repr(e)}")
        raise