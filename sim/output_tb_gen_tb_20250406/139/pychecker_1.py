import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No state variables needed for this combinational circuit
        """
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """
        Process inputs through XNOR and XOR gates to produce output
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            in1_bv = BinaryValue(value=stimulus["in1"], n_bits=1, bigEndian=False)
            in2_bv = BinaryValue(value=stimulus["in2"], n_bits=1, bigEndian=False)
            in3_bv = BinaryValue(value=stimulus["in3"], n_bits=1, bigEndian=False)

            # Get integer values
            in1 = in1_bv.integer
            in2 = in2_bv.integer
            in3 = in3_bv.integer

            # Calculate XNOR of in1 and in2
            xnor_result = int(not (in1 ^ in2))

            # Calculate XOR of XNOR result and in3
            out = xnor_result ^ in3

            # Convert output to BinaryValue and then to binary string
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add to outputs
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
