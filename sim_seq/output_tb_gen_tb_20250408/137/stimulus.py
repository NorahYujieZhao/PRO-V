import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Initial Reset State
    scenarios.append({
        "scenario": "InitialResetState",
        "input variable": [{
            "clock cycles": 3,
            "reset": ["1", "1", "0"],
            "in": ["0", "0", "0"]
        }]
    })
    
    # Scenario 2: State B to A Transition
    scenarios.append({
        "scenario": "StateBtoATransition",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["1", "0", "0", "0"],
            "in": ["1", "1", "0", "0"]
        }]
    })
    
    # Scenario 3: State B Self Loop
    scenarios.append({
        "scenario": "StateBSelfLoop",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["1", "0", "0", "0"],
            "in": ["1", "1", "1", "1"]
        }]
    })
    
    # Scenario 4: State A to B Transition
    scenarios.append({
        "scenario": "StateAtoBTransition",
        "input variable": [{
            "clock cycles": 5,
            "reset": ["1", "0", "0", "0", "0"],
            "in": ["1", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 5: State A Self Loop
    scenarios.append({
        "scenario": "StateASelfLoop",
        "input variable": [{
            "clock cycles": 5,
            "reset": ["1", "0", "0", "0", "0"],
            "in": ["0", "1", "1", "1", "1"]
        }]
    })
    
    # Scenario 6: Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["1", "0", "0", "1", "0", "0"],
            "in": ["1", "0", "1", "1", "1", "1"]
        }]
    })
    
    # Scenario 7: Multiple State Transitions
    scenarios.append({
        "scenario": "MultipleStateTransitions",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0"],
            "in": ["1", "0", "1", "0", "1", "0", "1", "0"]
        }]
    })
    
    # Scenario 8: Clock Edge Behavior
    scenarios.append({
        "scenario": "ClockEdgeBehavior",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["1", "0", "0", "0", "0", "0"],
            "in": ["1", "0", "1", "0", "1", "0"]
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
