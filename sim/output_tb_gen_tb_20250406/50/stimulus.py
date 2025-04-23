import json
def _to_bit_str(value: int, width: int = 4) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [0b0000]
        },
        {
            "scenario": "AllOnes",
            "vectors": [0b1111]
        },
        {
            "scenario": "AlternatingBits",
            "vectors": [0b1010]
        },
        {
            "scenario": "SingleOneHot",
            "vectors": [0b0100]
        },
        {
            "scenario": "AdjacentPairOnes",
            "vectors": [0b0011]
        },
        {
            "scenario": "WrapAroundDifferent",
            "vectors": [0b1000]
        },
        {
            "scenario": "UpperBoundaryCheck",
            "vectors": [0b1100]
        },
        {
            "scenario": "LowerBoundaryCheck",
            "vectors": [0b0001]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for vec in sc["vectors"]:
            inputs.append({
                "in": _to_bit_str(vec, width=4)
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
