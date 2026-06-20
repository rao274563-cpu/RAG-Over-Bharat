from PyPDF2 import PdfReader
import numpy as np
import faiss
from embeddings import get_embedding
import os
from dotenv import load_dotenv
#from google import genai
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# Step 3: PDF Extraction
def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PdfReader(pdf_file)
    
    for page in reader.pages:
        page_text = page.extract_text()
        
        if page_text:
            text += page_text + "\n"

    return text       

# Step 4. LLMs and embeddings work better on smaller chunks rather than entire PDFs. 

def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        
        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap
    return chunks    

def create_vector_store(chunks):
    embeddings = []

    for chunk in chunks:
        vector = get_embedding(chunk)
        embeddings.append(vector)

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )    

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)
    return index

def retrieve_relevant_chunks(
        question,
        index,
        chunks,
        k=3
):
    question_embedding = get_embedding(question)
    query_vector = np.array(
        [question_embedding],
        dtype = np.float32
    )

    distances, indices = index.search(
        query_vector,
        k
    )

    retrieved_chunks = []

    for idx in indices[0]:
        if idx < len(chunks):
            retrieved_chunks.append({
                "text": chunks[idx],
                "source": f"Chunk {idx + 1}"
            })
    return retrieved_chunks        

# Answer function
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(question, retrieved_chunks):
    context = "\n\n".join([chunk["text"] for chunk in retrieved_chunks])

    prompt = f"""
You are an AI assistant for Indian government schemes.

Use ONLY the context below to answer the question.
If answer is not in context, say "Not found in document".

Context:
{context}

Question:
{question}

Answer in a simple, clear, helpful way.
"""

    # response = client.models.generate_content(
    #     model="gemini-2.5-flash",
    #     contents=prompt
    # )

    # return response.text
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text