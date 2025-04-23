import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize all outputs to 0
        """
        self.left = 0
        self.down = 0
        self.right = 0
        self.up = 0

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process input scancode and set appropriate outputs
        """
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert scancode string to BinaryValue
            scancode = BinaryValue(
                value=stimulus["scancode"], n_bits=16, bigEndian=False
            )
            scancode_int = scancode.integer

            # Reset all outputs
            self.left = 0
            self.down = 0
            self.right = 0
            self.up = 0

            # Check scancode and set appropriate output
            if scancode_int == 0xE06B:
                self.left = 1
            elif scancode_int == 0xE072:
                self.down = 1
            elif scancode_int == 0xE074:
                self.right = 1
            elif scancode_int == 0xE075:
                self.up = 1

            # Add current outputs to output list
            output_list.append(
                {
                    "left": BinaryValue(
                        value=self.left, n_bits=1, bigEndian=False
                    ).binstr,
                    "down": BinaryValue(
                        value=self.down, n_bits=1, bigEndian=False
                    ).binstr,
                    "right": BinaryValue(
                        value=self.right, n_bits=1, bigEndian=False
                    ).binstr,
                    "up": BinaryValue(value=self.up, n_bits=1, bigEndian=False).binstr,
                }
            )

        return {"scenario": stimulus_dict["scenario"], "output variable": output_list}


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
