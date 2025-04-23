import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        """
        No state initialization needed for combinational logic
        """
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Implement NAND gate logic
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary string inputs to integers
            in1 = int(stimulus["in1"], 2)
            in2 = int(stimulus["in2"], 2)

            # Implement NAND logic
            # First invert in2, then AND with in1
            not_in2 = ~in2 & 1  # Mask to keep 1 bit
            out = (in1 & not_in2) & 1

            # Convert result back to binary string
            stimulus_outputs.append({"out": format(out, "b")})

        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }

        return output_dict


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
