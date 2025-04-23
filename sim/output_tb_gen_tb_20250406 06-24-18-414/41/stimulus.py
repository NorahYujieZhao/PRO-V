import json
def _to_bit_str(value: int) -> str:
    return format(value, '01b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "vectors": [(0,0,0,0)]
        },
        {
            "scenario": "AllOneInputs",
            "vectors": [(1,1,1,1)]
        },
        {
            "scenario": "FirstAndGateActive",
            "vectors": [(1,1,0,0)]
        },
        {
            "scenario": "SecondAndGateActive",
            "vectors": [(0,0,1,1)]
        },
        {
            "scenario": "BothAndGatesActive",
            "vectors": [(1,1,1,1)]
        },
        {
            "scenario": "AlternatingInputs",
            "vectors": [(1,0,1,0)]
        },
        {
            "scenario": "FirstInputsOnly",
            "vectors": [(1,1,0,1)]
        },
        {
            "scenario": "SecondInputsOnly",
            "vectors": [(0,1,1,1)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val, c_val, d_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val),
                "b": _to_bit_str(b_val),
                "c": _to_bit_str(c_val),
                "d": _to_bit_str(d_val)
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
