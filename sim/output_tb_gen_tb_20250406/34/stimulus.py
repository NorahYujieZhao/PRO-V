import json
def _to_bit_str(value: int, width: int = 8) -> str:
    # Convert integer to binary string with leading zeros
    # Handle negative numbers for 2's complement
    if value < 0:
        value = (1 << width) + value
    return format(value & ((1 << width) - 1), f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "vectors": [(0, 0)]
        },
        {
            "scenario": "AllOnes",
            "vectors": [(-1, -1)]
        },
        {
            "scenario": "MaxPositiveNumbers",
            "vectors": [(127, 127)]
        },
        {
            "scenario": "MaxNegativeNumbers",
            "vectors": [(-128, -128)]
        },
        {
            "scenario": "PositiveNegativePair",
            "vectors": [(127, -127)]
        },
        {
            "scenario": "AlternatingBitPattern",
            "vectors": [(0x55, 0xAA)]
        },
        {
            "scenario": "SmallPositiveNumbers",
            "vectors": [(1, 2)]
        },
        {
            "scenario": "SmallNegativeNumbers",
            "vectors": [(-2, -3)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val, b_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val),
                "b": _to_bit_str(b_val)
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
