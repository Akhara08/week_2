# initialize_chromadb.py
import chromadb
from chromadb.config import Settings

# Initialize ChromaDB client
def initialize_chromadb():
    # Initialize the client with default settings
    client = chromadb.Client(Settings())
    print("ChromaDB initialized successfully!")
    return client

# Initialize the ChromaDB client
client = initialize_chromadb()

# Optionally, you can create a collection here if needed
collection_name = "sample_collection"
if collection_name not in client.list_collections():
    collection = client.create_collection(name=collection_name)
    print(f"Collection '{collection_name}' created.")
else:
    collection = client.get_collection(name=collection_name)
    print(f"Collection '{collection_name}' already exists.")
