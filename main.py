from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from app.file_handler import extract_text_from_file
from app.nlp_processing import process_text, score_resume
from app.models import ResumeRequest
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def root():
    return {"message": "Resume Analyzer API"}

@app.post("/upload")
async def upload_file(job_description: str, file: UploadFile = File(...)):
    print(job_description)
    extracted_text = await extract_text_from_file(file)
    pdftext_normalized_list = process_text(extracted_text)
    job_description_list = process_text(job_description)
    score = score_resume(pdftext_normalized_list, job_description_list)
    result = {
        "filename": file.filename,
        "score": score
    }

    return result

@app.post("/test_pydantic")
async def test_pydantic(req: ResumeRequest):
    return req.model_dump()

@app.post("/upload_test")
async def test_upload_file(file: UploadFile):
    return {"filename": file.filename.split(".")[0]}
@app.get("/health")
async def health():
    return {"status": "ok"}