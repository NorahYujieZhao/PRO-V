import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=8, bigEndian=False)

            # Get the sign bit (MSB)
            sign_bit = in_bv[7]

            # Create the 32-bit output
            # If sign bit is 1, extend with 1s (0xFFFFFF), if 0 extend with 0s (0x000000)
            if sign_bit:
                out_value = (0xFFFFFF << 8) | in_bv.integer
            else:
                out_value = (
                    in_bv.integer
                )  # Lower 8 bits remain unchanged, upper bits are 0

            # Convert to 32-bit BinaryValue
            out_bv = BinaryValue(value=out_value, n_bits=32, bigEndian=False)

            # Add to output list
            stimulus_outputs.append({"out": out_bv.binstr})

        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }

        return output_dict


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
