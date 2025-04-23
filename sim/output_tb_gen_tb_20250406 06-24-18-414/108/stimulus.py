import json
def _to_bit_str(value: int, width: int = 2) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [(0, 0)]
        },
        {
            "scenario": "AllOnes",
            "vectors": [(3, 3)]
        },
        {
            "scenario": "MismatchZeroOne",
            "vectors": [(0, 3)]
        },
        {
            "scenario": "MismatchOneZero",
            "vectors": [(3, 0)]
        },
        {
            "scenario": "AdjacentValues",
            "vectors": [(1, 2)]
        },
        {
            "scenario": "OneHotA",
            "vectors": [(2, 1)]
        },
        {
            "scenario": "MidrangeEqual",
            "vectors": [(1, 1)]
        },
        {
            "scenario": "AlternatingBits",
            "vectors": [(2, 2)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val in sc["vectors"]:
            inputs.append({
                "A": _to_bit_str(a_val, width=2),
                "B": _to_bit_str(b_val, width=2)
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
