import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Data Capture
    scenarios.append({
        "scenario": "BasicDataCapture",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["10101010", "11001100", "11110000", "00001111"],
                "reset": ["0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 2: Synchronous Reset Operation
    scenarios.append({
        "scenario": "SynchronousResetOperation",
        "input variable": [
            {
                "clock cycles": 3,
                "d": ["11111111", "11111111", "11111111"],
                "reset": ["0", "1", "1"]
            }
        ]
    })
    
    # Scenario 3: Data Change During Reset
    scenarios.append({
        "scenario": "DataChangeDuringReset",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["10101010", "11001100", "00110011", "11110000"],
                "reset": ["1", "1", "1", "1"]
            }
        ]
    })
    
    # Scenario 4: Reset Deactivation
    scenarios.append({
        "scenario": "ResetDeactivation",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["10101010", "11001100", "11001100", "11001100"],
                "reset": ["1", "1", "0", "0"]
            }
        ]
    })
    
    # Scenario 5: Setup Time Verification
    scenarios.append({
        "scenario": "SetupTimeVerification",
        "input variable": [
            {
                "clock cycles": 3,
                "d": ["10101010", "11110000", "00001111"],
                "reset": ["0", "0", "0"]
            }
        ]
    })
    
    # Scenario 6: Hold Time Verification
    scenarios.append({
        "scenario": "HoldTimeVerification",
        "input variable": [
            {
                "clock cycles": 3,
                "d": ["11001100", "11001100", "00110011"],
                "reset": ["0", "0", "0"]
            }
        ]
    })
    
    # Scenario 7: Input Boundary Values
    scenarios.append({
        "scenario": "InputBoundaryValues",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["00000000", "11111111", "00000000", "11111111"],
                "reset": ["0", "0", "0", "0"]
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
