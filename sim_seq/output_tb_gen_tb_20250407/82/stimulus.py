import json


def stimulus_gen():
    scenarios = []

    # Helper function to create scenario dictionary
    def create_scenario(name, inputs):
        return {
            "scenario": name,
            "input variable": [{"x": format(val, "04b")} for val in inputs],
        }

    # Scenario 1: Known Output Zero Cases
    zero_cases = create_scenario(
        "Known Output Zero Cases", [0b0001, 0b1001]
    )  # x=0001 and x=1001
    scenarios.append(zero_cases)

    # Scenario 2: Known Output One Cases
    one_cases = create_scenario(
        "Known Output One Cases", [0b1100, 0b1000]
    )  # x=1100 and x=1000
    scenarios.append(one_cases)

    # Scenario 3: Don't Care Values
    dont_care = create_scenario("Dont Care Values", [0b0000, 0b0011, 0b0010, 0b0110])
    scenarios.append(dont_care)

    # Scenario 4: Adjacent Cell Transitions
    adjacent = create_scenario(
        "Adjacent Cell Transitions", [0b0001, 0b0101, 0b1101, 0b1001]
    )
    scenarios.append(adjacent)

    # Scenario 5: Boundary Value Analysis
    boundary = create_scenario("Boundary Value Analysis", [0b0000, 0b1111])
    scenarios.append(boundary)

    # Scenario 6: Input Signal Timing
    timing = create_scenario(
        "Input Signal Timing", [0b0000, 0b0001, 0b0011, 0b0111, 0b1111]
    )
    scenarios.append(timing)

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
