import json
def generate_n_bit_string(n, value):
    return format(value, f'0{n}b')

def stimulus_gen():
    scenarios = []
    
    # Basic selection tests
    scenarios.append({
        'scenario': 'SelectInputA',
        'input variable': [{
            'a': '1' * 100,
            'b': '0' * 100,
            'sel': '0'
        }]
    })
    
    scenarios.append({
        'scenario': 'SelectInputB',
        'input variable': [{
            'a': '0' * 100,
            'b': '1' * 100,
            'sel': '1'
        }]
    })
    
    # Edge cases - all zeros/ones
    scenarios.append({
        'scenario': 'AllZeros',
        'input variable': [{
            'a': '0' * 100,
            'b': '0' * 100,
            'sel': '0'
        }]
    })
    
    scenarios.append({
        'scenario': 'AllOnes',
        'input variable': [{
            'a': '1' * 100,
            'b': '1' * 100,
            'sel': '1'
        }]
    })
    
    # Alternating patterns
    alt_pattern_a = '10' * 50
    alt_pattern_b = '01' * 50
    scenarios.append({
        'scenario': 'AlternatingPatterns',
        'input variable': [{
            'a': alt_pattern_a,
            'b': alt_pattern_b,
            'sel': '0'
        }]
    })
    
    # Boundary testing - MSB/LSB
    scenarios.append({
        'scenario': 'BoundaryBits',
        'input variable': [{
            'a': '1' + '0' * 98 + '1',
            'b': '0' + '1' * 98 + '0',
            'sel': '1'
        }]
    })
    
    # Random test cases
    import random
    for i in range(10):
        a_val = random.getrandbits(100)
        b_val = random.getrandbits(100)
        scenarios.append({
            'scenario': f'RandomTest_{i}',
            'input variable': [{
                'a': format(a_val, '0100b'),
                'b': format(b_val, '0100b'),
                'sel': str(random.randint(0, 1))
            }]
        })
    
    return scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # 将结果转换为 JSON 字符串
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
