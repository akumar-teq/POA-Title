from app.models.extracted_document_model import ExtractedDocument
from app.core.database import SessionLocal

def save_document(data, raw_text):

    db = SessionLocal()

    document = ExtractedDocument(
        homeowner=data.get("homeowner"),
        lender=data.get("lender"),
        loan_amount=data.get("loan_amount"),
        recording_date=data.get("recording_date"),
        document_number=data.get("document_number"),
        property_address=data.get("property_address"),
        county=data.get("county"),
        firm_file_no=data.get("firm_file_no"),
        raw_text=raw_text,
        owelty=data.get("owelty", False),
        heloc=data.get("heloc", False),
        renewal_extension=data.get("renewal_extension", False),
        cash_advance=data.get("cash_advance", False),
    )

    db.add(document)

    db.commit()

    db.close()
