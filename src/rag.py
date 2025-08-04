import google.generativeai as genai
from src.vectordb import qdrant
from qdrant_client.http import models as qmodels
import os

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def embed_texts(texts):
    """Generate embeddings using Gemini embedding-001 model."""
    embeddings = []
    for text in texts:
        resp = genai.embed_content(
            model="models/embedding-001",
            content=text
        )
        embeddings.append(resp["embedding"])
    return embeddings

def ingest_pdf(file_path: str, collection_name="pdf_docs"):
    import fitz
    doc = fitz.open(file_path)
    texts = [page.get_text("text") for page in doc]

    embeddings = embed_texts(texts)
    payloads = [{"text": t} for t in texts]

    qdrant.upsert(
        collection_name=collection_name,
        points=[
            qmodels.PointStruct(
                id=i,
                vector=embeddings[i],
                payload=payloads[i]
            )
            for i in range(len(texts))
        ]
    )

def query_pdf(query: str, collection_name="pdf_docs"):
    query_vec = embed_texts([query])[0]
    results = qdrant.search(
        collection_name=collection_name,
        query_vector=query_vec,
        limit=3
    )
    return " ".join([r.payload["text"] for r in results])
