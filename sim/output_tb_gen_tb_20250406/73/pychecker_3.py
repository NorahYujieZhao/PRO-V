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
            # Convert sel to BinaryValue (3 bits)
            sel = BinaryValue(value=stimulus["sel"], n_bits=3, bigEndian=False)
            sel_int = sel.integer

            # Convert all data inputs to BinaryValue (4 bits each)
            data = []
            for i in range(6):
                data.append(
                    BinaryValue(value=stimulus[f"data{i}"], n_bits=4, bigEndian=False)
                )

            # Implement multiplexer logic
            if sel_int <= 5:
                out = data[sel_int].integer
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
