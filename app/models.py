from fastapi import UploadFile
from pydantic import BaseModel

class ResumeRequest(BaseModel):
    job_description: str