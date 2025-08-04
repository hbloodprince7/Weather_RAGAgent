from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels

# Initialize Qdrant client (local memory)
qdrant = QdrantClient(url="http://localhost:6333")

def init_collection(collection_name="pdf_docs", vector_size=768):
    qdrant.recreate_collection(
        collection_name=collection_name,
        vectors_config=qmodels.VectorParams(size=vector_size, distance="Cosine")
    )
