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
            # Convert input binary strings to BinaryValue
            in1_bv = BinaryValue(stimulus["in1"], n_bits=1, bigEndian=False)
            in2_bv = BinaryValue(stimulus["in2"], n_bits=1, bigEndian=False)

            # Get integer values
            in1 = in1_bv.integer
            in2 = in2_bv.integer

            # Implement NOR gate logic
            out = 1 if (in1 == 0 and in2 == 0) else 0

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
