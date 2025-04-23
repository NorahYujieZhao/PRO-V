import json
import random

def stimulus_gen():
    # Helper function to format 4-bit input as binary string
    def format_input(x1, x2, x3, x4):
        return {'x': f'{x1}{x2}{x3}{x4}'}

    scenarios = [
        {
            'scenario': 'KnownOutput0',
            'input variable': [
                format_input('0','0','0','1'),  # x[4:1] = 0001
                format_input('0','1','0','1'),  # x[4:1] = 0101
                format_input('1','0','0','1'),  # x[4:1] = 1001
                format_input('1','1','1','0')   # x[4:1] = 1110
            ]
        },
        {
            'scenario': 'KnownOutput1',
            'input variable': [
                format_input('1','1','0','0'),  # x[4:1] = 1100
                format_input('1','1','0','1'),  # x[4:1] = 1101
                format_input('0','1','1','1'),  # x[4:1] = 0111
                format_input('1','1','1','1')   # x[4:1] = 1111
            ]
        },
        {
            'scenario': 'EdgeTransitions',
            'input variable': [
                format_input('0','1','0','1'),  # x[4:1] = 0101 (output 0)
                format_input('0','1','1','1'),  # x[4:1] = 0111 (output 1)
                format_input('1','1','1','0'),  # x[4:1] = 1110 (output 0)
                format_input('1','1','0','0')   # x[4:1] = 1100 (output 1)
            ]
        },
        {
            'scenario': 'ValidRandomCombinations',
            'input variable': [
                format_input('1','1','0','0'),  # x[4:1] = 1100
                format_input('0','1','0','1'),  # x[4:1] = 0101
                format_input('1','1','1','0'),  # x[4:1] = 1110
                format_input('0','1','1','1')   # x[4:1] = 0111
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
