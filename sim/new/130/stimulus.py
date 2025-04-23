import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to generate n-bit binary string
    def gen_bin(n, val='0'):
        return val * n
    
    # All zeros
    scenarios.append({
        'scenario': 'AllZeros',
        'input variable': [{'in': gen_bin(100, '0')}]
    })
    
    # All ones
    scenarios.append({
        'scenario': 'AllOnes',
        'input variable': [{'in': gen_bin(100, '1')}]
    })
    
    # Single one at different positions
    scenarios.append({
        'scenario': 'SingleOneAtStart',
        'input variable': [{'in': '1' + gen_bin(99, '0')}]
    })
    
    scenarios.append({
        'scenario': 'SingleOneAtMiddle',
        'input variable': [{'in': gen_bin(50, '0') + '1' + gen_bin(49, '0')}]
    })
    
    scenarios.append({
        'scenario': 'SingleOneAtEnd',
        'input variable': [{'in': gen_bin(99, '0') + '1'}]
    })
    
    # Single zero in ones
    scenarios.append({
        'scenario': 'SingleZeroInOnes',
        'input variable': [{'in': gen_bin(50, '1') + '0' + gen_bin(49, '1')}]
    })
    
    # Alternating pattern
    scenarios.append({
        'scenario': 'AlternatingBits',
        'input variable': [{'in': '10' * 50}]
    })
    
    # Random patterns
    import random
    for i in range(10):
        random_bits = ''.join([str(random.randint(0, 1)) for _ in range(100)])
        scenarios.append({
            'scenario': f'RandomPattern_{i}',
            'input variable': [{'in': random_bits}]
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
