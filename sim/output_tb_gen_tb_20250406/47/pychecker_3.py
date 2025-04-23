import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational circuit
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a = BinaryValue(value=int(stimulus["a"], 2), n_bits=1, bigEndian=False)
            b = BinaryValue(value=int(stimulus["b"], 2), n_bits=1, bigEndian=False)
            c = BinaryValue(value=int(stimulus["c"], 2), n_bits=1, bigEndian=False)
            d = BinaryValue(value=int(stimulus["d"], 2), n_bits=1, bigEndian=False)

            # Implement combinational logic: q = b | (a & (c | d))
            c_or_d = c.integer | d.integer
            a_and_cd = a.integer & c_or_d
            q = b.integer | a_and_cd

            # Convert output to BinaryValue
            q_bv = BinaryValue(value=q, n_bits=1, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"q": q_bv.binstr})

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
