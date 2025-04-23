import json


def stimulus_gen():
    scenarios = []

    # Helper function to create scenario dictionary
    def create_scenario(name, input_list):
        return {"scenario": name, "input variable": input_list}

    # Scenario 1: All Zeros
    scenarios.append(create_scenario("All Zeros Input", [{"in": "0" * 255}]))

    # Scenario 2: All Ones
    scenarios.append(create_scenario("All Ones Input", [{"in": "1" * 255}]))

    # Scenario 3: Single One at different positions
    single_one_inputs = []
    for pos in [0, 127, 254]:  # Test beginning, middle, end
        input_vec = list("0" * 255)
        input_vec[pos] = "1"
        single_one_inputs.append({"in": "".join(input_vec)})
    scenarios.append(create_scenario("Single One", single_one_inputs))

    # Scenario 4: Alternating Bits
    alt_pattern = "".join(["10"] * 127 + ["1"])
    scenarios.append(create_scenario("Alternating Bits", [{"in": alt_pattern}]))

    # Scenario 5: Random Distribution
    import random

    random.seed(42)  # For reproducibility
    rand_pattern = "".join([str(random.randint(0, 1)) for _ in range(255)])
    scenarios.append(create_scenario("Random Distribution", [{"in": rand_pattern}]))

    # Scenario 6: Walking Ones
    walking_ones = []
    for pos in range(0, 255, 32):  # Sample positions for walking 1
        input_vec = list("0" * 255)
        input_vec[pos] = "1"
        walking_ones.append({"in": "".join(input_vec)})
    scenarios.append(create_scenario("Walking Ones", walking_ones))

    # Scenario 7: Sparse Pattern (10% ones)
    sparse_vec = list("0" * 255)
    for i in random.sample(range(255), 25):  # ~10% of 255
        sparse_vec[i] = "1"
    scenarios.append(create_scenario("Sparse Pattern", [{"in": "".join(sparse_vec)}]))

    # Scenario 8: Dense Pattern (90% ones)
    dense_vec = list("1" * 255)
    for i in random.sample(range(255), 25):  # ~10% of 255 as zeros
        dense_vec[i] = "0"
    scenarios.append(create_scenario("Dense Pattern", [{"in": "".join(dense_vec)}]))

    # Scenario 9: Block Patterns
    block_pattern = list("0" * 255)
    block_pattern[50:100] = "1" * 50  # 50-bit block of ones
    scenarios.append(
        create_scenario("Block Patterns", [{"in": "".join(block_pattern)}])
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
