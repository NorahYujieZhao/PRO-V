import json
def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            'scenario': 'BothInputsZero',
            'input variable': [
                {'x': '0', 'y': '0'}
            ]
        },
        {
            'scenario': 'XOnlyHigh',
            'input variable': [
                {'x': '1', 'y': '0'}
            ]
        },
        {
            'scenario': 'YOnlyHigh',
            'input variable': [
                {'x': '0', 'y': '1'}
            ]
        },
        {
            'scenario': 'BothInputsOne',
            'input variable': [
                {'x': '1', 'y': '1'}
            ]
        },
        {
            'scenario': 'XTransitionLowToHigh',
            'input variable': [
                {'x': '0', 'y': '0'},
                {'x': '1', 'y': '0'}
            ]
        },
        {
            'scenario': 'YTransitionLowToHigh',
            'input variable': [
                {'x': '0', 'y': '0'},
                {'x': '0', 'y': '1'}
            ]
        },
        {
            'scenario': 'XTransitionHighToLow',
            'input variable': [
                {'x': '1', 'y': '1'},
                {'x': '0', 'y': '1'}
            ]
        },
        {
            'scenario': 'YTransitionHighToLow',
            'input variable': [
                {'x': '1', 'y': '1'},
                {'x': '1', 'y': '0'}
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
