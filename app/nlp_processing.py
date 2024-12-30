import spacy
import re
import string

nlp = spacy.load("en_core_web_sm")

def process_text(text: str) -> list:
    doc = nlp(text)
    processed_text = []
    for token in doc:
        if token.is_punct or token.text.isnumeric():
            continue
        cleaned = re.sub(r"[^\w\s]", "", token.text)
        processed_text.append(cleaned.lower())
    return processed_text

def score_resume(resume_text: list[str], job_description: list[str]) -> float:
    resume_words = set(resume_text)
    job_words = set(job_description)
    match_count = len(job_words.intersection(resume_words))
    return match_count/len(job_words) if job_words else 0.0