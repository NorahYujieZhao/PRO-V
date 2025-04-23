import json
def stimulus_gen():
    scenarios = []
    
    def create_reset_sequence(cycles, reset_val):
        return {
            'clock cycles': cycles,
            'resetn': ['0' if reset_val else '1'] * cycles,
            'x': ['0'] * cycles,
            'y': ['0'] * cycles
        }
    
    def create_x_pattern():
        return {
            'clock cycles': 3,
            'resetn': ['1', '1', '1'],
            'x': ['1', '0', '1'],
            'y': ['0', '0', '0']
        }
    
    # Scenario 1: Initial Reset State
    scenarios.append({
        'scenario': 'InitialResetState',
        'input variable': [create_reset_sequence(5, True)]
    })
    
    # Scenario 2: Single F Pulse After Reset Release
    scenarios.append({
        'scenario': 'SingleFPulseAfterResetRelease',
        'input variable': [
            create_reset_sequence(3, True),
            {
                'clock cycles': 3,
                'resetn': ['1', '1', '1'],
                'x': ['0', '0', '0'],
                'y': ['0', '0', '0']
            }
        ]
    })
    
    # Scenario 3: X Input Pattern Detection
    scenarios.append({
        'scenario': 'XInputPatternDetection',
        'input variable': [
            create_reset_sequence(2, True),
            {
                'clock cycles': 2,
                'resetn': ['1', '1'],
                'x': ['0', '0'],
                'y': ['0', '0']
            },
            create_x_pattern()
        ]
    })
    
    # Scenario 4: Y Input Quick Response
    scenarios.append({
        'scenario': 'YInputQuickResponse',
        'input variable': [
            create_reset_sequence(2, True),
            {
                'clock cycles': 2,
                'resetn': ['1', '1'],
                'x': ['0', '0'],
                'y': ['0', '0']
            },
            create_x_pattern(),
            {
                'clock cycles': 2,
                'resetn': ['1', '1'],
                'x': ['0', '0'],
                'y': ['1', '1']
            }
        ]
    })
    
    # Scenario 5: Y Input Timeout
    scenarios.append({
        'scenario': 'YInputTimeout',
        'input variable': [
            create_reset_sequence(2, True),
            create_x_pattern(),
            {
                'clock cycles': 3,
                'resetn': ['1', '1', '1'],
                'x': ['0', '0', '0'],
                'y': ['0', '0', '0']
            }
        ]
    })
    
    # Scenario 6: Reset During Operation
    scenarios.append({
        'scenario': 'ResetDuringOperation',
        'input variable': [
            create_reset_sequence(2, True),
            create_x_pattern(),
            {
                'clock cycles': 2,
                'resetn': ['0', '0'],
                'x': ['0', '0'],
                'y': ['0', '0']
            }
        ]
    })
    
    # Scenario 7: Incomplete X Pattern
    scenarios.append({
        'scenario': 'IncompleteXPattern',
        'input variable': [
            create_reset_sequence(2, True),
            {
                'clock cycles': 3,
                'resetn': ['1', '1', '1'],
                'x': ['1', '0', '0'],
                'y': ['0', '0', '0']
            }
        ]
    })
    
    # Scenario 8: Multiple X Patterns
    scenarios.append({
        'scenario': 'MultipleXPatterns',
        'input variable': [
            create_reset_sequence(2, True),
            create_x_pattern(),
            create_x_pattern()
        ]
    })
    
    # Scenario 9: Y Input Edge Timing
    scenarios.append({
        'scenario': 'YInputEdgeTiming',
        'input variable': [
            create_reset_sequence(2, True),
            create_x_pattern(),
            {
                'clock cycles': 2,
                'resetn': ['1', '1'],
                'x': ['0', '0'],
                'y': ['0', '1']
            }
        ]
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
