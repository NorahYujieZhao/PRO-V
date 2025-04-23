import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for this simple module
        """
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """
        Generate constant output of 1 regardless of input
        """
        # Create output list for all stimuli
        stimulus_outputs = []

        # For each input stimulus, generate an output of 1
        for _ in stimulus_dict["input variable"]:
            # Create a 1-bit BinaryValue with value 1
            one_value = BinaryValue(value=1, n_bits=1, bigEndian=False)
            # Add the output dictionary for this stimulus
            stimulus_outputs.append({"one": one_value.binstr})

        # Return the formatted output dictionary
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
