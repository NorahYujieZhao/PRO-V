import json
def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Basic Pattern Detection
    scenarios.append({
        "scenario": "BasicPatternDetection",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 2: Shift Enable Duration
    scenarios.append({
        "scenario": "ShiftEnableDuration",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "1", "0", "1", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 3: Counting State Operation
    scenarios.append({
        "scenario": "CountingStateOperation",
        "input variable": [{
            "clock cycles": 12,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 4: Timer Completion
    scenarios.append({
        "scenario": "TimerCompletion",
        "input variable": [{
            "clock cycles": 12,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1"]
        }]
    })
    
    # Scenario 5: Synchronous Reset
    scenarios.append({
        "scenario": "SynchronousReset",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["1", "0", "0", "0", "0", "1", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 6: Partial Pattern Reset
    scenarios.append({
        "scenario": "PartialPatternReset",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["1", "0", "0", "0", "1", "0"],
            "data": ["0", "1", "1", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0"],
            "ack": ["0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 7: Pattern Overlap
    scenarios.append({
        "scenario": "PatternOverlap",
        "input variable": [{
            "clock cycles": 10,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "1", "1", "0", "1", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        }]
    })
    
    # Scenario 8: Quick Acknowledgment
    scenarios.append({
        "scenario": "QuickAcknowledgment",
        "input variable": [{
            "clock cycles": 12,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"]
        }]
    })
    
    # Scenario 9: Delayed Acknowledgment
    scenarios.append({
        "scenario": "DelayedAcknowledgment",
        "input variable": [{
            "clock cycles": 15,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1"]
        }]
    })
    
    # Scenario 10: Invalid Pattern Recovery
    scenarios.append({
        "scenario": "InvalidPatternRecovery",
        "input variable": [{
            "clock cycles": 12,
            "reset": ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "0", "0"],
            "done_counting": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            "ack": ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
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
