import json
import random

def gen_byte(bit3_val, other_bits=None):
    if other_bits is None:
        other_bits = format(random.randint(0, 127), '07b')
    return f'{other_bits[:3]}{bit3_val}{other_bits[3:]}'

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Message Reception
    basic_msg = {
        'scenario': 'BasicMessageReception',
        'input variable': [{
            'clock cycles': 3,
            'in': [gen_byte('1'), gen_byte('0'), gen_byte('0')],
            'reset': ['0', '0', '0']
        }]
    }
    scenarios.append(basic_msg)

    # Scenario 2: Multiple Sequential Messages
    multi_msg = {
        'scenario': 'MultipleSequentialMessages',
        'input variable': [{
            'clock cycles': 6,
            'in': [gen_byte('1'), gen_byte('0'), gen_byte('0'),
                   gen_byte('1'), gen_byte('0'), gen_byte('0')],
            'reset': ['0']*6
        }]
    }
    scenarios.append(multi_msg)

    # Scenario 3: Invalid Start Byte Handling
    invalid_start = {
        'scenario': 'InvalidStartByteHandling',
        'input variable': [{
            'clock cycles': 5,
            'in': [gen_byte('0'), gen_byte('0'), gen_byte('1'),
                   gen_byte('0'), gen_byte('0')],
            'reset': ['0']*5
        }]
    }
    scenarios.append(invalid_start)

    # Scenario 4: Reset During Message
    reset_msg = {
        'scenario': 'ResetDuringMessage',
        'input variable': [{
            'clock cycles': 4,
            'in': [gen_byte('1'), gen_byte('0'), gen_byte('0'),
                   gen_byte('1')],
            'reset': ['0', '0', '1', '0']
        }]
    }
    scenarios.append(reset_msg)

    # Scenario 5: Mixed Valid Invalid Bytes
    mixed_bytes = {
        'scenario': 'MixedValidInvalidBytes',
        'input variable': [{
            'clock cycles': 7,
            'in': [gen_byte('0'), gen_byte('1'), gen_byte('0'),
                   gen_byte('0'), gen_byte('1'), gen_byte('0'),
                   gen_byte('0')],
            'reset': ['0']*7
        }]
    }
    scenarios.append(mixed_bytes)

    # Scenario 6: Back to Back Messages
    back_to_back = {
        'scenario': 'BackToBackMessages',
        'input variable': [{
            'clock cycles': 6,
            'in': [gen_byte('1'), gen_byte('0'), gen_byte('0'),
                   gen_byte('1'), gen_byte('0'), gen_byte('0')],
            'reset': ['0']*6
        }]
    }
    scenarios.append(back_to_back)

    # Scenario 7: Done Signal Timing
    done_timing = {
        'scenario': 'DoneSignalTiming',
        'input variable': [{
            'clock cycles': 4,
            'in': [gen_byte('1'), gen_byte('0'), gen_byte('0'),
                   gen_byte('1')],
            'reset': ['0']*4
        }]
    }
    scenarios.append(done_timing)

    # Scenario 8: Start Byte with Different Data
    diff_data = {
        'scenario': 'StartByteWithDifferentData',
        'input variable': [{
            'clock cycles': 6,
            'in': [gen_byte('1', '1010101'), gen_byte('0'), gen_byte('0'),
                   gen_byte('1', '0101010'), gen_byte('0'), gen_byte('0')],
            'reset': ['0']*6
        }]
    }
    scenarios.append(diff_data)

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
