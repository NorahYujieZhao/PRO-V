import json
def stimulus_gen():
    scenarios = [
        {
            'scenario': 'AllZeros',
            'input variable': [{'in': '0000'}]
        },
        {
            'scenario': 'AllOnes',
            'input variable': [{'in': '1111'}]
        },
        {
            'scenario': 'SingleBitHigh',
            'input variable': [
                {'in': '0001'},
                {'in': '0010'},
                {'in': '0100'},
                {'in': '1000'}
            ]
        },
        {
            'scenario': 'AlternatingBits',
            'input variable': [
                {'in': '0101'},
                {'in': '1010'}
            ]
        },
        {
            'scenario': 'WalkingOnes',
            'input variable': [
                {'in': '0001'},
                {'in': '0011'},
                {'in': '0111'},
                {'in': '1111'}
            ]
        },
        {
            'scenario': 'WalkingZeros',
            'input variable': [
                {'in': '1110'},
                {'in': '1100'},
                {'in': '1000'},
                {'in': '0000'}
            ]
        }
    ]
    
    # Add random test cases
    import random
    random_scenario = {
        'scenario': 'RandomCombinations',
        'input variable': []
    }
    for _ in range(10):
        random_val = format(random.randint(0, 15), '04b')
        random_scenario['input variable'].append({'in': random_val})
    scenarios.append(random_scenario)
    
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
