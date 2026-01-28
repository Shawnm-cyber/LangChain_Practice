from langgraph.graph import StateGraph, END
from typing import TypedDict

from nodes.fetch_aws import fetch_aws
from llm.agent import llm_analyze  # This now contains your Gemini logic
from nodes.assess_risk import assess_risk
from nodes.best_approach import best_approach

class AgentState(TypedDict, total=False):
    input: str
    data: str           # Raw JSON from AWS Boto3
    analysis: str       # Plain English explanation from Gemini
    risk: str           # Risk score/assessment
    recommendation: str # Final advice

builder = StateGraph(AgentState)

# Define the Nodes
builder.add_node("fetch", fetch_aws)
builder.add_node("llm", llm_analyze)   # GEMINI NODE
builder.add_node("risk", assess_risk)
builder.add_node("recommend", best_approach)

# Define the Edges
builder.set_entry_point("fetch")
builder.add_edge("fetch", "llm")       # Pass AWS data to Gemini
builder.add_edge("llm", "risk")        # Pass Gemini's analysis to Risk node
builder.add_edge("risk", "recommend")
builder.add_edge("recommend", END)

app = builder.compile()

if __name__ == "__main__":
    inputs = {"input": "Estimate AWS EC2 cost for us-east-1"}
    result = app.invoke(inputs)
    
    # Add these lines to see the output!
    print("--- ANALYSIS ---")
    print(result.get("analysis", "No analysis generated"))
    print("--- RECOMMENDATION ---")
    print(result.get("recommendation", "No recommendation generated"))