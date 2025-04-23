import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create sequence dictionary
    def create_sequence(cycles, a_vals, b_vals):
        return {
            "clock cycles": cycles,
            "a": a_vals,
            "b": b_vals
        }
    
    # Scenario 1: Initialize State Register
    scenarios.append({
        "scenario": "InitializeStateRegister",
        "input variable": [
            create_sequence(2, ["1", "0"], ["0", "0"])
        ]
    })
    
    # Scenario 2: State Zero Behavior
    scenarios.append({
        "scenario": "StateZeroBehavior",
        "input variable": [
            create_sequence(4, ["0", "0", "1", "1"], ["0", "1", "0", "1"])
        ]
    })
    
    # Scenario 3: State One Behavior
    scenarios.append({
        "scenario": "StateOneBehavior",
        "input variable": [
            create_sequence(4, ["0", "0", "1", "1"], ["0", "1", "0", "1"])
        ]
    })
    
    # Scenario 4: State Transition Zero to One
    scenarios.append({
        "scenario": "StateTransitionZeroToOne",
        "input variable": [
            create_sequence(3, ["0", "1", "0"], ["0", "1", "0"])
        ]
    })
    
    # Scenario 5: State Transition One to Zero
    scenarios.append({
        "scenario": "StateTransitionOneToZero",
        "input variable": [
            create_sequence(3, ["1", "0", "0"], ["0", "1", "0"])
        ]
    })
    
    # Scenario 6: Clock Edge Sensitivity
    scenarios.append({
        "scenario": "ClockEdgeSensitivity",
        "input variable": [
            create_sequence(4, ["0", "0", "1", "1"], ["0", "1", "0", "1"])
        ]
    })
    
    # Scenario 7: Input Change Timing
    scenarios.append({
        "scenario": "InputChangeTiming",
        "input variable": [
            create_sequence(3, ["0", "1", "0"], ["0", "1", "1"])
        ]
    })
    
    # Scenario 8: Extended Operation
    scenarios.append({
        "scenario": "ExtendedOperation",
        "input variable": [
            create_sequence(8, ["0", "0", "1", "1", "0", "0", "1", "1"],
                             ["0", "1", "0", "1", "0", "1", "0", "1"])
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
