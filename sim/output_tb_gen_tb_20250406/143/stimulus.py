import json
def stimulus_gen():
    # Helper function to format 4 bits into x[4:1] format
    def format_input(x4, x3, x2, x1):
        return {'x': f'{x4}{x3}{x2}{x1}'}

    scenarios = [
        # Test all defined 1s from K-map
        {
            'scenario': 'TestOnes',
            'input variable': [
                format_input(0,0,0,0),  # x[4:1] = 0000
                format_input(0,0,1,0),  # x[4:1] = 0010
                format_input(1,1,0,0),  # x[4:1] = 1100
                format_input(1,1,0,1),  # x[4:1] = 1101
                format_input(1,1,1,1),  # x[4:1] = 1111
                format_input(1,0,0,0),  # x[4:1] = 1000
                format_input(1,0,0,1)   # x[4:1] = 1001
            ]
        },
        # Test all defined 0s from K-map
        {
            'scenario': 'TestZeros',
            'input variable': [
                format_input(0,0,0,1),  # x[4:1] = 0001
                format_input(0,0,1,1),  # x[4:1] = 0011
                format_input(0,1,0,0),  # x[4:1] = 0100
                format_input(0,1,0,1),  # x[4:1] = 0101
                format_input(0,1,1,1),  # x[4:1] = 0111
                format_input(0,1,1,0),  # x[4:1] = 0110
                format_input(1,1,1,0),  # x[4:1] = 1110
                format_input(1,0,1,1)   # x[4:1] = 1011
            ]
        },
        # Edge cases - all zeros and all ones
        {
            'scenario': 'EdgeCases',
            'input variable': [
                format_input(0,0,0,0),  # All zeros
                format_input(1,1,1,1)   # All ones
            ]
        },
        # Random test cases
        {
            'scenario': 'RandomTests',
            'input variable': [
                format_input(1,0,1,0),
                format_input(0,1,1,0),
                format_input(1,1,0,1),
                format_input(0,0,1,1),
                format_input(1,0,0,1),
                format_input(0,1,0,1),
                format_input(1,1,1,0),
                format_input(0,0,0,1),
                format_input(1,0,1,1),
                format_input(0,1,1,1)
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
