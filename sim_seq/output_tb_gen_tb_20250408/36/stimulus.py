import json

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Increment Until Saturation
    scenarios.append({
        'scenario': 'IncrementUntilSaturation',
        'input variable': [{
            'clock cycles': 5,
            'areset': ['0', '0', '0', '0', '0'],
            'train_valid': ['1', '1', '1', '1', '1'],
            'train_taken': ['1', '1', '1', '1', '1']
        }]
    })
    
    # Scenario 2: Decrement Until Saturation
    scenarios.append({
        'scenario': 'DecrementUntilSaturation',
        'input variable': [{
            'clock cycles': 5,
            'areset': ['0', '0', '0', '0', '0'],
            'train_valid': ['1', '1', '1', '1', '1'],
            'train_taken': ['0', '0', '0', '0', '0']
        }]
    })
    
    # Scenario 3: Hold Value When Not Training
    scenarios.append({
        'scenario': 'HoldValueWhenNotTraining',
        'input variable': [{
            'clock cycles': 4,
            'areset': ['0', '0', '0', '0'],
            'train_valid': ['0', '0', '0', '0'],
            'train_taken': ['1', '0', '1', '0']
        }]
    })
    
    # Scenario 4: Asynchronous Reset Operation
    scenarios.append({
        'scenario': 'AsynchronousResetOperation',
        'input variable': [{
            'clock cycles': 5,
            'areset': ['0', '1', '0', '1', '0'],
            'train_valid': ['1', '1', '1', '1', '1'],
            'train_taken': ['1', '1', '1', '1', '1']
        }]
    })
    
    # Scenario 5: Increment Decrement Sequence
    scenarios.append({
        'scenario': 'IncrementDecrementSequence',
        'input variable': [{
            'clock cycles': 6,
            'areset': ['0', '0', '0', '0', '0', '0'],
            'train_valid': ['1', '1', '1', '1', '1', '1'],
            'train_taken': ['1', '1', '0', '0', '1', '1']
        }]
    })
    
    # Scenario 6: Maximum Value Saturation
    scenarios.append({
        'scenario': 'MaximumValueSaturation',
        'input variable': [{
            'clock cycles': 6,
            'areset': ['0', '0', '0', '0', '0', '0'],
            'train_valid': ['1', '1', '1', '1', '1', '1'],
            'train_taken': ['1', '1', '1', '1', '1', '1']
        }]
    })
    
    # Scenario 7: Minimum Value Saturation
    scenarios.append({
        'scenario': 'MinimumValueSaturation',
        'input variable': [{
            'clock cycles': 6,
            'areset': ['0', '0', '0', '0', '0', '0'],
            'train_valid': ['1', '1', '1', '1', '1', '1'],
            'train_taken': ['0', '0', '0', '0', '0', '0']
        }]
    })
    
    # Scenario 8: Reset During Operation
    scenarios.append({
        'scenario': 'ResetDuringOperation',
        'input variable': [{
            'clock cycles': 6,
            'areset': ['0', '0', '1', '0', '0', '0'],
            'train_valid': ['1', '1', '1', '1', '1', '1'],
            'train_taken': ['1', '1', '1', '0', '0', '1']
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
