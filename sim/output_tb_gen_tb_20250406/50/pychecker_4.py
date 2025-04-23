import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=4, bigEndian=False)

            # Calculate out_both[2:0]
            out_both = 0
            for i in range(3):
                if in_bv[i] == 1 and in_bv[i + 1] == 1:
                    out_both |= 1 << i
            out_both_bv = BinaryValue(value=out_both, n_bits=3, bigEndian=False)

            # Calculate out_any[3:1]
            out_any = 0
            for i in range(1, 4):
                if in_bv[i] == 1 or in_bv[i - 1] == 1:
                    out_any |= 1 << (i - 1)
            out_any_bv = BinaryValue(value=out_any, n_bits=3, bigEndian=False)

            # Calculate out_different[3:0]
            out_different = 0
            for i in range(4):
                left_neighbor = in_bv[0] if i == 3 else in_bv[i + 1]
                if in_bv[i] != left_neighbor:
                    out_different |= 1 << i
            out_different_bv = BinaryValue(
                value=out_different, n_bits=4, bigEndian=False
            )

            # Add results to output
            stimulus_outputs.append(
                {
                    "out_both": out_both_bv.binstr,
                    "out_any": out_any_bv.binstr,
                    "out_different": out_different_bv.binstr,
                }
            )

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
