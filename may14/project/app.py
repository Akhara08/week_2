import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Step 1: Load and process the PDF
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Step 2: Split the text into chunks
def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(raw_text)

# Step 3: Create vector store using Chroma
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Convert to Document objects
    documents = [Document(page_content=chunk) for chunk in text_chunks]

    # Create and persist ChromaDB vector store
    vector_store = Chroma.from_documents(
        documents, 
        embedding=embeddings, 
        persist_directory="faiss_index"
    )
    vector_store.persist()

# Step 4: Load QA chain
def get_conversational_chain():
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)
    chain = load_qa_chain(model, chain_type="stuff")
    return chain

# Step 5: Handle user query
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Load persisted vector store
    vector_store = Chroma(
        persist_directory="faiss_index", 
        embedding_function=embeddings
    )

    # Perform similarity search
    docs = vector_store.similarity_search(user_question)

    # Generate response
    chain = get_conversational_chain()
    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    st.write("Reply:", response["output_text"])

# Streamlit UI
def main():
    st.set_page_config("PDF Q&A with ChromaDB")
    st.header("Ask Questions from PDF 💬")

    user_question = st.text_input("Ask a question based on your PDF:")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Upload your PDF")
        pdf_docs = st.file_uploader("Upload PDFs", accept_multiple_files=True)

        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done!")

if __name__ == "__main__":
    main()
