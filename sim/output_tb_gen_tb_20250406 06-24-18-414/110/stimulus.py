
import json
import random

def stimulus_gen():
    scenarios = [
        {
            "scenario": "BasicOperation_EnableHigh",
            "input variable": [
                {"d": "0", "ena": "1"},
                {"d": "1", "ena": "1"},
                {"d": "0", "ena": "1"},
                {"d": "1", "ena": "1"}
            ]
        },
        {
            "scenario": "LatchOperation_EnableLow",
            "input variable": [
                {"d": "1", "ena": "1"},
                {"d": "1", "ena": "0"},
                {"d": "0", "ena": "0"},
                {"d": "1", "ena": "0"}
            ]
        },
        {
            "scenario": "EdgeCases",
            "input variable": [
                {"d": "0", "ena": "0"},
                {"d": "0", "ena": "1"},
                {"d": "1", "ena": "0"},
                {"d": "1", "ena": "1"}
            ]
        },
        {
            "scenario": "MultipleTransitions",
            "input variable": [
                {"d": "0", "ena": "1"},
                {"d": "1", "ena": "0"},
                {"d": "0", "ena": "0"},
                {"d": "1", "ena": "1"},
                {"d": "0", "ena": "1"}
            ]
        },
        # Generate 10 random test cases
        *[{
            "scenario": f"RandomSequence_{i}",
            "input variable": [
                {"d": format(i & (1 << j) != 0, 'b'), 
                 "ena": format((i >> 1) & (1 << j) != 0, 'b')} 
                for j in range(4)
            ]
        } for i in range(10)]
    ]
    return scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
