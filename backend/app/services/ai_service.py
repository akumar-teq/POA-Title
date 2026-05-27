import re


def parse_document(text):

    homeowner = None
    lender = None
    loan_amount = None
    recording_date = None
    document_number = None

    # Loan Amount
    amount_match = re.search(
        r"\$[\d,]+(?:\.\d{2})?",
        text
    )

    if amount_match:
        loan_amount = amount_match.group()

    # Recording Date
    date_match = re.search(
        r"\d{2}/\d{2}/\d{4}",
        text
    )

    if date_match:
        recording_date = date_match.group()

    # Document Number
    doc_match = re.search(
        r"(Document Number|Doc Number|Instrument Number)\s*:?\s*([A-Za-z0-9\-]+)",
        text,
        re.IGNORECASE
    )

    if doc_match:
        document_number = doc_match.group(2)

    # Homeowner
    owner_match = re.search(
        r"(?:Borrower[s]?|Owner(?:\(s\))?\s*Name)\s*:?\s*(.+)",
        text,
        re.IGNORECASE
    )

    if owner_match:
        homeowner = owner_match.group(1).strip()

    # Lender
    lender_match = re.search(
        r"Lender\s*:?\s*(.+)",
        text,
        re.IGNORECASE
    )

    if lender_match:
        lender = lender_match.group(1).strip()

    # Property Address
    address_match = re.search(
        r"Property\s+Address\s*:?\s*(.+)",
        text,
        re.IGNORECASE
    )
    property_address = address_match.group(1).strip() if address_match else None

    # County
    county_match = re.search(
        r"County\s*:?\s*(.+)",
        text,
        re.IGNORECASE
    )
    county = county_match.group(1).strip() if county_match else None

    # Firm File No
    firm_match = re.search(
        r"Firm\s+File\s+No\.?\s*:?\s*(.+)",
        text,
        re.IGNORECASE
    )
    firm_file_no = firm_match.group(1).strip() if firm_match else None

    return {
        "homeowner": homeowner,
        "lender": lender,
        "loan_amount": loan_amount,
        "recording_date": recording_date,
        "document_number": document_number,
        "property_address": property_address,
        "county": county,
        "firm_file_no": firm_file_no
    }