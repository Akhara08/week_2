# store_sample_document.py
import chromadb

# Initialize ChromaDB client (import the initialization from the first program)
def initialize_chromadb():
    from chromadb.config import Settings
    client = chromadb.Client(Settings())
    return client

# Function to store a sample document
def store_sample_document():
    client = initialize_chromadb()

    # Create or get the collection (ensure it's created if it doesn't exist)
    collection_name = "sample_collection"
    
    # Check if the collection exists, if not create it
    if collection_name not in client.list_collections():
        collection = client.create_collection(name=collection_name)
        print(f"Collection '{collection_name}' created.")
    else:
        collection = client.get_collection(name=collection_name)
        print(f"Collection '{collection_name}' found.")

    # Sample document to store
    sample_document = {
        "id": "doc1",
        "content": "This is a sample document stored in ChromaDB",
        "metadata": {"author": "John Doe", "date": "2025-05-12"}
    }

    # Add document to the collection
    collection.add(
        ids=[sample_document["id"]],
        documents=[sample_document["content"]],
        metadatas=[sample_document["metadata"]],
    )

    print("Document added successfully!")

# Store the sample document
store_sample_document()
