import json


def stimulus_gen():
    scenarios = []

    # Helper function to format input value as 4-bit binary string
    def format_in(value):
        return format(value, "04b")

    # Scenario 1: Single Bit Detection
    single_bit_seq = [
        {"in": format_in(0b0001)},
        {"in": format_in(0b0010)},
        {"in": format_in(0b0100)},
        {"in": format_in(0b1000)},
    ]
    scenarios.append(
        {"scenario": "Single Bit Detection", "input variable": single_bit_seq}
    )

    # Scenario 2: Multiple Bits Active
    multiple_bits_seq = [
        {"in": format_in(0b1100)},
        {"in": format_in(0b1110)},
        {"in": format_in(0b1011)},
        {"in": format_in(0b1101)},
    ]
    scenarios.append(
        {"scenario": "Multiple Bits Active", "input variable": multiple_bits_seq}
    )

    # Scenario 3: All Zeros Input
    all_zeros_seq = [{"in": format_in(0b0000)}]
    scenarios.append({"scenario": "All Zeros Input", "input variable": all_zeros_seq})

    # Scenario 4: All Ones Input
    all_ones_seq = [{"in": format_in(0b1111)}]
    scenarios.append({"scenario": "All Ones Input", "input variable": all_ones_seq})

    # Scenario 5: Adjacent Bits
    adjacent_bits_seq = [
        {"in": format_in(0b0011)},
        {"in": format_in(0b0110)},
        {"in": format_in(0b1100)},
    ]
    scenarios.append({"scenario": "Adjacent Bits", "input variable": adjacent_bits_seq})

    # Scenario 6: Alternating Patterns
    alternating_seq = [{"in": format_in(0b0101)}, {"in": format_in(0b1010)}]
    scenarios.append(
        {"scenario": "Alternating Patterns", "input variable": alternating_seq}
    )

    # Scenario 7: Walking Ones
    walking_ones_seq = [
        {"in": format_in(0b0001)},
        {"in": format_in(0b0010)},
        {"in": format_in(0b0100)},
        {"in": format_in(0b1000)},
    ]
    scenarios.append({"scenario": "Walking Ones", "input variable": walking_ones_seq})

    # Scenario 8: Walking Zeros
    walking_zeros_seq = [
        {"in": format_in(0b1110)},
        {"in": format_in(0b1101)},
        {"in": format_in(0b1011)},
        {"in": format_in(0b0111)},
    ]
    scenarios.append({"scenario": "Walking Zeros", "input variable": walking_zeros_seq})

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
