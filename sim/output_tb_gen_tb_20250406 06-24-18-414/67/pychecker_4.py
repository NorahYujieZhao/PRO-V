import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational circuit
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Convert binary string inputs to BinaryValue
            a_bv = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)

            # Perform AND operation
            q = a_bv.integer & b_bv.integer

            # Convert output to binary string format
            q_bv = BinaryValue(value=q, n_bits=1, bigEndian=False)

            # Add result to outputs list
            stimulus_outputs.append({"q": q_bv.binstr})

        # Return results in required format
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
