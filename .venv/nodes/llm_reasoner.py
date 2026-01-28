import os
from google import genai


client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def llm_reasoner(state: dict) -> dict:
    prompt = f"""
    AWS RISK: {state.get("risk")}
    Recommendation: {state.get("recommendation")}
    """

    given_response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = prompt
    )
    
    state["llm_rundown"] = given_response.text
    return state

