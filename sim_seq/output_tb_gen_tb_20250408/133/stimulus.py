import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic State Transition OFF to ON
    scenarios.append({
        "scenario": "BasicStateTransitionOFFtoON",
        "input variable": [
            {
                "clock cycles": 4,
                "j": ["0", "1", "1", "0"],
                "k": ["0", "0", "0", "0"],
                "reset": ["0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 2: Basic State Transition ON to OFF
    scenarios.append({
        "scenario": "BasicStateTransitionONtoOFF",
        "input variable": [
            {
                "clock cycles": 5,
                "j": ["0", "1", "0", "0", "0"],
                "k": ["0", "0", "1", "1", "0"],
                "reset": ["0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 3: State Retention OFF
    scenarios.append({
        "scenario": "StateRetentionOFF",
        "input variable": [
            {
                "clock cycles": 4,
                "j": ["0", "0", "0", "0"],
                "k": ["0", "0", "0", "0"],
                "reset": ["0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 4: State Retention ON
    scenarios.append({
        "scenario": "StateRetentionON",
        "input variable": [
            {
                "clock cycles": 5,
                "j": ["0", "1", "0", "0", "0"],
                "k": ["0", "0", "0", "0", "0"],
                "reset": ["0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 5: Synchronous Reset
    scenarios.append({
        "scenario": "SynchronousReset",
        "input variable": [
            {
                "clock cycles": 6,
                "j": ["0", "1", "0", "0", "0", "0"],
                "k": ["0", "0", "0", "0", "0", "0"],
                "reset": ["0", "0", "0", "1", "0", "0"]
            }
        ]
    })
    
    # Scenario 6: Input Change at Clock Edge
    scenarios.append({
        "scenario": "InputChangeAtClockEdge",
        "input variable": [
            {
                "clock cycles": 6,
                "j": ["0", "1", "0", "1", "0", "1"],
                "k": ["0", "0", "1", "0", "1", "0"],
                "reset": ["0", "0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 7: Multiple State Transitions
    scenarios.append({
        "scenario": "MultipleStateTransitions",
        "input variable": [
            {
                "clock cycles": 8,
                "j": ["0", "1", "0", "0", "1", "0", "0", "1"],
                "k": ["0", "0", "1", "0", "0", "1", "0", "0"],
                "reset": ["0", "0", "0", "0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 8: Reset During Transition
    scenarios.append({
        "scenario": "ResetDuringTransition",
        "input variable": [
            {
                "clock cycles": 5,
                "j": ["0", "1", "0", "0", "0"],
                "k": ["0", "0", "0", "0", "0"],
                "reset": ["0", "0", "1", "0", "0"]
            }
        ]
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
