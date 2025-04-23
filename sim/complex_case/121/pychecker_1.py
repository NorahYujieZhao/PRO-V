import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            in_val = int(stimulus["in"], 2)  # Convert binary string to integer
            pos = 0  # Default position if no bits are set

            # Check bits from MSB to LSB
            if in_val & 0b1000:  # bit[3] is set
                pos = 3
            elif in_val & 0b0100:  # bit[2] is set
                pos = 2
            elif in_val & 0b0010:  # bit[1] is set
                pos = 1
            elif in_val & 0b0001:  # bit[0] is set
                pos = 0

            # Convert position to 2-bit binary string
            pos_bin = format(pos, "02b")
            stimulus_outputs.append({"pos": pos_bin})

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
