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
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False).integer
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False).integer
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False).integer
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False).integer

            # Calculate outputs
            # SOP form: out when input is 2 (0010), 7 (0111), or 15 (1111)
            out_sop = (
                (not a and not b and c and not d)
                or (not a and b and c and d)
                or (a and b and c and d)
            )

            # POS form: same logic but in product-of-sums
            out_pos = (
                (a or b or not c or d)
                and (a or not b or not c or d)
                and (not a or b or not c or d)
                and (not a or not b or c or d)
            )

            # Convert boolean to BinaryValue for output
            out_sop_bv = BinaryValue(value=int(out_sop), n_bits=1, bigEndian=False)
            out_pos_bv = BinaryValue(value=int(out_pos), n_bits=1, bigEndian=False)

            # Add outputs to results
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
