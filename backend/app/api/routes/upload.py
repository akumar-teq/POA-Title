from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    os.makedirs(
        "storage/pdfs",
        exist_ok=True
    )

    file_path = f"storage/pdfs/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message": "File uploaded successfully",
        "pdf_path": file_path
    }