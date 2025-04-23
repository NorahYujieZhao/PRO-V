import json


def stimulus_gen():
    scenarios = []

    # Helper function to format binary strings
    def format_bin(val, width):
        return format(val, f"0{width}b")

    # Scenario 1: All Zero Inputs
    scenarios.append(
        {"scenario": "All Zero Inputs", "input variable": [{"c": "0", "d": "0"}]}
    )

    # Scenario 2: C Only High
    scenarios.append(
        {"scenario": "C Only High", "input variable": [{"c": "1", "d": "0"}]}
    )

    # Scenario 3: D Only High
    scenarios.append(
        {"scenario": "D Only High", "input variable": [{"c": "0", "d": "1"}]}
    )

    # Scenario 4: Both Inputs High
    scenarios.append(
        {"scenario": "Both Inputs High", "input variable": [{"c": "1", "d": "1"}]}
    )

    # Scenario 5: Input Transitions
    transition_sequence = [
        {"c": "0", "d": "0"},
        {"c": "0", "d": "1"},
        {"c": "1", "d": "1"},
        {"c": "1", "d": "0"},
    ]
    scenarios.append(
        {"scenario": "Input Transitions", "input variable": transition_sequence}
    )

    # Scenario 6: Setup Time Verification
    setup_sequence = [{"c": "0", "d": "0"}, {"c": "1", "d": "0"}, {"c": "1", "d": "1"}]
    scenarios.append(
        {"scenario": "Setup Time Verification", "input variable": setup_sequence}
    )

    # Scenario 7: Hold Time Verification
    hold_sequence = [{"c": "1", "d": "1"}, {"c": "0", "d": "1"}, {"c": "0", "d": "0"}]
    scenarios.append(
        {"scenario": "Hold Time Verification", "input variable": hold_sequence}
    )

    # Scenario 8: Glitch Detection
    glitch_sequence = [
        {"c": "0", "d": "0"},
        {"c": "1", "d": "0"},
        {"c": "1", "d": "1"},
        {"c": "0", "d": "1"},
        {"c": "0", "d": "0"},
    ]
    scenarios.append(
        {"scenario": "Glitch Detection", "input variable": glitch_sequence}
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
