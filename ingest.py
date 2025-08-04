import sys
from src.vectordb import init_collection
from src.rag import ingest_pdf

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    init_collection("pdf_docs", 768)
    ingest_pdf(pdf_path, "pdf_docs")
    print(f"{pdf_path} ingested into Qdrant.")
