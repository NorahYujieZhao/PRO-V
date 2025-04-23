import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed as this is combinational logic
        """
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Initialize outputs to 0
            left = down = right = up = "0"

            # Get scancode input
            scancode = stimulus["scancode"]
            scancode_bv = BinaryValue(value=scancode, n_bits=16, bigEndian=False)

            # Check scancode against arrow key values
            if scancode_bv.integer == 0xE06B:
                left = "1"
            elif scancode_bv.integer == 0xE072:
                down = "1"
            elif scancode_bv.integer == 0xE074:
                right = "1"
            elif scancode_bv.integer == 0xE075:
                up = "1"

            # Add outputs to list
            output_dict = {"left": left, "down": down, "right": right, "up": up}
            stimulus_outputs.append(output_dict)

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
