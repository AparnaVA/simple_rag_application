# Simple RAG Application using ChromaDB and Gemini

## Project Overview

This project is a simple **Retrieval-Augmented Generation (RAG)** application built using Python, ChromaDB, and Google's Gemini API.

It allows users to upload text files, store their content in a vector database, and ask questions based on the uploaded information.

The application retrieves relevant information from ChromaDB and uses Gemini to generate answers based on the retrieved content.

## Features

- Read and upload text files (`.txt`).
- Split large text content into smaller chunks.
- Generate embeddings for document chunks using ChromaDB's default embedding function.
- Store document chunks and embeddings in ChromaDB.
- Retrieve relevant information based on user questions.
- Generate context-based answers using Gemini API.
- Store vector database data persistently.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| ChromaDB | Vector database for storing and retrieving document embeddings |
| Gemini API | Generates answers using retrieved information |
| google-genai | Connects Python application with Gemini |
| python-dotenv | Manages API keys using environment variables |

## Project Structure

```text
simple-rag-app/
│
├── data/
│   └── sample.txt
│
├── chroma_data/
│
├── store_data.py
├── search_data.py
├── upload_data.py
├── rag_app.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

The application follows the RAG workflow:

1. **Document Upload:** The user provides a text file.
2. **Text Extraction:** Python reads the uploaded text file.
3. **Chunking:** The document is divided into smaller text chunks.
4. **Embedding Generation:** ChromaDB converts the chunks into numerical embeddings using its default embedding function.
5. **Vector Storage:** The embeddings and document chunks are stored in ChromaDB.
6. **Retrieval:** When a user asks a question, ChromaDB searches for the most relevant document chunks.
7. **Answer Generation:** The retrieved information and user's question are sent to Gemini.
8. **Final Answer:** Gemini generates an answer using the retrieved information.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd simple-rag-app
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Create a `.env` file in the project root.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).


## How to Run the Application

### Step 1: Upload a text file

Run:

```bash
python upload_data.py
```

Enter the text file path when prompted:

```text
data/sample.txt
```

The application reads the file, splits its content into chunks, and stores them in the ChromaDB collection named `uploaded_documents`.

### Step 2: Ask questions

Run:

```bash
python rag_app.py
```

Enter a question related to your uploaded document.

Example:

```text
Ask a question: What is ChromaDB?
```

The application retrieves relevant information from ChromaDB and sends it to Gemini to generate an answer.


## Example Workflow

```text
       Text File
           |
           v
      Read Document
           |
           v
      Split into Chunks
           |
           v
    Generate Embeddings
           |
           v
       ChromaDB
           |
           v
      User Question
           |
           v
   Retrieve Relevant Chunks
           |
           v
   Send Context to Gemini
           |
           v
      Generate Answer
```

## Future Improvements

- Support PDF and DOCX file uploads.
- Allow multiple document uploads.
- Improve text chunking with configurable chunk sizes and overlap.
- Add a Streamlit-based user interface.
- Implement duplicate document detection.
- Display source documents and relevant retrieved chunks.
- Add better error handling and retry mechanisms.

## Learning Outcomes

Through this project, I learned:

- Fundamentals of Retrieval-Augmented Generation (RAG).
- Working with vector databases using ChromaDB.
- Understanding embeddings and semantic search.
- Document loading and text chunking.
- Retrieving relevant information from stored documents.
- Integrating an LLM using the Gemini API.

## Author

**Aparna V A**