import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Counting Operation
    scenarios.append({
        'scenario': 'BasicCountingOperation',
        'input variable': [{
            'clock cycles': 10,
            'slowena': ['1']*10,
            'reset': ['0']*10
        }]
    })
    
    # Scenario 2: Counter Rollover
    scenarios.append({
        'scenario': 'CounterRollover',
        'input variable': [{
            'clock cycles': 11,
            'slowena': ['1']*11,
            'reset': ['0']*11
        }]
    })
    
    # Scenario 3: Synchronous Reset
    scenarios.append({
        'scenario': 'SynchronousReset',
        'input variable': [{
            'clock cycles': 5,
            'slowena': ['1']*5,
            'reset': ['0', '0', '1', '0', '0']
        }]
    })
    
    # Scenario 4: Disable Counter
    scenarios.append({
        'scenario': 'DisableCounter',
        'input variable': [{
            'clock cycles': 8,
            'slowena': ['1', '1', '1', '0', '0', '0', '0', '0'],
            'reset': ['0']*8
        }]
    })
    
    # Scenario 5: Enable After Pause
    scenarios.append({
        'scenario': 'EnableAfterPause',
        'input variable': [{
            'clock cycles': 8,
            'slowena': ['1', '1', '0', '0', '1', '1', '1', '1'],
            'reset': ['0']*8
        }]
    })
    
    # Scenario 6: Reset While Disabled
    scenarios.append({
        'scenario': 'ResetWhileDisabled',
        'input variable': [{
            'clock cycles': 6,
            'slowena': ['1', '1', '0', '0', '0', '0'],
            'reset': ['0', '0', '0', '1', '0', '0']
        }]
    })
    
    # Scenario 7: Simultaneous Reset and Enable
    scenarios.append({
        'scenario': 'SimultaneousResetAndEnable',
        'input variable': [{
            'clock cycles': 5,
            'slowena': ['1']*5,
            'reset': ['0', '0', '1', '1', '0']
        }]
    })
    
    # Scenario 8: Multiple Counter Cycles
    scenarios.append({
        'scenario': 'MultipleCounterCycles',
        'input variable': [{
            'clock cycles': 25,
            'slowena': ['1']*25,
            'reset': ['0']*25
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
