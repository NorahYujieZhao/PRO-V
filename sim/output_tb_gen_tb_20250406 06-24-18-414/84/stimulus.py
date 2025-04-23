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
            "scenario": "AlternatingStartZero",
            "vectors": [0x55]
        },
        {
            "scenario": "AlternatingStartOne",
            "vectors": [0xAA]
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
            "scenario": "WalkingOnes",
            "vectors": [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        },
        {
            "scenario": "RandomPattern",
            "vectors": [0xB2]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for val in sc["vectors"]:
            inputs.append({"in": _to_bit_str(val, width=8)})
        
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
