import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state registers"""
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and generate outputs"""
        # Create output list for all stimulus cycles
        stimulus_outputs = []

        # Process each stimulus cycle
        for _ in stimulus_dict["input variable"]:
            # Create 1-bit BinaryValue with value 0
            out = BinaryValue(value=0, n_bits=1, bigEndian=False)
            # Add output dictionary for this cycle
            stimulus_outputs.append({"out": out.binstr})

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
