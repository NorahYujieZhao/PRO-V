import json
def _to_bit_str(value: int, width: int = 4) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "vectors": [(0, 0)]
        },
        {
            "scenario": "AllOnesInputs",
            "vectors": [(15, 15)]
        },
        {
            "scenario": "AlternatingBitsX",
            "vectors": [(10, 5)]
        },
        {
            "scenario": "SingleBitCarry",
            "vectors": [(1, 15)]
        },
        {
            "scenario": "MidrangeAddition",
            "vectors": [(7, 7)]
        },
        {
            "scenario": "OneHotX",
            "vectors": [(8, 1)]
        },
        {
            "scenario": "SmallNumbers",
            "vectors": [(3, 2)]
        },
        {
            "scenario": "JustOverflow",
            "vectors": [(8, 8)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for x_val, y_val in sc["vectors"]:
            inputs.append({
                "x": _to_bit_str(x_val, width=4),
                "y": _to_bit_str(y_val, width=4)
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
