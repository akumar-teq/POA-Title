from app.services.ai_service import parse_document

sample_text = """

Borrower: JOHN DOE
Lender: ABC BANK
Document Number: 20240012345
Loan Amount: $350,000
01/15/2024

"""

result = parse_document(sample_text)

print(result)
