import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for this combinational logic
        pass

    def reverse_bits(self, input_val: str) -> str:
        # Convert input binary string to BinaryValue
        bv = BinaryValue(input_val, n_bits=8, bigEndian=False)
        # Get integer value
        val = bv.integer
        # Reverse bits
        reversed_val = int("{:08b}".format(val)[::-1], 2)
        # Convert back to BinaryValue
        out_bv = BinaryValue(value=reversed_val, n_bits=8, bigEndian=False)
        return out_bv.binstr

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        # Process each stimulus input
        for stimulus in stimulus_dict["input variable"]:
            input_val = stimulus["in"]
            # Reverse the bits
            output_val = self.reverse_bits(input_val)
            # Add to output list
            output_list.append({"out": output_val})

        return {"scenario": stimulus_dict["scenario"], "output variable": output_list}


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
