import json
def stimulus_gen():
    # Helper function to generate binary string for a number
    def get_bin(x, width=1):
        return format(x, f'0{width}b')

    scenarios = []
    
    # 1. Test all 16 possible input combinations
    for i in range(16):
        bits = get_bin(i, 4)
        scenarios.append({
            'scenario': f'InputCombination_{bits}',
            'input variable': [{
                'a': bits[0],
                'b': bits[1],
                'c': bits[2],
                'd': bits[3]
            }]
        })

    # 2. Alternating patterns
    scenarios.append({
        'scenario': 'AlternatingPattern',
        'input variable': [
            {'a': '0', 'b': '1', 'c': '0', 'd': '1'},
            {'a': '1', 'b': '0', 'c': '1', 'd': '0'}
        ]
    })

    # 3. Walking ones
    walking_ones = []
    for i in range(4):
        inputs = {'a': '0', 'b': '0', 'c': '0', 'd': '0'}
        if i == 0: inputs['a'] = '1'
        elif i == 1: inputs['b'] = '1'
        elif i == 2: inputs['c'] = '1'
        else: inputs['d'] = '1'
        walking_ones.append(inputs)
    scenarios.append({
        'scenario': 'WalkingOnes',
        'input variable': walking_ones
    })

    # 4. Walking zeros
    walking_zeros = []
    for i in range(4):
        inputs = {'a': '1', 'b': '1', 'c': '1', 'd': '1'}
        if i == 0: inputs['a'] = '0'
        elif i == 1: inputs['b'] = '0'
        elif i == 2: inputs['c'] = '0'
        else: inputs['d'] = '0'
        walking_zeros.append(inputs)
    scenarios.append({
        'scenario': 'WalkingZeros',
        'input variable': walking_zeros
    })

    # 5. Random test cases (10 cases)
    import random
    random_cases = []
    for i in range(10):
        rand_num = random.randint(0, 15)
        bits = get_bin(rand_num, 4)
        random_cases.append({
            'a': bits[0],
            'b': bits[1],
            'c': bits[2],
            'd': bits[3]
        })
    scenarios.append({
        'scenario': 'RandomCases',
        'input variable': random_cases
    })

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
