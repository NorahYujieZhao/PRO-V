import json
def stimulus_gen():
    import random

    scenarios = []
    
    # Basic cases - one clear minimum
    scenarios.append({
        'scenario': 'BasicCase1',
        'input variable': [{'a': '00000001', 'b': '11111111', 'c': '11111111', 'd': '11111111'}]
    })
    
    # Edge case - all equal
    scenarios.append({
        'scenario': 'AllEqual',
        'input variable': [{'a': '10101010', 'b': '10101010', 'c': '10101010', 'd': '10101010'}]
    })
    
    # Boundary conditions - zeros and max values
    scenarios.append({
        'scenario': 'BoundaryZeros',
        'input variable': [{'a': '00000000', 'b': '00000000', 'c': '00000000', 'd': '00000000'}]
    })
    
    scenarios.append({
        'scenario': 'BoundaryMax',
        'input variable': [{'a': '11111111', 'b': '11111111', 'c': '11111111', 'd': '11111111'}]
    })
    
    # Multiple equal but not minimum
    scenarios.append({
        'scenario': 'MultipleEqual',
        'input variable': [{'a': '00000010', 'b': '00000001', 'c': '00000010', 'd': '00000010'}]
    })
    
    # Sequential values
    scenarios.append({
        'scenario': 'Sequential',
        'input variable': [{'a': '00000100', 'b': '00000011', 'c': '00000010', 'd': '00000001'}]
    })
    
    # Random cases (10 cases)
    for i in range(10):
        a = format(random.randint(0, 255), '08b')
        b = format(random.randint(0, 255), '08b')
        c = format(random.randint(0, 255), '08b')
        d = format(random.randint(0, 255), '08b')
        scenarios.append({
            'scenario': f'Random{i+1}',
            'input variable': [{'a': a, 'b': b, 'c': c, 'd': d}]
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
