import json


def stimulus_gen():
    scenarios = []

    # Helper function to format binary strings
    def format_100bit(value):
        return format(value, "0100b")

    # Scenario 1: All Zeros
    scenarios.append(
        {"scenario": "All Zeros Input", "input variable": [{"in": "0" * 100}]}
    )

    # Scenario 2: All Ones
    scenarios.append(
        {"scenario": "All Ones Input", "input variable": [{"in": "1" * 100}]}
    )

    # Scenario 3: Alternating Bits
    alt_pattern = "".join(["10"] * 50)
    scenarios.append(
        {"scenario": "Alternating Bits", "input variable": [{"in": alt_pattern}]}
    )

    # Scenario 4: Single Bit High
    single_high = "0" * 50 + "1" + "0" * 49
    scenarios.append(
        {"scenario": "Single Bit High", "input variable": [{"in": single_high}]}
    )

    # Scenario 5: Edge Bit Verification
    edge_pattern = "1" + "0" * 98 + "1"
    scenarios.append(
        {"scenario": "Edge Bit Verification", "input variable": [{"in": edge_pattern}]}
    )

    # Scenario 6: Random Pattern
    import random

    random.seed(42)  # For reproducibility
    rand_pattern = "".join([str(random.randint(0, 1)) for _ in range(100)])
    scenarios.append(
        {"scenario": "Random Pattern", "input variable": [{"in": rand_pattern}]}
    )

    # Scenario 7: Walking Ones
    walking_ones = []
    base = "0" * 100
    for i in range(100):
        pattern = list(base)
        pattern[i] = "1"
        walking_ones.append({"in": "".join(pattern)})
    scenarios.append({"scenario": "Walking Ones", "input variable": walking_ones})

    # Scenario 8: Walking Zeros
    walking_zeros = []
    base = "1" * 100
    for i in range(100):
        pattern = list(base)
        pattern[i] = "0"
        walking_zeros.append({"in": "".join(pattern)})
    scenarios.append({"scenario": "Walking Zeros", "input variable": walking_zeros})

    # Scenario 9: Adjacent Pairs
    adjacent_pairs = []
    base = "0" * 100
    for i in range(99):
        pattern = list(base)
        pattern[i] = "1"
        pattern[i + 1] = "1"
        adjacent_pairs.append({"in": "".join(pattern)})
    scenarios.append({"scenario": "Adjacent Pairs", "input variable": adjacent_pairs})

    # Scenario 10: Wraparound Check
    wraparound_patterns = [
        "1" + "0" * 98 + "1",  # Test bits 99 and 0
        "1" + "0" * 97 + "11",  # Test bits 98, 99 and 0
        "11" + "0" * 97 + "1",  # Test bits 99, 0 and 1
    ]
    scenarios.append(
        {
            "scenario": "Wraparound Check",
            "input variable": [{"in": pattern} for pattern in wraparound_patterns],
        }
    )

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
