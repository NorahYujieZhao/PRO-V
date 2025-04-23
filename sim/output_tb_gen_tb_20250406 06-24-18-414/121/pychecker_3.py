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
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=4, bigEndian=False)
            in_val = in_bv.integer

            # Priority encode the input
            if in_val & 0b1000:  # bit 3 is set
                pos = 3
            elif in_val & 0b0100:  # bit 2 is set
                pos = 2
            elif in_val & 0b0010:  # bit 1 is set
                pos = 1
            elif in_val & 0b0001:  # bit 0 is set
                pos = 0
            else:  # no bits set
                pos = 0

            # Convert position to 2-bit BinaryValue
            pos_bv = BinaryValue(value=pos, n_bits=2, bigEndian=False)

            # Add to output list as binary string
            stimulus_outputs.append({"pos": pos_bv.binstr})

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
