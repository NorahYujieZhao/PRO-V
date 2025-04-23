import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value & ((1 << width) - 1), f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [
                {"do_sub": "0", "a": "00000000", "b": "00000000"},
                {"do_sub": "1", "a": "00000000", "b": "00000000"}
            ]
        },
        {
            "scenario": "AllOnesInputs",
            "input variable": [
                {"do_sub": "0", "a": "11111111", "b": "11111111"},
                {"do_sub": "1", "a": "11111111", "b": "11111111"}
            ]
        },
        {
            "scenario": "AdditionOverflow",
            "input variable": [
                {"do_sub": "0", "a": "10000000", "b": "10000000"}
            ]
        },
        {
            "scenario": "SubtractionUnderflow",
            "input variable": [
                {"do_sub": "1", "a": "00000000", "b": "00000001"}
            ]
        },
        {
            "scenario": "AlternatingBitPattern",
            "input variable": [
                {"do_sub": "0", "a": "10101010", "b": "01010101"},
                {"do_sub": "1", "a": "10101010", "b": "01010101"}
            ]
        },
        {
            "scenario": "OneHotPattern",
            "input variable": [
                {"do_sub": "0", "a": "00000001", "b": "00000000"},
                {"do_sub": "0", "a": "00000010", "b": "00000000"},
                {"do_sub": "0", "a": "00000100", "b": "00000000"},
                {"do_sub": "0", "a": "00001000", "b": "00000000"},
                {"do_sub": "1", "a": "00010000", "b": "00000000"},
                {"do_sub": "1", "a": "00100000", "b": "00000000"},
                {"do_sub": "1", "a": "01000000", "b": "00000000"},
                {"do_sub": "1", "a": "10000000", "b": "00000000"}
            ]
        },
        {
            "scenario": "ZeroResultAddition",
            "input variable": [
                {"do_sub": "0", "a": "01011010", "b": "10100101"}
            ]
        },
        {
            "scenario": "ZeroResultSubtraction",
            "input variable": [
                {"do_sub": "1", "a": "00110111", "b": "00110111"}
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
