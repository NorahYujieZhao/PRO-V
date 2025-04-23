import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Flag Detection
    scenarios.append({
        "scenario": "BasicFlagDetection",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "in": ["0", "1", "1", "1", "1", "1", "1", "0"]
        }]
    })
    
    # Scenario 2: Zero Bit Discard
    scenarios.append({
        "scenario": "ZeroBitDiscard",
        "input variable": [{
            "clock cycles": 7,
            "reset": ["0", "0", "0", "0", "0", "0", "0"],
            "in": ["0", "1", "1", "1", "1", "1", "0"]
        }]
    })
    
    # Scenario 3: Error Detection
    scenarios.append({
        "scenario": "ErrorDetection",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "in": ["0", "1", "1", "1", "1", "1", "1", "1"]
        }]
    })
    
    # Scenario 4: Reset Behavior
    scenarios.append({
        "scenario": "ResetBehavior",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["1", "0", "0", "0"],
            "in": ["1", "1", "1", "1"]
        }]
    })
    
    # Scenario 5: Multiple Consecutive Flags
    scenarios.append({
        "scenario": "MultipleConsecutiveFlags",
        "input variable": [{
            "clock cycles": 16,
            "reset": ["0"]*16,
            "in": ["0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0"]
        }]
    })
    
    # Scenario 6: Partial Pattern Recovery
    scenarios.append({
        "scenario": "PartialPatternRecovery",
        "input variable": [{
            "clock cycles": 7,
            "reset": ["0"]*7,
            "in": ["0", "1", "1", "1", "1", "1", "0"]
        }]
    })
    
    # Scenario 7: Extended Error State
    scenarios.append({
        "scenario": "ExtendedErrorState",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["0"]*10,
            "in": ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        }]
    })
    
    # Scenario 8: Reset During Pattern
    scenarios.append({
        "scenario": "ResetDuringPattern",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "1", "0", "0", "0", "0"],
            "in": ["0", "1", "1", "1", "1", "1", "1", "0"]
        }]
    })
    
    # Scenario 9: Alternating Bits
    scenarios.append({
        "scenario": "AlternatingBits",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0"]*8,
            "in": ["1", "0", "1", "0", "1", "0", "1", "0"]
        }]
    })
    
    # Scenario 10: Back to Back Special Patterns
    scenarios.append({
        "scenario": "BackToBackSpecialPatterns",
        "input variable": [{
            "clock cycles": 13,
            "reset": ["0"]*13,
            "in": ["0", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1"]
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
