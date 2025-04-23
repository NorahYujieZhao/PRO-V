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
            # Convert input strings to BinaryValue objects
            in1_bv = BinaryValue(value=stimulus["in1"], n_bits=1, bigEndian=False)
            in2_bv = BinaryValue(value=stimulus["in2"], n_bits=1, bigEndian=False)

            # Implement NOR gate logic
            in1_val = in1_bv.integer
            in2_val = in2_bv.integer
            out_val = 1 if (in1_val == 0 and in2_val == 0) else 0

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=out_val, n_bits=1, bigEndian=False)

            # Add output to results
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
