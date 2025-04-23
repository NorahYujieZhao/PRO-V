import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def calculate_output(self, a, b, c, d):
        # Convert inputs to integer
        value = (int(a) << 3) | (int(b) << 2) | (int(c) << 1) | int(d)

        # Truth table for output 1: 2 (0010), 7 (0111), 15 (1111)
        output_1_values = {2, 7, 15}

        return 1 if value in output_1_values else 0

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input values
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Calculate outputs
            out = self.calculate_output(a, b, c, d)

            # Format output as dictionary with binary strings
            output_dict = {"out_sop": format(out, "b"), "out_pos": format(out, "b")}

            outputs.append(output_dict)

        return {"scenario": stimulus_dict["scenario"], "output variable": outputs}


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
