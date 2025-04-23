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
            # Convert input strings to BinaryValue objects
            a_bv = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)
            c_bv = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to integers for easier processing
            a = a_bv.integer
            b = b_bv.integer
            c = c_bv.integer
            d = d_bv.integer

            # Implement Karnaugh map logic
            ab = (a << 1) | b
            cd = (c << 1) | d

            # Evaluate output based on input combinations
            if ab == 0b01:  # ab = 01
                out = 0 if cd in [0b01, 0b11, 0b10] else 0  # Choose 0 for don't care
            elif ab == 0b00:  # ab = 00
                out = 1 if cd in [0b11, 0b10] else 0
            elif ab == 0b10:  # ab = 10
                out = 1  # All cases are 1 or don't care (chosen as 1)
            else:  # ab = 11
                out = 1  # All cases are 1 or don't care (chosen as 1)

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)
            stimulus_outputs.append({"out": out_bv.binstr})

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
