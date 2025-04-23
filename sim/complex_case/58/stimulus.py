import json


def stimulus_gen():
    scenarios = []

    # Helper function to format binary values
    def bin_format(val):
        return format(val, "01b")

    # Scenario 1: Basic Input Combinations
    basic_inputs = {
        "scenario": "Basic Input Combinations",
        "input variable": [
            {"x": "0", "y": "0"},
            {"x": "0", "y": "1"},
            {"x": "1", "y": "0"},
            {"x": "1", "y": "1"},
        ],
    }
    scenarios.append(basic_inputs)

    # Scenario 2: Module B Timing Pattern
    timing_pattern = {
        "scenario": "Module B Timing Pattern",
        "input variable": [
            {"x": "0", "y": "0"},
            {"x": "1", "y": "0"},
            {"x": "0", "y": "1"},
            {"x": "1", "y": "1"},
            {"x": "0", "y": "0"},
            {"x": "0", "y": "1"},
            {"x": "1", "y": "1"},
            {"x": "0", "y": "1"},
            {"x": "1", "y": "0"},
        ],
    }
    scenarios.append(timing_pattern)

    # Scenario 3: Rapid Input Transitions
    rapid_transitions = {
        "scenario": "Rapid Input Transitions",
        "input variable": [
            {"x": "0", "y": "0"},
            {"x": "1", "y": "0"},
            {"x": "1", "y": "1"},
            {"x": "0", "y": "1"},
            {"x": "0", "y": "0"},
        ],
    }
    scenarios.append(rapid_transitions)

    # Scenario 4: Static Input Verification
    static_inputs = {
        "scenario": "Static Input Verification",
        "input variable": [
            {"x": "0", "y": "0"},
            {"x": "0", "y": "0"},
            {"x": "0", "y": "0"},
            {"x": "1", "y": "1"},
            {"x": "1", "y": "1"},
        ],
    }
    scenarios.append(static_inputs)

    # Scenario 5: OR Gate Path Verification
    or_path = {
        "scenario": "OR Gate Path Verification",
        "input variable": [
            {"x": "1", "y": "0"},
            {"x": "0", "y": "1"},
            {"x": "1", "y": "1"},
            {"x": "0", "y": "0"},
        ],
    }
    scenarios.append(or_path)

    # Scenario 6: AND Gate Path Verification
    and_path = {
        "scenario": "AND Gate Path Verification",
        "input variable": [
            {"x": "1", "y": "1"},
            {"x": "1", "y": "0"},
            {"x": "0", "y": "1"},
            {"x": "0", "y": "0"},
        ],
    }
    scenarios.append(and_path)

    # Scenario 7: XOR Output Validation
    xor_validation = {
        "scenario": "XOR Output Validation",
        "input variable": [
            {"x": "1", "y": "1"},
            {"x": "1", "y": "0"},
            {"x": "0", "y": "1"},
            {"x": "0", "y": "0"},
        ],
    }
    scenarios.append(xor_validation)

    # Scenario 8: Module A Function Verification
    module_a_verify = {
        "scenario": "Module A Function Verification",
        "input variable": [
            {"x": "0", "y": "0"},
            {"x": "1", "y": "0"},
            {"x": "1", "y": "1"},
            {"x": "0", "y": "1"},
        ],
    }
    scenarios.append(module_a_verify)

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
