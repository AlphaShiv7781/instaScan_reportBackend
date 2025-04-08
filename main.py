from crew import crew

# Example disease input
result = crew.kickoff(inputs={
    'label': 'Skin Cancer',
    'confidence': 20.65
})

print(result)
