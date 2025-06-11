from fastapi import APIRouter, UploadFile, Form
from app.services.pdf_parser import extract_text_from_pdf
from app.services.embedder import get_embeddings
from app.services.vector_store import VectorStore
from app.services.llm_infer import query_ollama
from app.services.summarizer import create_prompt
from app.core.logger import get_logger
import os, shutil

router = APIRouter()
logger = get_logger()

@router.post("/summarize")
async def summarize(file: UploadFile, persona: str = Form(...)):
    temp_path = f"app/pdf/{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    logger.info(f"Uploaded file saved to {temp_path}")

    try:
        text = extract_text_from_pdf(temp_path)
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        embeddings = get_embeddings(chunks)
        store = VectorStore(dim=384)
        store.add(embeddings, chunks)

        query_embedding = get_embeddings([persona])[0]
        relevant = store.search(query_embedding, k=5)

        prompt = create_prompt(relevant, persona)
        summary = query_ollama(prompt)

        logger.info(f"Generated summary for persona: {persona}")
        return {"summary": summary.strip()}
    finally:
        os.remove(temp_path)
