# app/services/pdf_extractor.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file: bytes):
    """
    Extracts text from a PDF file.

    Args:
    - pdf_file: byte data of the uploaded PDF file.

    Returns:
    - Extracted text as a string.
    """
    # Open the PDF file from bytes data
    pdf_document = fitz.open(stream=pdf_file, filetype="pdf")

    # Extract text from each page
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)  # page_num starts from 0
        text += page.get_text("text")  # Extract text in plain text format

    return text
