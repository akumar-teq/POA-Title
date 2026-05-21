import requests

def download_pdf(url, save_path):

    response = requests.get(url)

    with open(save_path, "wb") as file:
        file.write(response.content)

    return save_path
