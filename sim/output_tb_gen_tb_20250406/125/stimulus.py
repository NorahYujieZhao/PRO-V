import json
def generate_alternating_bits(width, start_with_one=True):
    pattern = ''
    for i in range(width):
        pattern += '1' if (i + (0 if start_with_one else 1)) % 2 == 0 else '0'
    return pattern

def generate_checkerboard(width, block_size=4):
    pattern = ''
    for i in range(0, width, block_size*2):
        pattern += '1' * block_size
        remaining = min(block_size, width - (i + block_size))
        if remaining > 0:
            pattern += '0' * remaining
    return pattern[:width]

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
            "input variable": [{"in": generate_alternating_bits(100)}]
        },
        {
            "scenario": "BoundaryBitsSet",
            "input variable": [{"in": "1" + "0" * 98 + "1"}]
        },
        {
            "scenario": "LeftHalfOnes",
            "input variable": [{"in": "1" * 50 + "0" * 50}]
        },
        {
            "scenario": "RightHalfOnes",
            "input variable": [{"in": "0" * 50 + "1" * 50}]
        },
        {
            "scenario": "OneHotPattern",
            "input variable": [{
                "in": ''.join('1' if i in [0, 25, 50, 75, 99] else '0' for i in range(100))
            }]
        },
        {
            "scenario": "CheckerboardPattern",
            "input variable": [{"in": generate_checkerboard(100)}]
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
