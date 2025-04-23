import json

# Convert result to JSON string
if isinstance(result, list):
    result = json.dumps(result, indent=4)
elif not isinstance(result, str):
    result = json.dumps(result, indent=4)

with open("stimulus.json", "w") as f:
    f.write(result) 