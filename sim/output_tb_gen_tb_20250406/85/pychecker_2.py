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
            # Convert input binary strings to BinaryValue
            a_bv = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)
            c_bv = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to integers for easier processing
            a = a_bv.integer
            b = b_bv.integer
            c = c_bv.integer
            d = d_bv.integer

            # Implement logic based on Karnaugh map
            # Form 4-bit index from inputs
            idx = (c << 3) | (d << 2) | (a << 1) | b

            # Truth table (with don't cares set to convenient values)
            truth_table = {
                0b0000: 0,  # cd=00, ab=00
                0b0001: 0,  # cd=00, ab=01 (don't care, set to 0)
                0b0010: 1,  # cd=00, ab=10
                0b0011: 1,  # cd=00, ab=11
                0b0100: 0,  # cd=01, ab=00
                0b0101: 0,  # cd=01, ab=01
                0b0110: 0,  # cd=01, ab=10 (don't care, set to 0)
                0b0111: 0,  # cd=01, ab=11 (don't care, set to 0)
                0b1000: 0,  # cd=10, ab=00
                0b1001: 0,  # cd=10, ab=01
                0b1010: 1,  # cd=10, ab=10
                0b1011: 1,  # cd=10, ab=11
                0b1100: 0,  # cd=11, ab=00
                0b1101: 0,  # cd=11, ab=01
                0b1110: 1,  # cd=11, ab=10
                0b1111: 1,  # cd=11, ab=11
            }

            # Get output value from truth table
            out = truth_table[idx]

            # Convert to BinaryValue for output
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add to outputs
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
