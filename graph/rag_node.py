from graph.state import GraphState
from rag.loader import load_and_split_pdf
from rag.embeddings import create_vectorstore
from rag.retriever import get_retriever

docs = load_and_split_pdf("data/cities_of_the_world.pdf")
vectorstore = create_vectorstore(docs)
retriever = get_retriever(vectorstore)

def rag_node(state: GraphState, llm) -> GraphState:
    chunks = retriever.invoke(state.query)
    context="\n".join(d.page_content for d in chunks)

    response = llm.invoke(
        f"""
        Answer the question using ONLY the context below.

        Context: 
        {context}

        Question:
        {state.query}
        """
    )
    
    state.answer = response.content
    return state