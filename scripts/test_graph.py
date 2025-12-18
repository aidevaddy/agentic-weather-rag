from graph.graph import app
from graph.state import GraphState

# Query for weather
state = GraphState(query="What is the weather in Paris today?")
result = app.invoke(state)
print("Weather result: ", result)

# Query for RAG
state = GraphState(query="Tell me about Paris")
result = app.invoke(state)
print("RAG result: ", result)