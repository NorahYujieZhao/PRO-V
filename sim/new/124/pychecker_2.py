import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this simple circuit
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        # Create output list for each stimulus cycle
        stimulus_outputs = []

        # Process each input stimulus
        for _ in stimulus_dict["input variable"]:
            # Create a 1-bit binary value with value 1
            one = BinaryValue(value=1, n_bits=1, bigEndian=False)

            # Add the output to stimulus_outputs
            stimulus_outputs.append({"one": one.binstr})

        # Return the output dictionary
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
