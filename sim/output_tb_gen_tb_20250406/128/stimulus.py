import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "vectors": [(0, 0, 0)]
        },
        {
            "scenario": "AllOneInputs",
            "vectors": [(1, 1, 1)]
        },
        {
            "scenario": "AlternatingPattern1",
            "vectors": [(0, 1, 0)]
        },
        {
            "scenario": "AlternatingPattern2",
            "vectors": [(1, 0, 1)]
        },
        {
            "scenario": "LowBitsActive",
            "vectors": [(0, 1, 1)]
        },
        {
            "scenario": "HighBitsActive",
            "vectors": [(1, 1, 0)]
        },
        {
            "scenario": "SingleBitHigh1",
            "vectors": [(0, 0, 1)]
        },
        {
            "scenario": "SingleBitHigh2",
            "vectors": [(1, 0, 0)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for x3_val, x2_val, x1_val in sc["vectors"]:
            inputs.append({
                "x3": _to_bit_str(x3_val),
                "x2": _to_bit_str(x2_val),
                "x1": _to_bit_str(x1_val)
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
