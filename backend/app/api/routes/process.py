from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ocr_service import (
    extract_text_from_pdf
)

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

    # OCR
    text = extract_text_from_pdf(
        pdf_path
    )

    # AI Extraction
    parsed = parse_document(text)

    # Lien Classification
    lien_results = classify_lien(text)

    parsed.update(lien_results)

    # Risk Level
    parsed["risk_level"] = calculate_risk(
        lien_results
    )

    return parsed