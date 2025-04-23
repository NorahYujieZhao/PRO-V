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
            # Convert input binary strings to BinaryValue objects
            p1a = BinaryValue(value=stimulus["p1a"], n_bits=1, bigEndian=False)
            p1b = BinaryValue(value=stimulus["p1b"], n_bits=1, bigEndian=False)
            p1c = BinaryValue(value=stimulus["p1c"], n_bits=1, bigEndian=False)
            p1d = BinaryValue(value=stimulus["p1d"], n_bits=1, bigEndian=False)
            p2a = BinaryValue(value=stimulus["p2a"], n_bits=1, bigEndian=False)
            p2b = BinaryValue(value=stimulus["p2b"], n_bits=1, bigEndian=False)
            p2c = BinaryValue(value=stimulus["p2c"], n_bits=1, bigEndian=False)
            p2d = BinaryValue(value=stimulus["p2d"], n_bits=1, bigEndian=False)

            # Implement NAND logic for first gate
            p1y = not (p1a.integer and p1b.integer and p1c.integer and p1d.integer)
            # Implement NAND logic for second gate
            p2y = not (p2a.integer and p2b.integer and p2c.integer and p2d.integer)

            # Convert boolean results to BinaryValue
            p1y_bv = BinaryValue(value=int(p1y), n_bits=1, bigEndian=False)
            p2y_bv = BinaryValue(value=int(p2y), n_bits=1, bigEndian=False)

            # Add outputs to results
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
