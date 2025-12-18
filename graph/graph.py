from langgraph.graph import StateGraph, END
from graph.state import GraphState
from graph.router import router_node
from graph.nodes import weather_node
from graph.rag_node import rag_node
from llm.provider import get_llm

llm = get_llm()

graph = StateGraph(GraphState)

graph.add_node("router", lambda s: router_node(s, llm))
graph.add_node("weather", lambda s: weather_node(s,llm))
graph.add_node("rag", lambda s: rag_node(s, llm))

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda s: s.route,
    {
        "weather": "weather",
        "rag": "rag"
    }
)

graph.add_edge("weather", END)
graph.add_edge("rag", END)

app = graph.compile()