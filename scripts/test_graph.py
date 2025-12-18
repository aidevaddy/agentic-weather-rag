from graph.graph import app
from graph.state import GraphState

# Query for weather
state = GraphState(query="Is it going to rain in London today?")
result = app.invoke(state)
print("Weather result: ", result)

# Query for RAG
state = GraphState(query="London was founded by?")
result = app.invoke(state)
print("RAG result: ", result)