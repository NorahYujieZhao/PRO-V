import json
def _to_bit_str(value: int, width: int = 3) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "vectors": [(0, 0)]
        },
        {
            "scenario": "AllOneInputs",
            "vectors": [(7, 7)]
        },
        {
            "scenario": "AlternatingBitsComplementary",
            "vectors": [(5, 2)]
        },
        {
            "scenario": "OneHotA",
            "vectors": [(4, 0)]
        },
        {
            "scenario": "OneHotB",
            "vectors": [(0, 2)]
        },
        {
            "scenario": "MixedPattern1",
            "vectors": [(6, 1)]
        },
        {
            "scenario": "MixedPattern2",
            "vectors": [(3, 4)]
        },
        {
            "scenario": "LogicalORCheck",
            "vectors": [(1, 4)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val, width=3),
                "b": _to_bit_str(b_val, width=3)
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
