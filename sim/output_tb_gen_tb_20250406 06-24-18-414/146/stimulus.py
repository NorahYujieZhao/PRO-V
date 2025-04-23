import json

from cocotb.binary import BinaryValue


def create_sensor_input(s1, s2, s3):
    return f"{s3}{s2}{s1}"


def stimulus_gen():
    scenarios = []

    # Initial Power Up State
    scenarios.append(
        {
            "scenario": "Initial Power Up State",
            "input variable": [{"reset": "0", "s": "000"}, {"reset": "0", "s": "000"}],
        }
    )

    # Synchronous Reset Operation
    scenarios.append(
        {
            "scenario": "Synchronous Reset Operation",
            "input variable": [
                {"reset": "0", "s": "111"},
                {"reset": "1", "s": "111"},
                {"reset": "1", "s": "000"},
                {"reset": "0", "s": "000"},
            ],
        }
    )

    # Rising Water Level Transitions
    scenarios.append(
        {
            "scenario": "Rising Water Level Transitions",
            "input variable": [
                {"reset": "0", "s": "000"},
                {"reset": "0", "s": "001"},
                {"reset": "0", "s": "011"},
                {"reset": "0", "s": "111"},
            ],
        }
    )

    # Falling Water Level Transitions
    scenarios.append(
        {
            "scenario": "Falling Water Level Transitions",
            "input variable": [
                {"reset": "0", "s": "111"},
                {"reset": "0", "s": "011"},
                {"reset": "0", "s": "001"},
                {"reset": "0", "s": "000"},
            ],
        }
    )

    # Maximum Water Level
    scenarios.append(
        {
            "scenario": "Maximum Water Level",
            "input variable": [
                {"reset": "0", "s": "000"},
                {"reset": "0", "s": "111"},
                {"reset": "0", "s": "111"},
            ],
        }
    )

    # Minimum Water Level
    scenarios.append(
        {
            "scenario": "Minimum Water Level",
            "input variable": [
                {"reset": "0", "s": "111"},
                {"reset": "0", "s": "000"},
                {"reset": "0", "s": "000"},
            ],
        }
    )

    # Invalid Sensor Combinations
    scenarios.append(
        {
            "scenario": "Invalid Sensor Combinations",
            "input variable": [
                {"reset": "0", "s": "100"},
                {"reset": "0", "s": "101"},
                {"reset": "0", "s": "110"},
            ],
        }
    )

    # Rapid Sensor Changes
    scenarios.append(
        {
            "scenario": "Rapid Sensor Changes",
            "input variable": [
                {"reset": "0", "s": "000"},
                {"reset": "0", "s": "111"},
                {"reset": "0", "s": "000"},
                {"reset": "0", "s": "111"},
            ],
        }
    )

    # Direction Change Detection
    scenarios.append(
        {
            "scenario": "Direction Change Detection",
            "input variable": [
                {"reset": "0", "s": "000"},
                {"reset": "0", "s": "111"},
                {"reset": "0", "s": "001"},
                {"reset": "0", "s": "011"},
                {"reset": "0", "s": "001"},
            ],
        }
    )

    return scenarios


if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
