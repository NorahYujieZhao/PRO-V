import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize the golden model"""
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and generate outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get the input value and convert to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=3, bigEndian=False)

            # Count number of 1's in the input
            count = bin(in_bv.integer).count("1")

            # Convert count to 2-bit BinaryValue
            out_bv = BinaryValue(value=count, n_bits=2, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"out": out_bv.binstr})

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
