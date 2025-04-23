import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Normal Data Loading
    scenarios.append({
        "scenario": "NormalDataLoading",
        "input variable": [{
            "clock cycles": 4,
            "d": ["10101010", "11110000", "00001111", "11111111"],
            "reset": ["0", "0", "0", "0"]
        }]
    })
    
    # Scenario 2: Synchronous Reset Operation
    scenarios.append({
        "scenario": "SynchronousResetOperation",
        "input variable": [{
            "clock cycles": 4,
            "d": ["11111111", "11111111", "11111111", "11111111"],
            "reset": ["0", "1", "1", "1"]
        }]
    })
    
    # Scenario 3: Reset Deassert Operation
    scenarios.append({
        "scenario": "ResetDeassertOperation",
        "input variable": [{
            "clock cycles": 5,
            "d": ["00000000", "11111111", "10101010", "11001100", "00110011"],
            "reset": ["1", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 4: Clock Edge Alignment
    scenarios.append({
        "scenario": "ClockEdgeAlignment",
        "input variable": [{
            "clock cycles": 3,
            "d": ["10101010", "01010101", "11110000"],
            "reset": ["0", "0", "0"]
        }]
    })
    
    # Scenario 5: Data Setup Time
    scenarios.append({
        "scenario": "DataSetupTime",
        "input variable": [{
            "clock cycles": 4,
            "d": ["00000000", "11111111", "10101010", "01010101"],
            "reset": ["0", "0", "0", "0"]
        }]
    })
    
    # Scenario 6: Data Hold Time
    scenarios.append({
        "scenario": "DataHoldTime",
        "input variable": [{
            "clock cycles": 4,
            "d": ["11110000", "00001111", "11001100", "00110011"],
            "reset": ["0", "0", "0", "0"]
        }]
    })
    
    # Scenario 7: Alternating Data Pattern
    scenarios.append({
        "scenario": "AlternatingDataPattern",
        "input variable": [{
            "clock cycles": 6,
            "d": ["00000000", "11111111", "00000000", "11111111", "00000000", "11111111"],
            "reset": ["0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 8: Reset During Data Change
    scenarios.append({
        "scenario": "ResetDuringDataChange",
        "input variable": [{
            "clock cycles": 5,
            "d": ["10101010", "11001100", "00110011", "11110000", "00001111"],
            "reset": ["0", "0", "1", "1", "0"]
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
