import json
def stimulus_gen():
    scenarios = [
        {
            "scenario": "AllZeros",
            "input variable": [{
                "p1a": "0", "p1b": "0", "p1c": "0",
                "p1d": "0", "p1e": "0", "p1f": "0",
                "p2a": "0", "p2b": "0", "p2c": "0", "p2d": "0"
            }]
        },
        {
            "scenario": "AllOnes",
            "input variable": [{
                "p1a": "1", "p1b": "1", "p1c": "1",
                "p1d": "1", "p1e": "1", "p1f": "1",
                "p2a": "1", "p2b": "1", "p2c": "1", "p2d": "1"
            }]
        },
        {
            "scenario": "FirstP1ANDGateOnly",
            "input variable": [{
                "p1a": "1", "p1b": "1", "p1c": "1",
                "p1d": "0", "p1e": "0", "p1f": "0",
                "p2a": "0", "p2b": "0", "p2c": "0", "p2d": "0"
            }]
        },
        {
            "scenario": "SecondP1ANDGateOnly",
            "input variable": [{
                "p1a": "0", "p1b": "0", "p1c": "0",
                "p1d": "1", "p1e": "1", "p1f": "1",
                "p2a": "0", "p2b": "0", "p2c": "0", "p2d": "0"
            }]
        },
        {
            "scenario": "FirstP2ANDGateOnly",
            "input variable": [{
                "p1a": "0", "p1b": "0", "p1c": "0",
                "p1d": "0", "p1e": "0", "p1f": "0",
                "p2a": "1", "p2b": "1", "p2c": "0", "p2d": "0"
            }]
        },
        {
            "scenario": "SecondP2ANDGateOnly",
            "input variable": [{
                "p1a": "0", "p1b": "0", "p1c": "0",
                "p1d": "0", "p1e": "0", "p1f": "0",
                "p2a": "0", "p2b": "0", "p2c": "1", "p2d": "1"
            }]
        },
        {
            "scenario": "BothP1ANDGates",
            "input variable": [{
                "p1a": "1", "p1b": "1", "p1c": "1",
                "p1d": "1", "p1e": "1", "p1f": "1",
                "p2a": "0", "p2b": "0", "p2c": "0", "p2d": "0"
            }]
        },
        {
            "scenario": "BothP2ANDGates",
            "input variable": [{
                "p1a": "0", "p1b": "0", "p1c": "0",
                "p1d": "0", "p1e": "0", "p1f": "0",
                "p2a": "1", "p2b": "1", "p2c": "1", "p2d": "1"
            }]
        },
        {
            "scenario": "AlternatingPattern",
            "input variable": [{
                "p1a": "1", "p1b": "0", "p1c": "1",
                "p1d": "0", "p1e": "1", "p1f": "0",
                "p2a": "1", "p2b": "0", "p2c": "1", "p2d": "0"
            }]
        },
        {
            "scenario": "SingleBitHigh",
            "input variable": [{
                "p1a": "1", "p1b": "0", "p1c": "0",
                "p1d": "0", "p1e": "0", "p1f": "0",
                "p2a": "0", "p2b": "0", "p2c": "0", "p2d": "0"
            }]
        }
    ]
    
    # Add 10 random test cases
    import random
    for i in range(10):
        random_inputs = {
            "p1a": str(random.randint(0, 1)),
            "p1b": str(random.randint(0, 1)),
            "p1c": str(random.randint(0, 1)),
            "p1d": str(random.randint(0, 1)),
            "p1e": str(random.randint(0, 1)),
            "p1f": str(random.randint(0, 1)),
            "p2a": str(random.randint(0, 1)),
            "p2b": str(random.randint(0, 1)),
            "p2c": str(random.randint(0, 1)),
            "p2d": str(random.randint(0, 1))
        }
        scenarios.append({
            "scenario": f"RandomTest{i+1}",
            "input variable": [random_inputs]
        })
    
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
