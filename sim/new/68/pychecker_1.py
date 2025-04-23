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
            # Convert input strings to BinaryValue objects
            p1a = BinaryValue(stimulus["p1a"], n_bits=1, bigEndian=False)
            p1b = BinaryValue(stimulus["p1b"], n_bits=1, bigEndian=False)
            p1c = BinaryValue(stimulus["p1c"], n_bits=1, bigEndian=False)
            p1d = BinaryValue(stimulus["p1d"], n_bits=1, bigEndian=False)
            p1e = BinaryValue(stimulus["p1e"], n_bits=1, bigEndian=False)
            p1f = BinaryValue(stimulus["p1f"], n_bits=1, bigEndian=False)
            p2a = BinaryValue(stimulus["p2a"], n_bits=1, bigEndian=False)
            p2b = BinaryValue(stimulus["p2b"], n_bits=1, bigEndian=False)
            p2c = BinaryValue(stimulus["p2c"], n_bits=1, bigEndian=False)
            p2d = BinaryValue(stimulus["p2d"], n_bits=1, bigEndian=False)

            # Calculate p1y: (p1a & p1b & p1c) | (p1d & p1e & p1f)
            and1 = p1a.integer and p1b.integer and p1c.integer
            and2 = p1d.integer and p1e.integer and p1f.integer
            p1y = and1 or and2

            # Calculate p2y: (p2a & p2b) | (p2c & p2d)
            and3 = p2a.integer and p2b.integer
            and4 = p2c.integer and p2d.integer
            p2y = and3 or and4

            # Convert results to BinaryValue for output
            p1y_bv = BinaryValue(value=p1y, n_bits=1, bigEndian=False)
            p2y_bv = BinaryValue(value=p2y, n_bits=1, bigEndian=False)

            # Add outputs to results list
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
