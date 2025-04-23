import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            in_val = int(stimulus["in"], 2)  # Convert binary string to integer
            pos = 0  # Default output for zero input

            # Check bits from MSB to LSB
            if in_val & 0b1000:  # Bit 3
                pos = 3
            elif in_val & 0b0100:  # Bit 2
                pos = 2
            elif in_val & 0b0010:  # Bit 1
                pos = 1
            elif in_val & 0b0001:  # Bit 0
                pos = 0

            # Format output as 2-bit binary string
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
