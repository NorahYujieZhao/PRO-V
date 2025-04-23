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
        Process each input stimulus and generate corresponding output
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=8, bigEndian=False)

            # Get binary string and reverse it
            in_str = in_bv.binstr
            out_str = in_str[::-1]

            # Convert reversed string back to BinaryValue
            out_bv = BinaryValue(value=out_str, n_bits=8, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"out": out_bv.binstr})

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
