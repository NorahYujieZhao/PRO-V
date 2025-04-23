import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a_bv = BinaryValue(value=stimulus["a"], n_bits=8, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=8, bigEndian=False)

            # Get signed values
            a_signed = a_bv.signed_integer
            b_signed = b_bv.signed_integer

            # Compute sum
            sum_val = a_signed + b_signed

            # Create sum BinaryValue (handle wrap-around for 8 bits)
            s_bv = BinaryValue(value=sum_val & 0xFF, n_bits=8, bigEndian=False)

            # Check for overflow
            # Overflow occurs when adding two numbers with the same sign
            # but getting a result with different sign
            a_sign = a_signed >= 0
            b_sign = b_signed >= 0
            s_sign = s_bv.signed_integer >= 0

            overflow = (a_sign == b_sign) and (a_sign != s_sign)

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
