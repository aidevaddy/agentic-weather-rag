from graph.state import GraphState
from graph.nodes import weather_node
from llm.provider import get_llm

state = GraphState(query="What is the weather in London today?")
llm = get_llm()

new_state = weather_node(state, llm)
print(new_state.context)
