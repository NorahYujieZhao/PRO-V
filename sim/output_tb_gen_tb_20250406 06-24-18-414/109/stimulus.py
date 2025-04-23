
import json
import random

def generate_random_100bit():
    import random
    return ''.join([str(random.randint(0, 1)) for _ in range(100)])

def stimulus_gen():
    scenarios = [
        {
            "scenario": "AllZeros",
            "input variable": [{"in": "0" * 100}]
        },
        {
            "scenario": "AllOnes",
            "input variable": [{"in": "1" * 100}]
        },
        {
            "scenario": "AlternatingBits",
            "input variable": [{"in": "01" * 50}]
        },
        {
            "scenario": "WalkingOnes",
            "input variable": [{"in": format(1 << i, '0100b') for i in range(100)}]
        },
        {
            "scenario": "AdjacentPairsTest",
            "input variable": [{"in": "11" * 25 + "00" * 25}]
        },
        {
            "scenario": "WrapAroundTest",
            "input variable": [{"in": "1" + "0" * 98 + "0"}]
        },
        {
            "scenario": "RandomPatterns",
            "input variable": [{"in": generate_random_100bit()} for _ in range(10)]
        }
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
