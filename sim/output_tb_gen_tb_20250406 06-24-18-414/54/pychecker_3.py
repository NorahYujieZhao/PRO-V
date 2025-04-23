import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """No state variables needed for this combinational circuit"""
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process each input and generate corresponding output"""
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input value and convert to BinaryValue
            in_val = BinaryValue(value=stimulus["in"], n_bits=1, bigEndian=False)

            # Output is same as input
            out_val = in_val.binstr

            # Add to output list
            output_list.append({"out": out_val})

        return {"scenario": stimulus_dict["scenario"], "output variable": output_list}


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
