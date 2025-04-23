import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to format binary strings
    def bin_str(val, width=1):
        return format(val, f'0{width}b')
    
    # Scenario 1: Reset Operation
    scenarios.append({
        "scenario": "ResetOperation",
        "input variable": [{
            "clock cycles": 3,
            "areset": ["1", "1", "0"],
            "x": ["0", "0", "0"]
        }]
    })
    
    # Scenario 2: Stay in State A
    scenarios.append({
        "scenario": "StayInStateA",
        "input variable": [{
            "clock cycles": 4,
            "areset": ["0", "0", "0", "0"],
            "x": ["0", "0", "0", "0"]
        }]
    })
    
    # Scenario 3: Transition A to B
    scenarios.append({
        "scenario": "TransitionAtoB",
        "input variable": [{
            "clock cycles": 3,
            "areset": ["0", "0", "0"],
            "x": ["0", "1", "1"]
        }]
    })
    
    # Scenario 4: Stay in State B with x=0
    scenarios.append({
        "scenario": "StayInStateB_x0",
        "input variable": [{
            "clock cycles": 4,
            "areset": ["0", "0", "0", "0"],
            "x": ["1", "0", "0", "0"]
        }]
    })
    
    # Scenario 5: Stay in State B with x=1
    scenarios.append({
        "scenario": "StayInStateB_x1",
        "input variable": [{
            "clock cycles": 4,
            "areset": ["0", "0", "0", "0"],
            "x": ["1", "1", "1", "1"]
        }]
    })
    
    # Scenario 6: Multiple Input Transitions
    scenarios.append({
        "scenario": "MultipleInputTransitions",
        "input variable": [{
            "clock cycles": 8,
            "areset": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "x": ["0", "1", "0", "1", "0", "1", "0", "1"]
        }]
    })
    
    # Scenario 7: Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [{
            "clock cycles": 5,
            "areset": ["0", "0", "1", "0", "0"],
            "x": ["1", "1", "1", "0", "0"]
        }]
    })
    
    # Scenario 8: Clock Edge Behavior
    scenarios.append({
        "scenario": "ClockEdgeBehavior",
        "input variable": [{
            "clock cycles": 6,
            "areset": ["0", "0", "0", "0", "0", "0"],
            "x": ["0", "1", "1", "0", "1", "0"]
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
