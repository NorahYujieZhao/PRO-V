import json


def stimulus_gen():
    scenarios = []

    # Helper function to format binary inputs
    def format_inputs(in1, in2):
        return {"in1": format(in1, "01b"), "in2": format(in2, "01b")}

    # Scenario 1: All Input Combinations
    input_combinations = []
    for i in range(4):
        in1 = (i >> 1) & 1
        in2 = i & 1
        input_combinations.append(format_inputs(in1, in2))
    scenarios.append(
        {"scenario": "All Input Combinations", "input variable": input_combinations}
    )

    # Scenario 2: Input Transitions
    transitions = []
    for i in range(4):
        for j in range(4):
            if i != j:
                in1_start = (i >> 1) & 1
                in2_start = i & 1
                in1_end = (j >> 1) & 1
                in2_end = j & 1
                transitions.extend(
                    [
                        format_inputs(in1_start, in2_start),
                        format_inputs(in1_end, in2_end),
                    ]
                )
    scenarios.append({"scenario": "Input Transitions", "input variable": transitions})

    # Scenario 3: Input Signal Stability
    stability = []
    for _ in range(10):  # Hold each combination for 10 cycles
        stability.append(format_inputs(0, 0))
    for _ in range(10):
        stability.append(format_inputs(1, 1))
    scenarios.append(
        {"scenario": "Input Signal Stability", "input variable": stability}
    )

    # Scenario 4: Propagation Delay
    prop_delay = []
    for _ in range(5):
        prop_delay.extend(
            [
                format_inputs(0, 0),
                format_inputs(1, 1),
                format_inputs(1, 0),
                format_inputs(0, 1),
            ]
        )
    scenarios.append({"scenario": "Propagation Delay", "input variable": prop_delay})

    # Scenario 5: Simultaneous Input Changes
    simultaneous = []
    for _ in range(5):
        simultaneous.extend(
            [
                format_inputs(0, 0),
                format_inputs(1, 1),
                format_inputs(0, 1),
                format_inputs(1, 0),
            ]
        )
    scenarios.append(
        {"scenario": "Simultaneous Input Changes", "input variable": simultaneous}
    )

    # Scenario 6: Input Setup Time
    setup_time = []
    for _ in range(5):
        setup_time.extend(
            [
                format_inputs(0, 0),
                format_inputs(0, 1),
                format_inputs(1, 0),
                format_inputs(1, 1),
            ]
        )
    scenarios.append({"scenario": "Input Setup Time", "input variable": setup_time})

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
