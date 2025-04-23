import json
def stimulus_gen():
    scenarios = []
    
    # Normal Counting Sequence
    normal_count = {
        'scenario': 'NormalCountingSequence',
        'input variable': [{
            'clock cycles': 12,
            'reset': ['0'] * 12
        }]
    }
    scenarios.append(normal_count)
    
    # Reset to One
    reset_to_one = {
        'scenario': 'ResetToOne',
        'input variable': [{
            'clock cycles': 5,
            'reset': ['0', '0', '0', '1', '0']
        }]
    }
    scenarios.append(reset_to_one)
    
    # Upper Boundary Transition
    upper_boundary = {
        'scenario': 'UpperBoundaryTransition',
        'input variable': [{
            'clock cycles': 15,
            'reset': ['0'] * 15
        }]
    }
    scenarios.append(upper_boundary)
    
    # Multiple Counting Cycles
    multiple_cycles = {
        'scenario': 'MultipleCountingCycles',
        'input variable': [{
            'clock cycles': 30,
            'reset': ['0'] * 30
        }]
    }
    scenarios.append(multiple_cycles)
    
    # Reset During Count
    reset_during_count = {
        'scenario': 'ResetDuringCount',
        'input variable': [{
            'clock cycles': 15,
            'reset': ['0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0']
        }]
    }
    scenarios.append(reset_during_count)
    
    # Initial Power Up State
    initial_power_up = {
        'scenario': 'InitialPowerUpState',
        'input variable': [{
            'clock cycles': 5,
            'reset': ['1', '0', '0', '0', '0']
        }]
    }
    scenarios.append(initial_power_up)
    
    # Reset Pulse Width
    reset_pulse_width = {
        'scenario': 'ResetPulseWidth',
        'input variable': [{
            'clock cycles': 12,
            'reset': ['0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0']
        }]
    }
    scenarios.append(reset_pulse_width)
    
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
