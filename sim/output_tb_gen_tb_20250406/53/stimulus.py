import json
def _to_bit_str(value: int) -> str:
    return format(value, '01b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [{
                "in1": "0",
                "in2": "0"
            }]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [{
                "in1": "1",
                "in2": "1"
            }]
        },
        {
            "scenario": "Input1HighInput2Low",
            "input variable": [{
                "in1": "1",
                "in2": "0"
            }]
        },
        {
            "scenario": "Input1LowInput2High",
            "input variable": [{
                "in1": "0",
                "in2": "1"
            }]
        },
        {
            "scenario": "Input1ToggleInput2Zero",
            "input variable": [
                {"in1": "0", "in2": "0"},
                {"in1": "1", "in2": "0"}
            ]
        },
        {
            "scenario": "Input1ToggleInput2One",
            "input variable": [
                {"in1": "0", "in2": "1"},
                {"in1": "1", "in2": "1"}
            ]
        },
        {
            "scenario": "Input2ToggleInput1Zero",
            "input variable": [
                {"in1": "0", "in2": "0"},
                {"in1": "0", "in2": "1"}
            ]
        },
        {
            "scenario": "Input2ToggleInput1One",
            "input variable": [
                {"in1": "1", "in2": "0"},
                {"in1": "1", "in2": "1"}
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
