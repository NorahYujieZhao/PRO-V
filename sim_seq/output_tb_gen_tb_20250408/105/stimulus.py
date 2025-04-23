import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Single Bit Transition
    scenarios.append({
        "scenario": "SingleBitTransition",
        "input variable": [
            {
                "clock cycles": 3,
                "in": ["00000000", "00000001", "00000001"]
            }
        ]
    })
    
    # Scenario 2: Multiple Simultaneous Transitions
    scenarios.append({
        "scenario": "MultipleSimultaneousTransitions",
        "input variable": [
            {
                "clock cycles": 3,
                "in": ["00000000", "10100101", "10100101"]
            }
        ]
    })
    
    # Scenario 3: Sequential Transitions
    scenarios.append({
        "scenario": "SequentialTransitions",
        "input variable": [
            {
                "clock cycles": 5,
                "in": ["00000000", "00000001", "00000011", "00000111", "00001111"]
            }
        ]
    })
    
    # Scenario 4: No Change Detection
    scenarios.append({
        "scenario": "NoChangeDetection",
        "input variable": [
            {
                "clock cycles": 4,
                "in": ["11111111", "11111111", "00000000", "00000000"]
            }
        ]
    })
    
    # Scenario 5: One Cycle Pulse Detection
    scenarios.append({
        "scenario": "OneCyclePulseDetection",
        "input variable": [
            {
                "clock cycles": 4,
                "in": ["00000000", "11111111", "00000000", "00000000"]
            }
        ]
    })
    
    # Scenario 6: All Bits Transition
    scenarios.append({
        "scenario": "AllBitsTransition",
        "input variable": [
            {
                "clock cycles": 3,
                "in": ["00000000", "11111111", "11111111"]
            }
        ]
    })
    
    # Scenario 7: Alternating Pattern
    scenarios.append({
        "scenario": "AlternatingPattern",
        "input variable": [
            {
                "clock cycles": 5,
                "in": ["00000000", "10101010", "01010101", "10101010", "01010101"]
            }
        ]
    })
    
    # Scenario 8: Back to Back Transitions
    scenarios.append({
        "scenario": "BackToBackTransitions",
        "input variable": [
            {
                "clock cycles": 5,
                "in": ["00000001", "00000000", "00000001", "00000000", "00000001"]
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
