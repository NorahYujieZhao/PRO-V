import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize internal state variables
        """
        self.out = 0
        self.result_is_zero = 0

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process input stimulus and generate outputs
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to BinaryValue objects
            do_sub_bv = BinaryValue(stimulus["do_sub"], n_bits=1, bigEndian=False)
            a_bv = BinaryValue(stimulus["a"], n_bits=8, bigEndian=False)
            b_bv = BinaryValue(stimulus["b"], n_bits=8, bigEndian=False)

            # Get integer values
            do_sub = do_sub_bv.integer
            a = a_bv.integer
            b = b_bv.integer

            # Perform addition or subtraction
            if do_sub == 0:
                self.out = (a + b) & 0xFF  # 8-bit addition
            else:
                self.out = (a - b) & 0xFF  # 8-bit subtraction

            # Set zero flag
            self.result_is_zero = 1 if self.out == 0 else 0

            # Convert results to binary strings
            out_bv = BinaryValue(value=self.out, n_bits=8, bigEndian=False)
            result_is_zero_bv = BinaryValue(
                value=self.result_is_zero, n_bits=1, bigEndian=False
            )

            # Add outputs to results list
            stimulus_outputs.append(
                {"out": out_bv.binstr, "result_is_zero": result_is_zero_bv.binstr}
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
