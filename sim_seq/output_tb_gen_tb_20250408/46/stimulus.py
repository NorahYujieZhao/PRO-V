import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create binary sequences
    def create_sequence(reset_pattern, cycles):
        return {
            "clock cycles": cycles,
            "reset": reset_pattern
        }
    
    # Scenario 1: Synchronous Reset Verification
    scenarios.append({
        "scenario": "SynchronousResetVerification",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0"], 5)
        ]
    })
    
    # Scenario 2: Basic Shift Operation
    scenarios.append({
        "scenario": "BasicShiftOperation",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0"], 20)
        ]
    })
    
    # Scenario 3: Multiple Reset Cycles
    scenarios.append({
        "scenario": "MultipleResetCycles",
        "input variable": [
            create_sequence(["1", "0", "0", "1", "0", "0", "1", "0"], 8)
        ]
    })
    
    # Scenario 4: Tap Position Verification
    scenarios.append({
        "scenario": "TapPositionVerification",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0"], 32)
        ]
    })
    
    # Scenario 5: Full Sequence Generation
    scenarios.append({
        "scenario": "FullSequenceGeneration",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0"], 100)
        ]
    })
    
    # Scenario 6: Clock Edge Sensitivity
    scenarios.append({
        "scenario": "ClockEdgeSensitivity",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0"], 10)
        ]
    })
    
    # Scenario 7: Reset During Operation
    scenarios.append({
        "scenario": "ResetDuringOperation",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0", "0", "0", "0", "1", "0"], 6)
        ]
    })
    
    # Scenario 8: Maximum Sequence Length
    scenarios.append({
        "scenario": "MaximumSequenceLength",
        "input variable": [
            create_sequence(["1"], 1),
            create_sequence(["0"], 1000)
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
