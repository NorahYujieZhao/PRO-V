import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize state registers
        self.fr3 = 1  # Start with maximum flow
        self.fr2 = 1
        self.fr1 = 1
        self.dfr = 1
        self.prev_level = 0  # Previous water level

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert inputs to appropriate format
            reset = int(stimulus["reset"], 2)
            s = int(stimulus["s"], 2)

            if reset:
                # Reset to lowest level state
                self.fr3 = 1
                self.fr2 = 1
                self.fr1 = 1
                self.dfr = 1
                self.prev_level = 0
            else:
                # Determine current water level (0=lowest to 3=highest)
                current_level = bin(s).count("1")

                # Set flow rates based on water level
                if s & 0b100:  # Above s[3]
                    self.fr3 = 0
                    self.fr2 = 0
                    self.fr1 = 0
                elif s & 0b010:  # Between s[3] and s[2]
                    self.fr3 = 0
                    self.fr2 = 0
                    self.fr1 = 1
                elif s & 0b001:  # Between s[2] and s[1]
                    self.fr3 = 0
                    self.fr2 = 1
                    self.fr1 = 1
                else:  # Below s[1]
                    self.fr3 = 1
                    self.fr2 = 1
                    self.fr1 = 1

                # Set dfr if water level increased
                self.dfr = 1 if current_level > self.prev_level else 0
                self.prev_level = current_level

            # Create output dictionary for this stimulus
            outputs = {
                "fr3": format(self.fr3, "b"),
                "fr2": format(self.fr2, "b"),
                "fr1": format(self.fr1, "b"),
                "dfr": format(self.dfr, "b"),
            }
            stimulus_outputs.append(outputs)

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
