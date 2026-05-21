import fitz
from google.cloud import vision


# Extract text directly from PDF
def extract_text_from_pdf(pdf_path):

    document = fitz.open(pdf_path)

    full_text = ""

    for page in document:

        text = page.get_text()

        full_text += text

    return full_text


# Google OCR for scanned images
def google_ocr(image_path):

    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    texts = response.text_annotations

    if texts:
        return texts[0].description

    return ""