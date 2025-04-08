import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_community.chat_models import ChatLiteLLM

# Set up Gemini LLM
llm = ChatLiteLLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.1,
    verbose=True,
    api_key="AIzaSyCJkcCpvggxQj9SD5Wx50mKVRSel4uW5Rs" 
)

# Agent to analyze disease & risk
medical_analyst = Agent(
    role="Medical Analyst",
    goal="Analyze the given disease label and confidence score to determine threat level and give a short description.",
    verbose=True,
    memory=True,
    backstory="An experienced medical expert who specializes in disease classification, diagnostics, and explanation.",
    llm=llm
)

# Agent to provide suggestions or precautions
treatment_advisor = Agent(
    role="Healthcare Advisor",
    goal="Suggest treatments, precautions, or lifestyle recommendations based on risk level and disease type.",
    verbose=True,
    memory=True,
    backstory="Skilled in providing medically sound, easy-to-follow advice for various risk levels.",
    llm=llm
)

# Agent to explain and summarize for patient understanding
explanation_agent = Agent(
    role="Patient-Friendly Explainer",
    goal="Summarize the disease analysis in layman's terms in English.",
    verbose=True,
    memory=True,
    backstory="Communicates medical information in simple, patient-friendly formats.",
    llm=llm
)

# Formatter Agent
json_formatter = Agent(
    role="Health JSON Formatter",
    goal="Combine all medical insights into a structured JSON format.",
    verbose=True,
    memory=True,
    backstory="Expert in preparing API-ready structured JSON output from healthcare analysis.",
    llm=llm
)
