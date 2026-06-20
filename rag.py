from PyPDF2 import PdfReader

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