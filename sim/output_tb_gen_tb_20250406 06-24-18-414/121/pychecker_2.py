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
            # Get the input value and convert to BinaryValue
            in_val = BinaryValue(value=stimulus["in"], n_bits=4, bigEndian=False)

            # Find position of first 1 from MSB
            if in_val[3] == 1:
                pos = 3
            elif in_val[2] == 1:
                pos = 2
            elif in_val[1] == 1:
                pos = 1
            elif in_val[0] == 1:
                pos = 0
            else:
                pos = 0

            # Convert position to 2-bit BinaryValue
            pos_bv = BinaryValue(value=pos, n_bits=2, bigEndian=False)

            # Add to output list
            stimulus_outputs.append({"pos": pos_bv.binstr})

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
