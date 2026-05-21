from app.core.database import engine, Base

# Import ALL models
from app.models.request_model import Request
from app.models.extracted_document_model import ExtractedDocument


Base.metadata.create_all(bind=engine)

print("Tables created successfully")