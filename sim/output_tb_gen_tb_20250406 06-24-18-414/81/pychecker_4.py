import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize internal state variables
        """
        self.out = BinaryValue(value=0, n_bits=8, bigEndian=False)
        self.result_is_zero = BinaryValue(value=0, n_bits=1, bigEndian=False)

    def load(self, stimulus_dict: Dict[str, Any]):
        """
        Process inputs and generate outputs
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to BinaryValue
            do_sub_bv = BinaryValue(value=stimulus["do_sub"], n_bits=1, bigEndian=False)
            a_bv = BinaryValue(value=stimulus["a"], n_bits=8, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=8, bigEndian=False)

            # Perform add/subtract based on do_sub
            if do_sub_bv.integer == 0:
                out_val = (a_bv.integer + b_bv.integer) & 0xFF  # Keep 8 bits
            else:
                out_val = (a_bv.integer - b_bv.integer) & 0xFF  # Keep 8 bits

            # Update output values
            self.out = BinaryValue(value=out_val, n_bits=8, bigEndian=False)
            self.result_is_zero = BinaryValue(
                value=1 if out_val == 0 else 0, n_bits=1, bigEndian=False
            )

            # Add outputs to results
            stimulus_outputs.append(
                {"out": self.out.binstr, "result_is_zero": self.result_is_zero.binstr}
            )

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
