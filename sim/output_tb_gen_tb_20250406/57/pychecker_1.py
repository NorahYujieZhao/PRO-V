import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # XNOR gate is combinational, no state needed
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a_bv = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)

            # Perform XNOR operation
            # XNOR is TRUE when inputs are same (NOT XOR)
            a_val = a_bv.integer
            b_val = b_bv.integer
            out_val = int(not (a_val ^ b_val))

            # Convert to BinaryValue for consistent output format
            out_bv = BinaryValue(value=out_val, n_bits=1, bigEndian=False)

            # Add to output list
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
