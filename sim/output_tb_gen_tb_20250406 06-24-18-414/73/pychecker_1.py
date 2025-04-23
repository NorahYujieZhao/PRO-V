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
            # Convert input binary strings to BinaryValue objects
            sel = BinaryValue(value=stimulus["sel"], n_bits=3, bigEndian=False).integer
            data0 = BinaryValue(
                value=stimulus["data0"], n_bits=4, bigEndian=False
            ).integer
            data1 = BinaryValue(
                value=stimulus["data1"], n_bits=4, bigEndian=False
            ).integer
            data2 = BinaryValue(
                value=stimulus["data2"], n_bits=4, bigEndian=False
            ).integer
            data3 = BinaryValue(
                value=stimulus["data3"], n_bits=4, bigEndian=False
            ).integer
            data4 = BinaryValue(
                value=stimulus["data4"], n_bits=4, bigEndian=False
            ).integer
            data5 = BinaryValue(
                value=stimulus["data5"], n_bits=4, bigEndian=False
            ).integer

            # Implement 6-to-1 multiplexer logic
            if sel == 0:
                out = data0
            elif sel == 1:
                out = data1
            elif sel == 2:
                out = data2
            elif sel == 3:
                out = data3
            elif sel == 4:
                out = data4
            elif sel == 5:
                out = data5
            else:
                out = 0

            # Convert output to 4-bit BinaryValue
            out_bv = BinaryValue(value=out, n_bits=4, bigEndian=False)
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
