from app.services.pdf_service import generate_summary_pdf

sample_data = {
    "Homeowner": "JOHN DOE",
    "Lender": "ABC BANK",
    "Loan Amount": "$350,000",
    "Recording Date": "01/15/2024",
    "HELOC": True,
    "Owelty": False
}

generate_summary_pdf(
    sample_data,
    "storage/reports/sample_report.pdf"
)

print("PDF generated successfully")
