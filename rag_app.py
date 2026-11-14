import os
import chromadb
from dotenv import load_dotenv
from google import genai


# ----------------------------------
# 1. Load the Gemini API key
# ----------------------------------

load_dotenv()

api_key = os.getenv("GEMINI API KEY")

gemini_client = genai.Client(
    api_key=api_key
)


# ----------------------------------
# 2. Connect to ChromaDB
# ----------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_data"
)


# Get the collection containing uploaded files
collection = chroma_client.get_collection(
    name="documents"
)


# ----------------------------------
# 3. Get a question from the user
# ----------------------------------

question = input("Ask a question: ")


# ----------------------------------
# 4. Search the uploaded document
# ----------------------------------

results = collection.query(
    query_texts=[question],
    n_results=2
)


# Get the relevant chunks
relevant_documents = results["documents"][0]


# Combine the chunks into one context
context = "\n".join(relevant_documents)


# Optional: Show what ChromaDB found
print("\nRelevant information:")
print(context)


# ----------------------------------
# 5. Create a prompt for Gemini
# ----------------------------------

prompt = f"""
Answer the user's question using only the information below.

Information:
{context}

Question:
{question}

If the answer is not available in the information, say:
"I could not find the answer in the uploaded document."
"""


# ----------------------------------
# 6. Ask Gemini to generate an answer
# ----------------------------------

try:
    print("\nGenerating answer...")

    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nAnswer:")
    print(response.text)

except Exception as error:
    print("\nGemini is currently unavailable.")
    print("Error:", error)