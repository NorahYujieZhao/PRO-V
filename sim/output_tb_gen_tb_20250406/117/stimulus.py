import json
def stimulus_gen():
    scenarios = [
        {
            'scenario': 'AllZerosInput',
            'input variable': [{'a': '0', 'b': '0', 'c': '0', 'd': '0'}]
        },
        {
            'scenario': 'TopRowSweep',
            'input variable': [
                {'a': '0', 'b': '0', 'c': '0', 'd': '0'},
                {'a': '0', 'b': '1', 'c': '0', 'd': '0'},
                {'a': '1', 'b': '1', 'c': '0', 'd': '0'},
                {'a': '1', 'b': '0', 'c': '0', 'd': '0'}
            ]
        },
        {
            'scenario': 'BottomRowSweep',
            'input variable': [
                {'a': '0', 'b': '0', 'c': '1', 'd': '1'},
                {'a': '0', 'b': '1', 'c': '1', 'd': '1'},
                {'a': '1', 'b': '1', 'c': '1', 'd': '1'},
                {'a': '1', 'b': '0', 'c': '1', 'd': '1'}
            ]
        },
        {
            'scenario': 'LeftColumnSweep',
            'input variable': [
                {'a': '0', 'b': '0', 'c': '0', 'd': '0'},
                {'a': '0', 'b': '0', 'c': '0', 'd': '1'},
                {'a': '0', 'b': '0', 'c': '1', 'd': '1'},
                {'a': '0', 'b': '0', 'c': '1', 'd': '0'}
            ]
        },
        {
            'scenario': 'RightColumnSweep',
            'input variable': [
                {'a': '1', 'b': '0', 'c': '0', 'd': '0'},
                {'a': '1', 'b': '0', 'c': '0', 'd': '1'},
                {'a': '1', 'b': '0', 'c': '1', 'd': '1'},
                {'a': '1', 'b': '0', 'c': '1', 'd': '0'}
            ]
        },
        {
            'scenario': 'AlternatingBitPattern',
            'input variable': [
                {'a': '0', 'b': '1', 'c': '0', 'd': '1'},
                {'a': '1', 'b': '0', 'c': '1', 'd': '0'}
            ]
        },
        {
            'scenario': 'DiagonalTransition',
            'input variable': [
                {'a': '0', 'b': '0', 'c': '0', 'd': '0'},
                {'a': '0', 'b': '1', 'c': '0', 'd': '1'},
                {'a': '1', 'b': '1', 'c': '1', 'd': '1'}
            ]
        },
        {
            'scenario': 'BoundaryTransition',
            'input variable': [
                {'a': '0', 'b': '0', 'c': '0', 'd': '0'},
                {'a': '0', 'b': '1', 'c': '0', 'd': '1'},
                {'a': '1', 'b': '1', 'c': '0', 'd': '0'},
                {'a': '1', 'b': '0', 'c': '1', 'd': '0'}
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
