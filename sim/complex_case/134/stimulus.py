import json
import random


def format_5bit(value):
    return format(value, "05b")


def stimulus_gen():
    scenarios = []

    # Scenario 1: All Zeros Input
    scenarios.append(
        {
            "scenario": "All Zeros Input",
            "input variable": [
                {
                    "a": "00000",
                    "b": "00000",
                    "c": "00000",
                    "d": "00000",
                    "e": "00000",
                    "f": "00000",
                }
            ],
        }
    )

    # Scenario 2: All Ones Input
    scenarios.append(
        {
            "scenario": "All Ones Input",
            "input variable": [
                {
                    "a": "11111",
                    "b": "11111",
                    "c": "11111",
                    "d": "11111",
                    "e": "11111",
                    "f": "11111",
                }
            ],
        }
    )

    # Scenario 3: Alternating Pattern
    scenarios.append(
        {
            "scenario": "Alternating Pattern",
            "input variable": [
                {
                    "a": "11111",
                    "b": "00000",
                    "c": "11111",
                    "d": "00000",
                    "e": "11111",
                    "f": "00000",
                }
            ],
        }
    )

    # Scenario 4: Walking Ones
    walking_ones = []
    for i in range(30):
        pos = i // 5
        val = 1 << (4 - (i % 5))
        inputs = {
            "a": "00000",
            "b": "00000",
            "c": "00000",
            "d": "00000",
            "e": "00000",
            "f": "00000",
        }
        inputs[list(inputs.keys())[pos]] = format_5bit(val)
        walking_ones.append(inputs)

    scenarios.append({"scenario": "Walking Ones", "input variable": walking_ones})

    # Scenario 5: Random Values
    scenarios.append(
        {
            "scenario": "Random Values",
            "input variable": [
                {
                    "a": format_5bit(random.randint(0, 31)),
                    "b": format_5bit(random.randint(0, 31)),
                    "c": format_5bit(random.randint(0, 31)),
                    "d": format_5bit(random.randint(0, 31)),
                    "e": format_5bit(random.randint(0, 31)),
                    "f": format_5bit(random.randint(0, 31)),
                }
            ],
        }
    )

    # Scenario 6: Verify LSB Bits
    scenarios.append(
        {
            "scenario": "Verify LSB Bits",
            "input variable": [
                {
                    "a": "10101",
                    "b": "01010",
                    "c": "11000",
                    "d": "00111",
                    "e": "10101",
                    "f": "01010",
                }
            ],
        }
    )

    # Scenario 7: Boundary Check
    scenarios.append(
        {
            "scenario": "Boundary Check",
            "input variable": [
                {
                    "a": "11111",
                    "b": "00000",
                    "c": "11111",
                    "d": "00000",
                    "e": "11111",
                    "f": "00000",
                }
            ],
        }
    )

    # Scenario 8: Output Segment Verification
    scenarios.append(
        {
            "scenario": "Output Segment Verification",
            "input variable": [
                {
                    "a": "10101",
                    "b": "01010",
                    "c": "11001",
                    "d": "00110",
                    "e": "11100",
                    "f": "00011",
                }
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
