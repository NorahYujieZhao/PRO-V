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
            in_val = BinaryValue(value=stimulus["in"], n_bits=8, bigEndian=False)

            # Get the sign bit (MSB)
            sign_bit = in_val[7]

            # Create the 32-bit output
            # Replicate sign bit 24 times and concatenate with original 8 bits
            if sign_bit == "1":
                out_val = BinaryValue(
                    "1" * 24 + in_val.binstr, n_bits=32, bigEndian=False
                )
            else:
                out_val = BinaryValue(
                    "0" * 24 + in_val.binstr, n_bits=32, bigEndian=False
                )

            # Add to output list
            stimulus_outputs.append({"out": out_val.binstr})

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
