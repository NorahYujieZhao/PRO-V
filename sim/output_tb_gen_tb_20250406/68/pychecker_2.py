import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Extract inputs
            p1a = int(stimulus["p1a"], 2)
            p1b = int(stimulus["p1b"], 2)
            p1c = int(stimulus["p1c"], 2)
            p1d = int(stimulus["p1d"], 2)
            p1e = int(stimulus["p1e"], 2)
            p1f = int(stimulus["p1f"], 2)
            p2a = int(stimulus["p2a"], 2)
            p2b = int(stimulus["p2b"], 2)
            p2c = int(stimulus["p2c"], 2)
            p2d = int(stimulus["p2d"], 2)

            # Calculate p1y: (p1a & p1b & p1c) | (p1d & p1e & p1f)
            p1y = (p1a & p1b & p1c) | (p1d & p1e & p1f)

            # Calculate p2y: (p2a & p2b) | (p2c & p2d)
            p2y = (p2a & p2b) | (p2c & p2d)

            # Convert to BinaryValue for output
            p1y_bv = BinaryValue(value=p1y, n_bits=1, bigEndian=False)
            p2y_bv = BinaryValue(value=p2y, n_bits=1, bigEndian=False)

            # Add outputs to result list
            output_list.append({"p1y": p1y_bv.binstr, "p2y": p2y_bv.binstr})

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
