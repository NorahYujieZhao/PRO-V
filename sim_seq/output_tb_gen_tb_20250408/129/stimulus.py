import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Normal Data Capture
    scenarios.append({
        "scenario": "NormalDataCapture",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["10101010", "11110000", "00001111", "11111111"],
                "areset": ["0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 2: Asynchronous Reset Assertion
    scenarios.append({
        "scenario": "AsynchronousResetAssertion",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["11111111", "11111111", "11111111", "11111111"],
                "areset": ["0", "1", "1", "1"]
            }
        ]
    })
    
    # Scenario 3: Reset Release Operation
    scenarios.append({
        "scenario": "ResetReleaseOperation",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["10101010", "11001100", "11110000", "00001111"],
                "areset": ["1", "1", "0", "0"]
            }
        ]
    })
    
    # Scenario 4: Setup Time Verification
    scenarios.append({
        "scenario": "SetupTimeVerification",
        "input variable": [
            {
                "clock cycles": 3,
                "d": ["00000000", "11111111", "10101010"],
                "areset": ["0", "0", "0"]
            }
        ]
    })
    
    # Scenario 5: Hold Time Verification
    scenarios.append({
        "scenario": "HoldTimeVerification",
        "input variable": [
            {
                "clock cycles": 3,
                "d": ["11111111", "00000000", "10101010"],
                "areset": ["0", "0", "0"]
            }
        ]
    })
    
    # Scenario 6: Alternating Bit Patterns
    scenarios.append({
        "scenario": "AlternatingBitPatterns",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["10101010", "01010101", "10101010", "01010101"],
                "areset": ["0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 7: Walking Ones Pattern
    scenarios.append({
        "scenario": "WalkingOnesPattern",
        "input variable": [
            {
                "clock cycles": 8,
                "d": ["00000001", "00000010", "00000100", "00001000",
                     "00010000", "00100000", "01000000", "10000000"],
                "areset": ["0", "0", "0", "0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 8: Reset During Data Change
    scenarios.append({
        "scenario": "ResetDuringDataChange",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["11111111", "10101010", "01010101", "11110000"],
                "areset": ["0", "0", "1", "1"]
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
