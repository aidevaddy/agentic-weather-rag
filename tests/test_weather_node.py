from unittest.mock import Mock
from graph.state import GraphState
from graph.nodes import weather_node

def test_weather_node_updates_state():
    mock_llm=Mock()
    mock_llm.invoke.return_value.content="Chennai"

    fake_weather={
        "city":"Chennai",
        "temperature":20.0,
        "unit":"celsius",
        "description":"clear sky"
    }

    import graph.nodes as nodes
    nodes.get_current_weather=Mock()
    nodes.get_current_weather.invoke.return_value = fake_weather

    state=GraphState(query="What is the weather in Chennai?")
    new_state=weather_node(state,mock_llm)

    assert new_state.context == fake_weather