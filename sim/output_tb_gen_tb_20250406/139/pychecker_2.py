import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]) -> Dict[str, Any]:
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            in1_bv = BinaryValue(value=stimulus["in1"], n_bits=1, bigEndian=False)
            in2_bv = BinaryValue(value=stimulus["in2"], n_bits=1, bigEndian=False)
            in3_bv = BinaryValue(value=stimulus["in3"], n_bits=1, bigEndian=False)

            # Convert to integers for logic operations
            in1 = in1_bv.integer
            in2 = in2_bv.integer
            in3 = in3_bv.integer

            # Compute XNOR of in1 and in2
            xnor_result = ~(in1 ^ in2) & 1

            # Compute XOR of XNOR result with in3
            out = (xnor_result ^ in3) & 1

            # Convert output to BinaryValue and then to binary string
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add the output to the list
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
