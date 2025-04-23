import json
def stimulus_gen():
    # List to store all test scenarios
    scenarios = []
    
    # Basic Data Capture
    basic_data = {
        "scenario": "BasicDataCapture",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["00000000", "11111111", "10101010", "01010101"]
            }
        ]
    }
    scenarios.append(basic_data)
    
    # Alternating Bit Patterns
    alternating = {
        "scenario": "AlternatingBitPatterns",
        "input variable": [
            {
                "clock cycles": 6,
                "d": ["01010101", "10101010", "01010101", "10101010", "01010101", "10101010"]
            }
        ]
    }
    scenarios.append(alternating)
    
    # Walking Ones Pattern
    walking_ones = {
        "scenario": "WalkingOnesPattern",
        "input variable": [
            {
                "clock cycles": 8,
                "d": ["00000001", "00000010", "00000100", "00001000",
                      "00010000", "00100000", "01000000", "10000000"]
            }
        ]
    }
    scenarios.append(walking_ones)
    
    # Walking Zeros Pattern
    walking_zeros = {
        "scenario": "WalkingZerosPattern",
        "input variable": [
            {
                "clock cycles": 8,
                "d": ["11111110", "11111101", "11111011", "11110111",
                      "11101111", "11011111", "10111111", "01111111"]
            }
        ]
    }
    scenarios.append(walking_zeros)
    
    # Setup Time Verification
    setup_time = {
        "scenario": "SetupTimeVerification",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["11110000", "00001111", "11001100", "00110011"]
            }
        ]
    }
    scenarios.append(setup_time)
    
    # Hold Time Verification
    hold_time = {
        "scenario": "HoldTimeVerification",
        "input variable": [
            {
                "clock cycles": 4,
                "d": ["11001100", "00110011", "11110000", "00001111"]
            }
        ]
    }
    scenarios.append(hold_time)
    
    # Multiple Clock Cycles Stability
    stability = {
        "scenario": "MultipleClockCyclesStability",
        "input variable": [
            {
                "clock cycles": 5,
                "d": ["10101010", "10101010", "10101010", "10101010", "10101010"]
            }
        ]
    }
    scenarios.append(stability)
    
    # High Frequency Operation
    high_freq = {
        "scenario": "HighFrequencyOperation",
        "input variable": [
            {
                "clock cycles": 8,
                "d": ["11111111", "00000000", "11111111", "00000000",
                      "11111111", "00000000", "11111111", "00000000"]
            }
        ]
    }
    scenarios.append(high_freq)
    
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
