import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            sel = BinaryValue(value=stimulus["sel"], n_bits=3, bigEndian=False)
            data0 = BinaryValue(value=stimulus["data0"], n_bits=4, bigEndian=False)
            data1 = BinaryValue(value=stimulus["data1"], n_bits=4, bigEndian=False)
            data2 = BinaryValue(value=stimulus["data2"], n_bits=4, bigEndian=False)
            data3 = BinaryValue(value=stimulus["data3"], n_bits=4, bigEndian=False)
            data4 = BinaryValue(value=stimulus["data4"], n_bits=4, bigEndian=False)
            data5 = BinaryValue(value=stimulus["data5"], n_bits=4, bigEndian=False)

            # Implement 6-to-1 multiplexer logic
            sel_int = sel.integer
            if sel_int == 0:
                out = data0.integer
            elif sel_int == 1:
                out = data1.integer
            elif sel_int == 2:
                out = data2.integer
            elif sel_int == 3:
                out = data3.integer
            elif sel_int == 4:
                out = data4.integer
            elif sel_int == 5:
                out = data5.integer
            else:
                out = 0

            # Convert output to 4-bit BinaryValue
            out_bv = BinaryValue(value=out, n_bits=4, bigEndian=False)

            # Add output to stimulus_outputs list
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
