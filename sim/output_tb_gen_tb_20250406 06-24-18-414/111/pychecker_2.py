import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for combinational multiplexer
        """
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """
        Process inputs and generate outputs according to multiplexer logic
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=1024, bigEndian=False)
            sel_bv = BinaryValue(value=stimulus["sel"], n_bits=8, bigEndian=False)

            # Calculate starting bit position based on selector
            start_pos = sel_bv.integer * 4

            # Extract 4 bits from the input vector
            # Note: We need to specify exact bit range to avoid None index
            out_bits = in_bv[start_pos : start_pos + 4]

            # Create output dictionary with 4-bit result
            output = {"out": out_bits.binstr}
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
