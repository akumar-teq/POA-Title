import fitz

def pdf_to_images(pdf_path):

    document = fitz.open(pdf_path)

    image_paths = []

    for page_num in range(len(document)):

        page = document.load_page(page_num)

        pix = page.get_pixmap()

        image_path = f"storage/ocr/page_{page_num}.png"

        pix.save(image_path)

        image_paths.append(image_path)

    return image_paths
