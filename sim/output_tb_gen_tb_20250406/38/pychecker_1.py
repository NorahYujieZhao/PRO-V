import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert input scancode string to BinaryValue
            scancode = BinaryValue(stimulus["scancode"], n_bits=16, bigEndian=False)
            scancode_int = scancode.integer

            # Initialize outputs
            left = down = right = up = 0

            # Check scancode and set appropriate output
            if scancode_int == 0xE06B:
                left = 1
            elif scancode_int == 0xE072:
                down = 1
            elif scancode_int == 0xE074:
                right = 1
            elif scancode_int == 0xE075:
                up = 1

            # Add outputs to stimulus_outputs list
            output_dict = {
                "left": BinaryValue(value=left, n_bits=1, bigEndian=False).binstr,
                "down": BinaryValue(value=down, n_bits=1, bigEndian=False).binstr,
                "right": BinaryValue(value=right, n_bits=1, bigEndian=False).binstr,
                "up": BinaryValue(value=up, n_bits=1, bigEndian=False).binstr,
            }
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
