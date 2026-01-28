from langgraph.graph import StateGraph
from typing import TypedDict

from nodes.fetch_aws import fetch_aws
from nodes.assess_risk import assess_risk
from nodes.best_approach import best_approach
from nodes.llm_reasoner import llm_reasoner

class AgentState(TypedDict):
    aws_data: dict
    risk: str
    recommendation: str
    llm_rundown: str

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("fetch", fetch_aws)
    graph.add_node("risk", assess_risk)
    graph.add_node("recommend", best_approach)
    graph.add_node("llm", llm_reasoner)

    graph.set_entry_point("fetch")

    graph.add_edge("fetch", "risk")
    graph.add_edge("risk", "recommend")
    graph.add_edge("recommend", "llm")

    graph.set_finish_point("llm")

    return graph.compile()

