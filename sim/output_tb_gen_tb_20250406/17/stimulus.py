import json
def _to_bit_str(value: int, width: int = 3) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [0]
        },
        {
            "scenario": "AllOnes",
            "vectors": [7]
        },
        {
            "scenario": "AlternatingBitsStartZero",
            "vectors": [2]
        },
        {
            "scenario": "AlternatingBitsStartOne",
            "vectors": [5]
        },
        {
            "scenario": "OneHotLSB",
            "vectors": [1]
        },
        {
            "scenario": "OneHotMSB",
            "vectors": [4]
        },
        {
            "scenario": "OneHotMiddle",
            "vectors": [2]
        },
        {
            "scenario": "GrayCodePattern",
            "vectors": [3]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for vec_val in sc["vectors"]:
            inputs.append({
                "vec": _to_bit_str(vec_val, width=3)
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
