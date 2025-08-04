# Weather Agent

This project is an AI assistant that can answer questions based on weather information or a PDF document. It uses LangGraph to define a graph of operations, Gemini for LLM tasks, Qdrant for vector storage, and Streamlit for the user interface.

## Project Structure

*   `app.py`: The main application file that uses Streamlit to create a user interface. It takes user input, invokes the LangGraph graph, and displays the response.
*   `src/graph.py`: This file defines the LangGraph graph, which consists of a router node, a weather node, and a RAG (Retrieval-Augmented Generation) node. The router node determines whether to call the weather node or the RAG node based on the user's query.
*   `src/weatherapi.py`: This file contains the `fetch_weather` function, which fetches weather information for a given city using the OpenWeatherMap API.
*   `src/rag.py`: This file contains functions for embedding texts, ingesting a PDF document into Qdrant, and querying the PDF document.
*   `src/gemini.py`: This file contains the `call_gemini` function, which calls the Gemini LLM with a prompt and returns the response.
*   `src/vectordb.py`: This file initializes the Qdrant client and defines a function for initializing a collection.
*   `ingest.py`: This script is used to ingest a PDF document into the Qdrant vector database. It takes the path to the PDF as a command-line argument.
*   `tests`: This directory contains unit tests for the `src/weatherapi.py`, `src/rag.py`, and `src/gemini.py` files.
*   `.env`: This file stores the Gemini API key.
*   `requirements.txt`: This file lists the Python packages required to run the project.
*   `weatherresearch.pdf`: This is a PDF document that can be ingested into the Qdrant vector database and queried by the RAG node.
*   `src/utils.py`: This file contains utility functions such as `clean_text`.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    *   **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up the environment variables:**

    *   Create a `.env` file in the root directory of the project.
    *   Add your Gemini API key to the `.env` file:

        ```
        GOOGLE_API_KEY=<your_gemini_api_key>
        ```

    *   You can obtain a Gemini API key from the [Google AI Studio](https://makersuite.google.com/app/apikey).

6.  **Set up Qdrant:**

    *   You can either use a local Qdrant instance or a cloud-based Qdrant instance.
    *   If you are using a local Qdrant instance, make sure that it is running before you run the application.
    *   If you are using a cloud-based Qdrant instance, you will need to set the `QDRANT_URL` and `QDRANT_API_KEY` environment variables.

## Running the Application

1.  **Ingest the PDF document (optional):**

    *   If you want to query the PDF document, you need to ingest it into the Qdrant vector database.
    *   Run the `ingest.py` script with the path to the PDF document as a command-line argument:

        ```bash
        python ingest.py weatherresearch.pdf
        ```

2.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

3.  **Open the application in your browser:**

    *   Streamlit will print the URL of the application in the terminal.
    *   Open the URL in your browser to use the application.

## Testing

To run the unit tests, use the following command:

```bash
pytest