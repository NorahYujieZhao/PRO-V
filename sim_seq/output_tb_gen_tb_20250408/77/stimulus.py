import json
def stimulus_gen():
    # Helper function to format binary strings
    def format_bin(num, width=8):
        return format(num, f'0{width}b')

    scenarios = []

    # Scenario 1: Single Bit Rising Edge
    single_rising = {
        "scenario": "SingleBitRisingEdge",
        "input variable": [
            {
                "clock cycles": 8,
                "in": [format_bin(0), format_bin(1), format_bin(0), format_bin(2),
                      format_bin(0), format_bin(4), format_bin(0), format_bin(8)]
            }
        ]
    }
    scenarios.append(single_rising)

    # Scenario 2: Single Bit Falling Edge
    single_falling = {
        "scenario": "SingleBitFallingEdge",
        "input variable": [
            {
                "clock cycles": 8,
                "in": [format_bin(255), format_bin(254), format_bin(255),
                      format_bin(253), format_bin(255), format_bin(251),
                      format_bin(255), format_bin(247)]
            }
        ]
    }
    scenarios.append(single_falling)

    # Scenario 3: Multiple Simultaneous Edges
    multiple_edges = {
        "scenario": "MultipleSimultaneousEdges",
        "input variable": [
            {
                "clock cycles": 4,
                "in": [format_bin(0), format_bin(153), format_bin(102),
                      format_bin(255)]
            }
        ]
    }
    scenarios.append(multiple_edges)

    # Scenario 4: Consecutive Transitions
    consecutive = {
        "scenario": "ConsecutiveTransitions",
        "input variable": [
            {
                "clock cycles": 6,
                "in": [format_bin(0), format_bin(255), format_bin(0),
                      format_bin(255), format_bin(0), format_bin(255)]
            }
        ]
    }
    scenarios.append(consecutive)

    # Scenario 5: Alternating Bit Patterns
    alternating = {
        "scenario": "AlternatingBitPatterns",
        "input variable": [
            {
                "clock cycles": 4,
                "in": [format_bin(170), format_bin(85), format_bin(170),
                      format_bin(85)]
            }
        ]
    }
    scenarios.append(alternating)

    # Scenario 6: Stable Input
    stable = {
        "scenario": "StableInput",
        "input variable": [
            {
                "clock cycles": 4,
                "in": [format_bin(170), format_bin(170), format_bin(170),
                      format_bin(170)]
            }
        ]
    }
    scenarios.append(stable)

    # Scenario 7: Walking Ones Pattern
    walking_ones = {
        "scenario": "WalkingOnesPattern",
        "input variable": [
            {
                "clock cycles": 8,
                "in": [format_bin(1), format_bin(2), format_bin(4),
                      format_bin(8), format_bin(16), format_bin(32),
                      format_bin(64), format_bin(128)]
            }
        ]
    }
    scenarios.append(walking_ones)

    # Scenario 8: Walking Zeros Pattern
    walking_zeros = {
        "scenario": "WalkingZerosPattern",
        "input variable": [
            {
                "clock cycles": 8,
                "in": [format_bin(254), format_bin(253), format_bin(251),
                      format_bin(247), format_bin(239), format_bin(223),
                      format_bin(191), format_bin(127)]
            }
        ]
    }
    scenarios.append(walking_zeros)

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
