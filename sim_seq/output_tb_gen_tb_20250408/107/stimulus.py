import json

import random

def gen_alternating_pattern(width=512):
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(width)])

def gen_single_cell_pattern(width=512, pos=256):
    pattern = ['0'] * width
    pattern[pos] = '1'
    return ''.join(pattern)

def gen_random_pattern(width=512):
    return ''.join([str(random.randint(0, 1)) for _ in range(width)])

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Initial Load Operation
    scenarios.append({
        'scenario': 'InitialLoadOperation',
        'input variable': [{
            'clock cycles': 2,
            'load': ['1', '0'],
            'data': [gen_alternating_pattern(), gen_alternating_pattern()]
        }]
    })
    
    # Scenario 2: Boundary Cell Evolution
    scenarios.append({
        'scenario': 'BoundaryCellEvolution',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1', '0', '0', '0', '0'],
            'data': ['1' + '0'*510 + '1'] * 5
        }]
    })
    
    # Scenario 3: Alternating Pattern Evolution
    scenarios.append({
        'scenario': 'AlternatingPatternEvolution',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1', '0', '0', '0', '0'],
            'data': [gen_alternating_pattern()] * 5
        }]
    })
    
    # Scenario 4: Single Cell Propagation
    scenarios.append({
        'scenario': 'SingleCellPropagation',
        'input variable': [{
            'clock cycles': 10,
            'load': ['1'] + ['0']*9,
            'data': [gen_single_cell_pattern()] * 10
        }]
    })
    
    # Scenario 5: All Ones Pattern
    scenarios.append({
        'scenario': 'AllOnesPattern',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1', '0', '0', '0', '0'],
            'data': ['1'*512] * 5
        }]
    })
    
    # Scenario 6: All Zeros Pattern
    scenarios.append({
        'scenario': 'AllZerosPattern',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1', '0', '0', '0', '0'],
            'data': ['0'*512] * 5
        }]
    })
    
    # Scenario 7: Random Pattern Evolution
    random_pattern = gen_random_pattern()
    scenarios.append({
        'scenario': 'RandomPatternEvolution',
        'input variable': [{
            'clock cycles': 10,
            'load': ['1'] + ['0']*9,
            'data': [random_pattern] * 10
        }]
    })
    
    # Scenario 8: Load During Evolution
    scenarios.append({
        'scenario': 'LoadDuringEvolution',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1', '0', '0', '1', '0'],
            'data': [gen_random_pattern(), gen_random_pattern(), 
                    gen_random_pattern(), gen_alternating_pattern(), 
                    gen_alternating_pattern()]
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
