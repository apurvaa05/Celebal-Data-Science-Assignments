from typing import TypedDict
from langgraph.graph import StateGraph, END

from tools import (
    calculator_tool,
    keyword_tool,
    greeting_tool,
    datetime_tool
)

class AgentState(TypedDict):
    query: str
    result: str


def calculator_node(state):
    return {
        "result": calculator_tool(state["query"])
    }


def keyword_node(state):
    return {
        "result": keyword_tool(state["query"])
    }


def greeting_node(state):
    return {
        "result": greeting_tool(state["query"])
    }


def datetime_node(state):
    return {
        "result": datetime_tool()
    }


def router(state):

    query = state["query"].lower()

    if "calculate" in query:
        return "calculator"

    elif "keyword" in query:
        return "keyword"

    elif "time" in query or "date" in query:
        return "datetime"

    else:
        return "greeting"


def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node("calculator", calculator_node)
    builder.add_node("keyword", keyword_node)
    builder.add_node("greeting", greeting_node)
    builder.add_node("datetime", datetime_node)

    builder.set_conditional_entry_point(
        router,
        {
            "calculator": "calculator",
            "keyword": "keyword",
            "datetime": "datetime",
            "greeting": "greeting"
        }
    )

    builder.add_edge("calculator", END)
    builder.add_edge("keyword", END)
    builder.add_edge("datetime", END)
    builder.add_edge("greeting", END)

    return builder.compile()