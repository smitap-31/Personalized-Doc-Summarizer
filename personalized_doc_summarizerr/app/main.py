from fastapi import FastAPI, UploadFile, Form
from app.services.pdf_parser import extract_text_from_pdf
from app.services.embedder import get_embeddings
from app.services.vector_store import VectorStore
from app.services.summarizer import create_prompt
from app.services.llm_infer import query_ollama
import os, tempfile

app = FastAPI()
store = VectorStore(dim=384)  # MiniLM output size

@app.post("/summarize/")
async def summarize(file: UploadFile, persona: str = Form(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    full_text = extract_text_from_pdf(tmp_path)
    chunks = [full_text[i:i+500] for i in range(0, len(full_text), 500)]
    embeddings = get_embeddings(chunks)
    store.add(embeddings, chunks)

    query_embed = get_embeddings(["summary context"])[0]
    relevant_chunks = store.search(query_embed)

    prompt = create_prompt(relevant_chunks, persona)
    summary = query_ollama(prompt)
    os.remove(tmp_path)

    return {"summary": summary.strip()}
