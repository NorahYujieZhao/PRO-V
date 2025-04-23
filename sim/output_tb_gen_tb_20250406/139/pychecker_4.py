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
            in1 = BinaryValue(value=stimulus["in1"], n_bits=1, bigEndian=False)
            in2 = BinaryValue(value=stimulus["in2"], n_bits=1, bigEndian=False)
            in3 = BinaryValue(value=stimulus["in3"], n_bits=1, bigEndian=False)

            # Calculate XNOR of in1 and in2
            xnor_result = not (in1.integer ^ in2.integer)

            # XOR the XNOR result with in3
            out = xnor_result ^ in3.integer

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add to outputs list
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
