import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for this combinational logic
        """
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Perform sign extension from 8 bits to 32 bits
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input to BinaryValue
            in_val = BinaryValue(value=stimulus["in"], n_bits=8, bigEndian=False)

            # Get the sign bit (MSB)
            sign_bit = in_val[7]

            # Create the sign extension (24 copies of sign bit)
            if sign_bit == "1":
                sign_extend = "1" * 24
            else:
                sign_extend = "0" * 24

            # Combine sign extension with original input
            out_val = sign_extend + in_val.binstr

            # Add to outputs
            stimulus_outputs.append({"out": out_val})

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
