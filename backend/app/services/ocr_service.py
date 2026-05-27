import fitz
import base64
from anthropic import Anthropic


# Extract text directly from PDF
def extract_text_from_pdf(pdf_path):

    document = fitz.open(pdf_path)

    full_text = ""

    for page in document:

        text = page.get_text()

        full_text += text

    return full_text


# Claude OCR for scanned images
def claude_ocr(image_path):

    client = Anthropic()

    content_type = "image/png" if str(image_path).lower().endswith(".png") else "image/jpeg"

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": content_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Please extract all readable text from this image exactly as it appears. Do not add any commentary or explanation. Provide only the extracted text."
                    }
                ],
            }
        ],
    )

    return response.content[0].text