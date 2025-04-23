import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def module_a(self, x: int, y: int) -> int:
        # z = (x^y) & x
        return (x ^ y) & x

    def module_b(self, x: int, y: int) -> int:
        # Implementation based on waveform truth table
        if x == 0 and y == 0:
            return 1
        elif x == 1 and y == 1:
            return 1
        else:
            return 0

    def load(self, stimulus_dict: Dict[str, Any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            x_bv = BinaryValue(stimulus["x"], n_bits=1, bigEndian=False)
            y_bv = BinaryValue(stimulus["y"], n_bits=1, bigEndian=False)

            # Convert to integers for calculation
            x = x_bv.integer
            y = y_bv.integer

            # Calculate outputs of all submodules
            a1_out = self.module_a(x, y)
            a2_out = self.module_a(x, y)
            b1_out = self.module_b(x, y)
            b2_out = self.module_b(x, y)

            # Combine outputs according to top-level structure
            or_out = a1_out | b1_out
            and_out = a2_out & b2_out
            z = or_out ^ and_out

            # Convert output to BinaryValue and then to string
            z_bv = BinaryValue(value=z, n_bits=1, bigEndian=False)
            output_list.append({"z": z_bv.binstr})

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
