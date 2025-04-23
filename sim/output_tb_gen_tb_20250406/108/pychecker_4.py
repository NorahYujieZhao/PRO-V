import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state registers"""
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and generate outputs"""
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to BinaryValue objects
            A = BinaryValue(value=stimulus["A"], n_bits=2, bigEndian=False)
            B = BinaryValue(value=stimulus["B"], n_bits=2, bigEndian=False)

            # Compare A and B
            z = "1" if A.integer == B.integer else "0"

            # Add result to outputs
            outputs.append({"z": z})

        # Return formatted output dictionary
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
