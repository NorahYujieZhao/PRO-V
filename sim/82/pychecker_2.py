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
            # Get x input and convert to integer
            x_bv = BinaryValue(value=stimulus["x"], n_bits=4, bigEndian=False)
            x = x_bv.integer

            # Extract individual bits
            x1 = (x >> 0) & 1  # LSB
            x2 = (x >> 1) & 1
            x3 = (x >> 2) & 1
            x4 = (x >> 3) & 1  # MSB

            # Implement Karnaugh map logic
            # Don't care conditions are chosen for optimization
            if x3 == 0 and x4 == 0:
                f = 0 if x2 == 1 else 0  # Choose 0 for don't care
            elif x3 == 0 and x4 == 1:
                if x1 == 0 and x2 == 0:
                    f = 0
                elif x1 == 0 and x2 == 1:
                    f = 1 if x3 == 1 else 0
                else:
                    f = 0  # Choose 0 for don't care
            elif x3 == 1 and x4 == 1:
                f = 1
            else:  # x3 == 1 and x4 == 0
                if x1 == 0 and x2 == 0:
                    f = 1
                elif x1 == 0 and x2 == 1:
                    f = 1
                elif x1 == 1 and x2 == 1:
                    f = 0
                else:
                    f = 0  # Choose 0 for don't care

            # Convert output to binary string
            f_bv = BinaryValue(value=f, n_bits=1, bigEndian=False)
            stimulus_outputs.append({"f": f_bv.binstr})

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
