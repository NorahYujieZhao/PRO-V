import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for combinational logic
        """
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process each input stimulus and compute sum and overflow
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a_bv = BinaryValue(value=stimulus["a"], n_bits=8, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=8, bigEndian=False)

            # Get signed integer values
            a_int = a_bv.signed_integer
            b_int = b_bv.signed_integer

            # Compute sum
            s_int = (a_int + b_int) & 0xFF  # Keep 8 bits
            s_bv = BinaryValue(value=s_int, n_bits=8, bigEndian=False)

            # Check for overflow
            # Overflow occurs when adding two numbers of the same sign
            # and getting a result with different sign
            a_sign = (a_bv.integer >> 7) & 1
            b_sign = (b_bv.integer >> 7) & 1
            s_sign = (s_bv.integer >> 7) & 1

            overflow = (a_sign == b_sign) and (s_sign != a_sign)
            overflow_str = "1" if overflow else "0"

            # Create output dictionary
            output = {"s": s_bv.binstr, "overflow": overflow_str}
            stimulus_outputs.append(output)

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
