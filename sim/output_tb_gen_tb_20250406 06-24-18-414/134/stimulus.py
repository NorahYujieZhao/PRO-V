import json
def _to_bit_str(value: int, width: int = 5) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [{
                "a": "00000",
                "b": "00000",
                "c": "00000",
                "d": "00000",
                "e": "00000",
                "f": "00000"
            }]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [{
                "a": "11111",
                "b": "11111",
                "c": "11111",
                "d": "11111",
                "e": "11111",
                "f": "11111"
            }]
        },
        {
            "scenario": "AlternatingBits",
            "input variable": [{
                "a": "10101",
                "b": "10101",
                "c": "10101",
                "d": "10101",
                "e": "10101",
                "f": "10101"
            }]
        },
        {
            "scenario": "CountingPattern",
            "input variable": [{
                "a": "00001",
                "b": "00010",
                "c": "00011",
                "d": "00100",
                "e": "00101",
                "f": "00110"
            }]
        },
        {
            "scenario": "OneHotInputs",
            "input variable": [{
                "a": "00001",
                "b": "00010",
                "c": "00100",
                "d": "01000",
                "e": "10000",
                "f": "00001"
            }]
        },
        {
            "scenario": "ReverseCountingPattern",
            "input variable": [{
                "a": "11111",
                "b": "11110",
                "c": "11101",
                "d": "11100",
                "e": "11011",
                "f": "11010"
            }]
        },
        {
            "scenario": "CheckerboardPattern",
            "input variable": [{
                "a": "11111",
                "b": "00000",
                "c": "11111",
                "d": "00000",
                "e": "11111",
                "f": "00000"
            }]
        },
        {
            "scenario": "WalkingOnes",
            "input variable": [{
                "a": "00001",
                "b": "00010",
                "c": "00100",
                "d": "01000",
                "e": "10000",
                "f": "00001"
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
