# Step 2 : Streamlit skleton creation
import streamlit as st
from rag import extract_text_from_pdf, chunk_text
from rag import(
    extract_text_from_pdf,
    chunk_text,
    create_vector_store
)

st.set_page_config(
    page_title="RAG Over Bharat",
    page_icon="IN",
    layout="wide"
)

st.title("🇮🇳 RAG Over Bharat")

# st.markdown("""
# Ask questions about Indian Government Schemes and documents using Gemini-powered RAg
# """)

uploaded_file = st.file_uploader(
    "Uploaded a PDF",
    type=["pdf"]
)

# user_question = st.text_input(
#     "Ask a question"
# )

# if uploaded_file:
#     st.success(f"Uploaded file: {uploaded_file.name}")

# if user_question:
#     st.write(f"Question: {user_question}")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(text)

    st.success("PDF Processed successfully!")
    st.write(f"Total Chunks Created: {len(chunks)}")
    vector_store = create_vector_store(chunks)

    st.success("Vector store created successfully!")
