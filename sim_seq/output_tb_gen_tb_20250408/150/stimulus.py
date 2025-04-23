import json
def generate_binary_sequence(length, value):
    return ['1' if value else '0'] * length

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Walking Direction Changes
    scenarios.append({
        "scenario": "BasicWalkingDirectionChanges",
        "input variable": [{
            "clock cycles": 8,
            "bump_left": ['0', '1', '0', '0', '0', '0', '1', '0'],
            "bump_right": ['0', '0', '0', '1', '0', '0', '0', '0'],
            "ground": ['1', '1', '1', '1', '1', '1', '1', '1'],
            "dig": ['0', '0', '0', '0', '0', '0', '0', '0'],
            "areset": ['0', '0', '0', '0', '0', '0', '0', '0']
        }]
    })

    # Scenario 2: Basic Falling Behavior
    scenarios.append({
        "scenario": "BasicFallingBehavior",
        "input variable": [{
            "clock cycles": 10,
            "bump_left": ['0'] * 10,
            "bump_right": ['0'] * 10,
            "ground": ['1', '1', '0', '0', '0', '0', '0', '1', '1', '1'],
            "dig": ['0'] * 10,
            "areset": ['0'] * 10
        }]
    })

    # Scenario 3: Basic Digging Operation
    scenarios.append({
        "scenario": "BasicDiggingOperation",
        "input variable": [{
            "clock cycles": 6,
            "bump_left": ['0'] * 6,
            "bump_right": ['0'] * 6,
            "ground": ['1', '1', '1', '1', '0', '0'],
            "dig": ['0', '1', '1', '1', '0', '0'],
            "areset": ['0'] * 6
        }]
    })

    # Scenario 4: Splatter Condition
    scenarios.append({
        "scenario": "SplatterCondition",
        "input variable": [{
            "clock cycles": 25,
            "bump_left": ['0'] * 25,
            "bump_right": ['0'] * 25,
            "ground": ['1'] + ['0'] * 21 + ['1', '1', '1'],
            "dig": ['0'] * 25,
            "areset": ['0'] * 25
        }]
    })

    # Scenario 5: Fall Priority Over Dig
    scenarios.append({
        "scenario": "FallPriorityOverDig",
        "input variable": [{
            "clock cycles": 5,
            "bump_left": ['0'] * 5,
            "bump_right": ['0'] * 5,
            "ground": ['1', '0', '0', '0', '1'],
            "dig": ['0', '1', '1', '1', '0'],
            "areset": ['0'] * 5
        }]
    })

    # Scenario 6: Dig Priority Over Direction Change
    scenarios.append({
        "scenario": "DigPriorityOverDirectionChange",
        "input variable": [{
            "clock cycles": 6,
            "bump_left": ['0', '1', '1', '0', '0', '0'],
            "bump_right": ['0', '0', '1', '1', '0', '0'],
            "ground": ['1', '1', '1', '1', '0', '0'],
            "dig": ['0', '1', '1', '1', '0', '0'],
            "areset": ['0'] * 6
        }]
    })

    # Scenario 7: Asynchronous Reset Operation
    scenarios.append({
        "scenario": "AsynchronousResetOperation",
        "input variable": [{
            "clock cycles": 5,
            "bump_left": ['0', '0', '0', '0', '0'],
            "bump_right": ['0', '0', '0', '0', '0'],
            "ground": ['1', '1', '1', '1', '1'],
            "dig": ['0', '0', '0', '0', '0'],
            "areset": ['0', '1', '0', '0', '0']
        }]
    })

    # Scenario 8: Bump While Falling Immunity
    scenarios.append({
        "scenario": "BumpWhileFallingImmunity",
        "input variable": [{
            "clock cycles": 8,
            "bump_left": ['0', '0', '1', '0', '0', '0', '0', '0'],
            "bump_right": ['0', '0', '0', '1', '0', '0', '0', '0'],
            "ground": ['1', '0', '0', '0', '0', '1', '1', '1'],
            "dig": ['0'] * 8,
            "areset": ['0'] * 8
        }]
    })

    # Scenario 9: Maximum Fall Duration
    scenarios.append({
        "scenario": "MaximumFallDuration",
        "input variable": [{
            "clock cycles": 30,
            "bump_left": ['0'] * 30,
            "bump_right": ['0'] * 30,
            "ground": ['1'] + ['0'] * 18 + ['1'] + ['1'] * 10,
            "dig": ['0'] * 30,
            "areset": ['0'] * 30
        }]
    })

    # Scenario 10: Simultaneous Bumps
    scenarios.append({
        "scenario": "SimultaneousBumps",
        "input variable": [{
            "clock cycles": 5,
            "bump_left": ['0', '1', '0', '1', '0'],
            "bump_right": ['0', '1', '0', '1', '0'],
            "ground": ['1', '1', '1', '1', '1'],
            "dig": ['0'] * 5,
            "areset": ['0'] * 5
        }]
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
