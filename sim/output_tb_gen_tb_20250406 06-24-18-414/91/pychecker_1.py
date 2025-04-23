import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            c = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)

            # Compute output based on Karnaugh map
            # out = a OR b OR c
            out = a.integer or b.integer or c.integer

            # Convert output to binary string
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add output to results
            stimulus_outputs.append({"out": out_bv.binstr})

        # Return results in required format
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
