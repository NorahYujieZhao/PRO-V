import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Synchronous Reset Verification
    reset_verify = {
        'scenario': 'SynchronousResetVerification',
        'input variable': [{
            'clock cycles': 4,
            'reset': ['0', '1', '0', '0'],
            'x': ['0', '0', '0', '0']
        }]
    }
    scenarios.append(reset_verify)
    
    # Scenario 2: State Transition with X=0
    x_zero_transitions = {
        'scenario': 'StateTransitionWithInputXZero',
        'input variable': [{
            'clock cycles': 6,
            'reset': ['1', '0', '0', '0', '0', '0'],
            'x': ['0', '0', '0', '0', '0', '0']
        }]
    }
    scenarios.append(x_zero_transitions)
    
    # Scenario 3: State Transition with X=1
    x_one_transitions = {
        'scenario': 'StateTransitionWithInputXOne',
        'input variable': [{
            'clock cycles': 6,
            'reset': ['1', '0', '0', '0', '0', '0'],
            'x': ['0', '1', '1', '1', '1', '1']
        }]
    }
    scenarios.append(x_one_transitions)
    
    # Scenario 4: Output Z Generation
    output_verify = {
        'scenario': 'OutputZGeneration',
        'input variable': [{
            'clock cycles': 8,
            'reset': ['1', '0', '0', '0', '0', '0', '0', '0'],
            'x': ['0', '1', '1', '0', '1', '1', '0', '1']
        }]
    }
    scenarios.append(output_verify)
    
    # Scenario 5: Multiple State Transitions
    multiple_transitions = {
        'scenario': 'MultipleStateTransitions',
        'input variable': [{
            'clock cycles': 10,
            'reset': ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            'x': ['0', '1', '0', '1', '1', '0', '1', '0', '1', '0']
        }]
    }
    scenarios.append(multiple_transitions)
    
    # Scenario 6: Reset During Operation
    reset_during_op = {
        'scenario': 'ResetDuringOperation',
        'input variable': [{
            'clock cycles': 8,
            'reset': ['0', '0', '1', '0', '0', '1', '0', '0'],
            'x': ['1', '1', '0', '1', '1', '0', '1', '1']
        }]
    }
    scenarios.append(reset_during_op)
    
    # Scenario 7: Rapid Input Changes
    rapid_changes = {
        'scenario': 'RapidInputChanges',
        'input variable': [{
            'clock cycles': 8,
            'reset': ['1', '0', '0', '0', '0', '0', '0', '0'],
            'x': ['0', '1', '0', '1', '0', '1', '0', '1']
        }]
    }
    scenarios.append(rapid_changes)
    
    # Scenario 8: Setup and Hold Time
    setup_hold = {
        'scenario': 'SetupAndHoldTime',
        'input variable': [{
            'clock cycles': 6,
            'reset': ['0', '0', '0', '0', '0', '0'],
            'x': ['0', '1', '0', '1', '0', '1']
        }]
    }
    scenarios.append(setup_hold)
    
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
