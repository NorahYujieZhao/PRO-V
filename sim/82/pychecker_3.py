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
            # Convert input x to BinaryValue
            x_bv = BinaryValue(stimulus["x"], n_bits=4, bigEndian=False)
            x_int = x_bv.integer

            # Extract individual bits
            x1 = (x_int >> 0) & 1  # LSB
            x2 = (x_int >> 1) & 1
            x3 = (x_int >> 2) & 1
            x4 = (x_int >> 3) & 1  # MSB

            # Implement Karnaugh map logic
            # Setting don't cares (d) to values that simplify logic
            if x3 == 0 and x4 == 0:
                f = 0 if x2 == 1 else 0  # Row 00
            elif x3 == 0 and x4 == 1:
                f = 1 if x1 == 1 and x2 == 1 else 0  # Row 01
            elif x3 == 1 and x4 == 1:
                f = 1  # Row 11
            else:  # x3 == 1 and x4 == 0
                f = 0 if x1 == 1 and x2 == 1 else 1  # Row 10

            # Convert output to BinaryValue
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
