import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to format binary inputs
    def format_input(j_val, k_val, cycles):
        return {
            'clock cycles': cycles,
            'j': [format(j_val, '01b')] * cycles,
            'k': [format(k_val, '01b')] * cycles
        }

    # Scenario 1: Hold State Operation
    hold_state = {
        'scenario': 'HoldStateOperation',
        'input variable': [
            format_input(0, 0, 4),  # Hold Q=0 for 4 cycles
            format_input(1, 0, 1),  # Set Q to 1
            format_input(0, 0, 4)   # Hold Q=1 for 4 cycles
        ]
    }
    scenarios.append(hold_state)

    # Scenario 2: Reset Operation
    reset_op = {
        'scenario': 'ResetOperation',
        'input variable': [
            format_input(1, 0, 1),  # Set Q to 1
            format_input(0, 1, 2),  # Reset to 0
            format_input(1, 0, 1),  # Set Q to 1 again
            format_input(0, 1, 2)   # Reset to 0 again
        ]
    }
    scenarios.append(reset_op)

    # Scenario 3: Set Operation
    set_op = {
        'scenario': 'SetOperation',
        'input variable': [
            format_input(0, 1, 1),  # Reset Q to 0
            format_input(1, 0, 2),  # Set to 1
            format_input(0, 1, 1),  # Reset to 0
            format_input(1, 0, 2)   # Set to 1 again
        ]
    }
    scenarios.append(set_op)

    # Scenario 4: Toggle Operation
    toggle_op = {
        'scenario': 'ToggleOperation',
        'input variable': [
            format_input(0, 1, 1),  # Reset to 0
            format_input(1, 1, 6)   # Toggle 6 times
        ]
    }
    scenarios.append(toggle_op)

    # Scenario 5: Input Changes Between Clock Edges
    input_changes = {
        'scenario': 'InputChangesBetweenClockEdges',
        'input variable': [
            {
                'clock cycles': 6,
                'j': ['0', '1', '0', '1', '0', '1'],
                'k': ['1', '0', '1', '0', '1', '0']
            }
        ]
    }
    scenarios.append(input_changes)

    # Scenario 6: Rapid Input Transitions
    rapid_transitions = {
        'scenario': 'RapidInputTransitions',
        'input variable': [
            {
                'clock cycles': 8,
                'j': ['0', '1', '1', '0', '0', '1', '1', '0'],
                'k': ['1', '0', '1', '0', '1', '1', '0', '1']
            }
        ]
    }
    scenarios.append(rapid_transitions)

    # Scenario 7: All State Transitions
    all_transitions = {
        'scenario': 'AllStateTransitions',
        'input variable': [
            {
                'clock cycles': 8,
                'j': ['0', '0', '1', '1', '0', '0', '1', '1'],
                'k': ['0', '1', '0', '1', '0', '1', '0', '1']
            }
        ]
    }
    scenarios.append(all_transitions)

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
