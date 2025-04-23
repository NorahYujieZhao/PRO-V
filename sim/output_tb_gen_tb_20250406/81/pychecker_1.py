import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize internal state registers
        """
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process input stimulus and generate output
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            do_sub = BinaryValue(value=stimulus["do_sub"], n_bits=1, bigEndian=False)
            a = BinaryValue(value=stimulus["a"], n_bits=8, bigEndian=False)
            b = BinaryValue(value=stimulus["b"], n_bits=8, bigEndian=False)

            # Perform addition or subtraction
            if do_sub.integer == 0:
                out = (a.integer + b.integer) & 0xFF  # 8-bit addition
            else:
                out = (a.integer - b.integer) & 0xFF  # 8-bit subtraction

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=out, n_bits=8, bigEndian=False)

            # Set zero flag
            result_is_zero = 1 if out == 0 else 0
            result_is_zero_bv = BinaryValue(
                value=result_is_zero, n_bits=1, bigEndian=False
            )

            # Append outputs to list
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
