
import json
import random

def stimulus_gen():
    # Helper function to format binary inputs
    def format_cd(c, d):
        return {
            'c': format(c, '01b'),
            'd': format(d, '01b')
        }

    scenarios = [
        {
            'scenario': 'CD_00',
            'input variable': [format_cd(0, 0)]
        },
        {
            'scenario': 'CD_01',
            'input variable': [format_cd(0, 1)]
        },
        {
            'scenario': 'CD_11',
            'input variable': [format_cd(1, 1)]
        },
        {
            'scenario': 'CD_10',
            'input variable': [format_cd(1, 0)]
        },
        {
            'scenario': 'ToggleC_KeepD0',
            'input variable': [
                format_cd(0, 0),
                format_cd(1, 0)
            ]
        },
        {
            'scenario': 'ToggleD_KeepC0',
            'input variable': [
                format_cd(0, 0),
                format_cd(0, 1)
            ]
        },
        {
            'scenario': 'ToggleC_KeepD1',
            'input variable': [
                format_cd(0, 1),
                format_cd(1, 1)
            ]
        },
        {
            'scenario': 'ComplexSequence',
            'input variable': [
                format_cd(0, 0),
                format_cd(0, 1),
                format_cd(1, 1),
                format_cd(1, 0)
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
