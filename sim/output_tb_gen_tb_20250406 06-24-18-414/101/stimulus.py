import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "StateATransitions",
            "input variable": [
                {"in": "0", "state": "00"},
                {"in": "1", "state": "00"}
            ]
        },
        {
            "scenario": "StateBTransitions",
            "input variable": [
                {"in": "0", "state": "01"},
                {"in": "1", "state": "01"}
            ]
        },
        {
            "scenario": "StateCTransitions",
            "input variable": [
                {"in": "0", "state": "10"},
                {"in": "1", "state": "10"}
            ]
        },
        {
            "scenario": "StateDTransitions",
            "input variable": [
                {"in": "0", "state": "11"},
                {"in": "1", "state": "11"}
            ]
        },
        {
            "scenario": "OutputZeroStateA",
            "input variable": [
                {"in": "0", "state": "00"},
                {"in": "1", "state": "00"}
            ]
        },
        {
            "scenario": "OutputZeroStateB",
            "input variable": [
                {"in": "0", "state": "01"},
                {"in": "1", "state": "01"}
            ]
        },
        {
            "scenario": "OutputZeroStateC",
            "input variable": [
                {"in": "0", "state": "10"},
                {"in": "1", "state": "10"}
            ]
        },
        {
            "scenario": "OutputOneStateD",
            "input variable": [
                {"in": "0", "state": "11"},
                {"in": "1", "state": "11"}
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
