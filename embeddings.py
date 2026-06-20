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

import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def get_embedding(text):
    result = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return result["embedding"]