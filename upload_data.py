import os
import chromadb


# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_or_create_collection(
    name="documents"
)


# Ask the user for the file path
file_path = input("Enter the path of the text file: ")


# Check whether the file exists
if not os.path.exists(file_path):
    print("File not found!")

else:
    # Open and read the file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    print("\nFile read successfully!")

    # Split the text into smaller chunks
    chunk_size = 200

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)


    # Create unique IDs for each chunk
    ids = []

    for i in range(len(chunks)):
        ids.append(f"chunk_{i}")


    # Store chunks in ChromaDB
    collection.add(
        documents=chunks,
        ids=ids
    )

    print(f"{len(chunks)} chunks stored successfully!")