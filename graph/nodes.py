from graph.state import GraphState
from tools.weather import get_current_weather

def weather_node(state: GraphState, llm)->GraphState:
    prompt = (
        "Extract the city name from the following query.\n"
        "Return only the city name and nothing else.\n\n"
        f"Query: {state.query}"
    )


    city=llm.invoke(prompt).content.strip()

    weather_result = get_current_weather.invoke({"city": city})
    state.context=weather_result
    return state