# app/routers/upload.py
from fastapi import APIRouter, UploadFile, File
from app.services.analyze import analyze_csv
from app.services.pdf_extractor import extract_text_from_pdf
from io import BytesIO
import pandas as pd
from fastapi.responses import StreamingResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    # Read the CSV file into a DataFrame
    contents = await file.read()
    df = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))

    # Analyze the CSV file using the service function
    analysis = analyze_csv(df)

    # Create PDF in memory with the analysis result
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "CSV Analysis Summary")
    c.drawString(100, height - 120, f"Summary: {analysis}")

    y_position = height - 140
    for line in analysis.split("\n"):
        c.drawString(100, y_position, line)
        y_position -= 20

    c.showPage()
    c.save()

    # Seek to the beginning of the buffer so it can be served
    pdf_buffer.seek(0)

    # Return the PDF as a response (StreamingResponse)
    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=analysis_report.pdf"})

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Read PDF file content
    pdf_content = await file.read()

    # Extract text from the PDF using the PDF extraction service
    extracted_text = extract_text_from_pdf(pdf_content)

    # Return extracted text as a response (could also save it, process it, or display)
    return {"extracted_text": extracted_text}
