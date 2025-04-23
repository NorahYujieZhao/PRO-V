import json
def _to_bit_str(value: int) -> str:
    return format(value, '01b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "LogicZero",
            "vectors": [0]
        },
        {
            "scenario": "LogicOne",
            "vectors": [1]
        },
        {
            "scenario": "ZeroToOne",
            "vectors": [0, 1]
        },
        {
            "scenario": "OneToZero",
            "vectors": [1, 0]
        },
        {
            "scenario": "FastToggling",
            "vectors": [0, 1, 0, 1, 0, 1]
        },
        {
            "scenario": "StableZero",
            "vectors": [0, 0, 0, 0]
        },
        {
            "scenario": "StableOne",
            "vectors": [1, 1, 1, 1]
        },
        {
            "scenario": "AlternatingPattern",
            "vectors": [0, 1, 0, 1, 0, 1, 0, 1]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for val in sc["vectors"]:
            inputs.append({"in": _to_bit_str(val)})
        
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
