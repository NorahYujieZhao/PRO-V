import json
def generate_random_1024bit():
    import random
    return format(random.getrandbits(1024), '01024b')

def stimulus_gen():
    scenarios = []
    
    # Test selecting first segment (sel = 0)
    scenarios.append({
        'scenario': 'SelectFirstSegment',
        'input variable': [{
            'in': '1111' + '0' * 1020,  # First 4 bits are 1, rest 0
            'sel': '00000000'
        }]
    })
    
    # Test selecting last segment (sel = 255)
    scenarios.append({
        'scenario': 'SelectLastSegment',
        'input variable': [{
            'in': '0' * 1020 + '1111',  # Last 4 bits are 1, rest 0
            'sel': '11111111'
        }]
    })
    
    # Test selecting middle segment (sel = 128)
    scenarios.append({
        'scenario': 'SelectMiddleSegment',
        'input variable': [{
            'in': '0' * 512 + '1111' + '0' * 508,
            'sel': '10000000'
        }]
    })
    
    # Test adjacent segments
    scenarios.append({
        'scenario': 'AdjacentSegments',
        'input variable': [{
            'in': '0' * 4 + '1111' + '0' * 1016,
            'sel': '00000001'
        }]
    })
    
    # Generate 10 random test cases
    import random
    for i in range(10):
        random_in = generate_random_1024bit()
        random_sel = format(random.randint(0, 255), '08b')
        scenarios.append({
            'scenario': f'RandomTest_{i}',
            'input variable': [{
                'in': random_in,
                'sel': random_sel
            }]
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
