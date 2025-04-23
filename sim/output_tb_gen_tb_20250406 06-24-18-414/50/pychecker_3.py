import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state"""
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """Process inputs and generate outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=4, bigEndian=False)
            in_val = in_bv.integer

            # Calculate out_both[2:0]
            out_both = 0
            for i in range(3):
                if (in_val & (1 << i)) and (in_val & (1 << (i + 1))):
                    out_both |= 1 << i
            out_both_bv = BinaryValue(value=out_both, n_bits=3, bigEndian=False)

            # Calculate out_any[3:1]
            out_any = 0
            for i in range(1, 4):
                if (in_val & (1 << i)) or (in_val & (1 << (i - 1))):
                    out_any |= 1 << i
            out_any_bv = BinaryValue(value=out_any, n_bits=4, bigEndian=False)[1:4]

            # Calculate out_different[3:0]
            out_different = 0
            for i in range(4):
                left_neighbor = (i + 1) % 4
                if ((in_val >> i) & 1) != ((in_val >> left_neighbor) & 1):
                    out_different |= 1 << i
            out_different_bv = BinaryValue(
                value=out_different, n_bits=4, bigEndian=False
            )

            # Create output dictionary
            output = {
                "out_both": out_both_bv.binstr,
                "out_any": out_any_bv.binstr,
                "out_different": out_different_bv.binstr,
            }
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
