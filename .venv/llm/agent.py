from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class AgentState(TypedDict, total=False):
    input: str
    data: str
    analysis: str

# Initialize Gemini without hardcoding the key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY") 
)

def llm_analyze(state: AgentState) -> AgentState:
    # Adding a safety check to ensure data exists
    aws_data = state.get('data', 'No data found')
    user_input = state.get('input', 'No input found')

    prompt = f"""
    You are a cloud cost analyst.
    User request: {user_input}
    AWS Data: {aws_data}
    Explain the cost implications in plain English.
    """

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        # Use return instead of modifying state in-place for cleaner LangGraph logic
        return {"analysis": response.content}
    except Exception as e:
        return {"analysis": f"Error during analysis: {str(e)}"}