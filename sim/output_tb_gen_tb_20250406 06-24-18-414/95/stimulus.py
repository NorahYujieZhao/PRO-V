import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "SelectInputA",
            "vectors": [(1, 0, 0)]  # a=1, b=0, sel=0
        },
        {
            "scenario": "SelectInputB",
            "vectors": [(0, 1, 1)]  # a=0, b=1, sel=1
        },
        {
            "scenario": "AllInputsZero",
            "vectors": [(0, 0, 0)]  # a=0, b=0, sel=0
        },
        {
            "scenario": "AllInputsOne",
            "vectors": [(1, 1, 1)]  # a=1, b=1, sel=1
        },
        {
            "scenario": "SelectAWithEqualInputs",
            "vectors": [(1, 1, 0)]  # a=1, b=1, sel=0
        },
        {
            "scenario": "SelectBWithEqualInputs",
            "vectors": [(0, 0, 1)]  # a=0, b=0, sel=1
        },
        {
            "scenario": "ComplementaryInputsSelectA",
            "vectors": [(1, 0, 0)]  # a=1, b=0, sel=0
        },
        {
            "scenario": "ComplementaryInputsSelectB",
            "vectors": [(0, 1, 1)]  # a=0, b=1, sel=1
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val, sel_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val),
                "b": _to_bit_str(b_val),
                "sel": _to_bit_str(sel_val)
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
