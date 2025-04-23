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
            # Convert input strings to BinaryValue
            a = BinaryValue(
                value=int(stimulus["a"], 2), n_bits=1, bigEndian=False
            ).integer
            b = BinaryValue(
                value=int(stimulus["b"], 2), n_bits=1, bigEndian=False
            ).integer
            c = BinaryValue(
                value=int(stimulus["c"], 2), n_bits=1, bigEndian=False
            ).integer
            d = BinaryValue(
                value=int(stimulus["d"], 2), n_bits=1, bigEndian=False
            ).integer

            # Calculate out_sop (Sum of Products)
            out_sop = (
                (not a and not b and c and not d)  # 2
                or (not a and b and c and d)  # 7
                or (a and b and c and d)
            )  # 15

            # Calculate out_pos (Product of Sums)
            out_pos = (
                (a or b or c or d)  # not 0
                and (a or b or c or not d)  # not 1
                and (a or b or not c or d)  # not 4
                and (a or b or not c or not d)  # not 5
                and (a or not b or c or d)  # not 6
                and (a or not b or not c or d)  # not 9
                and (a or not b or not c or not d)  # not 10
                and (not a or b or not c or d)  # not 13
                and (not a or b or not c or not d)
            )  # not 14

            # Convert boolean results to BinaryValue strings
            out_sop_bv = BinaryValue(value=int(out_sop), n_bits=1, bigEndian=False)
            out_pos_bv = BinaryValue(value=int(out_pos), n_bits=1, bigEndian=False)

            stimulus_outputs.append(
                {"out_sop": out_sop_bv.binstr, "out_pos": out_pos_bv.binstr}
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
