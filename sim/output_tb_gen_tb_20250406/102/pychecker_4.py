import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            x_bv = BinaryValue(value=stimulus["x"], n_bits=1, bigEndian=False)
            y_bv = BinaryValue(value=stimulus["y"], n_bits=1, bigEndian=False)

            # Convert to integers for comparison
            x = x_bv.integer
            y = y_bv.integer

            # Compute z = (x == y)
            z = 1 if x == y else 0

            # Convert output to BinaryValue
            z_bv = BinaryValue(value=z, n_bits=1, bigEndian=False)

            # Add to output list
            stimulus_outputs.append({"z": z_bv.binstr})

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
