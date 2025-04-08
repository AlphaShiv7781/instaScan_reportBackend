from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crew import crew
import re
import json

app = FastAPI(
    title="InstaScan AI Health API",
    description="API for Disease Risk Analysis using Agentic System",
    version="1.0"
)

class DiseaseInput(BaseModel):
    label: str
    confidence: float  # Accept percentage as float, e.g., 67.4

def extract_json_from_output(output_str):
    """Extract valid JSON block from agentic result."""
    json_match = re.search(r'```json\n(.*?)\n```', output_str, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return None
    try:
        return json.loads(output_str)  # Fallback if pure JSON
    except:
        return None

@app.post("/analyze", summary="Analyze disease label and confidence")
def analyze_disease(data: DiseaseInput):
    try:
        result = crew.kickoff(inputs={
            'label': data.label,
            'confidence': data.confidence
        })

        output_str = str(result)
        structured_json = extract_json_from_output(output_str)

        if not structured_json:
            raise ValueError("Could not parse JSON from output.")

        return {
            "status": "success",
            "data": structured_json
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")
