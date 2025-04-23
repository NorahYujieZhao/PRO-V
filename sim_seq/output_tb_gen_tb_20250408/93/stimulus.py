import json

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Normal Counting Sequence
    scenarios.append({
        'scenario': 'NormalCountingSequence',
        'input variable': [{
            'clock cycles': 12,
            'reset': ['0'] * 12  # Let counter run normally for 12 cycles
        }]
    })
    
    # Scenario 2: Counter Rollover
    scenarios.append({
        'scenario': 'CounterRollover',
        'input variable': [{
            'clock cycles': 11,
            'reset': ['0'] * 11  # Run through 0-9 and check rollover to 0
        }]
    })
    
    # Scenario 3: Synchronous Reset Operation
    scenarios.append({
        'scenario': 'SynchronousResetOperation',
        'input variable': [{
            'clock cycles': 5,
            'reset': ['0', '0', '0', '1', '0']  # Reset in middle of counting
        }]
    })
    
    # Scenario 4: Reset at Maximum Value
    scenarios.append({
        'scenario': 'ResetAtMaximumValue',
        'input variable': [{
            'clock cycles': 10,
            'reset': ['0'] * 9 + ['1']  # Reset when counter reaches 9
        }]
    })
    
    # Scenario 5: Multiple Reset Cycles
    scenarios.append({
        'scenario': 'MultipleResetCycles',
        'input variable': [{
            'clock cycles': 8,
            'reset': ['0', '1', '0', '0', '1', '0', '1', '0']  # Multiple reset pulses
        }]
    })
    
    # Scenario 6: Initial Power Up State
    scenarios.append({
        'scenario': 'InitialPowerUpState',
        'input variable': [{
            'clock cycles': 2,
            'reset': ['1', '0']  # Reset at start, then release
        }]
    })
    
    # Scenario 7: Clock Edge Behavior
    scenarios.append({
        'scenario': 'ClockEdgeBehavior',
        'input variable': [{
            'clock cycles': 4,
            'reset': ['0'] * 4  # Normal counting to verify clock edge behavior
        }]
    })
    
    # Scenario 8: Extended Operation
    scenarios.append({
        'scenario': 'ExtendedOperation',
        'input variable': [{
            'clock cycles': 30,
            'reset': ['0'] * 30  # Run for multiple complete cycles
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
