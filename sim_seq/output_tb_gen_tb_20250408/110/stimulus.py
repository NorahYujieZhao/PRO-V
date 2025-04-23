import json
def stimulus_gen():
    # List to store all test scenarios
    scenarios = []
    
    # Scenario 1: Basic Enable Operation
    scenarios.append({
        "scenario": "BasicEnableOperation",
        "input variable": [
            {
                "clock cycles": 6,
                "d": ["0", "1", "0", "1", "0", "1"],
                "ena": ["1", "1", "1", "1", "1", "1"]
            }
        ]
    })
    
    # Scenario 2: Basic Disable Operation
    scenarios.append({
        "scenario": "BasicDisableOperation",
        "input variable": [
            {
                "clock cycles": 6,
                "d": ["1", "0", "1", "0", "1", "0"],
                "ena": ["0", "0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 3: Enable to Disable Transition
    scenarios.append({
        "scenario": "EnableToDisableTransition",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["1", "1", "0", "0"],
                "ena": ["1", "1", "0", "0"]
            }
        ]
    })
    
    # Scenario 4: Disable to Enable Transition
    scenarios.append({
        "scenario": "DisableToEnableTransition",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["0", "0", "1", "1"],
                "ena": ["0", "0", "1", "1"]
            }
        ]
    })
    
    # Scenario 5: Multiple Data Transitions While Enabled
    scenarios.append({
        "scenario": "MultipleDataTransitionsWhileEnabled",
        "input variable": [
            {
                "clock cycles": 8,
                "d": ["0", "1", "0", "1", "0", "1", "0", "1"],
                "ena": ["1", "1", "1", "1", "1", "1", "1", "1"]
            }
        ]
    })
    
    # Scenario 6: Multiple Data Transitions While Disabled
    scenarios.append({
        "scenario": "MultipleDataTransitionsWhileDisabled",
        "input variable": [
            {
                "clock cycles": 8,
                "d": ["0", "1", "0", "1", "0", "1", "0", "1"],
                "ena": ["0", "0", "0", "0", "0", "0", "0", "0"]
            }
        ]
    })
    
    # Scenario 7: Enable Signal Setup Time
    scenarios.append({
        "scenario": "EnableSignalSetupTime",
        "input variable": [
            {
                "clock cycles": 6,
                "d": ["0", "1", "1", "0", "0", "1"],
                "ena": ["0", "0", "1", "1", "0", "0"]
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
