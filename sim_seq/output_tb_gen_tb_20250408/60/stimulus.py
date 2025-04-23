import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Counting Operation
    scenarios.append({
        "scenario": "BasicCountingOperation",
        "input variable": [{
            "clock cycles": 20,
            "reset": ["0"] * 20
        }]
    })
    
    # Scenario 2: Synchronous Reset
    scenarios.append({
        "scenario": "SynchronousReset",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 3: Counter Maximum Value
    scenarios.append({
        "scenario": "CounterMaximumValue",
        "input variable": [{
            "clock cycles": 1000,
            "reset": ["0"] * 1000
        }]
    })
    
    # Scenario 4: Counter Rollover
    scenarios.append({
        "scenario": "CounterRollover",
        "input variable": [{
            "clock cycles": 1005,
            "reset": ["0"] * 1005
        }]
    })
    
    # Scenario 5: Reset During Counting
    reset_seq = ["0"] * 50
    reset_seq[20] = "1"  # Reset at count 20
    reset_seq[40] = "1"  # Reset at count 40
    scenarios.append({
        "scenario": "ResetDuringCounting",
        "input variable": [{
            "clock cycles": 50,
            "reset": reset_seq
        }]
    })
    
    # Scenario 6: Full Cycle Verification
    scenarios.append({
        "scenario": "FullCycleVerification",
        "input variable": [{
            "clock cycles": 3000,  # 3 complete cycles
            "reset": ["0"] * 3000
        }]
    })
    
    # Scenario 7: Clock Edge Behavior
    scenarios.append({
        "scenario": "ClockEdgeBehavior",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["0"] * 10
        }]
    })
    
    # Scenario 8: Reset Setup and Hold
    reset_timing = ["0", "0", "1", "0", "0", "1", "0", "0", "1", "0"]
    scenarios.append({
        "scenario": "ResetSetupAndHold",
        "input variable": [{
            "clock cycles": 10,
            "reset": reset_timing
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
