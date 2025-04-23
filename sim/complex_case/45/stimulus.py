import json


def stimulus_gen():
    scenarios = []

    # Helper function to convert decimal to 4-bit binary string
    def dec_to_bin(dec):
        return format(dec, "04b")

    # Scenario 1: Logic 1 Output Cases
    logic1_inputs = [2, 7, 15]  # Valid inputs for logic-1 output
    scenario1 = {"scenario": "Logic 1 Output Cases", "input variable": []}
    for val in logic1_inputs:
        bin_val = dec_to_bin(val)
        scenario1["input variable"].append(
            {"a": bin_val[0], "b": bin_val[1], "c": bin_val[2], "d": bin_val[3]}
        )
    scenarios.append(scenario1)

    # Scenario 2: Logic 0 Output Cases
    logic0_inputs = [0, 1, 4, 5, 6, 9, 10, 13, 14]  # Valid inputs for logic-0 output
    scenario2 = {"scenario": "Logic 0 Output Cases", "input variable": []}
    for val in logic0_inputs:
        bin_val = dec_to_bin(val)
        scenario2["input variable"].append(
            {"a": bin_val[0], "b": bin_val[1], "c": bin_val[2], "d": bin_val[3]}
        )
    scenarios.append(scenario2)

    # Scenario 3: Output Equivalence
    all_valid_inputs = logic0_inputs + logic1_inputs
    scenario3 = {"scenario": "Output Equivalence", "input variable": []}
    for val in all_valid_inputs:
        bin_val = dec_to_bin(val)
        scenario3["input variable"].append(
            {"a": bin_val[0], "b": bin_val[1], "c": bin_val[2], "d": bin_val[3]}
        )
    scenarios.append(scenario3)

    # Scenario 4: Transition Coverage
    transitions = [(0, 2), (2, 0), (7, 14), (14, 15), (15, 1)]  # Example transitions
    scenario4 = {"scenario": "Transition Coverage", "input variable": []}
    for from_val, to_val in transitions:
        for val in [from_val, to_val]:
            bin_val = dec_to_bin(val)
            scenario4["input variable"].append(
                {"a": bin_val[0], "b": bin_val[1], "c": bin_val[2], "d": bin_val[3]}
            )
    scenarios.append(scenario4)

    # Scenario 5: Glitch Detection
    glitch_test = [(2, 7), (7, 15), (15, 2)]  # Test transitions between logic-1 outputs
    scenario5 = {"scenario": "Glitch Detection", "input variable": []}
    for from_val, to_val in glitch_test:
        for val in [from_val, to_val]:
            bin_val = dec_to_bin(val)
            scenario5["input variable"].append(
                {"a": bin_val[0], "b": bin_val[1], "c": bin_val[2], "d": bin_val[3]}
            )
    scenarios.append(scenario5)

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
