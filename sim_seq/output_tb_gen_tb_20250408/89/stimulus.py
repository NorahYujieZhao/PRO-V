import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Counting Operation
    scenarios.append({
        "scenario": "BasicCountingOperation",
        "input variable": [{
            "clock cycles": 16,
            "reset": ["0"] * 16
        }]
    })
    
    # Scenario 2: Synchronous Reset During Count
    scenarios.append({
        "scenario": "SynchronousResetDuringCount",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["0", "0", "0", "0", "1", "0", "0", "0", "1", "0"]
        }]
    })
    
    # Scenario 3: Counter Rollover
    scenarios.append({
        "scenario": "CounterRollover",
        "input variable": [{
            "clock cycles": 20,
            "reset": ["0"] * 20
        }]
    })
    
    # Scenario 4: Initial Power Up State
    scenarios.append({
        "scenario": "InitialPowerUpState",
        "input variable": [{
            "clock cycles": 2,
            "reset": ["1", "0"]
        }]
    })
    
    # Scenario 5: Multiple Reset Cycles
    scenarios.append({
        "scenario": "MultipleResetCycles",
        "input variable": [{
            "clock cycles": 12,
            "reset": ["1", "0", "0", "1", "0", "0", "1", "0", "0", "1", "0", "0"]
        }]
    })
    
    # Scenario 6: Setup Time Verification
    scenarios.append({
        "scenario": "SetupTimeVerification",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "1", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 7: Continuous Operation
    scenarios.append({
        "scenario": "ContinuousOperation",
        "input variable": [{
            "clock cycles": 48,
            "reset": ["0"] * 48
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
