import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input values
            in1 = BinaryValue(stimulus["in1"], n_bits=1, bigEndian=False)
            in2 = BinaryValue(stimulus["in2"], n_bits=1, bigEndian=False)

            # Perform NOR operation
            # Output is 1 only when both inputs are 0
            out = "1" if in1.integer == 0 and in2.integer == 0 else "0"

            # Add output to results
            stimulus_outputs.append({"out": out})

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
