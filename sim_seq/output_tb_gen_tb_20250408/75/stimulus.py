import json
def stimulus_gen():
    scenarios = []
    
    # Basic Pattern Detection
    scenarios.append({
        "scenario": "BasicPatternDetection",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["0", "0", "0", "0"],
            "data": ["1", "1", "0", "1"]
        }]
    })
    
    # Pattern Within Longer Sequence
    scenarios.append({
        "scenario": "PatternWithinLongerSequence",
        "input variable": [{
            "clock cycles": 7,
            "reset": ["0", "0", "0", "0", "0", "0", "0"],
            "data": ["0", "0", "1", "1", "1", "0", "1"]
        }]
    })
    
    # Multiple Pattern Occurrences
    scenarios.append({
        "scenario": "MultiplePatternOccurrences",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["1", "1", "0", "1", "1", "1", "0", "1"]
        }]
    })
    
    # Reset During Pattern
    scenarios.append({
        "scenario": "ResetDuringPattern",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["0", "0", "1", "0", "0", "0"],
            "data": ["1", "1", "0", "1", "1", "0"]
        }]
    })
    
    # Reset After Detection
    scenarios.append({
        "scenario": "ResetAfterDetection",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["0", "0", "0", "0", "1", "0"],
            "data": ["1", "1", "0", "1", "0", "0"]
        }]
    })
    
    # Partial Pattern Recovery
    scenarios.append({
        "scenario": "PartialPatternRecovery",
        "input variable": [{
            "clock cycles": 6,
            "reset": ["0", "0", "0", "0", "0", "0"],
            "data": ["1", "1", "0", "0", "1", "1"]
        }]
    })
    
    # Overlapping Patterns
    scenarios.append({
        "scenario": "OverlappingPatterns",
        "input variable": [{
            "clock cycles": 8,
            "reset": ["0", "0", "0", "0", "0", "0", "0", "0"],
            "data": ["1", "1", "0", "1", "1", "1", "0", "1"]
        }]
    })
    
    # Initial Reset State
    scenarios.append({
        "scenario": "InitialResetState",
        "input variable": [{
            "clock cycles": 4,
            "reset": ["1", "0", "0", "0"],
            "data": ["0", "0", "0", "0"]
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
