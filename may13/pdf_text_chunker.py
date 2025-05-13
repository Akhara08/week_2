from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def chunk_text(text, max_tokens=500):
    max_chars = max_tokens * 4
    chunks = []
    for i in range(0, len(text), max_chars):
        chunk = text[i:i + max_chars]
        chunks.append(chunk)
    return chunks

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Replace with your PDF filename
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text, max_tokens=500)
    
    print(f"Extracted {len(chunks)} chunks.")
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---\n{chunk[:500]}...\n")  # Print first 500 chars of each chunk


