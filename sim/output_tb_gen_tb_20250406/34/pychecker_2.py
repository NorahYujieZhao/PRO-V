import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state registers"""
        pass  # No internal state needed for combinational logic

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and compute outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a_bv = BinaryValue(value=stimulus["a"], n_bits=8, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=8, bigEndian=False)

            # Get signed integer values
            a_int = a_bv.signed_integer
            b_int = b_bv.signed_integer

            # Compute sum
            s_int = a_int + b_int

            # Create sum BinaryValue and handle 8-bit wraparound
            s_bv = BinaryValue(value=s_int & 0xFF, n_bits=8, bigEndian=False)

            # Detect overflow: occurs when operands have same sign but result has different sign
            a_sign = (a_bv.integer >> 7) & 1
            b_sign = (b_bv.integer >> 7) & 1
            s_sign = (s_bv.integer >> 7) & 1

            overflow = (a_sign == b_sign) and (s_sign != a_sign)

            # Create output dictionary for this stimulus
            output = {"s": s_bv.binstr, "overflow": "1" if overflow else "0"}
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
