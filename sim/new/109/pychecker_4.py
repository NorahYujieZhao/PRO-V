import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=100, bigEndian=False)

            # Initialize output BinaryValues
            out_both = BinaryValue(value=0, n_bits=99, bigEndian=False)
            out_any = BinaryValue(value=0, n_bits=99, bigEndian=False)
            out_different = BinaryValue(value=0, n_bits=100, bigEndian=False)

            # Calculate out_both[98:0]
            for i in range(99):
                if in_bv[i] == 1 and in_bv[i + 1] == 1:
                    out_both[i] = 1

            # Calculate out_any[99:1]
            for i in range(1, 100):
                if in_bv[i] == 1 or in_bv[i - 1] == 1:
                    out_any[i - 1] = 1

            # Calculate out_different[99:0] with wrap-around
            for i in range(100):
                left_neighbor = in_bv[0] if i == 99 else in_bv[i + 1]
                if in_bv[i] != left_neighbor:
                    out_different[i] = 1

            # Add outputs to stimulus_outputs list
            output_dict = {
                "out_both": out_both.binstr,
                "out_any": out_any.binstr,
                "out_different": out_different.binstr,
            }
            stimulus_outputs.append(output_dict)

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
