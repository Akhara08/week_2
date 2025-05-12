import fitz  # PyMuPDF

def extract_pdf_text(filepath):
    """Extracts and returns all text from a PDF file."""
    text = ""
    with fitz.open(filepath) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

# Example usage
if __name__ == "__main__":
    path = "sample.pdf"  # Make sure this file exists
    result = extract_pdf_text(path)
    print("Extracted PDF Text:\n", result)
