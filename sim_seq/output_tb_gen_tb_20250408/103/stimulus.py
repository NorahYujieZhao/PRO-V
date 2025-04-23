import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create a sequence dictionary
    def create_sequence(scenario_name, cycles, reset_seq, w_seq):
        return {
            "scenario": scenario_name,
            "input variable": [
                {
                    "clock cycles": cycles,
                    "reset": reset_seq,
                    "w": w_seq
                }
            ]
        }
    
    # Reset State Verification
    scenarios.append(create_sequence(
        "ResetStateVerification",
        4,
        ["1", "1", "0", "0"],
        ["0", "0", "0", "0"]
    ))
    
    # Path to Output One (A->B->C->E)
    scenarios.append(create_sequence(
        "PathToOutputOne",
        5,
        ["1", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "1"]
    ))
    
    # Path to Alternate Output One (A->B->D->F)
    scenarios.append(create_sequence(
        "PathToAlternateOutputOne",
        5,
        ["1", "0", "0", "0", "0"],
        ["0", "1", "0", "1", "1"]
    ))
    
    # State A Self Loop
    scenarios.append(create_sequence(
        "StateASelfLoop",
        6,
        ["1", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0"]
    ))
    
    # Output Toggle via D State
    scenarios.append(create_sequence(
        "OutputToggleViaDState",
        7,
        ["1", "0", "0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0", "0", "1"]
    ))
    
    # Maximum Path Coverage
    scenarios.append(create_sequence(
        "MaximumPathCoverage",
        8,
        ["1", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0", "1", "0", "1"]
    ))
    
    # Reset from Output High
    scenarios.append(create_sequence(
        "ResetFromOutputHigh",
        6,
        ["1", "0", "0", "0", "1", "0"],
        ["0", "1", "1", "1", "0", "0"]
    ))
    
    # Rapid Input Transitions
    scenarios.append(create_sequence(
        "RapidInputTransitions",
        8,
        ["1", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "1", "0", "1", "0", "1", "0", "1"]
    ))
    
    # State E Self Loop
    scenarios.append(create_sequence(
        "StateESelfLoop",
        7,
        ["1", "0", "0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "1", "1", "1"]
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
