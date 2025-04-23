import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary strings to BinaryValue objects
            a_bv = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            c_bv = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(value=stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to boolean values
            a = bool(a_bv.integer)
            b = bool(b_bv.integer)
            c = bool(c_bv.integer)
            d = bool(d_bv.integer)

            # Implement K-map logic (choosing d=0 for don't cares)
            out = (
                (not a and b)
                or (a and not b)
                or (a and b)
                or (not c and not d and not a and b)
                or (c and not a and b)
                or (c and a)
            )

            # Convert boolean output to binary string
            out_bv = BinaryValue(value=int(out), n_bits=1, bigEndian=False)
            stimulus_outputs.append({"out": out_bv.binstr})

        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }

        return output_dict


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
