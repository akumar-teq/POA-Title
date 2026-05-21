from app.services.ocr_service import extract_text_from_pdf

text = extract_text_from_pdf(
    "storage/pdfs/sample.pdf"
)

print(text)
