import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=4, bigEndian=False)

            # Calculate AND output - all bits must be 1
            out_and = 1 if in_bv.integer == 0b1111 else 0

            # Calculate OR output - any bit being 1
            out_or = 1 if in_bv.integer > 0 else 0

            # Calculate XOR output - count number of 1s
            out_xor = bin(in_bv.integer).count("1") % 2

            # Create output dictionary for this stimulus
            output = {
                "out_and": BinaryValue(value=out_and, n_bits=1, bigEndian=False).binstr,
                "out_or": BinaryValue(value=out_or, n_bits=1, bigEndian=False).binstr,
                "out_xor": BinaryValue(value=out_xor, n_bits=1, bigEndian=False).binstr,
            }
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
