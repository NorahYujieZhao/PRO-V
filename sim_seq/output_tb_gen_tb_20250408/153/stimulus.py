import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create a stimulus sequence
    def create_sequence(cycles, bump_l, bump_r, gnd, dig_sig):
        return {
            "clock cycles": cycles,
            "bump_left": bump_l,
            "bump_right": bump_r,
            "ground": gnd,
            "dig": dig_sig
        }
    
    # Scenario 1: Basic Walking Direction Change
    scenarios.append({
        "scenario": "BasicWalkingDirectionChange",
        "input variable": [
            create_sequence(3, ["0", "0", "1"], ["0", "0", "0"], ["1", "1", "1"], ["0", "0", "0"]),
            create_sequence(3, ["0", "0", "0"], ["0", "1", "0"], ["1", "1", "1"], ["0", "0", "0"])
        ]
    })
    
    # Scenario 2: Falling Behavior
    scenarios.append({
        "scenario": "FallingBehavior",
        "input variable": [
            create_sequence(4, ["0", "0", "0", "0"], ["0", "0", "0", "0"], 
                          ["1", "0", "0", "1"], ["0", "0", "0", "0"])
        ]
    })
    
    # Scenario 3: Digging Operation
    scenarios.append({
        "scenario": "DiggingOperation",
        "input variable": [
            create_sequence(5, ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"],
                          ["1", "1", "1", "0", "1"], ["0", "1", "1", "1", "0"])
        ]
    })
    
    # Scenario 4: Asynchronous Reset
    scenarios.append({
        "scenario": "AsynchronousReset",
        "input variable": [
            create_sequence(3, ["0", "0", "0"], ["0", "0", "0"], ["1", "1", "1"], ["0", "0", "0"])
        ]
    })
    
    # Scenario 5: Precedence Rules
    scenarios.append({
        "scenario": "PrecedenceRules",
        "input variable": [
            create_sequence(4, ["1", "0", "0", "0"], ["0", "0", "0", "0"],
                          ["1", "0", "1", "1"], ["0", "0", "1", "0"])
        ]
    })
    
    # Scenario 6: Bump While Falling
    scenarios.append({
        "scenario": "BumpWhileFalling",
        "input variable": [
            create_sequence(5, ["0", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
                          ["1", "0", "0", "0", "1"], ["0", "0", "0", "0", "0"])
        ]
    })
    
    # Scenario 7: Bump While Digging
    scenarios.append({
        "scenario": "BumpWhileDigging",
        "input variable": [
            create_sequence(4, ["0", "1", "0", "0"], ["0", "0", "1", "0"],
                          ["1", "1", "1", "1"], ["0", "1", "1", "0"])
        ]
    })
    
    # Scenario 8: Simultaneous Bumps
    scenarios.append({
        "scenario": "SimultaneousBumps",
        "input variable": [
            create_sequence(3, ["0", "1", "0"], ["0", "1", "0"], ["1", "1", "1"], ["0", "0", "0"])
        ]
    })
    
    # Scenario 9: Dig While Falling
    scenarios.append({
        "scenario": "DigWhileFalling",
        "input variable": [
            create_sequence(4, ["0", "0", "0", "0"], ["0", "0", "0", "0"],
                          ["1", "0", "0", "1"], ["0", "0", "1", "0"])
        ]
    })
    
    # Scenario 10: Ground Edge Transitions
    scenarios.append({
        "scenario": "GroundEdgeTransitions",
        "input variable": [
            create_sequence(4, ["0", "1", "0", "0"], ["0", "0", "0", "0"],
                          ["1", "0", "0", "1"], ["0", "0", "0", "0"])
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
