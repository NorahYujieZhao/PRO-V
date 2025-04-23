import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            x_bv = BinaryValue(value=stimulus["x"], n_bits=4, bigEndian=False)

            # Extract x[4:1] values
            x1 = (x_bv.integer >> 0) & 1
            x2 = (x_bv.integer >> 1) & 1
            x3 = (x_bv.integer >> 2) & 1
            x4 = (x_bv.integer >> 3) & 1

            # Implement K-map logic
            if x3 == 0 and x4 == 0:  # 00
                f = 1 if (x1 == 0 and x2 == 0) or (x1 == 0 and x2 == 1) else 0
            elif x3 == 0 and x4 == 1:  # 01
                f = 0
            elif x3 == 1 and x4 == 1:  # 11
                f = 0 if (x1 == 0 and x2 == 1) else 1
            else:  # 10
                f = 0 if (x1 == 1 and x2 == 1) else 1

            # Convert result to binary string
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
