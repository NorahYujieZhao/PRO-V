import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for this simple wire connection module
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Create output dictionary for current stimulus
            output = {}

            # Get input values and convert to BinaryValue
            a = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            c = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)

            # Implement the wire connections
            output["w"] = a.binstr  # w = a
            output["x"] = b.binstr  # x = b
            output["y"] = b.binstr  # y = b
            output["z"] = c.binstr  # z = c

            stimulus_outputs.append(output)

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
