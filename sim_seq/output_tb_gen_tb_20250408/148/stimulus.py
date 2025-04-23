import json

def stimulus_gen():
    scenarios = []
    
    # Helper function to create a valid byte sequence (start bit + 8 data bits + stop bit)
    def create_byte_sequence(byte_value):
        # Convert byte to binary string, padded to 8 bits
        data_bits = format(byte_value, '08b')
        # Return start bit (0) + data bits (LSB first) + stop bit (1)
        return ['0'] + [data_bits[7-i] for i in range(8)] + ['1']
    
    # Scenario 1: Normal Byte Reception
    scenarios.append({
        'scenario': 'NormalByteReception',
        'input variable': [{
            'clock cycles': 11,
            'in': ['1'] + create_byte_sequence(0x55),  # 0x55 = 01010101
            'reset': ['0']*11
        }]
    })
    
    # Scenario 2: Multiple Consecutive Bytes
    scenarios.append({
        'scenario': 'MultipleConsecutiveBytes',
        'input variable': [{
            'clock cycles': 22,
            'in': ['1'] + create_byte_sequence(0xAA) + create_byte_sequence(0x55),
            'reset': ['0']*22
        }]
    })
    
    # Scenario 3: Missing Stop Bit
    scenarios.append({
        'scenario': 'MissingStopBit',
        'input variable': [{
            'clock cycles': 15,
            'in': ['1'] + create_byte_sequence(0x33)[:-1] + ['0', '1', '1', '1'],  # Replace stop bit with 0
            'reset': ['0']*15
        }]
    })
    
    # Scenario 4: Idle Line Recovery
    scenarios.append({
        'scenario': 'IdleLineRecovery',
        'input variable': [{
            'clock cycles': 15,
            'in': ['1']*5 + create_byte_sequence(0x77),
            'reset': ['0']*15
        }]
    })
    
    # Scenario 5: Reset During Reception
    scenarios.append({
        'scenario': 'ResetDuringReception',
        'input variable': [{
            'clock cycles': 15,
            'in': ['1'] + create_byte_sequence(0x99),
            'reset': ['0']*5 + ['1'] + ['0']*9
        }]
    })
    
    # Scenario 6: LSB First Verification
    scenarios.append({
        'scenario': 'LSBFirstVerification',
        'input variable': [{
            'clock cycles': 11,
            'in': ['1'] + create_byte_sequence(0xA5),  # 10100101
            'reset': ['0']*11
        }]
    })
    
    # Scenario 7: Maximum Value Byte
    scenarios.append({
        'scenario': 'MaximumValueByte',
        'input variable': [{
            'clock cycles': 11,
            'in': ['1'] + create_byte_sequence(0xFF),
            'reset': ['0']*11
        }]
    })
    
    # Scenario 8: Minimum Value Byte
    scenarios.append({
        'scenario': 'MinimumValueByte',
        'input variable': [{
            'clock cycles': 11,
            'in': ['1'] + create_byte_sequence(0x00),
            'reset': ['0']*11
        }]
    })
    
    # Scenario 9: Glitch During Reception
    scenarios.append({
        'scenario': 'GlitchDuringReception',
        'input variable': [{
            'clock cycles': 12,
            'in': ['1'] + ['0'] + ['1', '0', '1'] + ['0'] + ['1', '0', '1', '0', '1'] + ['1'],
            'reset': ['0']*12
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
