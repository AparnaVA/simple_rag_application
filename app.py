
import streamlit as st
import chromadb
import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from io import BytesIO


# ----------------------------------
# 1. Page configuration
# ----------------------------------

st.set_page_config(
    page_title="My RAG Application",
    page_icon="📚",
    layout="centered"
)


# ----------------------------------
# 2. Connect to ChromaDB
# ----------------------------------

client = chromadb.PersistentClient(
    path="./chroma_data"
)


collection = client.get_or_create_collection(
    name="documents"
)

# Load Gemini API key
load_dotenv()

api_key = os.getenv("GEMINI API KEY")

gemini_client = genai.Client(
    api_key=api_key
)


# ----------------------------------
# 3. Application title
# ----------------------------------

st.title("📚 My RAG Application")

st.write(
    "Upload a document and ask questions about its contents."
)


# ----------------------------------
# 4. Upload a text file
# ----------------------------------

st.subheader("1. Upload your document")

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["txt", "pdf"]
)


# ----------------------------------
# 5. Process the uploaded file
# ----------------------------------

if uploaded_file is not None:

    # Read TXT or PDF file

    if uploaded_file.name.endswith(".txt"):

        text = uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".pdf"):

        pdf_reader = PdfReader(BytesIO(uploaded_file.read()))

        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    st.success("File uploaded successfully!")

    st.subheader("Document Preview")

    st.text_area(
        "File contents:",
        value=text,
        height=200
    )

    # Split text into paragraphs
    chunks = [
    line.strip()
    for line in text.splitlines()
        if line.strip()
]

    # Create IDs
    ids = [
        f"{uploaded_file.name}_chunk_{i}"
        for i in range(len(chunks))
    ]

    # Store chunks in ChromaDB
    if st.button("Store Document"):

        if chunks:

            collection.upsert(
                documents=chunks,
                ids=ids
            )

            st.success(
                f"{len(chunks)} chunks stored in ChromaDB!"
            )

        else:

            st.warning("No text found in the uploaded file.")


# ----------------------------------
# 6. Ask questions about the document
# ----------------------------------

st.subheader("2. Ask a Question")

question = st.text_input(
    "Enter your question:"
)

if st.button("Get Answer"):

    if not question.strip():

        st.warning("Please enter a question.")

    elif collection.count() == 0:

        st.warning("Please upload and store a document first.")

    else:

        try:

            # Search ChromaDB
            results = collection.query(
                query_texts=[question],
                n_results=2
            )

            # Get relevant chunks
            relevant_documents = results["documents"][0]

            # Combine chunks
            context = "\n".join(relevant_documents)

            # Create prompt
            prompt = f"""
            Answer the user's question using only the information below.

            Information:
            {context}

            Question:
            {question}

            If the answer is not available in the information,
            say:
            "I could not find the answer in the uploaded document."
            """

            # Generate answer using Gemini
            with st.spinner("Generating answer..."):

                response = gemini_client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            # Display answer
            st.subheader("Answer")

            st.write(response.text)

            # Display retrieved information
            with st.expander("View retrieved information"):

                st.write(context)

        except Exception as error:

            st.error("Something went wrong.")

            st.write(str(error))
