from rag.loader import load_and_split_pdf
from rag.embeddings import create_vectorstore
from rag.retriever import get_retriever
from llm.provider import get_llm

docs = load_and_split_pdf("data/cities_of_the_world.pdf")
vectorstore = create_vectorstore(docs)
retriever = get_retriever(vectorstore)

llm = get_llm()

query = "Tell me something about New York City"
chunks = retriever.invoke(query)

context = "\n".join(d.page_content for d in chunks)

response = llm.invoke(
    f"Answer the question using the context below:\n\n{context}\n\nQuestion: {query}"
)

print(response.content)