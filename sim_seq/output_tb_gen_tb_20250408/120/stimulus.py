import json
def stimulus_gen():
    # Helper function to create a sequence dictionary
    def create_sequence(cycles, in_seq, resetn_seq):
        return {
            "clock cycles": cycles,
            "in": in_seq,
            "resetn": resetn_seq
        }
    
    scenarios = []
    
    # Scenario 1: Basic Shift Operation
    basic_shift = {
        "scenario": "BasicShiftOperation",
        "input variable": [
            create_sequence(8,
                ["1", "0", "1", "0", "1", "0", "1", "0"],
                ["1", "1", "1", "1", "1", "1", "1", "1"])
        ]
    }
    scenarios.append(basic_shift)
    
    # Scenario 2: Reset Operation
    reset_op = {
        "scenario": "ResetOperation",
        "input variable": [
            create_sequence(4,
                ["1", "1", "1", "1"],
                ["1", "1", "1", "1"]),
            create_sequence(2,
                ["1", "1"],
                ["0", "0"]),
            create_sequence(4,
                ["1", "1", "1", "1"],
                ["1", "1", "1", "1"])
        ]
    }
    scenarios.append(reset_op)
    
    # Scenario 3: Continuous Input Stream
    continuous_stream = {
        "scenario": "ContinuousInputStream",
        "input variable": [
            create_sequence(8,
                ["1", "1", "0", "0", "1", "1", "0", "0"],
                ["1", "1", "1", "1", "1", "1", "1", "1"])
        ]
    }
    scenarios.append(continuous_stream)
    
    # Scenario 4: Reset Release
    reset_release = {
        "scenario": "ResetRelease",
        "input variable": [
            create_sequence(2,
                ["0", "0"],
                ["0", "0"]),
            create_sequence(6,
                ["1", "0", "1", "0", "1", "0"],
                ["1", "1", "1", "1", "1", "1"])
        ]
    }
    scenarios.append(reset_release)
    
    # Scenario 5: Setup Time Verification
    setup_time = {
        "scenario": "SetupTimeVerification",
        "input variable": [
            create_sequence(6,
                ["0", "1", "0", "1", "0", "1"],
                ["1", "1", "1", "1", "1", "1"])
        ]
    }
    scenarios.append(setup_time)
    
    # Scenario 6: Hold Time Verification
    hold_time = {
        "scenario": "HoldTimeVerification",
        "input variable": [
            create_sequence(6,
                ["1", "0", "1", "0", "1", "0"],
                ["1", "1", "1", "1", "1", "1"])
        ]
    }
    scenarios.append(hold_time)
    
    # Scenario 7: Clock Edge Response
    clock_edge = {
        "scenario": "ClockEdgeResponse",
        "input variable": [
            create_sequence(8,
                ["0", "1", "1", "0", "0", "1", "1", "0"],
                ["1", "1", "1", "1", "1", "1", "1", "1"])
        ]
    }
    scenarios.append(clock_edge)
    
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
