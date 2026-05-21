from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_summary_pdf(data, output_path):

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "<b>PROPERTY SUMMARY REPORT</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    for key, value in data.items():

        line = Paragraph(
            f"<b>{key}</b>: {value}",
            styles['BodyText']
        )

        elements.append(line)

        elements.append(Spacer(1, 10))

    doc.build(elements)

    return output_path
