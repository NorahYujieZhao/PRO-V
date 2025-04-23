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
            # Convert input strings to BinaryValue objects
            a_bv = BinaryValue(value=stimulus["a"], n_bits=8, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=8, bigEndian=False)

            # Get signed integer values
            a_int = a_bv.signed_integer
            b_int = b_bv.signed_integer

            # Calculate sum
            s_int = a_int + b_int

            # Create sum BinaryValue (temporarily with 9 bits to check overflow)
            s_bv = BinaryValue(value=s_int & 0xFF, n_bits=8, bigEndian=False)

            # Detect overflow
            # Overflow occurs when adding two positive numbers gives negative
            # or adding two negative numbers gives positive
            overflow = (a_int >= 0 and b_int >= 0 and s_int < 0) or (
                a_int < 0 and b_int < 0 and s_int >= 0
            )

            # Create output dictionary
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
