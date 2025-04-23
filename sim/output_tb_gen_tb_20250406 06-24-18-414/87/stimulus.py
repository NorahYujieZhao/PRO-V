import json
def _to_bit_str(value: int) -> str:
    return format(value, '01b')

def stimulus_gen() -> list[dict]:
    stimulus_list = [
        {
            "scenario": "StaticLowInput",
            "input variable": [
                {"in": "0"},
                {"in": "0"},
                {"in": "0"}
            ]
        },
        {
            "scenario": "StaticHighInput",
            "input variable": [
                {"in": "1"},
                {"in": "1"},
                {"in": "1"}
            ]
        },
        {
            "scenario": "LowToHighTransition",
            "input variable": [
                {"in": "0"},
                {"in": "1"}
            ]
        },
        {
            "scenario": "HighToLowTransition",
            "input variable": [
                {"in": "1"},
                {"in": "0"}
            ]
        },
        {
            "scenario": "AlternatingPattern",
            "input variable": [
                {"in": "0"},
                {"in": "1"},
                {"in": "0"},
                {"in": "1"}
            ]
        },
        {
            "scenario": "FastToggling",
            "input variable": [
                {"in": "0"},
                {"in": "1"},
                {"in": "0"},
                {"in": "1"},
                {"in": "0"},
                {"in": "1"}
            ]
        },
        {
            "scenario": "InitialPowerup",
            "input variable": [
                {"in": "0"},
                {"in": "1"}
            ]
        },
        {
            "scenario": "GlitchTest",
            "input variable": [
                {"in": "0"},
                {"in": "1"},
                {"in": "0"}
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
