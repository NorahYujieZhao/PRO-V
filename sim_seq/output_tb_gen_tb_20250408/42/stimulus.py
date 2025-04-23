import json
def stimulus_gen():
    scenarios = []
    
    # Basic Operation
    basic_op = {
        'scenario': 'BasicOperation',
        'input variable': [
            {
                'clock cycles': 8,
                'd': ['0', '1', '0', '1', '1', '0', '0', '1']
            }
        ]
    }
    scenarios.append(basic_op)
    
    # Multiple Data Transitions
    multiple_trans = {
        'scenario': 'MultipleDataTransitions',
        'input variable': [
            {
                'clock cycles': 4,
                'd': ['0', '1', '0', '1']
            },
            {
                'clock cycles': 4,
                'd': ['1', '0', '1', '0']
            }
        ]
    }
    scenarios.append(multiple_trans)
    
    # Setup Time Verification
    setup_time = {
        'scenario': 'SetupTimeVerification',
        'input variable': [
            {
                'clock cycles': 6,
                'd': ['0', '1', '1', '0', '0', '1']
            }
        ]
    }
    scenarios.append(setup_time)
    
    # Hold Time Verification
    hold_time = {
        'scenario': 'HoldTimeVerification',
        'input variable': [
            {
                'clock cycles': 6,
                'd': ['1', '0', '1', '0', '1', '0']
            }
        ]
    }
    scenarios.append(hold_time)
    
    # Clock Glitch Immunity
    glitch_immunity = {
        'scenario': 'ClockGlitchImmunity',
        'input variable': [
            {
                'clock cycles': 8,
                'd': ['1', '1', '1', '1', '0', '0', '0', '0']
            }
        ]
    }
    scenarios.append(glitch_immunity)
    
    # Data Retention
    data_retention = {
        'scenario': 'DataRetention',
        'input variable': [
            {
                'clock cycles': 10,
                'd': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
            },
            {
                'clock cycles': 10,
                'd': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
            }
        ]
    }
    scenarios.append(data_retention)
    
    # High Frequency Operation
    high_freq = {
        'scenario': 'HighFrequencyOperation',
        'input variable': [
            {
                'clock cycles': 10,
                'd': ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0']
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
