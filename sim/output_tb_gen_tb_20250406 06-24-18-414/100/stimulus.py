import json
def _to_bit_str(value: int, width: int = 8) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [0x00]
        },
        {
            "scenario": "AllOnes",
            "vectors": [0xFF]
        },
        {
            "scenario": "AlternatingBits",
            "vectors": [0xAA]
        },
        {
            "scenario": "SingleBitHigh",
            "vectors": [0x01]
        },
        {
            "scenario": "TwoBitsHigh",
            "vectors": [0x03]
        },
        {
            "scenario": "OddNumberOfOnes",
            "vectors": [0xE0]
        },
        {
            "scenario": "EvenNumberOfOnes",
            "vectors": [0xF0]
        },
        {
            "scenario": "ScatteredBits",
            "vectors": [0x92]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for value in sc["vectors"]:
            inputs.append({
                "in": _to_bit_str(value, width=8)
            })
        
        stimulus_list.append({
            "scenario": sc["scenario"],
            "input variable": inputs
        })
    
    return stimulus_list
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
