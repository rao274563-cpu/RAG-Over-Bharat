# 🇮🇳 RAG Over Bharat

## Project Overview

RAG Over Bharat is a Gemini-powered Retrieval-Augmented Generation (RAG) application designed to help users interact with Indian Government documents and schemes through natural language questions.

The system allows users to upload PDF documents, automatically processes and indexes the content using semantic embeddings, and generates grounded answers using retrieved document context.

The objective is to make government information more accessible, searchable, and understandable through AI-powered document intelligence.

---

## Application Preview

### Features

* Upload Government PDF documents
* Automatic PDF text extraction
* Intelligent text chunking
* Semantic search using FAISS
* Gemini-powered answer generation
* Grounded responses using retrieved document context
* Source chunk citations
* Interactive Streamlit interface

---

## Live Demo

Deployment Link:

```text
Coming Soon
```

---

## Problem Statement

Government documents often contain large amounts of information that can be difficult to navigate manually.

RAG Over Bharat enables users to:

* Ask questions in natural language
* Retrieve relevant information instantly
* Reduce time spent searching lengthy PDFs
* Improve accessibility of public information

---

## System Architecture

```text
User Question
      │
      ▼
Uploaded PDF
      │
      ▼
PDF Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Gemini Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Vertex AI Gemini
      │
      ▼
Grounded Answer
      │
      ▼
Streamlit UI
```

---

## Key Features

### PDF Processing

* Extracts text from uploaded PDF files
* Supports government scheme documents and reports

### Semantic Search

* Uses Gemini Embedding Model
* Creates vector representations of document chunks
* Retrieves contextually relevant information

### Retrieval-Augmented Generation (RAG)

* Retrieves top relevant chunks
* Sends retrieved context to Gemini
* Generates grounded answers

### Source Citations

* Displays retrieved chunks used to generate answers
* Improves transparency and trustworthiness

### Interactive UI

* Built using Streamlit
* User-friendly and responsive interface

---

## Technologies Used

### Artificial Intelligence

* Gemini 2.5 Flash
* Gemini Embedding Model

### Google Cloud Platform

* Vertex AI
* Google Cloud

### Backend

* Python

### Retrieval System

* FAISS Vector Database

### Frontend

* Streamlit

### PDF Processing

* PyPDF2

### Data Handling

* NumPy
* Pandas

---

## Dataset Information

### Sample Document Used

Prime Minister Internship Scheme (PMIS) PDF

The application supports any government PDF document uploaded by the user.

---

## Project Structure

```text
RAG-Over-Bharat/

├── app.py

├── rag.py

├── requirements.txt

├── .env

├── README.md

└── assets/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/rao274563-cpu/RAG-Over-Bharat.git

cd RAG-Over-Bharat
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## Workflow

1. Upload PDF document
2. Extract text from PDF
3. Split text into chunks
4. Generate embeddings
5. Create FAISS vector index
6. Ask a question
7. Retrieve relevant chunks
8. Generate grounded answer using Gemini
9. Display answer with sources

---

## Future Improvements

* Hindi and English language support
* Multiple PDF support
* Chat history
* Cloud Storage integration
* Vertex AI Vector Search
* Government Scheme Knowledge Base
* PDF highlighting and page references
* Multi-document retrieval

---

## Author

### Sachin Kumar Rao

GitHub:
https://github.com/rao274563-cpu

LinkedIn:
https://www.linkedin.com/in/sachin-rao-535b0b331

---

## Acknowledgements

* Google Gemini
* Vertex AI
* Google Cloud Platform
* Streamlit
* FAISS
* Gemini Hackday.EXE 2.0

---

If you found this project useful, please consider giving the repository a ⭐.
