import json

def stimulus_gen():
    scenarios = []
    
    # Helper function to create binary strings
    def to_bin(value, width=10):
        return format(value, f'0{width}b')
        
    # Scenario 1: Basic Load and Countdown
    scenarios.append({
        'scenario': 'BasicLoadAndCountdown',
        'input variable': [{
            'clock cycles': 7,
            'load': ['1'] + ['0']*6,
            'data': [to_bin(5)] + [to_bin(0)]*6
        }]
    })
    
    # Scenario 2: Load During Countdown
    scenarios.append({
        'scenario': 'LoadDuringCountdown',
        'input variable': [{
            'clock cycles': 8,
            'load': ['1', '0', '0', '1', '0', '0', '0', '0'],
            'data': [to_bin(5), to_bin(0), to_bin(0), to_bin(3), to_bin(0), to_bin(0), to_bin(0), to_bin(0)]
        }]
    })
    
    # Scenario 3: Load Maximum Value
    scenarios.append({
        'scenario': 'LoadMaximumValue',
        'input variable': [{
            'clock cycles': 1025,
            'load': ['1'] + ['0']*1024,
            'data': [to_bin(1023)] + [to_bin(0)]*1024
        }]
    })
    
    # Scenario 4: Load Minimum Value
    scenarios.append({
        'scenario': 'LoadMinimumValue',
        'input variable': [{
            'clock cycles': 3,
            'load': ['1', '0', '0'],
            'data': [to_bin(1), to_bin(0), to_bin(0)]
        }]
    })
    
    # Scenario 5: Load Zero Value
    scenarios.append({
        'scenario': 'LoadZeroValue',
        'input variable': [{
            'clock cycles': 3,
            'load': ['1', '0', '0'],
            'data': [to_bin(0), to_bin(0), to_bin(0)]
        }]
    })
    
    # Scenario 6: Continuous Loading
    scenarios.append({
        'scenario': 'ContinuousLoading',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1']*5,
            'data': [to_bin(5), to_bin(4), to_bin(3), to_bin(2), to_bin(1)]
        }]
    })
    
    # Scenario 7: Stay at Zero
    scenarios.append({
        'scenario': 'StayAtZero',
        'input variable': [{
            'clock cycles': 8,
            'load': ['1'] + ['0']*7,
            'data': [to_bin(1)] + [to_bin(0)]*7
        }]
    })
    
    # Scenario 8: Load after Terminal Count
    scenarios.append({
        'scenario': 'LoadAfterTerminalCount',
        'input variable': [{
            'clock cycles': 8,
            'load': ['1', '0', '0', '0', '1', '0', '0', '0'],
            'data': [to_bin(2), to_bin(0), to_bin(0), to_bin(0), to_bin(3), to_bin(0), to_bin(0), to_bin(0)]
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
