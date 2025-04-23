import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Initial Reset Behavior
    scenarios.append({
        "scenario": "InitialResetBehavior",
        "input variable": [{
            "clock cycles": 4,
            "areset": ["1", "1", "0", "0"],
            "j": ["0", "1", "1", "0"],
            "k": ["0", "1", "1", "0"]
        }]
    })
    
    # Scenario 2: OFF to ON Transition
    scenarios.append({
        "scenario": "OFFtoONTransition",
        "input variable": [{
            "clock cycles": 3,
            "areset": ["0", "0", "0"],
            "j": ["0", "1", "1"],
            "k": ["0", "0", "0"]
        }]
    })
    
    # Scenario 3: ON to OFF Transition
    scenarios.append({
        "scenario": "ONtoOFFTransition",
        "input variable": [{
            "clock cycles": 3,
            "areset": ["0", "0", "0"],
            "j": ["1", "0", "0"],
            "k": ["0", "1", "1"]
        }]
    })
    
    # Scenario 4: Maintain OFF State
    scenarios.append({
        "scenario": "MaintainOFFState",
        "input variable": [{
            "clock cycles": 3,
            "areset": ["0", "0", "0"],
            "j": ["0", "0", "0"],
            "k": ["0", "1", "0"]
        }]
    })
    
    # Scenario 5: Maintain ON State
    scenarios.append({
        "scenario": "MaintainONState",
        "input variable": [{
            "clock cycles": 3,
            "areset": ["0", "0", "0"],
            "j": ["1", "0", "0"],
            "k": ["0", "0", "0"]
        }]
    })
    
    # Scenario 6: Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [{
            "clock cycles": 4,
            "areset": ["0", "0", "1", "0"],
            "j": ["1", "1", "1", "0"],
            "k": ["0", "0", "0", "0"]
        }]
    })
    
    # Scenario 7: Input Changes Between Clocks
    scenarios.append({
        "scenario": "InputChangesBetweenClocks",
        "input variable": [{
            "clock cycles": 5,
            "areset": ["0", "0", "0", "0", "0"],
            "j": ["0", "1", "0", "1", "0"],
            "k": ["0", "0", "1", "0", "1"]
        }]
    })
    
    # Scenario 8: Setup Hold Time Verification
    scenarios.append({
        "scenario": "SetupHoldTimeVerification",
        "input variable": [{
            "clock cycles": 4,
            "areset": ["0", "0", "0", "0"],
            "j": ["0", "1", "1", "0"],
            "k": ["0", "0", "1", "1"]
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
