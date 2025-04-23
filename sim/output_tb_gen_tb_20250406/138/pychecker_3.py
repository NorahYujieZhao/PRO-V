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
            a_bv = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            cin_bv = BinaryValue(value=stimulus["cin"], n_bits=1, bigEndian=False)

            # Convert to integers for calculations
            a = a_bv.integer
            b = b_bv.integer
            cin = cin_bv.integer

            # Calculate sum and carry out
            sum_out = a ^ b ^ cin  # XOR operation
            cout = (a & b) | (cin & (a ^ b))  # Carry out logic

            # Convert results back to BinaryValue
            sum_bv = BinaryValue(value=sum_out, n_bits=1, bigEndian=False)
            cout_bv = BinaryValue(value=cout, n_bits=1, bigEndian=False)

            # Create output dictionary for this stimulus
            output = {"sum": sum_bv.binstr, "cout": cout_bv.binstr}
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
