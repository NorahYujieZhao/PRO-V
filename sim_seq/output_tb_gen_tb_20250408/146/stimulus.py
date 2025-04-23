import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Reset State Verification
    scenarios.append({
        "scenario": "ResetStateVerification",
        "input variable": [{
            "clock cycles": 3,
            "reset": ["1", "1", "0"],
            "s": ["000", "000", "000"]
        }]
    })
    
    # Scenario 2: Water Level Above Highest Sensor
    scenarios.append({
        "scenario": "WaterLevelAboveHighestSensor",
        "input variable": [{
            "clock cycles": 3,
            "reset": ["0", "0", "0"],
            "s": ["111", "111", "111"]
        }]
    })
    
    # Scenario 3: Water Level Between S3 and S2
    scenarios.append({
        "scenario": "WaterLevelBetweenS3andS2",
        "input variable": [{
            "clock cycles": 3,
            "reset": ["0", "0", "0"],
            "s": ["011", "011", "011"]
        }]
    })
    
    # Scenario 4: Water Level Between S2 and S1
    scenarios.append({
        "scenario": "WaterLevelBetweenS2andS1",
        "input variable": [{
            "clock cycles": 3,
            "reset": ["0", "0", "0"],
            "s": ["001", "001", "001"]
        }]
    })
    
    # Scenario 5: Water Level Below S1
    scenarios.append({
        "scenario": "WaterLevelBelowS1",
        "input variable": [{
            "clock cycles": 3,
            "reset": ["0", "0", "0"],
            "s": ["000", "000", "000"]
        }]
    })
    
    # Scenario 6: Rising Water Level Transition
    scenarios.append({
        "scenario": "RisingWaterLevelTransition",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["0", "0", "0", "0"],
            "s": ["000", "000", "001", "001"]
        }]
    })
    
    # Scenario 7: Falling Water Level Transition
    scenarios.append({
        "scenario": "FallingWaterLevelTransition",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["0", "0", "0", "0"],
            "s": ["111", "111", "011", "011"]
        }]
    })
    
    # Scenario 8: Multiple Level Changes
    scenarios.append({
        "scenario": "MultipleLevelChanges",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "s": ["000", "001", "011", "111", "011", "001", "000", "000"]
        }]
    })
    
    # Scenario 9: Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["0", "0", "1", "1", "0", "0"],
            "s": ["011", "011", "011", "011", "011", "011"]
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
