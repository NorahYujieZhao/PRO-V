import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)

            # Calculate each output
            out_and = BinaryValue(
                value=(a.integer & b.integer), n_bits=1, bigEndian=False
            )
            out_or = BinaryValue(
                value=(a.integer | b.integer), n_bits=1, bigEndian=False
            )
            out_xor = BinaryValue(
                value=(a.integer ^ b.integer), n_bits=1, bigEndian=False
            )
            out_nand = BinaryValue(
                value=~(a.integer & b.integer) & 1, n_bits=1, bigEndian=False
            )
            out_nor = BinaryValue(
                value=~(a.integer | b.integer) & 1, n_bits=1, bigEndian=False
            )
            out_xnor = BinaryValue(
                value=~(a.integer ^ b.integer) & 1, n_bits=1, bigEndian=False
            )
            out_anotb = BinaryValue(
                value=(a.integer & (~b.integer & 1)), n_bits=1, bigEndian=False
            )

            # Create output dictionary for this stimulus
            output = {
                "out_and": out_and.binstr,
                "out_or": out_or.binstr,
                "out_xor": out_xor.binstr,
                "out_nand": out_nand.binstr,
                "out_nor": out_nor.binstr,
                "out_xnor": out_xnor.binstr,
                "out_anotb": out_anotb.binstr,
            }
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
