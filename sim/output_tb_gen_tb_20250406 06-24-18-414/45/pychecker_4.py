import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize internal state. For this combinational logic,
        no state variables are needed.
        """
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a_bv = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            c_bv = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(value=stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to integers for computation
            a = a_bv.integer
            b = b_bv.integer
            c = c_bv.integer
            d = d_bv.integer

            # Calculate outputs
            # SOP form: out_sop = a'bc'd + a'bcd + abcd
            out_sop = (
                ((not a) and b and (not c) and d)
                or ((not a) and b and c and d)
                or (a and b and c and d)
            )

            # POS form: out_pos = (a+b+c+d)(a+b+c+d')(a+b'+c+d)(a+b'+c'+d')
            out_pos = (
                (a or b or c or d)
                and (a or b or c or (not d))
                and (a or (not b) or c or d)
                and (a or (not b) or (not c) or (not d))
            )

            # Convert boolean to BinaryValue
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
