from crewai import Task
from agents import medical_analyst, treatment_advisor, explanation_agent, json_formatter

disease_analysis_task = Task(
    description=(
        """Analyze the disease "{label}" with confidence {confidence:.2f}% and determine:
        - Risk Level (Low/Moderate/High)
        - Short Medical Description"""
    ),
    expected_output=(
        "JSON format:\n"
        "{\n"
        "  \"riskLevel\": \"Low/Moderate/High\",\n"
        "  \"description\": \"Short medical summary in 2 lines\"\n"
        "}"
    ),
    agent=medical_analyst
)

treatment_task = Task(
    description=(
        "Based on the {label} and risk level, suggest medically appropriate treatments in one line point and only 5 points, "
        "precautions, or lifestyle recommendations."
    ),
    expected_output=(
        "JSON format:\n"
        "{\n"
        "  \"suggestions\": [\"...\", \"...\", \"...\"]\n"
        "}"
    ),
    agent=treatment_advisor,
    context=[disease_analysis_task]
)

explanation_task = Task(
    description=(
        "Summarize the diagnosis and suggestions in simple language in English ."
    ),
    expected_output=(
        "JSON format:\n"
        "{\n"
        "  \"explanation\": {\n"
        "    \"en\": \"Easy-to-understand English explanation in 4 lines\",\n"
        "  }\n"
        "}"
    ),
    agent=explanation_agent,
    context=[disease_analysis_task, treatment_task]
)

format_task = Task(
    description="Combine all outputs into a single, structured JSON response.",
    expected_output=(
        "Final JSON structure:\n"
        "{\n"
        "  \"riskLevel\": \"...\",\n"
        "  \"description\": \"...\",\n"
        "  \"suggestions\": [\"...\"],\n"
        "  \"explanation\": {\"en\": \"...\"}\n"
        "}"
    ),
    agent=json_formatter,
    context=[disease_analysis_task, treatment_task, explanation_task]
)
