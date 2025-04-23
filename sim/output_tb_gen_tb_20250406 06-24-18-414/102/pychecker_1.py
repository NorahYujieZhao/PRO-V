import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state registers"""
        self.prev_z = 1  # Initial z state is 1
        self.prev_xy = 0  # Track if previous x and y were both 1

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and generate outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            x_bv = BinaryValue(value=stimulus["x"], n_bits=1, bigEndian=False)
            y_bv = BinaryValue(value=stimulus["y"], n_bits=1, bigEndian=False)

            # Convert to integers for logic operations
            x = x_bv.integer
            y = y_bv.integer

            # Implement the combinational logic
            z = (
                (not x and not y and self.prev_z)
                or (x and y)
                or (not x and y and not self.prev_xy)
            )

            # Update previous states
            self.prev_z = z
            self.prev_xy = x and y

            # Convert output to binary string
            z_bv = BinaryValue(value=int(z), n_bits=1, bigEndian=False)
            stimulus_outputs.append({"z": z_bv.binstr})

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
