
import json
import random

def stimulus_gen():
    scenarios = [
        {
            "scenario": "AllZeros",
            "input variable": [{"in": "0000"}]
        },
        {
            "scenario": "AllOnes",
            "input variable": [{"in": "1111"}]
        },
        {
            "scenario": "SingleBitPosition3",
            "input variable": [{"in": "1000"}]
        },
        {
            "scenario": "SingleBitPosition2",
            "input variable": [{"in": "0100"}]
        },
        {
            "scenario": "SingleBitPosition1",
            "input variable": [{"in": "0010"}]
        },
        {
            "scenario": "SingleBitPosition0",
            "input variable": [{"in": "0001"}]
        },
        {
            "scenario": "MultipleBitsHighestPriority3",
            "input variable": [{"in": "1010"}]
        },
        {
            "scenario": "MultipleBitsHighestPriority2",
            "input variable": [{"in": "0110"}]
        },
        {
            "scenario": "MultipleBitsHighestPriority1",
            "input variable": [{"in": "0011"}]
        },
        {
            "scenario": "AlternatingBits",
            "input variable": [{"in": "1010"}]
        },
        # Generate 10 random test cases
        *[{
            "scenario": f"RandomPattern{i}",
            "input variable": [{"in": format(i, '04b')}]
        } for i in range(6, 16)]
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
