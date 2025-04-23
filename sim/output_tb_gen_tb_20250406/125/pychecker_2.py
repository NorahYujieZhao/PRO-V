import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        output_values = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input value and convert to BinaryValue
            in_val = stimulus["in"]
            in_bv = BinaryValue(value=in_val, n_bits=100, bigEndian=False)

            # Reverse the bits
            reversed_bits = in_bv.binstr[::-1]

            # Convert reversed bits to BinaryValue
            out_bv = BinaryValue(value=reversed_bits, n_bits=100, bigEndian=False)

            # Store output
            output_values.append({"out": out_bv.binstr})

        return {"scenario": stimulus_dict["scenario"], "output variable": output_values}


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
