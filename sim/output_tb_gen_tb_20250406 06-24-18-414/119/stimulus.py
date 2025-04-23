import json
def _to_bit_str(value: int, width: int = 8) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZerosInput",
            "vectors": [0x00]
        },
        {
            "scenario": "AllOnesInput",
            "vectors": [0xFF]
        },
        {
            "scenario": "SmallestPositiveNumber",
            "vectors": [0x01]
        },
        {
            "scenario": "LargestPositiveNumber",
            "vectors": [0x7F]
        },
        {
            "scenario": "SmallestNegativeNumber",
            "vectors": [0x80]
        },
        {
            "scenario": "LargestNegativeNumber",
            "vectors": [0xFF]
        },
        {
            "scenario": "AlternatingBitsPositive",
            "vectors": [0x55]
        },
        {
            "scenario": "AlternatingBitsNegative",
            "vectors": [0xAA]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for val in sc["vectors"]:
            inputs.append({
                "in": _to_bit_str(val, width=8)
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
