import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for this combinational logic
        """
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process inputs and generate outputs according to mux logic
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)
            sel_b1 = BinaryValue(stimulus["sel_b1"], n_bits=1, bigEndian=False)
            sel_b2 = BinaryValue(stimulus["sel_b2"], n_bits=1, bigEndian=False)

            # Calculate outputs
            select_b = sel_b1.integer and sel_b2.integer
            out_value = b.integer if select_b else a.integer

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=out_value, n_bits=1, bigEndian=False)

            # Both outputs have the same logic
            stimulus_outputs.append(
                {"out_assign": out_bv.binstr, "out_always": out_bv.binstr}
            )

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
