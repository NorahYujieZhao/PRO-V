import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get inputs for first NAND gate
            p1a = BinaryValue(stimulus["p1a"], n_bits=1, bigEndian=False).integer
            p1b = BinaryValue(stimulus["p1b"], n_bits=1, bigEndian=False).integer
            p1c = BinaryValue(stimulus["p1c"], n_bits=1, bigEndian=False).integer
            p1d = BinaryValue(stimulus["p1d"], n_bits=1, bigEndian=False).integer

            # Get inputs for second NAND gate
            p2a = BinaryValue(stimulus["p2a"], n_bits=1, bigEndian=False).integer
            p2b = BinaryValue(stimulus["p2b"], n_bits=1, bigEndian=False).integer
            p2c = BinaryValue(stimulus["p2c"], n_bits=1, bigEndian=False).integer
            p2d = BinaryValue(stimulus["p2d"], n_bits=1, bigEndian=False).integer

            # Calculate NAND outputs
            p1y = int(not (p1a and p1b and p1c and p1d))
            p2y = int(not (p2a and p2b and p2c and p2d))

            # Convert outputs to binary strings
            p1y_bv = BinaryValue(value=p1y, n_bits=1, bigEndian=False)
            p2y_bv = BinaryValue(value=p2y, n_bits=1, bigEndian=False)

            # Add outputs to result list
            stimulus_outputs.append({"p1y": p1y_bv.binstr, "p2y": p2y_bv.binstr})

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
