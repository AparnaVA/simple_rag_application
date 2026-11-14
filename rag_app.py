import os
import chromadb
from dotenv import load_dotenv
from google import genai


# ----------------------------------
# 1. Load the API key
# ----------------------------------

load_dotenv()

api_key = os.getenv("GEMINI API KEY")


# ----------------------------------
# 2. Connect to Gemini
# ----------------------------------

gemini_client = genai.Client(api_key=api_key)


# ----------------------------------
# 3. Connect to ChromaDB
# ----------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = chroma_client.get_collection(
    name="documents"
)


# ----------------------------------
# 4. Get a question from the user
# ----------------------------------

question = input("Ask a question: ")


# ----------------------------------
# 5. Retrieve relevant documents
# ----------------------------------

results = collection.query(
    query_texts=[question],
    n_results=2
)

relevant_documents = results["documents"][0]


# Combine the retrieved documents
context = "\n".join(relevant_documents)

print(context)


# ----------------------------------
# 6. Create a prompt
# ----------------------------------

prompt = f"""
Answer the user's question using only the information below.

Information:
{context}

Question:
{question}

If the information does not contain the answer, say:
"I could not find the answer in the provided documents."
"""


# ----------------------------------
# 7. Ask Gemini to generate an answer
# ----------------------------------

response = gemini_client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)


# ----------------------------------
# 8. Display the answer
# ----------------------------------

print("\nAnswer:")
print(response.text)