import chromadb


# Connect to the existing ChromaDB database
client = chromadb.PersistentClient(path="./chroma_data")


# Get the collection where our documents are stored
collection = client.get_collection(
    name="documents"
)


# Get a question from the user
question = input("Ask a question: ")


# Search for the most relevant documents
results = collection.query(
    query_texts=[question],
    n_results=2
)


# Get the retrieved documents
documents = results["documents"][0]


# Display the results
print("\nRelevant information:")

for document in documents:
    print("-", document)