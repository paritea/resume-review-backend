from pdfminer.high_level import extract_text
from fastapi import UploadFile
from io import BytesIO

async def extract_text_from_file(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise ValueError("Unsupported file type!")
    binary_data = await file.read()
    with BytesIO(binary_data) as file_to_read:
        return extract_text(file_to_read)