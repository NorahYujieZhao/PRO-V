import json

def stimulus_gen():
    scenarios = []
    
    # Helper function to create a scenario dictionary
    def create_scenario(name, clock_cycles, reset_sequence):
        return {
            'scenario': name,
            'input variable': [{
                'clock cycles': clock_cycles,
                'reset': reset_sequence
            }]
        }
    
    # Scenario 1: Synchronous Reset Behavior
    scenarios.append(create_scenario(
        'SynchronousResetBehavior',
        5,
        ['1', '1', '1', '0', '0']  # Assert reset for 3 cycles, then deassert
    ))
    
    # Scenario 2: Basic LFSR Operation
    scenarios.append(create_scenario(
        'BasicLFSROperation',
        10,
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0']  # Initial reset then observe LFSR operation
    ))
    
    # Scenario 3: Maximum Length Sequence
    scenarios.append(create_scenario(
        'MaximumLengthSequence',
        32,
        ['1'] + ['0']*31  # Reset once then run for full sequence
    ))
    
    # Scenario 4: Multiple Reset Cycles
    scenarios.append(create_scenario(
        'MultipleResetCycles',
        20,
        ['1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
    ))
    
    # Scenario 5: Clock Edge Sensitivity
    scenarios.append(create_scenario(
        'ClockEdgeSensitivity',
        8,
        ['1', '0', '0', '0', '0', '0', '0', '0']
    ))
    
    # Scenario 6: Sequence Verification
    scenarios.append(create_scenario(
        'SequenceVerification',
        15,
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    ))
    
    # Scenario 7: Long Term Stability
    scenarios.append(create_scenario(
        'LongTermStability',
        100,
        ['1'] + ['0']*99  # Initial reset then run for multiple sequences
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
