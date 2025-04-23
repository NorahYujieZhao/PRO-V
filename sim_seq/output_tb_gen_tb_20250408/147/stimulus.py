import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to convert integer to 8-bit binary string LSB first
    def int_to_lsb_first(num):
        bin_str = format(num, '08b')
        return ''.join(reversed(bin_str))
    
    # Scenario 1: Valid Single Byte Reception
    scenarios.append({
        "scenario": "ValidSingleByteReception",
        "input variable": [{
            "clock cycles": 12,
            "in": ['1', '0'] + list(int_to_lsb_first(0xA5)) + ['1', '1'],
            "reset": ['0'] * 12
        }]
    })
    
    # Scenario 2: Multiple Consecutive Bytes
    scenarios.append({
        "scenario": "MultipleConsecutiveBytes",
        "input variable": [{
            "clock cycles": 22,
            "in": ['1', '0'] + list(int_to_lsb_first(0x55)) + ['1', '0'] + 
                  list(int_to_lsb_first(0xAA)) + ['1'],
            "reset": ['0'] * 22
        }]
    })
    
    # Scenario 3: Missing Stop Bit
    scenarios.append({
        "scenario": "MissingStopBit",
        "input variable": [{
            "clock cycles": 15,
            "in": ['1', '0'] + list(int_to_lsb_first(0x33)) + ['0', '1', '1', '1'],
            "reset": ['0'] * 15
        }]
    })
    
    # Scenario 4: Idle Line Recovery
    scenarios.append({
        "scenario": "IdleLineRecovery",
        "input variable": [{
            "clock cycles": 20,
            "in": ['1', '0'] + list(int_to_lsb_first(0x44)) + ['0'] + ['1'] * 5 + 
                  ['0'] + list(int_to_lsb_first(0x77)) + ['1'],
            "reset": ['0'] * 20
        }]
    })
    
    # Scenario 5: Reset During Reception
    scenarios.append({
        "scenario": "ResetDuringReception",
        "input variable": [{
            "clock cycles": 15,
            "in": ['1', '0'] + list(int_to_lsb_first(0x66)) + ['1'] * 5,
            "reset": ['0', '0', '0', '1', '1'] + ['0'] * 10
        }]
    })
    
    # Scenario 6: Extended Idle Period
    scenarios.append({
        "scenario": "ExtendedIdlePeriod",
        "input variable": [{
            "clock cycles": 16,
            "in": ['1'] * 6 + ['0'] + list(int_to_lsb_first(0x99)) + ['1'],
            "reset": ['0'] * 16
        }]
    })
    
    # Scenario 7: Bit Order Verification
    scenarios.append({
        "scenario": "BitOrderVerification",
        "input variable": [{
            "clock cycles": 12,
            "in": ['1', '0'] + list(int_to_lsb_first(0xF0)) + ['1', '1'],
            "reset": ['0'] * 12
        }]
    })
    
    # Scenario 8: Back to Back Bytes Minimum Gap
    scenarios.append({
        "scenario": "BackToBackBytesMinimumGap",
        "input variable": [{
            "clock cycles": 21,
            "in": ['1', '0'] + list(int_to_lsb_first(0x11)) + ['1', '0'] + 
                  list(int_to_lsb_first(0x22)) + ['1'],
            "reset": ['0'] * 21
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
