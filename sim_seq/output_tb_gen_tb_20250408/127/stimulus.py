import json

def stimulus_gen():
    scenarios = []
    
    # Helper function to create a stimulus sequence
    def create_sequence(name, cycles, areset_seq, load_seq, ena_seq, data_seq):
        return {
            'scenario': name,
            'input variable': [{
                'clock cycles': cycles,
                'areset': areset_seq,
                'load': load_seq,
                'ena': ena_seq,
                'data': data_seq
            }]
        }
    
    # Scenario 1: Basic Right Shift Operation
    scenarios.append(create_sequence(
        'BasicRightShiftOperation',
        6,
        ['0']*6,  # areset
        ['1'] + ['0']*5,  # load
        ['0'] + ['1']*5,  # ena
        ['1111'] + ['0000']*5  # data
    ))
    
    # Scenario 2: Asynchronous Reset Behavior
    scenarios.append(create_sequence(
        'AsynchronousResetBehavior',
        5,
        ['0', '1', '1', '0', '0'],
        ['1', '0', '0', '0', '1'],
        ['0', '0', '0', '0', '0'],
        ['1111', '1111', '1111', '1111', '1111']
    ))
    
    # Scenario 3: Load Operation
    scenarios.append(create_sequence(
        'LoadOperation',
        4,
        ['0']*4,
        ['0', '1', '1', '0'],
        ['0']*4,
        ['0000', '1010', '0101', '0000']
    ))
    
    # Scenario 4: Load Priority Over Enable
    scenarios.append(create_sequence(
        'LoadPriorityOverEnable',
        4,
        ['0']*4,
        ['0', '1', '1', '0'],
        ['0', '1', '1', '1'],
        ['0000', '1010', '0101', '0000']
    ))
    
    # Scenario 5: Disable State Hold
    scenarios.append(create_sequence(
        'DisableStateHold',
        5,
        ['0']*5,
        ['1'] + ['0']*4,
        ['0']*5,
        ['1010'] + ['0000']*4
    ))
    
    # Scenario 6: Sequential Operations
    scenarios.append(create_sequence(
        'SequentialOperations',
        6,
        ['0']*6,
        ['1'] + ['0']*5,
        ['0'] + ['1']*5,
        ['1111'] + ['0000']*5
    ))
    
    # Scenario 7: Boundary Value Loading
    scenarios.append(create_sequence(
        'BoundaryValueLoading',
        6,
        ['0']*6,
        ['1', '0', '0', '1', '0', '0'],
        ['0', '1', '1', '0', '1', '1'],
        ['0000', '0000', '0000', '1111', '1111', '1111']
    ))
    
    # Scenario 8: Reset Recovery
    scenarios.append(create_sequence(
        'ResetRecovery',
        6,
        ['1', '1', '0', '0', '0', '0'],
        ['0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '1', '1'],
        ['0000', '0000', '1111', '0000', '0000', '0000']
    ))
    
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
