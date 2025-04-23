import json

def stimulus_gen():
    scenarios = []
    
    # Helper function to create a sequence with reset and specified number of following cycles
    def create_sequence(reset_sequence, additional_cycles):
        return {
            'clock cycles': len(reset_sequence) + additional_cycles,
            'reset': reset_sequence + ['0'] * additional_cycles
        }
    
    # Scenario 1: Basic Reset Operation
    scenarios.append({
        'scenario': 'BasicResetOperation',
        'input variable': [
            create_sequence(['1'], 10)  # One reset cycle followed by 10 monitoring cycles
        ]
    })
    
    # Scenario 2: Multiple Reset Pulses
    scenarios.append({
        'scenario': 'MultipleResetPulses',
        'input variable': [
            create_sequence(['1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1'], 15)
        ]
    })
    
    # Scenario 3: Reset During Shift Operation
    scenarios.append({
        'scenario': 'ResetDuringShiftOperation',
        'input variable': [
            create_sequence(['1', '0', '0', '1'], 8)  # Reset during active shift_ena
        ]
    })
    
    # Scenario 4: Long Term Stability
    scenarios.append({
        'scenario': 'LongTermStability',
        'input variable': [
            create_sequence(['1'], 20)  # One reset followed by 20 cycles of stability check
        ]
    })
    
    # Scenario 5: Back to Back Reset
    scenarios.append({
        'scenario': 'BackToBackReset',
        'input variable': [
            create_sequence(['1', '0', '0', '0', '0', '1'], 8)  # Reset immediately after 4 cycles
        ]
    })
    
    # Scenario 6: Reset Pulse Width
    scenarios.append({
        'scenario': 'ResetPulseWidth',
        'input variable': [
            create_sequence(['1'], 5),  # Single cycle reset
            create_sequence(['1', '1', '1'], 5),  # Three cycle reset
            create_sequence(['1', '1', '1', '1', '1'], 5)  # Five cycle reset
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
