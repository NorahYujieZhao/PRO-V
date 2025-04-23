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
            "scenario": "OnlyAHigh",
            "vectors": [(1, 0, 0)]
        },
        {
            "scenario": "OnlyBHigh",
            "vectors": [(0, 1, 0)]
        },
        {
            "scenario": "OnlyCHigh",
            "vectors": [(0, 0, 1)]
        },
        {
            "scenario": "TwoInputsHigh",
            "vectors": [(1, 1, 0)]
        },
        {
            "scenario": "AlternatingPattern",
            "vectors": [(1, 0, 1)]
        },
        {
            "scenario": "ComplementPattern",
            "vectors": [(0, 1, 1)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val, c_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val),
                "b": _to_bit_str(b_val),
                "c": _to_bit_str(c_val)
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
