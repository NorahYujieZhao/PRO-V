import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Initial State Verification
    scenarios.append({
        "scenario": "InitialStateVerification",
        "input variable": [{
            "clock cycles": 5,
            "a": ["0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 2: Basic Input Following
    scenarios.append({
        "scenario": "BasicInputFollowing",
        "input variable": [{
            "clock cycles": 8,
            "a": ["0", "1", "0", "1", "0", "1", "0", "1"]
        }]
    })
    
    # Scenario 3: State Transition Detection
    scenarios.append({
        "scenario": "StateTransitionDetection",
        "input variable": [{
            "clock cycles": 10,
            "a": ["0", "1", "0", "1", "0", "1", "0", "1", "0", "1"]
        }]
    })
    
    # Scenario 4: Output Q Assertion
    scenarios.append({
        "scenario": "OutputQAssertion",
        "input variable": [{
            "clock cycles": 6,
            "a": ["0", "1", "0", "1", "0", "1"]
        }]
    })
    
    # Scenario 5: Pattern Reset Condition
    scenarios.append({
        "scenario": "PatternResetCondition",
        "input variable": [{
            "clock cycles": 8,
            "a": ["1", "0", "0", "0", "0", "1", "0", "0"]
        }]
    })
    
    # Scenario 6: Clock Edge Sensitivity
    scenarios.append({
        "scenario": "ClockEdgeSensitivity",
        "input variable": [{
            "clock cycles": 6,
            "a": ["0", "1", "1", "0", "0", "1"]
        }]
    })
    
    # Scenario 7: Rapid Input Changes
    scenarios.append({
        "scenario": "RapidInputChanges",
        "input variable": [{
            "clock cycles": 8,
            "a": ["0", "1", "0", "1", "0", "1", "0", "1"]
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
