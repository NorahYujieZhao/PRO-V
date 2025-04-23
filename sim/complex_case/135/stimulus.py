import json


def stimulus_gen():
    scenarios = []

    # Helper function to create binary strings
    def bin_str(val, width=1):
        return format(val, f"0{width}b")

    # Scenario 1: All Zeros Input Test
    scenarios.append(
        {
            "scenario": "All Zeros Input Test",
            "input variable": [{"a": "0", "b": "0", "c": "0", "d": "0"}],
        }
    )

    # Scenario 2: Single Input High Test
    single_high = {
        "scenario": "Single Input High Test",
        "input variable": [
            {"a": "1", "b": "0", "c": "0", "d": "0"},
            {"a": "0", "b": "1", "c": "0", "d": "0"},
            {"a": "0", "b": "0", "c": "1", "d": "0"},
            {"a": "0", "b": "0", "c": "0", "d": "1"},
        ],
    }
    scenarios.append(single_high)

    # Scenario 3: Two Inputs High Test
    two_high = {
        "scenario": "Two Inputs High Test",
        "input variable": [
            {"a": "1", "b": "1", "c": "0", "d": "0"},
            {"a": "1", "b": "0", "c": "1", "d": "0"},
            {"a": "1", "b": "0", "c": "0", "d": "1"},
            {"a": "0", "b": "1", "c": "1", "d": "0"},
            {"a": "0", "b": "1", "c": "0", "d": "1"},
            {"a": "0", "b": "0", "c": "1", "d": "1"},
        ],
    }
    scenarios.append(two_high)

    # Scenario 4: Three Inputs High Test
    three_high = {
        "scenario": "Three Inputs High Test",
        "input variable": [
            {"a": "1", "b": "1", "c": "1", "d": "0"},
            {"a": "1", "b": "1", "c": "0", "d": "1"},
            {"a": "1", "b": "0", "c": "1", "d": "1"},
            {"a": "0", "b": "1", "c": "1", "d": "1"},
        ],
    }
    scenarios.append(three_high)

    # Scenario 5: All Ones Input Test
    scenarios.append(
        {
            "scenario": "All Ones Input Test",
            "input variable": [{"a": "1", "b": "1", "c": "1", "d": "1"}],
        }
    )

    # Scenario 6: Input Transition Coverage
    transitions = {
        "scenario": "Input Transition Coverage",
        "input variable": [
            {"a": "0", "b": "0", "c": "0", "d": "0"},
            {"a": "0", "b": "0", "c": "0", "d": "1"},
            {"a": "0", "b": "0", "c": "1", "d": "0"},
            {"a": "0", "b": "0", "c": "1", "d": "1"},
            {"a": "0", "b": "1", "c": "0", "d": "0"},
        ],
    }
    scenarios.append(transitions)

    # Scenario 7: Output Pattern Verification
    output_pattern = {
        "scenario": "Output Pattern Verification",
        "input variable": [
            {
                "a": bin_str(i >> 3),
                "b": bin_str((i >> 2) & 1),
                "c": bin_str((i >> 1) & 1),
                "d": bin_str(i & 1),
            }
            for i in range(16)
        ],
    }
    scenarios.append(output_pattern)

    # Scenario 8: Propagation Delay Check
    prop_delay = {
        "scenario": "Propagation Delay Check",
        "input variable": [
            {"a": "0", "b": "0", "c": "0", "d": "0"},
            {"a": "1", "b": "1", "c": "1", "d": "1"},
            {"a": "0", "b": "0", "c": "0", "d": "0"},
            {"a": "1", "b": "0", "c": "1", "d": "0"},
        ],
    }
    scenarios.append(prop_delay)

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
