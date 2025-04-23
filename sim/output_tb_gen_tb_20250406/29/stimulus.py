import json
def _to_bit_str(value: int, width: int = 4) -> str:
    return format(value & ((1 << width) - 1), f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "SelectInputB",
            "vectors": [(0x5, 0xA, 0x0, 0x3, 0x7), (0xF, 0x3, 0x0, 0x5, 0x9)]
        },
        {
            "scenario": "SelectInputE",
            "vectors": [(0x3, 0x5, 0x1, 0x7, 0xA), (0x9, 0x6, 0x1, 0x4, 0xC)]
        },
        {
            "scenario": "SelectInputA",
            "vectors": [(0xA, 0x5, 0x2, 0x3, 0x7), (0x6, 0x9, 0x2, 0x5, 0x8)]
        },
        {
            "scenario": "SelectInputD",
            "vectors": [(0x5, 0x3, 0x3, 0xA, 0x7), (0x9, 0x6, 0x3, 0xC, 0x4)]
        },
        {
            "scenario": "DefaultOutput",
            "vectors": [(0x5, 0x3, 0x4, 0xA, 0x7), (0x9, 0x6, 0xF, 0xC, 0x4)]
        },
        {
            "scenario": "AllZeroInputs",
            "vectors": [(0x0, 0x0, 0x0, 0x0, 0x0), (0x0, 0x0, 0x1, 0x0, 0x0),
                        (0x0, 0x0, 0x2, 0x0, 0x0), (0x0, 0x0, 0x3, 0x0, 0x0)]
        },
        {
            "scenario": "AllOnesInputs",
            "vectors": [(0xF, 0xF, 0x0, 0xF, 0xF), (0xF, 0xF, 0x1, 0xF, 0xF),
                        (0xF, 0xF, 0x2, 0xF, 0xF), (0xF, 0xF, 0x3, 0xF, 0xF)]
        },
        {
            "scenario": "AlternatingPatterns",
            "vectors": [(0xA, 0x5, 0x0, 0xA, 0x5), (0x5, 0xA, 0x1, 0x5, 0xA),
                        (0xA, 0x5, 0x2, 0xA, 0x5), (0x5, 0xA, 0x3, 0x5, 0xA)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val, c_val, d_val, e_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val),
                "b": _to_bit_str(b_val),
                "c": _to_bit_str(c_val),
                "d": _to_bit_str(d_val),
                "e": _to_bit_str(e_val)
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
