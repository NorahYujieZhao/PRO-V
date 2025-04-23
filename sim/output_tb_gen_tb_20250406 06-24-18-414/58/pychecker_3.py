import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state"""
        pass

    def module_a(self, x: int, y: int) -> int:
        """Implement module A logic"""
        return (x ^ y) & x

    def module_b(self, x: int, y: int) -> int:
        """Implement module B logic"""
        return ~(x ^ y) & 1

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and generate outputs"""
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary strings to integers
            x = int(stimulus["x"], 2)
            y = int(stimulus["y"], 2)

            # Calculate outputs of both A modules
            a1_out = self.module_a(x, y)
            a2_out = self.module_a(x, y)

            # Calculate outputs of both B modules
            b1_out = self.module_b(x, y)
            b2_out = self.module_b(x, y)

            # Combine outputs through gates
            or_out = a1_out | b1_out
            and_out = a2_out & b2_out

            # Final XOR
            z = or_out ^ and_out

            # Convert to binary string
            z_bv = BinaryValue(value=z, n_bits=1, bigEndian=False)

            outputs.append({"z": z_bv.binstr})

        return {"scenario": stimulus_dict["scenario"], "output variable": outputs}


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
