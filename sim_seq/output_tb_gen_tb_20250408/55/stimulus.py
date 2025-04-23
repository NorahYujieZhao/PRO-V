import json
def stimulus_gen():
    scenarios = []
    
    # Basic State A to B Transition
    scenarios.append({
        "scenario": "BasicStateAtoBTransition",
        "input variable": [
            {
                "clock cycles": 2,
                "areset": ["1", "0"],  # Reset to get to known state
                "in": ["0", "0"]
            },
            {
                "clock cycles": 2,
                "areset": ["0", "0"],  # Test A->B transition
                "in": ["1", "0"]
            }
        ]
    })
    
    # Basic State B to A Transition
    scenarios.append({
        "scenario": "BasicStateBtoATransition",
        "input variable": [
            {
                "clock cycles": 2,
                "areset": ["1", "0"],  # Reset to get to B state
                "in": ["0", "0"]
            },
            {
                "clock cycles": 2,
                "areset": ["0", "0"],  # Test B->A transition
                "in": ["0", "0"]
            }
        ]
    })
    
    # State A Self Loop
    scenarios.append({
        "scenario": "StateASelfLoop",
        "input variable": [
            {
                "clock cycles": 2,
                "areset": ["1", "0"],  # Reset then go to A
                "in": ["0", "0"]
            },
            {
                "clock cycles": 3,
                "areset": ["0", "0", "0"],  # Test A->A loop
                "in": ["0", "1", "1"]
            }
        ]
    })
    
    # State B Self Loop
    scenarios.append({
        "scenario": "StateBSelfLoop",
        "input variable": [
            {
                "clock cycles": 1,
                "areset": ["1"],  # Reset to B
                "in": ["0"]
            },
            {
                "clock cycles": 3,
                "areset": ["0", "0", "0"],  # Test B->B loop
                "in": ["1", "1", "1"]
            }
        ]
    })
    
    # Asynchronous Reset Activation
    scenarios.append({
        "scenario": "AsynchronousResetActivation",
        "input variable": [
            {
                "clock cycles": 3,
                "areset": ["0", "0", "1"],  # Go to A then reset
                "in": ["0", "0", "0"]
            }
        ]
    })
    
    # Reset Release Operation
    scenarios.append({
        "scenario": "ResetReleaseOperation",
        "input variable": [
            {
                "clock cycles": 2,
                "areset": ["1", "0"],  # Release reset
                "in": ["0", "0"]
            },
            {
                "clock cycles": 3,
                "areset": ["0", "0", "0"],  # Normal operation
                "in": ["0", "1", "0"]
            }
        ]
    })
    
    # Multiple State Transitions
    scenarios.append({
        "scenario": "MultipleStateTransitions",
        "input variable": [
            {
                "clock cycles": 2,
                "areset": ["1", "0"],  # Start from known state
                "in": ["0", "0"]
            },
            {
                "clock cycles": 6,
                "areset": ["0", "0", "0", "0", "0", "0"],
                "in": ["0", "1", "0", "1", "0", "1"]
            }
        ]
    })
    
    # Reset During State Transition
    scenarios.append({
        "scenario": "ResetDuringStateTransition",
        "input variable": [
            {
                "clock cycles": 3,
                "areset": ["0", "0", "1"],  # Assert reset during transition
                "in": ["0", "1", "0"]
            },
            {
                "clock cycles": 2,
                "areset": ["1", "0"],  # Keep reset, then release
                "in": ["0", "0"]
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
