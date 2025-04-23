import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [
                {"in1": "0", "in2": "0"}
            ]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [
                {"in1": "1", "in2": "1"}
            ]
        },
        {
            "scenario": "Input1HighInput2Low",
            "input variable": [
                {"in1": "1", "in2": "0"}
            ]
        },
        {
            "scenario": "Input1LowInput2High",
            "input variable": [
                {"in1": "0", "in2": "1"}
            ]
        },
        {
            "scenario": "AlternatingInputs1",
            "input variable": [
                {"in1": "0", "in2": "0"},
                {"in1": "1", "in2": "0"}
            ]
        },
        {
            "scenario": "AlternatingInputs2",
            "input variable": [
                {"in1": "0", "in2": "0"},
                {"in1": "0", "in2": "1"}
            ]
        },
        {
            "scenario": "ComplementaryInputs1",
            "input variable": [
                {"in1": "0", "in2": "1"},
                {"in1": "1", "in2": "0"}
            ]
        },
        {
            "scenario": "SimultaneousTransitions",
            "input variable": [
                {"in1": "0", "in2": "0"},
                {"in1": "1", "in2": "1"},
                {"in1": "0", "in2": "0"}
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
