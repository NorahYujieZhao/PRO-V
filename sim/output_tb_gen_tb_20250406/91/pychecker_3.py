import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a_bv = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)
            c_bv = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False)

            # Get integer values
            a = a_bv.integer
            b = b_bv.integer
            c = c_bv.integer

            # Implement logic function: out = ~(~a & ~b & ~c)
            out = not (not a and not b and not c)

            # Convert output to binary string
            out_bv = BinaryValue(value=int(out), n_bits=1, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"out": out_bv.binstr})

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
