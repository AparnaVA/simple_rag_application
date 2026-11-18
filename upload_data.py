import os
import chromadb


# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_data"
)

# Delete the old collection if it exists
try:
    client.delete_collection(name="documents")
    print("Old collection deleted!")

except Exception:
    print("No existing collection found.")

# Create a fresh collection
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

    # Split the text into paragraphs
chunks = [
    paragraph.strip()
    for paragraph in text.split("\n\n")
    if paragraph.strip()
]
print(f"\nTotal chunks created: {len(chunks)}")

    # Create unique IDs for each chunk
ids = []

for i in range(len(chunks)):
        ids.append(f"chunk_{i}")


    # Store chunks in ChromaDB
if chunks:
    collection.add(
        documents=chunks,
        ids=ids
    )

    print(f"{len(chunks)} chunks stored successfully!")
else:

        print("No text found in the file.")