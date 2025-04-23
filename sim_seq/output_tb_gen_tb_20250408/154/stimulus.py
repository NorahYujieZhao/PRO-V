import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to convert decimal to BCD
    def dec_to_bcd(dec):
        tens = dec // 10
        ones = dec % 10
        return format((tens << 4) | ones, '08b')
    
    # Basic Time Increment
    scenarios.append({
        "scenario": "BasicTimeIncrement",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["1"] + ["0"]*9,
            "ena": ["0"] + ["1"]*9
        }]
    })
    
    # Minutes Rollover
    scenarios.append({
        "scenario": "MinutesRollover",
        "input variable": [{
            "clock cycles": 62,
            "reset": ["1"] + ["0"]*61,
            "ena": ["0"] + ["1"]*61
        }]
    })
    
    # Hours Rollover
    scenarios.append({
        "scenario": "HoursRollover",
        "input variable": [{
            "clock cycles": 3602,
            "reset": ["1"] + ["0"]*3601,
            "ena": ["0"] + ["1"]*3601
        }]
    })
    
    # AMPM Transition
    scenarios.append({
        "scenario": "AMPMTransition",
        "input variable": [{
            "clock cycles": 43202,
            "reset": ["1"] + ["0"]*43201,
            "ena": ["0"] + ["1"]*43201
        }]
    })
    
    # Hour Format Check
    scenarios.append({
        "scenario": "HourFormatCheck",
        "input variable": [{
            "clock cycles": 7200,
            "reset": ["1"] + ["0"]*7199,
            "ena": ["0"] + ["1"]*7199
        }]
    })
    
    # Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["1", "0", "0", "0", "1", "0", "0", "0", "1", "0"],
            "ena": ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        }]
    })
    
    # Reset Priority
    scenarios.append({
        "scenario": "ResetPriority",
        "input variable": [{
            "clock cycles": 5,
            "reset": ["1", "1", "1", "1", "1"],
            "ena": ["1", "1", "1", "1", "1"]
        }]
    })
    
    # Enable Control
    scenarios.append({
        "scenario": "EnableControl",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["1"] + ["0"]*9,
            "ena": ["0", "1", "1", "0", "0", "1", "1", "0", "1", "0"]
        }]
    })
    
    # BCD Format Validation
    scenarios.append({
        "scenario": "BCDFormatValidation",
        "input variable": [{
            "clock cycles": 100,
            "reset": ["1"] + ["0"]*99,
            "ena": ["0"] + ["1"]*99
        }]
    })
    
    # Full Day Cycle
    scenarios.append({
        "scenario": "FullDayCycle",
        "input variable": [{
            "clock cycles": 86400,
            "reset": ["1"] + ["0"]*86399,
            "ena": ["0"] + ["1"]*86399
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
