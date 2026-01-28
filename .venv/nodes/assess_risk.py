def assess_risk(state: dict) -> dict:
    """Access risk based on AWS price findings or usage.
       Here is a mock that assesses if the risk is high 
       if average prices > threshold."""
    aws_data = state.get("aws_data", {})

    risk = ""

    if aws_data > 5:
        risk = "High"
    elif aws_data > 3:
        risk = "Medium"
    else:
        risk = "Low"

    state["risk"] = risk
    return state 
    