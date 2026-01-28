def best_approach(state: str) -> str:
    """Provide recommendation based on risk
       element."""
    risk = state.get("risk", "UNKNOWN")
    
    
    if risk == "High":
        approach = "Recommendation: Delay provisioning or" 
        "optimize resources."
    elif risk == "Medium":
        approach = "Recommendation: Monitor usgae and budget."
    else:
        approach = "Recommendation: Safe to proceed."

    state["approach"] = approach
    return state
    
    