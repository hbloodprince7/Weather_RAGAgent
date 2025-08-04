import logging
from langgraph.graph import StateGraph, END
from src.weatherapi import fetch_weather
from src.rag import query_pdf
from src.gemini import call_gemini

logging.basicConfig(level=logging.INFO)

def router_condition(state):
    """Decide which branch to follow."""
    query = state.get("query", "").lower()
    logging.info(f"Router received state: {state}")

    if "weather" in query:
        logging.info("Routing to weather_node")
        return "weather_node"
    else:
        logging.info("Routing to rag_node")
        return "rag_node"

def weather_node(state: dict):
    logging.info(f"Weather node received: {state}")
    query = state.get("query", "")
    city = query.split("in")[-1].strip() if "in" in query else "your location"
    weather_info = fetch_weather(city)
    answer = call_gemini(f"Describe this weather info in 3 lines {weather_info}")
    return {"query": query, "answer": answer}

def rag_node(state: dict):
    logging.info(f"RAG node received: {state}")
    query = state.get("query", "")
    context = query_pdf(query)
    answer = call_gemini(f"Context: {context}\n\nQuestion: {query}\nAnswer:")
    return {"query": query, "answer": answer}

def build_graph():
    graph = StateGraph(dict)

    # Add router node (acts as entry point, just passes state through)
    graph.add_node("router", lambda state: state)
    graph.set_entry_point("router")

    # Conditional routing
    graph.add_conditional_edges(
        "router",
        router_condition,   # condition function
        {
            "weather_node": "weather_node",
            "rag_node": "rag_node",
        }
    )

    # Processing nodes
    graph.add_node("weather_node", weather_node)
    graph.add_node("rag_node", rag_node)

    # End edges
    graph.add_edge("weather_node", END)
    graph.add_edge("rag_node", END)

    return graph.compile()
