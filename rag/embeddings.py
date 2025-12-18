from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient

def create_vectorstore(documents):
    embeddings=OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Qdrant.from_documents(
        documents,
        embeddings,
        path="./qdrant_data",
        collection_name="rag_docs"
    )

    return vectorstore