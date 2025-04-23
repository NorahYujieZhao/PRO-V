import json
def stimulus_gen():
    # Helper function to create a sequence group
    def create_sequence(cycles, s_vals, w_vals):
        return {
            "clock cycles": cycles,
            "reset": ['0'] * cycles,
            "s": s_vals,
            "w": w_vals
        }
    
    scenarios = []
    
    # Scenario 1: Reset State Verification
    scenarios.append({
        "scenario": "ResetStateVerification",
        "input variable": [
            {
                "clock cycles": 3,
                "reset": ['1', '1', '1'],
                "s": ['0', '0', '0'],
                "w": ['0', '0', '0']
            }
        ]
    })
    
    # Scenario 2: Stay in State A
    scenarios.append({
        "scenario": "StayInStateA",
        "input variable": [
            create_sequence(5, ['0']*5, ['0']*5)
        ]
    })
    
    # Scenario 3: Basic State A to B Transition
    scenarios.append({
        "scenario": "BasicStateAToBTransition",
        "input variable": [
            create_sequence(3, ['0', '1', '0'], ['0', '0', '0'])
        ]
    })
    
    # Scenario 4: Exactly Two High W Inputs
    scenarios.append({
        "scenario": "ExactlyTwoHighWInputs",
        "input variable": [
            create_sequence(4, ['1', '0', '0', '0'], ['1', '1', '0', '0'])
        ]
    })
    
    # Scenario 5: Less Than Two High W Inputs
    scenarios.append({
        "scenario": "LessThanTwoHighWInputs",
        "input variable": [
            create_sequence(4, ['1', '0', '0', '0'], ['1', '0', '0', '0'])
        ]
    })
    
    # Scenario 6: More Than Two High W Inputs
    scenarios.append({
        "scenario": "MoreThanTwoHighWInputs",
        "input variable": [
            create_sequence(4, ['1', '0', '0', '0'], ['1', '1', '1', '0'])
        ]
    })
    
    # Scenario 7: Zero High W Inputs
    scenarios.append({
        "scenario": "ZeroHighWInputs",
        "input variable": [
            create_sequence(4, ['1', '0', '0', '0'], ['0', '0', '0', '0'])
        ]
    })
    
    # Scenario 8: Multiple Three Cycle Windows
    scenarios.append({
        "scenario": "MultipleThreeCycleWindows",
        "input variable": [
            create_sequence(8, 
                ['1', '0', '0', '0', '0', '0', '0', '0'],
                ['1', '1', '0', '0', '1', '0', '1', '0'])
        ]
    })
    
    # Scenario 9: Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [
            {
                "clock cycles": 5,
                "reset": ['0', '0', '1', '0', '0'],
                "s": ['1', '0', '0', '0', '0'],
                "w": ['1', '1', '0', '0', '0']
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
