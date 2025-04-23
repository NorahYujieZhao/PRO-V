import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [{"x": "0", "y": "0"}]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [{"x": "1", "y": "1"}]
        },
        {
            "scenario": "InputXOnlyHigh",
            "input variable": [{"x": "1", "y": "0"}]
        },
        {
            "scenario": "InputYOnlyHigh",
            "input variable": [{"x": "0", "y": "1"}]
        },
        {
            "scenario": "AlternatingXFirst",
            "input variable": [
                {"x": "0", "y": "0"},
                {"x": "1", "y": "0"},
                {"x": "0", "y": "1"},
                {"x": "1", "y": "1"}
            ]
        },
        {
            "scenario": "AlternatingYFirst",
            "input variable": [
                {"x": "0", "y": "0"},
                {"x": "0", "y": "1"},
                {"x": "1", "y": "0"},
                {"x": "1", "y": "1"}
            ]
        },
        {
            "scenario": "AlternatingBoth",
            "input variable": [
                {"x": "0", "y": "0"},
                {"x": "1", "y": "1"},
                {"x": "0", "y": "1"},
                {"x": "1", "y": "0"}
            ]
        },
        {
            "scenario": "RandomPatterns",
            "input variable": [
                {"x": "0", "y": "1"},
                {"x": "1", "y": "1"},
                {"x": "1", "y": "0"},
                {"x": "0", "y": "0"}
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
