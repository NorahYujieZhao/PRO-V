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
            "scenario": "AllOneInputs",
            "input variable": [
                {"a": "1", "b": "1"}
            ]
        },
        {
            "scenario": "MixedInputsAZeroBOne",
            "input variable": [
                {"a": "0", "b": "1"}
            ]
        },
        {
            "scenario": "MixedInputsAOneBZero",
            "input variable": [
                {"a": "1", "b": "0"}
            ]
        },
        {
            "scenario": "TransitionFromZeroToOne",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "1", "b": "0"},
                {"a": "1", "b": "1"}
            ]
        },
        {
            "scenario": "TransitionFromOneToZero",
            "input variable": [
                {"a": "1", "b": "1"},
                {"a": "1", "b": "0"},
                {"a": "0", "b": "0"}
            ]
        },
        {
            "scenario": "AlternatingInputs",
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
                {"a": "1", "b": "1"},
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
