import json
def _to_bit_str(value: int, width: int = 8) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [0]
        },
        {
            "scenario": "AllOnes",
            "vectors": [0xFF]
        },
        {
            "scenario": "SingleBitLSB",
            "vectors": [0x01]
        },
        {
            "scenario": "SingleBitMSB",
            "vectors": [0x80]
        },
        {
            "scenario": "AlternatingPattern",
            "vectors": [0xAA]
        },
        {
            "scenario": "WalkingOneFromRight",
            "vectors": [1 << i for i in range(8)]
        },
        {
            "scenario": "RightmostOfMany",
            "vectors": [0xF4]
        },
        {
            "scenario": "IsolatedMiddleBit",
            "vectors": [0x10]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for val in sc["vectors"]:
            inputs.append({"in": _to_bit_str(val)})
        
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
