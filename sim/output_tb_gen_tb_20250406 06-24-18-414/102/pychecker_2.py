import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert string inputs to BinaryValue
            x_bv = BinaryValue(stimulus["x"], n_bits=1, bigEndian=False)
            y_bv = BinaryValue(stimulus["y"], n_bits=1, bigEndian=False)

            # Get integer values
            x = x_bv.integer
            y = y_bv.integer

            # Implement XNOR logic
            z = int(not (x ^ y))

            # Convert output to BinaryValue
            z_bv = BinaryValue(value=z, n_bits=1, bigEndian=False)

            # Create output dictionary for this stimulus
            output = {"z": z_bv.binstr}
            stimulus_outputs.append(output)

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
