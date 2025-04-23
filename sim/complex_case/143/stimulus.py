import json


def generate_binary_string(value, width=4):
    return format(value, f"0{width}b")


def get_true_cases():
    return [0b0000, 0b0010, 0b1000, 0b1010, 0b1100, 0b1101, 0b1110, 0b1111]


def get_false_cases():
    return [0b0001, 0b0100, 0b0101, 0b0110, 0b0111, 0b1011]


def generate_transitions():
    transitions = []
    # Adjacent transitions in K-map
    transition_pairs = [
        (0b0000, 0b0001),
        (0b0010, 0b0011),
        (0b1000, 0b1001),
        (0b1100, 0b1101),
    ]
    for start, end in transition_pairs:
        transitions.extend([start, end])
    return transitions


def stimulus_gen():
    scenarios = []

    # Scenario 1: All Zero Input
    scenarios.append(
        {
            "scenario": "All Zero Input",
            "input variable": [{"x": generate_binary_string(0)}],
        }
    )

    # Scenario 2: All One Input
    scenarios.append(
        {
            "scenario": "All One Input",
            "input variable": [{"x": generate_binary_string(15)}],
        }
    )

    # Scenario 3: K Map True Cases
    true_cases = get_true_cases()
    scenarios.append(
        {
            "scenario": "K Map True Cases",
            "input variable": [
                {"x": generate_binary_string(val)} for val in true_cases
            ],
        }
    )

    # Scenario 4: K Map False Cases
    false_cases = get_false_cases()
    scenarios.append(
        {
            "scenario": "K Map False Cases",
            "input variable": [
                {"x": generate_binary_string(val)} for val in false_cases
            ],
        }
    )

    # Scenario 5: Input Transitions
    transitions = generate_transitions()
    scenarios.append(
        {
            "scenario": "Input Transitions",
            "input variable": [
                {"x": generate_binary_string(val)} for val in transitions
            ],
        }
    )

    # Scenario 6: Random Combinations
    import random

    random_inputs = [random.randint(0, 15) for _ in range(5)]
    scenarios.append(
        {
            "scenario": "Random Combinations",
            "input variable": [
                {"x": generate_binary_string(val)} for val in random_inputs
            ],
        }
    )

    # Scenario 7: Fast Input Changes
    fast_changes = [0b0000, 0b1111, 0b0101, 0b1010]
    scenarios.append(
        {
            "scenario": "Fast Input Changes",
            "input variable": [
                {"x": generate_binary_string(val)} for val in fast_changes
            ],
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
