
import json
import random

def stimulus_gen():
    # Define valid input combinations and their expected outputs
    valid_inputs = {
        'ZERO': '0000',
        'ONE': '0001',
        'TWO': '0010',
        'FOUR': '0100',
        'FIVE': '0101',
        'SIX': '0110',
        'SEVEN': '0111',
        'NINE': '1001',
        'TEN': '1010',
        'THIRTEEN': '1101',
        'FOURTEEN': '1110',
        'FIFTEEN': '1111'
    }

    stimuli = []
    
    # Generate test scenarios for each valid input combination
    for scenario_name, input_val in valid_inputs.items():
        scenario = {
            'scenario': f'TEST_{scenario_name}',
            'input variable': [{
                'a': input_val[0],
                'b': input_val[1],
                'c': input_val[2],
                'd': input_val[3]
            }]
        }
        stimuli.append(scenario)

    # Add edge case scenarios
    # Alternating bits
    stimuli.append({
        'scenario': 'ALTERNATING_BITS',
        'input variable': [
            {'a': '0', 'b': '1', 'c': '0', 'd': '1'},
            {'a': '1', 'b': '0', 'c': '1', 'd': '0'}
        ]
    })

    # Walking ones through valid combinations
    stimuli.append({
        'scenario': 'WALKING_ONES',
        'input variable': [
            {'a': '0', 'b': '0', 'c': '0', 'd': '1'},
            {'a': '0', 'b': '0', 'c': '1', 'd': '0'},
            {'a': '0', 'b': '1', 'c': '0', 'd': '0'},
            {'a': '1', 'b': '0', 'c': '0', 'd': '0'}
        ]
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
