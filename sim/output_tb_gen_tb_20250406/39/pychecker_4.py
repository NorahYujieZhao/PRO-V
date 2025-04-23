import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational adder
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to BinaryValue
            x_bv = BinaryValue(value=stimulus["x"], n_bits=4, bigEndian=False)
            y_bv = BinaryValue(value=stimulus["y"], n_bits=4, bigEndian=False)

            # Convert to integers and perform addition
            x_int = x_bv.integer
            y_int = y_bv.integer
            sum_int = x_int + y_int

            # Convert sum to 5-bit BinaryValue to include overflow
            sum_bv = BinaryValue(value=sum_int, n_bits=5, bigEndian=False)

            # Create output dictionary for this stimulus
            output = {"sum": sum_bv.binstr}
            stimulus_outputs.append(output)

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
