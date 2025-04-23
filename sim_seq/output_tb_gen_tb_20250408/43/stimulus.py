import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Shift Operation
    # Shift in pattern 10101010 and verify
    scenarios.append({
        "scenario": "BasicShiftOperation",
        "input variable": [{
            "clock cycles": 8,
            "enable": ["1", "1", "1", "1", "1", "1", "1", "1"],
            "S": ["1", "0", "1", "0", "1", "0", "1", "0"],
            "A": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "B": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "C": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })

    # Scenario 2: Disabled Shift Operation
    scenarios.append({
        "scenario": "DisabledShiftOperation",
        "input variable": [{
            "clock cycles": 8,
            "enable": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "S": ["1", "1", "1", "1", "0", "0", "0", "0"],
            "A": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "B": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "C": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })

    # Scenario 3: Memory Read Access
    scenarios.append({
        "scenario": "MemoryReadAccess",
        "input variable": [{
            "clock cycles": 8,
            "enable": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "S": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "A": ["0", "0", "0", "0", "1", "1", "1", "1"],
            "B": ["0", "0", "1", "1", "0", "0", "1", "1"],
            "C": ["0", "1", "0", "1", "0", "1", "0", "1"]
        }]
    })

    # Scenario 4: Sequential Read Write
    scenarios.append({
        "scenario": "SequentialReadWrite",
        "input variable": [{
            "clock cycles": 8,
            "enable": ["1", "0", "1", "0", "1", "0", "1", "0"],
            "S": ["1", "0", "1", "0", "1", "0", "1", "0"],
            "A": ["0", "1", "0", "1", "0", "1", "0", "1"],
            "B": ["0", "0", "1", "1", "0", "0", "1", "1"],
            "C": ["0", "1", "0", "1", "0", "1", "0", "1"]
        }]
    })

    # Scenario 5: Clock Edge Sensitivity
    scenarios.append({
        "scenario": "ClockEdgeSensitivity",
        "input variable": [{
            "clock cycles": 4,
            "enable": ["1", "1", "1", "1"],
            "S": ["1", "0", "1", "0"],
            "A": ["0", "0", "0", "0"],
            "B": ["0", "0", "0", "0"],
            "C": ["0", "0", "0", "0"]
        }]
    })

    # Scenario 6: Enable Setup Hold Time
    scenarios.append({
        "scenario": "EnableSetupHoldTime",
        "input variable": [{
            "clock cycles": 4,
            "enable": ["0", "1", "0", "1"],
            "S": ["1", "1", "1", "1"],
            "A": ["0", "0", "0", "0"],
            "B": ["0", "0", "0", "0"],
            "C": ["0", "0", "0", "0"]
        }]
    })

    # Scenario 7: ABC Address Changes
    scenarios.append({
        "scenario": "ABCAddressChanges",
        "input variable": [{
            "clock cycles": 8,
            "enable": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "S": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "A": ["0", "0", "0", "0", "1", "1", "1", "1"],
            "B": ["0", "0", "1", "1", "0", "0", "1", "1"],
            "C": ["0", "1", "0", "1", "0", "1", "0", "1"]
        }]
    })

    # Scenario 8: Rapid Address Switching
    scenarios.append({
        "scenario": "RapidAddressSwitching",
        "input variable": [{
            "clock cycles": 8,
            "enable": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "S": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "A": ["1", "0", "1", "0", "1", "0", "1", "0"],
            "B": ["0", "1", "0", "1", "0", "1", "0", "1"],
            "C": ["1", "0", "1", "0", "1", "0", "1", "0"]
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
