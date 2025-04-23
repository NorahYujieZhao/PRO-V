import json
import random

def gen_walking_one(pos, width=100):
    return format(1 << pos, f'0{width}b')

def stimulus_gen():
    scenarios = []
    
    # Basic Load Operation
    scenarios.append({
        "scenario": "BasicLoadOperation",
        "input variable": [{
            "clock cycles": 2,
            "load": ["1", "0"],
            "ena": ["00", "00"],
            "data": [format(random.getrandbits(100), '0100b'), format(0, '0100b')]
        }]
    })

    # Right Rotation Operation
    scenarios.append({
        "scenario": "RightRotationOperation",
        "input variable": [{
            "clock cycles": 4,
            "load": ["1", "0", "0", "0"],
            "ena": ["00", "01", "01", "01"],
            "data": [gen_walking_one(98), gen_walking_one(98), gen_walking_one(98), gen_walking_one(98)]
        }]
    })

    # Left Rotation Operation
    scenarios.append({
        "scenario": "LeftRotationOperation",
        "input variable": [{
            "clock cycles": 4,
            "load": ["1", "0", "0", "0"],
            "ena": ["00", "10", "10", "10"],
            "data": [gen_walking_one(1), gen_walking_one(1), gen_walking_one(1), gen_walking_one(1)]
        }]
    })

    # Multiple Right Rotations
    scenarios.append({
        "scenario": "MultipleRightRotations",
        "input variable": [{
            "clock cycles": 102,
            "load": ["1"] + ["0"]*101,
            "ena": ["00"] + ["01"]*101,
            "data": [gen_walking_one(0)] + [gen_walking_one(0)]*101
        }]
    })

    # Multiple Left Rotations
    scenarios.append({
        "scenario": "MultipleLeftRotations",
        "input variable": [{
            "clock cycles": 102,
            "load": ["1"] + ["0"]*101,
            "ena": ["00"] + ["10"]*101,
            "data": [gen_walking_one(0)] + [gen_walking_one(0)]*101
        }]
    })

    # Hold Current Value
    scenarios.append({
        "scenario": "HoldCurrentValue",
        "input variable": [{
            "clock cycles": 5,
            "load": ["1", "0", "0", "0", "0"],
            "ena": ["00", "00", "11", "00", "11"],
            "data": [gen_walking_one(50)]*5
        }]
    })

    # Load During Rotation
    scenarios.append({
        "scenario": "LoadDuringRotation",
        "input variable": [{
            "clock cycles": 5,
            "load": ["1", "0", "0", "1", "0"],
            "ena": ["00", "01", "01", "01", "01"],
            "data": [gen_walking_one(0), gen_walking_one(0), gen_walking_one(0), gen_walking_one(50), gen_walking_one(50)]
        }]
    })

    # Alternating Direction
    scenarios.append({
        "scenario": "AlternatingDirection",
        "input variable": [{
            "clock cycles": 6,
            "load": ["1", "0", "0", "0", "0", "0"],
            "ena": ["00", "01", "10", "01", "10", "01"],
            "data": [gen_walking_one(50)]*6
        }]
    })

    # All Ones Pattern
    scenarios.append({
        "scenario": "AllOnesPattern",
        "input variable": [{
            "clock cycles": 4,
            "load": ["1", "0", "0", "0"],
            "ena": ["00", "01", "10", "01"],
            "data": ["1"*100]*4
        }]
    })

    # All Zeros Pattern
    scenarios.append({
        "scenario": "AllZerosPattern",
        "input variable": [{
            "clock cycles": 4,
            "load": ["1", "0", "0", "0"],
            "ena": ["00", "01", "10", "01"],
            "data": ["0"*100]*4
        }]
    })

    # Walking One Pattern
    scenarios.append({
        "scenario": "WalkingOnePattern",
        "input variable": [{
            "clock cycles": 5,
            "load": ["1", "0", "0", "0", "0"],
            "ena": ["00", "01", "01", "01", "01"],
            "data": [gen_walking_one(0)]*5
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
