import json
def _to_bit_str(value: int, width: int = 32) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [0x00000000]
        },
        {
            "scenario": "AllOnes",
            "vectors": [0xFFFFFFFF]
        },
        {
            "scenario": "AlternatingBytes",
            "vectors": [0xFF00FF00]
        },
        {
            "scenario": "SingleBytePattern",
            "vectors": [0x000000FF]
        },
        {
            "scenario": "ReverseBytePattern",
            "vectors": [0xFF000000]
        },
        {
            "scenario": "UniqueBytes",
            "vectors": [0x12345678]
        },
        {
            "scenario": "AlternatingBits",
            "vectors": [0x55AA55AA]
        },
        {
            "scenario": "RandomPattern",
            "vectors": [0xA5C37F19]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for value in sc["vectors"]:
            inputs.append({
                "in": _to_bit_str(value, width=32)
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
