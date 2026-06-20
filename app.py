# Step 2 : Streamlit skleton creation
import streamlit as st
from rag import extract_text_from_pdf, chunk_text
from rag import(
    extract_text_from_pdf,
    chunk_text,
    create_vector_store,
    retrieve_relevant_chunks,
    generate_answer
)

st.set_page_config(
    page_title="RAG Over Bharat",
    page_icon="IN",
    layout="wide"
)

st.sidebar.title("🇮🇳 RAG Over Bharat")
st.sidebar.markdown("Upload PDF and ask question using Gemini AI")

st.divider()

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

    st.header("📄Processing Document")
    text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(text)

    st.success("PDF Processed successfully!")
    st.write(f"Total Chunks Created: {len(chunks)}")
    vector_store = create_vector_store(chunks)

    st.success("Vector store created successfully!")

    st.divider()
    
    st.header("❓Ask Questions")
    user_question = st.text_input(
        "Enter your question about the document"
    )

    if user_question:
        retrieved_chunks = retrieve_relevant_chunks(
            user_question,
            vector_store,
            chunks
        )
        st.divider()

        # st.subheader("Retrieved Context")
        # for i, chunk in enumerate(retrieved_chunk, start=1):
        #     st.write(f"Chunk{i}")   
        #     st.write(chunk[:1000])
        st.header("🤖 AI Response")
        with st.spinner("Thinking using Gemini + RAG..."):
            answer = generate_answer(
            user_question,
            retrieved_chunks
        )   

        st.subheader("📌Answer")
        st.markdown(answer)

        st.divider()

        st.subheader("📚 Sources Used")

        for chunk in retrieved_chunks:
            with st.expander(chunk["source"]):
                st.write(chunk["text"])