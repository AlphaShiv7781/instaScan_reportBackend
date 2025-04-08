from crewai import Crew, Process
from agents import (
    medical_analyst,
    treatment_advisor,
    explanation_agent,
    json_formatter
)

from tasks import (
    disease_analysis_task,
    treatment_task,
    explanation_task,
    format_task
)

crew = Crew(
    agents=[
        medical_analyst,
        treatment_advisor,
        explanation_agent,
        json_formatter
    ],
    tasks=[
        disease_analysis_task,
        treatment_task,
        explanation_task,
        format_task
    ],
    process=Process.sequential
)
