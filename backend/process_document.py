from app.services.ocr_service import extract_text_from_pdf

from app.services.ai_service import parse_document

from app.services.lien_classifier import (
    classify_lien,
    calculate_risk
)

from app.services.applega_service import (
    upload_document,
    update_matter_status
)

from app.services.document_service import save_document

from app.services.pdf_service import generate_summary_pdf


pdf_path = "storage/pdfs/sample.pdf"

matter_id = "TEST123"

upload_response = upload_document(
    "storage/reports/report.pdf",
    matter_id
)

print(upload_response)

update_matter_status(
    matter_id,
    "Completed"
)

# OCR Extraction
text = extract_text_from_pdf(pdf_path)


# AI Parsing
parsed = parse_document(text)


# Lien Classification
lien_results = classify_lien(text)


# Add lien results into parsed data
parsed.update(lien_results)


# Calculate risk level
risk_level = calculate_risk(lien_results)


# Add risk level to parsed data
parsed["risk_level"] = risk_level


# Save into database
save_document(parsed, text)


# Generate PDF
generate_summary_pdf(
    parsed,
    "storage/reports/report.pdf"
)


print(parsed)

text = extract_text_from_pdf(pdf_path)

print(text)

parsed = parse_document(text)
