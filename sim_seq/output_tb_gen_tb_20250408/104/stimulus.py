import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Write Lower Byte Only
    scenarios.append({
        "scenario": "WriteLowerByteOnly",
        "input variable": [{
            "clock cycles": 4,
            "resetn": ["1", "1", "1", "1"],
            "byteena": ["01", "01", "01", "01"],
            "d": ["1010101011111111", "0000000011111111", "1111111100000000", "0101010111111111"]
        }]
    })
    
    # Scenario 2: Write Upper Byte Only
    scenarios.append({
        "scenario": "WriteUpperByteOnly",
        "input variable": [{
            "clock cycles": 4,
            "resetn": ["1", "1", "1", "1"],
            "byteena": ["10", "10", "10", "10"],
            "d": ["1111111100000000", "0000000011111111", "1010101010101010", "0101010101010101"]
        }]
    })
    
    # Scenario 3: Write Both Bytes
    scenarios.append({
        "scenario": "WriteBothBytes",
        "input variable": [{
            "clock cycles": 3,
            "resetn": ["1", "1", "1"],
            "byteena": ["11", "11", "11"],
            "d": ["1111111111111111", "0000000000000000", "1010101010101010"]
        }]
    })
    
    # Scenario 4: No Byte Write
    scenarios.append({
        "scenario": "NoByteWrite",
        "input variable": [{
            "clock cycles": 3,
            "resetn": ["1", "1", "1"],
            "byteena": ["00", "00", "00"],
            "d": ["1111111111111111", "0000000000000000", "1010101010101010"]
        }]
    })
    
    # Scenario 5: Synchronous Reset
    scenarios.append({
        "scenario": "SynchronousReset",
        "input variable": [{
            "clock cycles": 4,
            "resetn": ["1", "0", "0", "1"],
            "byteena": ["11", "11", "11", "11"],
            "d": ["1111111111111111", "1111111111111111", "1111111111111111", "1111111111111111"]
        }]
    })
    
    # Scenario 6: Alternating Byte Enables
    scenarios.append({
        "scenario": "AlternatingByteEnables",
        "input variable": [{
            "clock cycles": 4,
            "resetn": ["1", "1", "1", "1"],
            "byteena": ["01", "10", "11", "00"],
            "d": ["1010101010101010", "0101010101010101", "1111111111111111", "0000000000000000"]
        }]
    })
    
    # Scenario 7: Data Toggle Coverage
    scenarios.append({
        "scenario": "DataToggleCoverage",
        "input variable": [{
            "clock cycles": 4,
            "resetn": ["1", "1", "1", "1"],
            "byteena": ["11", "11", "11", "11"],
            "d": ["0000000000000000", "1111111111111111", "1010101010101010", "0101010101010101"]
        }]
    })
    
    # Scenario 8: Reset Recovery
    scenarios.append({
        "scenario": "ResetRecovery",
        "input variable": [{
            "clock cycles": 5,
            "resetn": ["0", "1", "1", "1", "1"],
            "byteena": ["11", "01", "10", "11", "00"],
            "d": ["1111111111111111", "0000000011111111", "1111111100000000", "1010101010101010", "0101010101010101"]
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
