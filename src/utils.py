def clean_text(text: str) -> str:
    """Utility to clean text output from PDFs or LLMs."""
    return text.replace("\n", " ").strip()
