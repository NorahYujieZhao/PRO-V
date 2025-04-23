import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def _calculate_value(self, a: str, b: str, c: str, d: str) -> tuple:
        # Convert inputs to integer for easier comparison
        input_val = (int(a) << 3) | (int(b) << 2) | (int(c) << 1) | int(d)

        # Define sets for 1s and 0s
        ones = {2, 7, 15}
        zeros = {0, 1, 4, 5, 6, 9, 10, 13, 14}

        # Calculate outputs
        out_sop = "1" if input_val in ones else "0"
        out_pos = "1" if input_val in ones else "0"

        return out_sop, out_pos

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to values
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False).binstr
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False).binstr
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False).binstr
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False).binstr

            # Calculate outputs
            out_sop, out_pos = self._calculate_value(a, b, c, d)

            # Create output dictionary for this stimulus
            output_dict = {"out_sop": out_sop, "out_pos": out_pos}
            output_list.append(output_dict)

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
