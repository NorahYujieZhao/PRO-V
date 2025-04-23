import json
def _to_bit_str(value: int, width: int = 16) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "LeftArrowScancode",
            "vectors": [0xe06b]
        },
        {
            "scenario": "DownArrowScancode",
            "vectors": [0xe072]
        },
        {
            "scenario": "RightArrowScancode",
            "vectors": [0xe074]
        },
        {
            "scenario": "UpArrowScancode",
            "vectors": [0xe075]
        },
        {
            "scenario": "AllZeroInput",
            "vectors": [0x0000]
        },
        {
            "scenario": "AllOneInput",
            "vectors": [0xffff]
        },
        {
            "scenario": "AlternatingPattern",
            "vectors": [0x5555]
        },
        {
            "scenario": "NearValidCode",
            "vectors": [0xe06a, 0xe06c]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for val in sc["vectors"]:
            inputs.append({
                "scancode": _to_bit_str(val)
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
