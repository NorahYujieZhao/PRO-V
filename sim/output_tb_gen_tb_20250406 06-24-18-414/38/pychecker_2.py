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
        Process scancode input and determine which arrow key (if any) was pressed
        """
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get scancode input
            scancode = int(stimulus["scancode"], 2)

            # Initialize outputs
            left = 0
            down = 0
            right = 0
            up = 0

            # Check scancode against patterns
            if scancode == 0xE06B:  # left arrow
                left = 1
            elif scancode == 0xE072:  # down arrow
                down = 1
            elif scancode == 0xE074:  # right arrow
                right = 1
            elif scancode == 0xE075:  # up arrow
                up = 1

            # Create output dictionary for this stimulus
            output_dict = {
                "left": format(left, "b"),
                "down": format(down, "b"),
                "right": format(right, "b"),
                "up": format(up, "b"),
            }
            outputs.append(output_dict)

        return {"scenario": stimulus_dict["scenario"], "output variable": outputs}


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
