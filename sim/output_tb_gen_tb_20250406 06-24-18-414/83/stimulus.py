import json
def _to_bit_str(value: int, width: int = 8) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllValidScancodes",
            "input variable": [
                {"code": _to_bit_str(0x45)},
                {"code": _to_bit_str(0x16)},
                {"code": _to_bit_str(0x1e)},
                {"code": _to_bit_str(0x26)},
                {"code": _to_bit_str(0x25)},
                {"code": _to_bit_str(0x2e)},
                {"code": _to_bit_str(0x36)},
                {"code": _to_bit_str(0x3d)},
                {"code": _to_bit_str(0x3e)},
                {"code": _to_bit_str(0x46)}
            ]
        },
        {
            "scenario": "AllZeros",
            "input variable": [{"code": _to_bit_str(0x00)}]
        },
        {
            "scenario": "AllOnes",
            "input variable": [{"code": _to_bit_str(0xff)}]
        },
        {
            "scenario": "NearValidCodes",
            "input variable": [
                {"code": _to_bit_str(0x44)},
                {"code": _to_bit_str(0x46)},
                {"code": _to_bit_str(0x15)},
                {"code": _to_bit_str(0x17)}
            ]
        },
        {
            "scenario": "AlternatingBits",
            "input variable": [
                {"code": _to_bit_str(0x55)},
                {"code": _to_bit_str(0xaa)}
            ]
        },
        {
            "scenario": "SingleBitSet",
            "input variable": [
                {"code": _to_bit_str(0x01)},
                {"code": _to_bit_str(0x02)},
                {"code": _to_bit_str(0x04)},
                {"code": _to_bit_str(0x08)},
                {"code": _to_bit_str(0x10)},
                {"code": _to_bit_str(0x20)},
                {"code": _to_bit_str(0x40)},
                {"code": _to_bit_str(0x80)}
            ]
        },
        {
            "scenario": "ValidCodeBoundaries",
            "input variable": [
                {"code": _to_bit_str(0x44)},
                {"code": _to_bit_str(0x46)},
                {"code": _to_bit_str(0x15)},
                {"code": _to_bit_str(0x17)},
                {"code": _to_bit_str(0x1d)},
                {"code": _to_bit_str(0x1f)}
            ]
        },
        {
            "scenario": "RandomInvalidCodes",
            "input variable": [
                {"code": _to_bit_str(0x12)},
                {"code": _to_bit_str(0x34)},
                {"code": _to_bit_str(0x56)},
                {"code": _to_bit_str(0x78)},
                {"code": _to_bit_str(0x9a)},
                {"code": _to_bit_str(0xbc)},
                {"code": _to_bit_str(0xde)}
            ]
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
