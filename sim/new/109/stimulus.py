import json
def generate_random_binary(length):
    import random
    return ''.join([str(random.randint(0, 1)) for _ in range(length)])

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
            "input variable": [{"in": ("10" * 50)}]
        },
        {
            "scenario": "BoundaryTest",
            "input variable": [{"in": "1" + "0" * 98 + "1"}]
        },
        {
            "scenario": "WalkingOnes",
            "input variable": [{"in": format(1 << i, '0100b') for i in range(100)}]
        },
        {
            "scenario": "AdjacentPairsTest",
            "input variable": [{"in": "11" * 25 + "00" * 25}]
        }
    ]
    
    # Add 10 random test cases
    for i in range(10):
        scenarios.append({
            "scenario": f"RandomTest_{i}",
            "input variable": [{"in": generate_random_binary(100)}]
        })
    
    return scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # 将结果转换为 JSON 字符串
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
