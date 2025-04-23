import json
def stimulus_gen():
    test_scenarios = []
    
    # Scenario 1: Initial Value Check
    test_scenarios.append({
        "scenario": "InitialValueCheck",
        "input variable": [{
            "clock cycles": 4,
            "a": ["1", "1", "1", "1"]
        }]
    })
    
    # Scenario 2: Fixed Value Operation
    test_scenarios.append({
        "scenario": "FixedValueOperation",
        "input variable": [{
            "clock cycles": 8,
            "a": ["1", "1", "1", "1", "1", "1", "1", "1"]
        }]
    })
    
    # Scenario 3: Start Counting Sequence
    test_scenarios.append({
        "scenario": "StartCountingSequence",
        "input variable": [{
            "clock cycles": 6,
            "a": ["1", "1", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 4: Counter Rollover
    test_scenarios.append({
        "scenario": "CounterRollover",
        "input variable": [{
            "clock cycles": 8,
            "a": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 5: Stop Counting Operation
    test_scenarios.append({
        "scenario": "StopCountingOperation",
        "input variable": [{
            "clock cycles": 6,
            "a": ["0", "0", "0", "1", "1", "1"]
        }]
    })
    
    # Scenario 6: Multiple Counting Cycles
    test_scenarios.append({
        "scenario": "MultipleCountingCycles",
        "input variable": [{
            "clock cycles": 12,
            "a": ["1", "1", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0"]
        }]
    })
    
    return test_scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # 将结果转换为 JSON 字符串
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
