import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert binary strings to integers
            in1 = int(stimulus["in1"], 2)
            in2 = int(stimulus["in2"], 2)

            # Perform the logic operations
            # 1. Invert in2 (NOT operation)
            # 2. AND with in1
            out = in1 & (~in2 & 1)

            # Convert result back to binary string
            out_str = format(out, "b")

            # Add to output list
            stimulus_outputs.append({"out": out_str})

        # Return formatted output dictionary
        return {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }


def check_output(stimulus_list):

    dut = GoldenDUT()
    tb_outputs = []

    for stimulus in stimulus_list:

        tb_outputs.append(dut.load(stimulus))

    return tb_outputs


if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)

    if isinstance(stimulus_data, dict):
        stimulus_list = stimulus_data.get("input variable", [])
    else:
        stimulus_list = stimulus_data

    outputs = check_output(stimulus_list)

    print(json.dumps(outputs, indent=2))
