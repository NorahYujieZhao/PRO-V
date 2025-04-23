import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize any internal state if needed"""
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process input stimuli and generate output"""
        stimulus_outputs = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a_bv = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)

            # Perform XNOR operation
            # XNOR is true when inputs are the same
            out = int(a_bv.integer == b_bv.integer)

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add output to results
            stimulus_outputs.append({"out": out_bv.binstr})

        # Return formatted output dictionary
        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }

        return output_dict


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
