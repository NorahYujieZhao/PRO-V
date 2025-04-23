import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
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
            "scenario": "OnlyAHigh",
            "input variable": [
                {"a": "1", "b": "0"}
            ]
        },
        {
            "scenario": "OnlyBHigh",
            "input variable": [
                {"a": "0", "b": "1"}
            ]
        },
        {
            "scenario": "ALeadingTransition",
            "input variable": [
                {"a": "0", "b": "1"},
                {"a": "1", "b": "1"}
            ]
        },
        {
            "scenario": "BLeadingTransition",
            "input variable": [
                {"a": "1", "b": "0"},
                {"a": "1", "b": "1"}
            ]
        },
        {
            "scenario": "ATrailingTransition",
            "input variable": [
                {"a": "1", "b": "1"},
                {"a": "0", "b": "1"}
            ]
        },
        {
            "scenario": "BTrailingTransition",
            "input variable": [
                {"a": "1", "b": "1"},
                {"a": "1", "b": "0"}
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
