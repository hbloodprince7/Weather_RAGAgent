import pytest
from unittest.mock import patch
from src.graph import build_graph

graph = build_graph()

def test_weather_node_routing():
    """Ensure queries with 'weather' are routed to weather_node."""
    with patch("src.graph.fetch_weather") as mock_fetch, \
         patch("src.graph.call_gemini") as mock_gemini:   # patch where used

        mock_fetch.return_value = {"temp": "25°C", "condition": "Clear"}
        mock_gemini.return_value = "Mocked weather summary"

        res = graph.invoke({"query": "What is the weather in London"})
        assert "Mocked weather summary" in res["answer"]
        mock_fetch.assert_called_once()
        mock_gemini.assert_called_once()

def test_rag_node_routing():
    """Ensure non-weather queries are routed to rag_node."""
    with patch("src.graph.query_pdf") as mock_rag, \
         patch("src.graph.call_gemini") as mock_gemini:   # patch where used

        mock_rag.return_value = "Mocked PDF context"
        mock_gemini.return_value = "Mocked rag answer"

        res = graph.invoke({"query": "Who is the author of the paper?"})
        assert "Mocked rag answer" in res["answer"]
        mock_rag.assert_called_once()
        mock_gemini.assert_called_once()

def test_llm_direct_mock(monkeypatch):
    """Unit test Gemini call directly (bypasses graph)."""
    import google.generativeai as genai
    from src.gemini import call_gemini

    class MockResponse:
        text = "Mocked Gemini response"

    def mock_generate_content(self, prompt):
        return MockResponse()

    # Patch the method on GenerativeModel directly
    monkeypatch.setattr(genai.GenerativeModel, "generate_content", mock_generate_content)

    res = call_gemini("Hello")
    assert "Mocked Gemini response" in res
