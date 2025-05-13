import google.generativeai as genai
from pdf_text_chunker import extract_text_from_pdf, chunk_text

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-pro-latest')

def ask_gemini(model, prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    API_KEY = "AIzaSyDxsZ7llhXOT9HzG9bCPZ4p0xGxBEMNYAQ"  # <-- Replace with your actual key
    PDF_PATH = "sample.pdf"

    model = setup_gemini(API_KEY)
    text = extract_text_from_pdf(PDF_PATH)
    chunks = chunk_text(text, max_tokens=500)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Gemini Output for Chunk {i+1} ---")
        response = ask_gemini(model, f"Summarize the following text:\n\n{chunk}")
        print(response)
