import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create a sequence dictionary
    def create_sequence(name, cycles, areset_seq, bump_left_seq, bump_right_seq):
        return {
            "scenario": name,
            "input variable": [
                {
                    "clock cycles": cycles,
                    "areset": areset_seq,
                    "bump_left": bump_left_seq,
                    "bump_right": bump_right_seq
                }
            ]
        }
    
    # Scenario 1: Initial State After Reset
    scenarios.append(create_sequence(
        "InitialStateAfterReset",
        4,
        ["1", "1", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"]
    ))
    
    # Scenario 2: Left to Right Direction Change
    scenarios.append(create_sequence(
        "LeftToRightDirectionChange",
        5,
        ["1", "0", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ))
    
    # Scenario 3: Right to Left Direction Change
    scenarios.append(create_sequence(
        "RightToLeftDirectionChange",
        6,
        ["1", "0", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "0"]
    ))
    
    # Scenario 4: Simultaneous Bumps While Walking Left
    scenarios.append(create_sequence(
        "SimultaneousBumpsWhileWalkingLeft",
        5,
        ["1", "0", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "1", "0", "0"]
    ))
    
    # Scenario 5: Simultaneous Bumps While Walking Right
    scenarios.append(create_sequence(
        "SimultaneousBumpsWhileWalkingRight",
        6,
        ["1", "0", "0", "0", "0", "0"],
        ["0", "1", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "0", "0"]
    ))
    
    # Scenario 6: Reset During Walk Right
    scenarios.append(create_sequence(
        "ResetDuringWalkRight",
        6,
        ["1", "0", "0", "0", "1", "0"],
        ["0", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0"]
    ))
    
    # Scenario 7: Continuous Walking Left
    scenarios.append(create_sequence(
        "ContinuousWalkingLeft",
        5,
        ["1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ))
    
    # Scenario 8: Continuous Walking Right
    scenarios.append(create_sequence(
        "ContinuousWalkingRight",
        6,
        ["1", "0", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0"]
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
