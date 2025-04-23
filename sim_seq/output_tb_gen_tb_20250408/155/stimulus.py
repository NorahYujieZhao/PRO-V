
import json
import random
def stimulus_gen():
    stim_list = []

    # Basic walking and bumping
    stim_list.append({
        "scenario": "BasicWalkingAndBumping",
        "input variable": [{
            "clock cycles": 20,
            "areset": ["0"]*20,
            "bump_left": ["0","1","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","0","0"],
            "bump_right": ["0","0","0","1","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0"],
            "ground": ["1"]*20
        }]
    })

    # Falling sequence
    stim_list.append({
        "scenario": "FallingBehavior",
        "input variable": [{
            "clock cycles": 15,
            "areset": ["0"]*15,
            "bump_left": ["0"]*15,
            "bump_right": ["0"]*15,
            "ground": ["1","1","0","0","0","0","1","1","1","0","0","0","1","1","1"]
        }]
    })

    # Reset behavior
    stim_list.append({
        "scenario": "ResetBehavior",
        "input variable": [{
            "clock cycles": 12,
            "areset": ["1","0","0","0","1","0","0","0","0","1","0","0"],
            "bump_left": ["0"]*12,
            "bump_right": ["0"]*12,
            "ground": ["1"]*12
        }]
    })

    # Bumping while falling
    stim_list.append({
        "scenario": "BumpingWhileFalling",
        "input variable": [{
            "clock cycles": 16,
            "areset": ["0"]*16,
            "bump_left": ["0","0","1","0","1","0","0","0","0","1","0","0","0","0","0","0"],
            "bump_right": ["0","0","0","1","0","1","0","0","0","0","1","0","0","0","0","0"],
            "ground": ["1","1","0","0","0","0","0","1","1","1","0","0","0","1","1","1"]
        }]
    })

    # Both sides bumping
    stim_list.append({
        "scenario": "BothSidesBumping",
        "input variable": [{
            "clock cycles": 10,
            "areset": ["0"]*10,
            "bump_left": ["0","1","0","1","1","0","0","1","0","0"],
            "bump_right": ["0","0","1","1","1","0","1","0","0","0"],
            "ground": ["1"]*10
        }]
    })

    # Random test sequences
    import random
    for i in range(10):
        cycles = 20
        stim_list.append({
            "scenario": f"RandomTest{i}",
            "input variable": [{
                "clock cycles": cycles,
                "areset": [str(random.randint(0,1)) for _ in range(cycles)],
                "bump_left": [str(random.randint(0,1)) for _ in range(cycles)],
                "bump_right": [str(random.randint(0,1)) for _ in range(cycles)],
                "ground": [str(random.randint(0,1)) for _ in range(cycles)]
            }]
        })

    return stim_list
if __name__ == "__main__":
    result = stimulus_gen()
    # 将结果转换为 JSON 字符串
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
