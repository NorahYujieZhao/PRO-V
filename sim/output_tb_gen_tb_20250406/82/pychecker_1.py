import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to BinaryValue
            x_bv = BinaryValue(value=stimulus["x"], n_bits=4, bigEndian=False)
            x_val = x_bv.integer

            # Extract individual bits
            x1 = (x_val >> 0) & 1  # LSB
            x2 = (x_val >> 1) & 1
            x3 = (x_val >> 2) & 1
            x4 = (x_val >> 3) & 1  # MSB

            # Implement Karnaugh map logic
            if x3 == 0 and x4 == 0:  # Row 00
                f = 0 if x1 == 0 and x2 == 1 else 0  # Choose 0 for don't-cares
            elif x3 == 0 and x4 == 1:  # Row 01
                if x1 == 0 and x2 == 0:
                    f = 0
                elif x1 == 1 and x2 == 1:
                    f = 1
                elif x1 == 1 and x2 == 0:
                    f = 0
                else:
                    f = 0  # don't-care case
            elif x3 == 1 and x4 == 1:  # Row 11
                if x1 == 0 and x2 == 0:
                    f = 1
                elif x1 == 0 and x2 == 1:
                    f = 1
                else:
                    f = 0  # don't-care cases
            else:  # Row 10
                if x1 == 0 and x2 == 0:
                    f = 1
                elif x1 == 0 and x2 == 1:
                    f = 1
                elif x1 == 1 and x2 == 1:
                    f = 0
                else:
                    f = 0  # don't-care case

            # Convert output to BinaryValue and then to binary string
            f_bv = BinaryValue(value=f, n_bits=1, bigEndian=False)
            output_list.append({"f": f_bv.binstr})

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
