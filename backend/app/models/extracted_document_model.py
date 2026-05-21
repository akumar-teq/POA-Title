from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base
from sqlalchemy import Boolean


class ExtractedDocument(Base):

    __tablename__ = "extracted_documents"

    id = Column(Integer, primary_key=True)

    homeowner = Column(String)
    lender = Column(String)
    loan_amount = Column(String)
    recording_date = Column(String)
    document_number = Column(String)

    raw_text = Column(Text)

    owelty = Column(Boolean, default=False)
    heloc = Column(Boolean, default=False)
    renewal_extension = Column(Boolean, default=False)
    cash_advance = Column(Boolean, default=False)