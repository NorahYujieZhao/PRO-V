
import json
import random

def stimulus_gen():
    # Helper function to convert 4 bits to string format
    def bits_to_str(x1, x2, x3, x4):
        return f'{x1}{x2}{x3}{x4}'

    # Known valid combinations from K-map (excluding don't cares)
    valid_combinations = {
        'OUTPUT_0': [
            bits_to_str(0,0,0,1),  # x[4:1] = 0001
            bits_to_str(0,1,0,1),  # x[4:1] = 0101
            bits_to_str(1,1,0,1),  # x[4:1] = 1101
            bits_to_str(1,1,1,0)   # x[4:1] = 1110
        ],
        'OUTPUT_1': [
            bits_to_str(1,0,1,1),  # x[4:1] = 1011
            bits_to_str(1,0,1,0),  # x[4:1] = 1010
            bits_to_str(0,1,1,1),  # x[4:1] = 0111
            bits_to_str(1,0,0,1),  # x[4:1] = 1001
            bits_to_str(1,0,0,0)   # x[4:1] = 1000
        ],
        'TRANSITION_SEQUENCE': [
            bits_to_str(1,0,0,0),  # Output 1
            bits_to_str(0,1,0,1),  # Output 0
            bits_to_str(1,0,1,1),  # Output 1
            bits_to_str(1,1,1,0)   # Output 0
        ]
    }

    stimuli = []
    
    # Generate test scenarios
    for scenario_name, input_patterns in valid_combinations.items():
        input_list = []
        for pattern in input_patterns:
            input_vars = {
                'x': pattern
            }
            input_list.append(input_vars)
        
        stimuli.append({
            'scenario': scenario_name,
            'input variable': input_list
        })

    return stimuli
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
