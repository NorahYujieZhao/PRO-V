import json
def _to_bit_str(value: int, width: int) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeros",
            "input variable": [{
                "in": _to_bit_str(0x0000, 16)
            }]
        },
        {
            "scenario": "AllOnes",
            "input variable": [{
                "in": _to_bit_str(0xFFFF, 16)
            }]
        },
        {
            "scenario": "UpperByteOnly",
            "input variable": [{
                "in": _to_bit_str(0xFF00, 16)
            }]
        },
        {
            "scenario": "LowerByteOnly",
            "input variable": [{
                "in": _to_bit_str(0x00FF, 16)
            }]
        },
        {
            "scenario": "AlternatingBitsUpper",
            "input variable": [{
                "in": _to_bit_str(0xAA00, 16)
            }]
        },
        {
            "scenario": "AlternatingBitsLower",
            "input variable": [{
                "in": _to_bit_str(0x0055, 16)
            }]
        },
        {
            "scenario": "AlternatingBytes",
            "input variable": [{
                "in": _to_bit_str(0x5555, 16)
            }]
        },
        {
            "scenario": "ComplementaryBytes",
            "input variable": [{
                "in": _to_bit_str(0xA55A, 16)
            }]
        }
    ]
    return scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
