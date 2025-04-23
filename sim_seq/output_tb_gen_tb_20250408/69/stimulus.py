import json

def stimulus_gen():
    scenarios = []
    
    # Helper function to format binary strings
    def bin_format(num, width):
        return format(num, f'0{width}b')
    
    # Scenario 1: State Transition x0
    state_trans_x0 = {
        'scenario': 'StateTransitionx0',
        'input variable': [{
            'clock cycles': 5,
            'x': ['0']*5,
            'y': [bin_format(i, 3) for i in range(5)]
        }]
    }
    scenarios.append(state_trans_x0)
    
    # Scenario 2: State Transition x1
    state_trans_x1 = {
        'scenario': 'StateTransitionx1',
        'input variable': [{
            'clock cycles': 5,
            'x': ['1']*5,
            'y': [bin_format(i, 3) for i in range(5)]
        }]
    }
    scenarios.append(state_trans_x1)
    
    # Scenario 3: Output z Verification
    output_z_verify = {
        'scenario': 'OutputzVerification',
        'input variable': [{
            'clock cycles': 10,
            'x': ['0', '1']*5,
            'y': ['011', '100', '000', '001', '010']*2
        }]
    }
    scenarios.append(output_z_verify)
    
    # Scenario 4: Y0 Output
    y0_output = {
        'scenario': 'Y0Output',
        'input variable': [{
            'clock cycles': 10,
            'x': ['0', '1']*5,
            'y': [bin_format(i, 3) for i in range(5)]*2
        }]
    }
    scenarios.append(y0_output)
    
    # Scenario 5: Clock Edge Behavior
    clock_edge = {
        'scenario': 'ClockEdgeBehavior',
        'input variable': [{
            'clock cycles': 8,
            'x': ['0', '0', '1', '1', '0', '0', '1', '1'],
            'y': ['000', '000', '001', '001', '010', '010', '011', '011']
        }]
    }
    scenarios.append(clock_edge)
    
    # Scenario 6: Invalid States
    invalid_states = {
        'scenario': 'InvalidStates',
        'input variable': [{
            'clock cycles': 6,
            'x': ['0', '1']*3,
            'y': ['101', '110', '111']*2
        }]
    }
    scenarios.append(invalid_states)
    
    # Scenario 7: Rapid Input Changes
    rapid_changes = {
        'scenario': 'RapidInputChanges',
        'input variable': [{
            'clock cycles': 8,
            'x': ['0', '1', '0', '1', '0', '1', '0', '1'],
            'y': ['000']*8
        }]
    }
    scenarios.append(rapid_changes)
    
    # Scenario 8: State Sequence
    state_sequence = {
        'scenario': 'StateSequence',
        'input variable': [{
            'clock cycles': 10,
            'x': ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
            'y': ['000', '001', '010', '011', '100', '000', '001', '010', '011', '100']
        }]
    }
    scenarios.append(state_sequence)
    
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
