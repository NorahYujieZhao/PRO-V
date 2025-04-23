import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def compute_and(self, in_val: BinaryValue) -> BinaryValue:
        # 4-input AND gate
        result = in_val.integer == 0b1111
        return BinaryValue(value=int(result), n_bits=1, bigEndian=False)

    def compute_or(self, in_val: BinaryValue) -> BinaryValue:
        # 4-input OR gate
        result = in_val.integer > 0
        return BinaryValue(value=int(result), n_bits=1, bigEndian=False)

    def compute_xor(self, in_val: BinaryValue) -> BinaryValue:
        # 4-input XOR gate
        # Count number of 1s in input
        num_ones = bin(in_val.integer).count("1")
        result = num_ones % 2 == 1
        return BinaryValue(value=int(result), n_bits=1, bigEndian=False)

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=4, bigEndian=False)

            # Compute all outputs
            out_and = self.compute_and(in_bv)
            out_or = self.compute_or(in_bv)
            out_xor = self.compute_xor(in_bv)

            # Create output dictionary for this stimulus
            outputs = {
                "out_and": out_and.binstr,
                "out_or": out_or.binstr,
                "out_xor": out_xor.binstr,
            }
            stimulus_outputs.append(outputs)

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
