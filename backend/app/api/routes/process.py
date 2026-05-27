from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import os
from app.services.ocr_service import (
    extract_text_from_pdf,
    claude_ocr
)
from app.services.pdf_service import generate_summary_pdf

from app.services.ai_service import (
    parse_document
)

from app.services.lien_classifier import (
    classify_lien,
    calculate_risk
)

router = APIRouter()


class ProcessRequest(BaseModel):

    pdf_path: str


@router.post("/process")
def process_document(
    request: ProcessRequest
):

    pdf_path = request.pdf_path

    try:
        # Handle OCR based on file type
        ext = os.path.splitext(pdf_path)[1].lower()
        if ext in ['.png', '.jpg', '.jpeg']:
            text = claude_ocr(pdf_path)
        else:
            text = extract_text_from_pdf(pdf_path)

        # AI Extraction
        parsed = parse_document(text)

        # Lien Classification
        lien_results = classify_lien(text)

        parsed.update(lien_results)

        # Risk Level
        parsed["risk_level"] = calculate_risk(
            lien_results
        )

        # Make sure to update the static report PDF so the download reflects the current document
        os.makedirs("storage/reports", exist_ok=True)
        generate_summary_pdf(parsed, "storage/reports/report.pdf")

        return parsed
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))