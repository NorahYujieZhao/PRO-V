import json
def _to_bit_str(value: int) -> str:
    return format(value, '01b')

def stimulus_gen() -> list[dict]:
    stimulus_list = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [
                {"a": "0", "b": "0"}
            ]
        },
        {
            "scenario": "InputAOneInputBZero",
            "input variable": [
                {"a": "1", "b": "0"}
            ]
        },
        {
            "scenario": "InputAZeroInputBOne",
            "input variable": [
                {"a": "0", "b": "1"}
            ]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [
                {"a": "1", "b": "1"}
            ]
        },
        {
            "scenario": "AlternatingPatternOne",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "1", "b": "0"},
                {"a": "0", "b": "0"},
                {"a": "1", "b": "0"}
            ]
        },
        {
            "scenario": "AlternatingPatternTwo",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "0", "b": "1"},
                {"a": "0", "b": "0"},
                {"a": "0", "b": "1"}
            ]
        },
        {
            "scenario": "ComplementaryInputs",
            "input variable": [
                {"a": "0", "b": "1"},
                {"a": "1", "b": "0"},
                {"a": "0", "b": "1"},
                {"a": "1", "b": "0"}
            ]
        },
        {
            "scenario": "SimultaneousTransitions",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "1", "b": "1"}
            ]
        }
    ]
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
