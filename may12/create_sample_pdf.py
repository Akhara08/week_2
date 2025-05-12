from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is a test PDF for ChromaDB.", ln=True)
pdf.cell(200, 10, txt="It has multiple lines of text.", ln=True)
pdf.output("sample.pdf")
