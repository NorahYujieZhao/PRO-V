import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to integer
            in_val = int(stimulus["in"], 2)

            # Priority encode the input
            if in_val & 0b1000:  # Check bit 3 (MSB)
                pos = 3
            elif in_val & 0b0100:  # Check bit 2
                pos = 2
            elif in_val & 0b0010:  # Check bit 1
                pos = 1
            elif in_val & 0b0001:  # Check bit 0 (LSB)
                pos = 0
            else:  # No bits set
                pos = 0

            # Convert position to 2-bit binary string
            pos_bin = format(pos, "02b")

            # Add to output list
            stimulus_outputs.append({"pos": pos_bin})

        # Return formatted output dictionary
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
