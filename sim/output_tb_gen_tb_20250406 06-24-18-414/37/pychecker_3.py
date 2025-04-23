import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=8, bigEndian=False)
            in_int = in_bv.integer

            # Find first '1' bit position
            pos = 0
            found = False

            for i in range(8):
                if in_int & (1 << i):
                    pos = i
                    found = True
                    break

            # Convert position to BinaryValue for output
            pos_bv = BinaryValue(value=pos, n_bits=3, bigEndian=False)

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
