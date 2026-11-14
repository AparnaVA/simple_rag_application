import chromadb


# 1. Create a ChromaDB client
client = chromadb.PersistentClient(path="./chroma_data")


# 2. Create a collection
collection = client.get_or_create_collection(
    name="documents"
)


# 3. Our sample documents
documents = [
    "Python is a popular programming language used for web development and data analysis.",
    "Django is a Python web framework used to build web applications.",
    "React is a JavaScript library used to build user interfaces.",
    "ChromaDB is a vector database that stores and searches data using embeddings."
]


# 4. Add documents to ChromaDB
collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# Get all documents from the collection
data = collection.get()


# Display the data
print("Documents stored in ChromaDB:\n")

for document_id, document in zip(data["ids"], data["documents"]):
    print(f"ID: {document_id}")
    print(f"Document: {document}")
    print()

print("Documents stored successfully!")