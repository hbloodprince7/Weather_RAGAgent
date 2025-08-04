import os
import streamlit as st
from src.graph import build_graph
from langsmith import Client
from dotenv import load_dotenv
load_dotenv()


client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))

print(client.list_projects())  

st.set_page_config(page_title="AI Assistant", layout="wide")
st.title("AI Engineer Assignment Demo")

graph = build_graph()

if "messages" not in st.session_state:
    st.session_state.messages = []

user_query = st.chat_input("Ask a question (Weather or PDF-based)...")

if user_query:
    st.session_state.messages.append(("user", user_query))
    res = graph.invoke({"query": user_query})
    st.session_state.messages.append(("ai", res["answer"]))


for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)
