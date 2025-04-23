import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to BinaryValue
            in_bv = BinaryValue(stimulus["in"], n_bits=8, bigEndian=False)
            in_val = in_bv.integer

            # Initialize position to 0 (default when no bits are set)
            pos = 0

            # Check each bit from LSB to MSB
            for i in range(8):
                if in_val & (1 << i):
                    pos = i
                    break

            # Convert position to 3-bit BinaryValue for output
            pos_bv = BinaryValue(value=pos, n_bits=3, bigEndian=False)

            # Add to output list as dictionary
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
