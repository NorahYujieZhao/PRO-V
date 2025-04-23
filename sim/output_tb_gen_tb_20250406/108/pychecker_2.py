import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Convert binary strings to BinaryValue objects
            a_bv = BinaryValue(value=stimulus["A"], n_bits=2, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["B"], n_bits=2, bigEndian=False)

            # Compare A and B
            z = 1 if a_bv.integer == b_bv.integer else 0

            # Convert output to BinaryValue
            z_bv = BinaryValue(value=z, n_bits=1, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"z": z_bv.binstr})

        # Return formatted output
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
