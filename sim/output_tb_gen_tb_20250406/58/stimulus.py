import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "vectors": [(0, 0)]
        },
        {
            "scenario": "AllOneInputs",
            "vectors": [(1, 1)]
        },
        {
            "scenario": "XOnlyHigh",
            "vectors": [(1, 0)]
        },
        {
            "scenario": "YOnlyHigh",
            "vectors": [(0, 1)]
        },
        {
            "scenario": "AlternateXY",
            "vectors": [(0, 1), (1, 0), (0, 1), (1, 0)]
        },
        {
            "scenario": "XTransitionOnly",
            "vectors": [(0, 0), (1, 0), (0, 0), (1, 0)]
        },
        {
            "scenario": "YTransitionOnly",
            "vectors": [(0, 0), (0, 1), (0, 0), (0, 1)]
        },
        {
            "scenario": "SimultaneousTransitions",
            "vectors": [(0, 0), (1, 1), (0, 0), (1, 1)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for x_val, y_val in sc["vectors"]:
            inputs.append({
                "x": _to_bit_str(x_val),
                "y": _to_bit_str(y_val)
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
