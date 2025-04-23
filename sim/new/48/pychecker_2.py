import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Extract inputs for first NAND gate
            p1a = int(stimulus["p1a"], 2)
            p1b = int(stimulus["p1b"], 2)
            p1c = int(stimulus["p1c"], 2)
            p1d = int(stimulus["p1d"], 2)

            # Extract inputs for second NAND gate
            p2a = int(stimulus["p2a"], 2)
            p2b = int(stimulus["p2b"], 2)
            p2c = int(stimulus["p2c"], 2)
            p2d = int(stimulus["p2d"], 2)

            # Compute NAND outputs
            p1y = int(not (p1a and p1b and p1c and p1d))
            p2y = int(not (p2a and p2b and p2c and p2d))

            # Convert to binary strings
            p1y_bv = BinaryValue(value=p1y, n_bits=1, bigEndian=False)
            p2y_bv = BinaryValue(value=p2y, n_bits=1, bigEndian=False)

            # Add outputs to result list
            output = {"p1y": p1y_bv.binstr, "p2y": p2y_bv.binstr}
            stimulus_outputs.append(output)

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
