import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create scenario dictionary
    def create_scenario(name, cycles, resetn_seq, r_seq):
        return {
            "scenario": name,
            "input variable": [
                {
                    "clock cycles": cycles,
                    "resetn": resetn_seq,
                    "r": r_seq
                }
            ]
        }
    
    # Initial Reset Behavior
    scenarios.append(create_scenario(
        "InitialResetBehavior",
        4,
        ["0", "0", "1", "1"],
        ["000", "000", "000", "000"]
    ))
    
    # No Requests Idle State
    scenarios.append(create_scenario(
        "NoRequestsIdleState",
        4,
        ["1", "1", "1", "1"],
        ["000", "000", "000", "000"]
    ))
    
    # Single Request Device 1
    scenarios.append(create_scenario(
        "SingleRequestDevice1",
        4,
        ["1", "1", "1", "1"],
        ["000", "100", "100", "100"]
    ))
    
    # Single Request Device 2
    scenarios.append(create_scenario(
        "SingleRequestDevice2",
        4,
        ["1", "1", "1", "1"],
        ["000", "010", "010", "010"]
    ))
    
    # Single Request Device 3
    scenarios.append(create_scenario(
        "SingleRequestDevice3",
        4,
        ["1", "1", "1", "1"],
        ["000", "001", "001", "001"]
    ))
    
    # Priority Check Device 1 Over 2
    scenarios.append(create_scenario(
        "PriorityCheckDevice1Over2",
        4,
        ["1", "1", "1", "1"],
        ["000", "110", "110", "110"]
    ))
    
    # Priority Check Device 1 Over 3
    scenarios.append(create_scenario(
        "PriorityCheckDevice1Over3",
        4,
        ["1", "1", "1", "1"],
        ["000", "101", "101", "101"]
    ))
    
    # Priority Check Device 2 Over 3
    scenarios.append(create_scenario(
        "PriorityCheckDevice2Over3",
        4,
        ["1", "1", "1", "1"],
        ["000", "011", "011", "011"]
    ))
    
    # All Requests Active
    scenarios.append(create_scenario(
        "AllRequestsActive",
        4,
        ["1", "1", "1", "1"],
        ["000", "111", "111", "111"]
    ))
    
    # Grant Persistence Device 1
    scenarios.append(create_scenario(
        "GrantPersistenceDevice1",
        6,
        ["1", "1", "1", "1", "1", "1"],
        ["000", "100", "100", "100", "100", "100"]
    ))
    
    # Grant Persistence Device 2
    scenarios.append(create_scenario(
        "GrantPersistenceDevice2",
        6,
        ["1", "1", "1", "1", "1", "1"],
        ["000", "010", "010", "010", "010", "010"]
    ))
    
    # Release Grant Device 1
    scenarios.append(create_scenario(
        "ReleaseGrantDevice1",
        5,
        ["1", "1", "1", "1", "1"],
        ["000", "100", "100", "000", "000"]
    ))
    
    # Release Grant Device 2
    scenarios.append(create_scenario(
        "ReleaseGrantDevice2",
        5,
        ["1", "1", "1", "1", "1"],
        ["000", "010", "010", "000", "000"]
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
